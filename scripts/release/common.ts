import fsp from 'fs/promises';

import config from '../../config/release.config.json' assert { type: 'json' };
import { run } from '../common.js';

export function getLastReleasedTag(): Promise<string> {
  return run(`git describe --abbrev=0 --tags --match "${config.releasedTag}*"`);
}

export function getNewReleasedTag(): string {
  const lastCommitHash = run(`git rev-parse --short HEAD`);
  const now = new Date().toISOString().split('T')[0];

  return `${config.releasedTag}-${now}-${lastCommitHash}`;
}

export function getTargetBranch(language: string): string {
  return config.targetBranch[language] || config.defaultTargetBranch;
}

export function getGitAuthor(): { name: string; email: string } {
  return config.gitAuthor;
}

/**
 * Writes `data` in a file at the given `ppath`, appends a newline at the end of the file.
 *
 * @param ppath - The absolute path to the file.
 * @param data - The data to store.
 */
export async function writeJsonFile(ppath: string, data: Record<string, any>): Promise<void> {
  await fsp.writeFile(ppath, JSON.stringify(data, null, 2).concat('\n'));
}
