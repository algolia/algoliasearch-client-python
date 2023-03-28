/* eslint-disable no-console */
import * as core from '@actions/core';

import { CLIENTS_JS_UTILS } from '../../common';
import { getLanguageFolder } from '../../config';

import { isBaseChanged } from './utils';

const JS_CLIENT_FOLDER = getLanguageFolder('javascript');
const JAVA_CLIENT_FOLDER = getLanguageFolder('java');
const PHP_CLIENT_FOLDER = getLanguageFolder('php');
const GO_CLIENT_FOLDER = getLanguageFolder('go');

// Files that are common to every clients
const CLIENTS_COMMON_FILES = [
  'config/openapitools.json',
  'config/clients.config.json',
  'generators/src/main/java/com/algolia/codegen/Utils.java',
  'generators/src/main/java/com/algolia/codegen/cts',
  'tests/CTS',
  ':!**node_modules',
];

/**
 * Dependencies that are common to every specs, clients or CTS jobs.
 */
export const COMMON_DEPENDENCIES = {
  GITHUB_ACTIONS_CHANGED: [
    '.github/actions',
    '.github/workflows',
    '.github/.cache_version',
  ],
  SCRIPTS_CHANGED: ['scripts', 'eslint', 'yarn.lock', '.eslintrc.js'],
  COMMON_SPECS_CHANGED: ['specs/common'],
};

/**
 * Exhaustive list of output variables to use in the CI.
 *
 * Those variables are used to determine if jobs should run, based on the changes
 * made in their respective dependencies.
 *
 * Negative paths should start with `:!`.
 *
 * The variable will be accessible in the CI via `steps.diff.outputs.<name>`.
 *
 * Variables starting by `LANGUAGENAME_` will be used in the `createMatrix` to determine
 * if a job should be added.
 */
export const DEPENDENCIES = {
  ...COMMON_DEPENDENCIES,
  JAVASCRIPT_UTILS_CHANGED: CLIENTS_JS_UTILS.map(
    (clientName) => `${JS_CLIENT_FOLDER}/packages/${clientName}`
  ),
  JAVASCRIPT_CLIENT_CHANGED: [
    ...CLIENTS_COMMON_FILES,
    JS_CLIENT_FOLDER,
    'templates/javascript',
    'generators/src/main/java/com/algolia/codegen/AlgoliaJavaScriptGenerator.java',
    `:!${JS_CLIENT_FOLDER}/.github`,
    `:!${JS_CLIENT_FOLDER}/README.md`,
  ],
  JAVA_CLIENT_CHANGED: [
    ...CLIENTS_COMMON_FILES,
    JAVA_CLIENT_FOLDER,
    'templates/java',
    'generators/src/main/java/com/algolia/codegen/AlgoliaJavaGenerator.java',
  ],
  PHP_CLIENT_CHANGED: [
    ...CLIENTS_COMMON_FILES,
    PHP_CLIENT_FOLDER,
    'templates/php',
    'generators/src/main/java/com/algolia/codegen/AlgoliaPhpGenerator.java',
  ],
  GO_CLIENT_CHANDED: [
    ...CLIENTS_COMMON_FILES,
    GO_CLIENT_FOLDER,
    'templates/go',
    'generators/src/main/java/com/algolia/codegen/AlgoliaGoGenerator.java',
  ],
};

/**
 * Outputs variables used in the CI to determine if a job should run.
 */
async function setRunVariables({
  originBranch,
}: {
  originBranch: string;
}): Promise<void> {
  console.log(`Checking diff between ${originBranch} and HEAD`);

  core.setOutput('ORIGIN_BRANCH', originBranch);

  await isBaseChanged(originBranch, DEPENDENCIES, true);
}

if (require.main === module) {
  const [originBranch] = process.argv.slice(2);

  if (!originBranch) {
    throw new Error(
      `Unable to retrieve the origin branch: ${JSON.stringify(originBranch)}`
    );
  }

  setRunVariables({ originBranch });
}
