/* eslint-disable no-console */
import { copy } from 'fs-extra';

import {
  emptyDirExceptForDotGit,
  gitCommit,
  LANGUAGES,
  run,
  toAbsolutePath,
  REPO_URL,
  ensureGitHubToken,
  configureGitHubAuthor,
  setVerbose,
} from '../../common.js';
import { getLanguageFolder, getPackageVersionDefault } from '../../config.js';
import { getNewReleasedTag } from '../../release/common.js';
import { cloneRepository, getNbGitDiff } from '../utils.js';

import text, { commitStartRelease } from './text.js';

export function cleanUpCommitMessage(commitMessage: string, version: string): string {
  if (commitMessage.startsWith(commitStartRelease)) {
    return `chore: release ${version}`;
  }

  const isCodeGenCommit = commitMessage.startsWith(text.commitStartMessage);

  if (isCodeGenCommit) {
    const hash = commitMessage.split(text.commitStartMessage)[1].replace('. [skip ci]', '').trim();

    if (!hash) {
      return commitMessage;
    }

    return [
      `${text.commitStartMessage} ${hash.substring(0, 8)}. [skip ci]`,
      `${REPO_URL}/commit/${hash}`,
    ].join('\n\n');
  }

  const prCommit = commitMessage.match(/(.+)\s\(#(\d+)\)$/);

  if (!prCommit) {
    return commitMessage;
  }

  return [prCommit[1], `${REPO_URL}/pull/${prCommit[2]}`].join('\n\n');
}

async function spreadGeneration(): Promise<void> {
  const githubToken = ensureGitHubToken();

  console.log('Starting spread generation script...');
  const lastCommitMessage = await run('git log -1 --format="%s"');
  const author = (await run('git log -1 --format="Co-authored-by: %an <%ae>"')).trim();
  const coAuthors = (await run('git log -1 --format="%(trailers:key=Co-authored-by)"'))
    .split('\n')
    .map((coAuthor) => coAuthor.trim())
    .filter(Boolean);

  const IS_RELEASE_COMMIT = lastCommitMessage.startsWith(commitStartRelease);
  console.log('Spreading code to the following repositories:', LANGUAGES.join(' | '));

  // At this point, we know the release will happen on at least one client
  // So we want to set the released tag at the monorepo level too.
  if (IS_RELEASE_COMMIT) {
    console.log('Creating new `released` tag for latest commit');
    await run(`git tag ${getNewReleasedTag()}`);
    await run('git push --tags');
  }

  for (const lang of LANGUAGES) {
    try {
      const { tempGitDir } = await cloneRepository({
        lang,
        githubToken,
        tempDir: process.env.RUNNER_TEMP!,
      });

      const clientPath = toAbsolutePath(getLanguageFolder(lang));
      await emptyDirExceptForDotGit(tempGitDir);
      await copy(clientPath, tempGitDir, { preserveTimestamps: true });

      if (
        (await getNbGitDiff({
          head: null,
          cwd: tempGitDir,
        })) === 0
      ) {
        console.log(`❎ Skipping ${lang} repository, because there is no change.`);
        continue;
      } else {
        console.log(`✅ Spreading code to the ${lang} repository.`);
      }

      const version = getPackageVersionDefault(lang);
      const commitMessage = cleanUpCommitMessage(lastCommitMessage, version);

      await configureGitHubAuthor(tempGitDir);

      await run('git add .', { cwd: tempGitDir });
      await gitCommit({
        message: commitMessage,
        coAuthors: [author, ...coAuthors],
        cwd: tempGitDir,
      });
      await run('git push', { cwd: tempGitDir });

      // In case of a release commit, we also want to update tags on the clients repositories
      if (IS_RELEASE_COMMIT) {
        // Go needs a 'v' prefix for tags.
        const tagVersion = lang === 'go' ? `v${version}` : version;

        console.log(
          `Processing release commit, creating new release tag ('${version}') for '${lang}' repository.`
        );

        // we always want to delete the tag in case it exists
        await run(`git tag -d ${tagVersion} || true`, { cwd: tempGitDir });
        await run(`git tag ${tagVersion} HEAD`, { cwd: tempGitDir });
        await run('git push --tags', { cwd: tempGitDir });
      }

      console.log(`✅ Code generation successfully pushed to ${lang} repository.`);
    } catch (e) {
      console.error(`Release failed for language ${lang}: ${e}`);
    }
  }
}

if (import.meta.url.endsWith(process.argv[1])) {
  setVerbose(false);
  spreadGeneration();
}
