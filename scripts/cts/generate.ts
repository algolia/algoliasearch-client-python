import { buildSpecs } from '../buildSpecs.js';
import { buildCustomGenerators, CI, run, toAbsolutePath } from '../common.js';
import { getTestOutputFolder } from '../config.js';
import { formatter } from '../formatter.js';
import { generateOpenapitools } from '../pre-gen/index.js';
import { createSpinner } from '../spinners.js';
import type { Generator } from '../types.js';

async function ctsGenerate(gen: Generator): Promise<void> {
  const spinner = createSpinner(`generating CTS for ${gen.key}`);

  await run(
    `yarn openapi-generator-cli --custom-generator=generators/build/libs/algolia-java-openapi-generator-1.0.0.jar generate \
     -g algolia-cts -i specs/bundled/${gen.client}.yml --additional-properties="language=${gen.language},client=${gen.client}"`
  );
  spinner.succeed();
}

export async function ctsGenerateMany(generators: Generator[]): Promise<void> {
  if (!CI) {
    const clients = [...new Set(generators.map((gen) => gen.client))];
    await buildSpecs(clients, 'yml', true);
  }

  await generateOpenapitools(generators);
  await buildCustomGenerators();

  for (const gen of generators) {
    if (!getTestOutputFolder(gen.language)) {
      continue;
    }
    await ctsGenerate(gen);
  }

  const langs = [...new Set(generators.map((gen) => gen.language))];
  for (const lang of langs) {
    if (!getTestOutputFolder(lang)) {
      continue;
    }

    if (lang === 'javascript') {
      await run('YARN_ENABLE_IMMUTABLE_INSTALLS=false yarn install', {
        cwd: 'tests/output/javascript',
      });
    }

    if (lang === 'go') {
      await run('go mod tidy', {
        cwd: 'tests/output/go',
      });
    }

    await formatter(lang, toAbsolutePath(`tests/output/${lang}`));
  }
}
