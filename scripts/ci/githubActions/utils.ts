/* eslint-disable no-console */
import crypto from 'crypto';

import * as core from '@actions/core';
import { hashElement } from 'folder-hash';

import { toAbsolutePath } from '../../common.js';
import { getNbGitDiff } from '../utils.js';
/**
 * This cache key holds the hash of the common dependencies of all the clients.
 */
const commonCacheKey = (async function (): Promise<string> {
  const ghHash = await hashElement(toAbsolutePath('.github'), {
    encoding: 'hex',
    folders: { exclude: ['ISSUE_TEMPLATE'] },
    files: { include: ['*.yml', '.cache_version'] },
  });
  const scriptsHash = await hashElement(toAbsolutePath('scripts'), {
    encoding: 'hex',
    folders: { exclude: ['docker', '__tests__'] },
    files: { include: ['**'] },
  });
  const configHash = await hashElement(toAbsolutePath('.'), {
    encoding: 'hex',
    folders: { include: ['config'] },
    files: {
      include: [
        'openapitools.json',
        'clients.config.json',
        'generation.config.mjs',
        'base.tsconfig.json',
      ],
    },
  });
  const ctsHash = await hashElement(toAbsolutePath('tests'), {
    encoding: 'hex',
    folders: { include: ['CTS'] },
    files: { include: ['**'] },
  });
  const depsHash = await hashElement(toAbsolutePath('.'), {
    encoding: 'hex',
    files: { include: ['yarn.lock'] },
  });

  return `${ghHash.hash}-${scriptsHash.hash}-${configHash.hash}-${depsHash.hash}-${ctsHash.hash}`;
})();

/**
 * Compute a cache key based on the changes in the `paths` array of dependency.
 *
 * The `paths` parameter is an array of string, that needs to be treated as dependencies.
 */
export async function computeCacheKey(baseName: string, paths: string[]): Promise<string> {
  let hash = '';

  for (const path of paths) {
    const pathHash = await hashElement(toAbsolutePath(path), {
      encoding: 'hex',
      files: {
        include: ['**'],
      },
    });

    hash += `-${pathHash.hash}`;
  }

  return `${baseName}-${crypto
    .createHash('sha256')
    .update(`${await commonCacheKey}-${hash}`)
    .digest('hex')}`;
}

/**
 * Determines if changes have been found in the `dependencies`, compared to the `baseBranch`.
 *
 * If `output` is true, it will set log the variable values for the CI.
 */
export async function isBaseChanged(
  baseBranch: string,
  dependencies: Record<string, string[]>,
  output?: boolean
): Promise<boolean> {
  for (const [key, path] of Object.entries(dependencies)) {
    const diff = await getNbGitDiff({
      branch: baseBranch,
      path: path.join(' '),
    });

    if (output) {
      console.log(`Found ${diff} changes for '${key}'`);
      core.setOutput(key, diff);
    } else if (diff > 0) {
      return true;
    }
  }

  return false;
}
