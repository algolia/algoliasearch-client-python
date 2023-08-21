import fsp from 'fs/promises';
import { resolve } from 'path';

import { run } from '../common.js';
import { getGitHubUrl } from '../config.js';
import { getTargetBranch } from '../release/common.js';
import type { Language } from '../types.js';

/**
 * Returns the number of diff between a `branch` and its `HEAD` for the given `path`.
 *
 * @param opts - Parameters of the method.
 * @param opts.branch - The branch to trigger the operation, defaults to '' (current branch).
 * @param opts.head - The head to compare the operation, defaults to 'HEAD', providing 'null' will check for unstaged changes.
 * @param opts.path - The path to look for changes in, defaults to '.' (current directory).
 * @param opts.cwd - The path to run the command, defaults to current directory.
 */
export async function getNbGitDiff({
  branch = '',
  head = 'HEAD',
  path = '.',
  cwd,
}: Partial<{
  branch: string;
  head: string | null;
  path: string;
  cwd: string;
}>): Promise<number> {
  const checkHead = head === null ? '' : `...${head}`;

  return parseInt(
    (
      await run(`git add -N . && git diff --shortstat ${branch}${checkHead} -- ${path} | wc -l`, {
        cwd,
      })
    ).trim(),
    10
  );
}

export async function cloneRepository({
  lang,
  githubToken,
  tempDir,
}: {
  lang: Language;
  githubToken: string;
  tempDir: string;
}): Promise<{ tempGitDir: string }> {
  const targetBranch = getTargetBranch(lang);

  const gitHubUrl = getGitHubUrl(lang, { token: githubToken });
  const tempGitDir = resolve(tempDir, lang);
  await fsp.rm(tempGitDir, { force: true, recursive: true });
  await run(`git clone --depth 1 --branch ${targetBranch} ${gitHubUrl} ${tempGitDir}`);

  return {
    tempGitDir,
  };
}
