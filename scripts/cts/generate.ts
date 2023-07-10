import { buildSpecs } from '../buildSpecs';
import { buildCustomGenerators, CI, run, toAbsolutePath } from '../common';
import { getTestOutputFolder } from '../config';
import { formatter } from '../formatter';
import { generateOpenapitools } from '../pre-gen';
import { createSpinner } from '../spinners';
import type { Generator } from '../types';

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
      await run('yarn install', { cwd: 'tests/output/javascript' });
    }

    await formatter(lang, toAbsolutePath(`tests/output/${lang}`));
  }
}
