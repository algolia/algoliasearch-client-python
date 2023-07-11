import fsp from 'fs/promises';

import yaml from 'js-yaml';

import {
  BUNDLE_WITH_DOC,
  checkForCache,
  exists,
  run,
  toAbsolutePath,
} from './common';
import { createSpinner } from './spinners';
import type { Spec } from './types';

const ALGOLIASEARCH_LITE_OPERATIONS = ['search', 'post'];

/**
 * This function will transform properties in the bundle depending on the context.
 * E.g:
 * - Check tags definition
 * - Add name of the client in tags
 * - Remove unecessary punctuation for documentation
 * - etc...
 */
async function transformBundle({
  bundledPath,
  withDoc,
  clientName,
  alias,
}: {
  bundledPath: string;
  withDoc: boolean;
  clientName: string;
  alias?: string;
}): Promise<void> {
  if (!(await exists(bundledPath))) {
    throw new Error(`Bundled file not found ${bundledPath}.`);
  }

  const bundledSpec = yaml.load(
    await fsp.readFile(bundledPath, 'utf8')
  ) as Spec;

  let bundledDocSpec: Spec | undefined;
  if (withDoc) {
    bundledDocSpec = yaml.load(await fsp.readFile(bundledPath, 'utf8')) as Spec;
  }
  const tagsDefinitions = bundledSpec.tags;

  for (const [pathKey, pathMethods] of Object.entries(bundledSpec.paths)) {
    for (const [method, specMethod] of Object.entries(pathMethods)) {
      // In the main bundle we need to have only the clientName
      // because open-api-generator will use this to determine the name of the client
      specMethod.tags = [clientName];

      // Doc special cases
      if (!withDoc || !bundledDocSpec) {
        continue;
      }

      const docMethod = bundledDocSpec.paths[pathKey][method];
      if (docMethod.summary) {
        // Remove dot at the end of summary for better sidebar display
        docMethod.summary = docMethod.summary.replace(/\.$/gm, '');
      }

      if (!docMethod.tags) {
        continue;
      }

      // Checks that specified tags are well defined at root level
      for (const tag of docMethod.tags) {
        if (tag === clientName) {
          throw new Error(
            `Tag name "${tag}" must be different from client name ${clientName}`
          );
        }
        if (alias && tag === alias) {
          throw new Error(
            `Tag name "${tag} must be different from alias ${alias}`
          );
        }

        const tagExists = tagsDefinitions
          ? tagsDefinitions.find((t) => t.name === tag)
          : null;
        if (!tagExists) {
          throw new Error(
            `Tag "${tag}" in "client[${clientName}] -> operation[${specMethod.operationId}]" is not defined`
          );
        }
      }
    }
  }

  await fsp.writeFile(
    bundledPath,
    yaml.dump(bundledSpec, {
      noRefs: true,
    })
  );

  if (withDoc) {
    const docFolderPath = toAbsolutePath('website/specs');
    if (!(await exists(docFolderPath))) {
      fsp.mkdir(docFolderPath, { recursive: true });
    }

    const pathToSpecDoc = `${docFolderPath}/${clientName}.doc.yml`;
    await fsp.writeFile(
      pathToSpecDoc,
      yaml.dump(bundledDocSpec, {
        noRefs: true,
      })
    );
  }
}

async function lintCommon(useCache: boolean): Promise<void> {
  const spinner = createSpinner('linting common spec');

  let hash = '';
  const cacheFile = toAbsolutePath(`specs/dist/common.cache`);
  if (useCache) {
    const { cacheExists, hash: newCache } = await checkForCache({
      folder: toAbsolutePath('specs/'),
      generatedFiles: [],
      filesToCache: ['common'],
      cacheFile,
    });

    if (cacheExists) {
      spinner.succeed("job skipped, cache found for 'common' spec");
      return;
    }

    hash = newCache;
  }

  await run(`yarn specs:lint common`);

  if (hash) {
    spinner.text = 'storing common spec cache';
    await fsp.writeFile(cacheFile, hash);
  }

  spinner.succeed();
}

/**
 * Creates a lite search spec with the `ALGOLIASEARCH_LITE_OPERATIONS` methods
 * from the `search` spec.
 */
async function buildLiteSpec({
  spec,
  bundledPath,
  outputFormat,
}: {
  spec: string;
  bundledPath: string;
  outputFormat: string;
}): Promise<void> {
  const parsed = yaml.load(
    await fsp.readFile(toAbsolutePath(bundledPath), 'utf8')
  ) as Spec;

  // Filter methods.
  parsed.paths = Object.entries(parsed.paths).reduce(
    (acc, [path, operations]) => {
      for (const [method, operation] of Object.entries(operations)) {
        if (
          method === 'post' &&
          ALGOLIASEARCH_LITE_OPERATIONS.includes(operation.operationId)
        ) {
          return { ...acc, [path]: { post: operation } };
        }
      }

      return acc;
    },
    {} as Spec['paths']
  );

  const liteBundledPath = `specs/bundled/${spec}.${outputFormat}`;
  await fsp.writeFile(toAbsolutePath(liteBundledPath), yaml.dump(parsed));

  await transformBundle({
    bundledPath: toAbsolutePath(liteBundledPath),
    clientName: spec,
    // Lite does not need documentation because it's just a subset
    withDoc: false,
  });
}

/**
 * Build spec file.
 */
async function buildSpec(
  spec: string,
  outputFormat: string,
  useCache: boolean
): Promise<void> {
  const isAlgoliasearch = spec === 'algoliasearch';
  // In case of lite we use a the `search` spec as a base because only its bundled form exists.
  const specBase = isAlgoliasearch ? 'search' : spec;
  const cacheFile = toAbsolutePath(`specs/dist/${spec}.cache`);
  let hash = '';

  const spinner = createSpinner(`starting '${spec}' spec`);

  if (useCache) {
    spinner.text = `checking cache for '${specBase}'`;

    const { cacheExists, hash: newCache } = await checkForCache({
      folder: toAbsolutePath('specs/'),
      generatedFiles: [`bundled/${spec}.yml`],
      filesToCache: [specBase, 'common'],
      cacheFile,
    });

    if (cacheExists) {
      spinner.succeed(`job skipped, cache found for '${specBase}'`);
      return;
    }

    spinner.text = `cache not found for '${specBase}'`;
    hash = newCache;
  }

  // First linting the base
  spinner.text = `linting '${spec}' spec`;
  await run(`yarn specs:fix ${specBase}`);

  // Then bundle the file
  const bundledPath = `specs/bundled/${spec}.${outputFormat}`;
  await run(
    `yarn openapi bundle specs/${specBase}/spec.yml -o ${bundledPath} --ext ${outputFormat}`
  );

  // Add the correct tags to be able to generate the proper client
  if (!isAlgoliasearch) {
    await transformBundle({
      bundledPath: toAbsolutePath(bundledPath),
      clientName: spec,
      withDoc: BUNDLE_WITH_DOC,
    });
  } else {
    await buildLiteSpec({
      spec,
      bundledPath: toAbsolutePath(bundledPath),
      outputFormat,
    });
  }

  // Validate and lint the final bundle
  spinner.text = `validating '${spec}' bundled spec`;
  await run(`yarn openapi lint specs/bundled/${spec}.${outputFormat}`);

  spinner.text = `linting '${spec}' bundled spec`;
  await run(`yarn specs:fix bundled/${spec}.${outputFormat}`);

  if (hash) {
    spinner.text = `storing '${spec}' spec cache`;
    await fsp.writeFile(cacheFile, hash);
  }

  spinner.succeed(`building complete for '${spec}' spec`);
}

export async function buildSpecs(
  clients: string[],
  outputFormat: 'json' | 'yml',
  useCache: boolean
): Promise<void> {
  await fsp.mkdir(toAbsolutePath('specs/dist'), { recursive: true });

  await lintCommon(useCache);

  await Promise.all(
    clients.map((client) => buildSpec(client, outputFormat, useCache))
  );
}
