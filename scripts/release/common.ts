import fsp from 'fs/promises';

import config from '../../config/release.config.json' assert { type: 'json' };

export const RELEASED_TAG = config.releasedTag;
export const TEAM_SLUG = config.teamSlug;

export function getTargetBranch(language: string): string {
  return config.targetBranch[language] || config.defaultTargetBranch;
}

export function getGitAuthor(): { name: string; email: string } {
  return config.gitAuthor;
}

/**
 * Reads a JSON file and returns its parsed data.
 *
 * @param ppath - The absolute path to the file.
 */
export async function readJsonFile(
  ppath: string
): Promise<Record<string, any>> {
  return JSON.parse(
    await fsp.readFile(ppath, {
      encoding: 'utf-8',
    })
  );
}

/**
 * Writes `data` in a file at the given `ppath`, appends a newline at the end of the file.
 *
 * @param ppath - The absolute path to the file.
 * @param data - The data to store.
 */
export async function writeJsonFile(
  ppath: string,
  data: Record<string, any>
): Promise<void> {
  await fsp.writeFile(ppath, JSON.stringify(data, null, 2).concat('\n'));
}
