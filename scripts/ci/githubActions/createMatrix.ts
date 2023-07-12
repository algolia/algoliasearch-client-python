/* eslint-disable no-case-declarations */
import * as core from '@actions/core';

import {
  CLIENTS,
  createClientName,
  GENERATORS,
  LANGUAGES,
} from '../../common.js';
import {
  getClientsConfigField,
  getLanguageFolder,
  getTestExtension,
  getTestOutputFolder,
} from '../../config.js';
import type { Language } from '../../types.js';
import { getNbGitDiff } from '../utils.js';

import { DEPENDENCIES, COMMON_DEPENDENCIES } from './setRunVariables.js';
import type {
  ClientMatrix,
  CreateMatrix,
  Matrix,
  SpecMatrix,
  ToRunMatrix,
} from './types.js';
import { computeCacheKey, isBaseChanged } from './utils.js';

// This empty matrix is required by the CI, otherwise it throws
const EMPTY_MATRIX = { client: ['no-run'] };

async function getClientMatrix(baseBranch: string): Promise<void> {
  const matrix = LANGUAGES.reduce(
    (curr, lang) => ({
      ...curr,
      [lang]: {
        path: getLanguageFolder(lang),
        toRun: [],
        cacheToCompute: [],
      },
    }),
    {} as Record<Language, ToRunMatrix>
  );

  for (const { language, client, output } of Object.values(GENERATORS)) {
    const languageDependencies = Object.entries(DEPENDENCIES).reduce(
      (finalDeps, [key, deps]) => {
        if (key.startsWith(`${language.toUpperCase()}_`)) {
          return {
            ...finalDeps,
            [key]: deps,
          };
        }

        return finalDeps;
      },
      {} as Record<string, string[]>
    );

    const bundledSpec = client === 'algoliasearch' ? 'search' : client;
    const specChanges = await getNbGitDiff({
      branch: baseBranch,
      path: `specs/${bundledSpec}`,
    });
    const clientChanges = await getNbGitDiff({
      branch: baseBranch,
      path: output,
    });
    const baseChanged = await isBaseChanged(baseBranch, {
      ...COMMON_DEPENDENCIES,
      ...languageDependencies,
    });

    // No changes found, we don't put this job in the matrix
    if (clientChanges === 0 && specChanges === 0 && !baseChanged) {
      continue;
    }

    matrix[language].toRun.push(client);
    matrix[language].cacheToCompute.push(`specs/${bundledSpec}`);
  }

  const clientMatrix: Matrix<ClientMatrix> = {
    client: [],
  };

  // Set output variables for the CI
  for (const language of LANGUAGES) {
    if (matrix[language].toRun.length === 0) {
      continue;
    }

    const testsRootFolder = `tests/output/${language}`;
    const testsOutputBase = `${testsRootFolder}/${getTestOutputFolder(
      language
    )}`;
    // We delete all tests because the CTS runs everything present in the folder
    // but we then re-generate the ones that needs to run
    const testsToDelete = `${testsOutputBase}/client ${testsOutputBase}/methods/requests`;

    // We only store tests of clients that ran during this job, the rest stay as is
    let testsToStore = matrix[language].toRun
      .map((client) => {
        const clientName = createClientName(client, language);
        const extension = getTestExtension(language);

        return `${testsOutputBase}/client/${clientName}${extension} ${testsOutputBase}/methods/requests/${clientName}${extension}`;
      })
      .join(' ');
    const toRun = matrix[language].toRun.join(' ');
    let buildCommand = `yarn cli build clients ${language} ${toRun}`;

    switch (language) {
      case 'java':
        testsToStore = `${testsToStore} ${testsRootFolder}/build.gradle`;
        break;
      case 'go':
        testsToStore = `${testsToStore} ${testsOutputBase}/methods/requests/common.go`;
        break;
      /**
       * The CI runs on a node docker image, therefore it's not needed to run
       * via the CLI for the JavaScript client.
       */
      case 'javascript':
        const npmNamespace = getClientsConfigField(
          'javascript',
          'npmNamespace'
        );
        const packageNames = matrix[language].toRun.map((client) => {
          const packageName =
            GENERATORS[`${language}-${client}`].additionalProperties
              .packageName;

          // `algoliasearch` is not preceded by `@algolia`
          return client === 'algoliasearch'
            ? packageName
            : `${npmNamespace}/${packageName}`;
        });

        buildCommand = `cd ${
          matrix[language].path
        } && yarn build:many '{${packageNames.join(',')},}'`;

        testsToStore = `${testsToStore} ${testsRootFolder}/package.json`;
        break;
      default:
        break;
    }

    clientMatrix.client.push({
      language,
      path: matrix[language].path,
      toRun,
      buildCommand,
      cacheKey: await computeCacheKey(`clients-${language}`, [
        ...matrix[language].cacheToCompute,
        'specs/common',
        `templates/${language}`,
        `generators/src`,
      ]),
      testsRootFolder,
      testsToDelete,
      testsToStore,
    });
    core.setOutput(`RUN_GEN_${language.toUpperCase()}`, true);
  }

  const shouldRun = clientMatrix.client.length > 0;

  core.setOutput('RUN_GEN', shouldRun);
  core.setOutput(
    'GEN_MATRIX',
    JSON.stringify(shouldRun ? clientMatrix : EMPTY_MATRIX)
  );
}

async function getSpecMatrix(): Promise<void> {
  const matrix: ToRunMatrix = {
    path: 'specs/bundled',
    toRun: [],
    cacheToCompute: [],
  };

  for (const client of CLIENTS) {
    // The `algoliasearch` spec is created by the `search` spec, for the `lite` JavaScript client.
    const bundledSpecName = client === 'algoliasearch' ? 'search' : client;

    matrix.toRun.push(client);
    matrix.cacheToCompute.push(`specs/${bundledSpecName}`);
  }

  const ciMatrix: SpecMatrix = {
    bundledPath: matrix.path,
    toRun: matrix.toRun.join(' '),
    cacheKey: await computeCacheKey('specs', [
      ...matrix.cacheToCompute,
      'specs/common',
    ]),
  };

  core.setOutput('MATRIX', JSON.stringify(ciMatrix));
}

/**
 * Creates a matrix for the CI jobs based on the files that changed.
 */
async function createMatrix(opts: CreateMatrix): Promise<void> {
  if (opts.forClients) {
    return await getClientMatrix(opts.baseBranch);
  }

  return await getSpecMatrix();
}

if (import.meta.url.endsWith(process.argv[1])) {
  const args = process.argv.slice(2);

  createMatrix({
    baseBranch: args[0],
    forClients: args[1] === 'clients',
  });
}
