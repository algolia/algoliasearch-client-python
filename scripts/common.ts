import fsp from 'fs/promises';
import path from 'path';

import { Octokit } from '@octokit/rest';
import execa from 'execa'; // https://github.com/sindresorhus/execa/tree/v5.1.1
import { hashElement } from 'folder-hash';
import { remove } from 'fs-extra';

import openapiConfig from '../config/openapitools.json';
import releaseConfig from '../config/release.config.json';

import { getGitAuthor } from './release/common';
import { createSpinner } from './spinners';
import type {
  CheckForCache,
  CheckForCacheOptions,
  Generator,
  Language,
  RunOptions,
} from './types';

export const MAIN_BRANCH = releaseConfig.mainBranch;
export const OWNER = releaseConfig.owner;
export const REPO = releaseConfig.repo;
export const REPO_URL = `https://github.com/${OWNER}/${REPO}`;
export const TODAY = new Date().toISOString().split('T')[0];

export const CI = Boolean(process.env.CI);
export const DOCKER = Boolean(process.env.DOCKER);
export const BUNDLE_WITH_DOC = process.env.BUNDLE_WITH_DOC === 'true';

// This script is run by `yarn workspace ...`, which means the current working directory is `./script`
export const ROOT_DIR = path.resolve(process.cwd(), '..');

export const ROOT_ENV_PATH = path.resolve(ROOT_DIR, '.env');

// Build `GENERATORS` from the openapitools file
export const GENERATORS = Object.entries(
  openapiConfig['generator-cli'].generators
).reduce(
  (current, [key, { output, ...gen }]) => {
    const language = key.slice(0, key.indexOf('-')) as Language;

    // eslint-disable-next-line no-param-reassign
    current[key] = {
      additionalProperties: {},
      ...gen,
      output: output.replace('#{cwd}/', ''),
      client: key.slice(key.indexOf('-') + 1),
      language,
      key,
    };

    if (language === 'javascript') {
      // eslint-disable-next-line no-param-reassign
      current[key].additionalProperties.packageName = output.substring(
        output.lastIndexOf('/') + 1
      );
    }

    return current;
  },
  {} as Record<string, Generator>
);

export const LANGUAGES = [
  ...new Set(Object.values(GENERATORS).map((gen) => gen.language)),
];

export const CLIENTS = [
  ...new Set(Object.values(GENERATORS).map((gen) => gen.client)),
];

export const CLIENTS_JS_UTILS = [
  'client-common',
  'requester-browser-xhr',
  'requester-fetch',
  'requester-node-http',
];

export async function run(
  command: string,
  { errorMessage, cwd }: RunOptions = {}
): Promise<string> {
  const realCwd = path.resolve(ROOT_DIR, cwd ?? '.');
  try {
    if (isVerbose()) {
      return (
        (
          await execa.command(command, {
            stdout: 'inherit',
            stderr: 'inherit',
            stdin: 'inherit',
            all: true,
            shell: 'bash',
            cwd: realCwd,
          })
        ).all ?? ''
      );
    }
    return (
      (await execa.command(command, { shell: 'bash', all: true, cwd: realCwd }))
        .all ?? ''
    );
  } catch (err) {
    if (errorMessage) {
      throw new Error(`[ERROR] ${errorMessage}`);
    } else {
      // it's already logged in the verbose case
      if (!isVerbose()) {
        // eslint-disable-next-line no-console
        console.log((err as execa.ExecaError).all);
      }
      throw new Error(`command failed: ${command}`);
    }
  }
}

export async function exists(ppath: string): Promise<boolean> {
  try {
    await fsp.stat(ppath);
    return true;
  } catch {
    return false;
  }
}

export function toAbsolutePath(ppath: string): string {
  return path.resolve(ROOT_DIR, ppath);
}

export async function runIfExists(
  scriptFile: string,
  args: string,
  opts: RunOptions = {}
): Promise<string> {
  if (await exists(toAbsolutePath(scriptFile))) {
    return await run(`${scriptFile} ${args}`, opts);
  }
  return '';
}

export async function gitCommit({
  message,
  coAuthors,
  cwd = ROOT_DIR,
}: {
  message: string;
  coAuthors?: string[];
  cwd?: string;
}): Promise<void> {
  const messageWithCoAuthors = coAuthors
    ? `${message}\n\n\n${coAuthors.join('\n')}`
    : message;

  await execa('git', ['commit', '-m', messageWithCoAuthors], {
    cwd,
  });
}

export async function checkForCache({
  folder,
  generatedFiles,
  filesToCache,
  cacheFile,
}: CheckForCacheOptions): Promise<CheckForCache> {
  const cache: CheckForCache = {
    cacheExists: false,
    hash: '',
  };
  const generatedFilesExists = (
    await Promise.all(
      generatedFiles.map((generatedFile) =>
        exists(`${folder}/${generatedFile}`)
      )
    )
  ).every((exist) => exist);

  for (const fileToCache of filesToCache) {
    const fileHash = (await hashElement(`${folder}/${fileToCache}`)).hash;

    cache.hash = `${cache.hash}-${fileHash}`;
  }

  // We only skip if both the cache and the generated file exists
  if (generatedFilesExists && (await exists(cacheFile))) {
    const storedHash = (await fsp.readFile(cacheFile)).toString();
    if (storedHash === cache.hash) {
      return {
        cacheExists: true,
        hash: cache.hash,
      };
    }
  }

  return cache;
}

export async function buildCustomGenerators(): Promise<void> {
  const spinner = createSpinner('building custom generators');

  const cacheFile = toAbsolutePath('generators/.cache');
  const { cacheExists, hash } = await checkForCache({
    folder: toAbsolutePath('generators/'),
    generatedFiles: ['build'],
    filesToCache: ['src', 'build.gradle', 'settings.gradle'],
    cacheFile,
  });

  if (cacheExists) {
    spinner.succeed('job skipped, cache found for custom generators');
    return;
  }

  await run('./gradle/gradlew --no-daemon -p generators assemble');

  if (hash) {
    spinner.text = 'storing custom generators cache';
    await fsp.writeFile(cacheFile, hash);
  }

  spinner.succeed();
}

export async function gitBranchExists(branchName: string): Promise<boolean> {
  return Boolean(await run(`git ls-remote --heads origin ${branchName}`));
}

export async function emptyDirExceptForDotGit(dir: string): Promise<void> {
  for (const file of await fsp.readdir(dir)) {
    if (file !== '.git') {
      await remove(path.resolve(dir, file));
    }
  }
}

export async function runComposerUpdate(): Promise<void> {
  if (!CI) {
    await run(
      'composer update --working-dir=clients/algoliasearch-client-php && composer dump-autoload --working-dir=clients/algoliasearch-client-php'
    );
  }
}

export function ensureGitHubToken(): string {
  // use process.env here to mock with jest
  if (!process.env.GITHUB_TOKEN) {
    throw new Error('Environment variable `GITHUB_TOKEN` does not exist.');
  }
  return process.env.GITHUB_TOKEN;
}

export function getOctokit(): Octokit {
  const token = ensureGitHubToken();
  return new Octokit({
    auth: token,
  });
}

export function wait(waitTime: number): Promise<void> {
  if (waitTime <= 0) {
    return Promise.resolve();
  }
  return new Promise((resolve) => {
    setTimeout(resolve, waitTime);
  });
}

export function createClientName(client: string, language: string): string {
  switch (language) {
    case 'javascript':
      return camelize(client);
    case 'go':
      return client;
    default:
      return capitalize(camelize(client));
  }
}

/**
 * Splits a string for a given `delimiter` (defaults to `-`) and capitalize each
 * parts except the first letter.
 *
 * `search-client` -> `searchClient`.
 */
export function camelize(str: string, delimiter: string = '-'): string {
  return str
    .split(delimiter)
    .map((part, i) => (i === 0 ? part : capitalize(part)))
    .join('');
}

/**
 * Sets the first letter of the given string in capital.
 *
 * `searchClient` -> `SearchClient`.
 */
export function capitalize(str: string): string {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

export async function configureGitHubAuthor(cwd?: string): Promise<void> {
  const { name, email } = getGitAuthor();

  await run(`git config user.name "${name}"`, { cwd });
  await run(`git config user.email "${email}"`, { cwd });
}

let verbose = false;
export function setVerbose(v: boolean): void {
  verbose = v;
}

export function isVerbose(): boolean {
  return verbose;
}
