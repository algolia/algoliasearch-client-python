import { buildSpecs } from './buildSpecs.js';
import { buildCustomGenerators, CI, run } from './common.js';
import { getCustomGenerator, getLanguageFolder } from './config.js';
import { formatter } from './formatter.js';
import { generateOpenapitools, removeExistingCodegen } from './pre-gen/index.js';
import { createSpinner } from './spinners.js';
import type { Generator } from './types.js';

async function preGen(gen: Generator): Promise<void> {
  await removeExistingCodegen(gen);
}

async function generateClient({ language, key }: Generator): Promise<void> {
  const customGenerator = getCustomGenerator(language);
  await run(
    `yarn openapi-generator-cli ${
      customGenerator
        ? '--custom-generator=generators/build/libs/algolia-java-openapi-generator-1.0.0.jar'
        : ''
    } generate --generator-key ${key}`
  );
}

export async function generate(generators: Generator[]): Promise<void> {
  if (!CI) {
    const clients = [...new Set(generators.map((gen) => gen.client))];
    await buildSpecs(clients, 'yml', true);
  }

  await generateOpenapitools(generators);

  const langs = [...new Set(generators.map((gen) => gen.language))];
  const useCustomGenerator = langs.map((lang) => getCustomGenerator(lang)).some(Boolean);
  if (useCustomGenerator) {
    await buildCustomGenerators();
  }

  for (const gen of generators) {
    const spinner = createSpinner(`pre-gen ${gen.key}`);
    await preGen(gen);

    spinner.text = `generating ${gen.key}`;
    await generateClient(gen);

    spinner.succeed();
  }

  for (const lang of langs) {
    let folder = getLanguageFolder(lang);

    // We have scoped output folder for JavaScript which allow us to
    // avoid linting the whole client, only the part that changed
    if (lang === 'javascript') {
      folder = generators.reduce((folders, gen) => {
        if (gen.language === 'javascript') {
          return `${folders} ${gen.output}`;
        }

        return folders;
      }, '');
    }

    await formatter(lang, folder);
  }
}
