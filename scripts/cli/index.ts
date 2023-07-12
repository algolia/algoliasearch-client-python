import { Argument, program } from 'commander';

import { buildClients } from '../buildClients.js';
import { buildSpecs } from '../buildSpecs.js';
import { CI, DOCKER, LANGUAGES, setVerbose } from '../common.js';
import { ctsGenerateMany } from '../cts/generate.js';
import { runCts } from '../cts/runCts.js';
import { formatter } from '../formatter.js';
import { generate } from '../generate.js';
import { playground } from '../playground.js';

import type { LangArg } from './utils.js';
import {
  ALL,
  getClientChoices,
  generatorList,
  prompt,
  PROMPT_CLIENTS,
  PROMPT_LANGUAGES,
} from './utils.js';

if (!CI && !DOCKER) {
  // eslint-disable-next-line no-console
  console.log('You should run scripts via the docker container, see README.md');
  // eslint-disable-next-line no-process-exit
  process.exit(1);
}

const args = {
  language: new Argument('[language]', 'The language').choices(
    PROMPT_LANGUAGES
  ),
  clients: new Argument('[client...]', 'The client').choices(
    getClientChoices('all')
  ),
  client: new Argument('[client]', 'The client').choices(PROMPT_CLIENTS),
};

const flags = {
  verbose: {
    flag: '-v, --verbose',
    description: 'make the generation verbose',
  },
  interactive: {
    flag: '-i, --interactive',
    description: 'open prompt to query parameters',
  },
  skipCache: {
    flag: '-s, --skip-cache',
    description: 'skip cache checking to force building specs',
  },
  outputType: {
    flag: '-json, --output-json',
    description: 'outputs the spec in JSON instead of yml',
  },
};

program.name('cli');

program
  .command('generate')
  .description('Generate a specified client')
  .addArgument(args.language)
  .addArgument(args.clients)
  .option(flags.verbose.flag, flags.verbose.description)
  .option(flags.interactive.flag, flags.interactive.description)
  .action(
    async (langArg: LangArg, clientArg: string[], { verbose, interactive }) => {
      const { language, client, clientList } = await prompt({
        langArg,
        clientArg,
        interactive,
      });

      setVerbose(Boolean(verbose));

      await generate(generatorList({ language, client, clientList }));
    }
  );

const buildCommand = program.command('build');

buildCommand
  .command('clients')
  .description('Build a specified client')
  .addArgument(args.language)
  .addArgument(args.clients)
  .option(flags.verbose.flag, flags.verbose.description)
  .option(flags.interactive.flag, flags.interactive.description)
  .action(
    async (langArg: LangArg, clientArg: string[], { verbose, interactive }) => {
      const { language, client, clientList } = await prompt({
        langArg,
        clientArg,
        interactive,
      });

      setVerbose(Boolean(verbose));

      await buildClients(generatorList({ language, client, clientList }));
    }
  );

buildCommand
  .command('specs')
  .description('Build a specified spec')
  .addArgument(args.clients)
  .option(flags.verbose.flag, flags.verbose.description)
  .option(flags.interactive.flag, flags.interactive.description)
  .option(flags.skipCache.flag, flags.skipCache.description)
  .option(flags.outputType.flag, flags.outputType.description)
  .action(
    async (
      clientArg: string[],
      { verbose, interactive, skipCache, outputJson }
    ) => {
      const { client, clientList } = await prompt({
        langArg: ALL,
        clientArg,
        interactive,
      });

      setVerbose(Boolean(verbose));

      const outputFormat = outputJson ? 'json' : 'yml';

      // ignore cache when building from cli
      await buildSpecs(
        client[0] === ALL ? clientList : client,
        outputFormat,
        !skipCache
      );
    }
  );

const ctsCommand = program.command('cts');

ctsCommand
  .command('generate')
  .description('Generate the CTS tests')
  .addArgument(args.language)
  .addArgument(args.clients)
  .option(flags.verbose.flag, flags.verbose.description)
  .option(flags.interactive.flag, flags.interactive.description)
  .action(
    async (langArg: LangArg, clientArg: string[], { verbose, interactive }) => {
      const { language, client, clientList } = await prompt({
        langArg,
        clientArg,
        interactive,
      });

      setVerbose(Boolean(verbose));

      await ctsGenerateMany(generatorList({ language, client, clientList }));
    }
  );

ctsCommand
  .command('run')
  .description('Run the tests for the CTS')
  .addArgument(args.language)
  .option(flags.verbose.flag, flags.verbose.description)
  .option(flags.interactive.flag, flags.interactive.description)
  .action(async (langArg: LangArg, { verbose, interactive }) => {
    const { language } = await prompt({
      langArg,
      clientArg: [ALL],
      interactive,
    });

    setVerbose(Boolean(verbose));

    await runCts(language === ALL ? LANGUAGES : [language]);
  });

program
  .command('playground')
  .description('Run the playground')
  .addArgument(args.language)
  .addArgument(args.client)
  .option(flags.interactive.flag, flags.interactive.description)
  .action(async (langArg: LangArg, cliClient: string, { interactive }) => {
    const { language, client } = await prompt({
      langArg,
      clientArg: [cliClient],
      interactive,
    });

    setVerbose(false);

    await playground({
      language,
      client: client[0],
    });
  });

program
  .command('format')
  .description('Format the specified folder for a specific language')
  .addArgument(args.language)
  .argument('folder', 'The folder to format')
  .option(flags.verbose.flag, flags.verbose.description)
  .action(async (language: string, folder: string, { verbose }) => {
    setVerbose(Boolean(verbose));

    await formatter(language, folder);
  });

program.parse();
