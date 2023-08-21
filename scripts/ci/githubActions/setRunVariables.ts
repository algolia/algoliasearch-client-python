/* eslint-disable no-console */
import * as core from '@actions/core';

import { CLIENTS_JS_UTILS, LANGUAGES, capitalize } from '../../common.js';
import { getLanguageFolder } from '../../config.js';

import { isBaseChanged } from './utils.js';

export const COMMON_DEPENDENCIES = {
  GITHUB_ACTIONS_CHANGED: ['.github/actions', '.github/workflows', '.github/.cache_version'],
  SCRIPTS_CHANGED: ['scripts', 'eslint', 'yarn.lock', '.eslintrc.js'],
  COMMON_SPECS_CHANGED: ['specs/common'],
};

/**
 * This dependency array is generated to match the "external" dependencies of a generated client.
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
export const DEPENDENCIES = LANGUAGES.reduce(
  (finalDependencies, lang) => {
    const key = `${lang.toUpperCase()}_CLIENT_CHANGED`;
    const langFolder = getLanguageFolder(lang);
    const langGenerator = capitalize(lang);

    return {
      ...finalDependencies,
      [key]: [
        // Files that are common to every clients, this is used to determine if we should generate the matrix for this job.
        'config/generation.config.mjs',
        'config/openapitools.json',
        'config/clients.config.json',
        'generators/src/main/java/com/algolia/codegen/Utils.java',
        'generators/src/main/java/com/algolia/codegen/GenericPropagator.java',
        'generators/src/main/java/com/algolia/codegen/cts',
        'tests/CTS',
        '.nvmrc',
        ':!**node_modules',
        // language related files
        langFolder,
        `templates/${lang}`,
        `generators/src/main/java/com/algolia/codegen/Algolia${langGenerator}Generator.java`,
        `config/.${lang}-version`,
        `:!${langFolder}/.github`,
        `:!${langFolder}/README.md`,
      ],
    };
  },
  {
    ...COMMON_DEPENDENCIES,
    // We default the JS utils client as it's a bit specific
    JAVASCRIPT_UTILS_CHANGED: CLIENTS_JS_UTILS.map(
      (clientName) => `${getLanguageFolder('javascript')}/packages/${clientName}`
    ),
  } as Record<string, string[]>
);

/**
 * Outputs variables used in the CI to determine if a job should run.
 */
async function setRunVariables({ originBranch }: { originBranch: string }): Promise<void> {
  console.log(`Checking diff between ${originBranch} and HEAD`);

  core.setOutput('ORIGIN_BRANCH', originBranch);

  await isBaseChanged(originBranch, DEPENDENCIES, true);
}

if (import.meta.url.endsWith(process.argv[1])) {
  const [originBranch] = process.argv.slice(2);

  if (!originBranch) {
    throw new Error(`Unable to retrieve the origin branch: ${JSON.stringify(originBranch)}`);
  }

  setRunVariables({ originBranch });
}
