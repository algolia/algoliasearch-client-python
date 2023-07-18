/* eslint-disable no-console */
import chalk from 'chalk';
import dotenv from 'dotenv';
import semver from 'semver';

import generationCommitText from '../ci/codegen/text.js';
import { getNbGitDiff } from '../ci/utils.js';
import {
  LANGUAGES,
  ROOT_ENV_PATH,
  run,
  MAIN_BRANCH,
  OWNER,
  REPO,
  getOctokit,
  ensureGitHubToken,
  TODAY,
  CI,
  gitBranchExists,
  setVerbose,
  configureGitHubAuthor,
} from '../common.js';
import { getPackageVersionDefault } from '../config.js';

import { RELEASED_TAG } from './common.js';
import TEXT from './text.js';
import type {
  Versions,
  VersionsBeforeBump,
  PassedCommit,
  Commit,
  Scope,
  Changelog,
} from './types.js';
import { updateAPIVersions, updateDartPackages } from './updateAPIVersions.js';

dotenv.config({ path: ROOT_ENV_PATH });

export const COMMON_SCOPES = ['specs', 'clients'];

// Prevent fetching the same user multiple times
const fetchedUsers: Record<string, string> = {};

export function readVersions(): VersionsBeforeBump {
  return Object.fromEntries(
    LANGUAGES.map((lang) => [lang, { current: getPackageVersionDefault(lang) }])
  );
}

export function getVersionChangesText(versions: Versions): string {
  return LANGUAGES.map((lang) => {
    const { current, releaseType, noCommit, skipRelease, next } =
      versions[lang];

    if (noCommit) {
      return `- ~${lang}: ${current} (${TEXT.noCommit})~`;
    }

    if (!current) {
      return `- ~${lang}: (${TEXT.currentVersionNotFound})~`;
    }

    if (skipRelease) {
      return [
        `- ~${lang}: ${current} -> **\`${releaseType}\` _(e.g. ${next})_**~`,
        TEXT.descriptionForSkippedLang,
      ].join('\n');
    }

    return `- ${lang}: ${current} -> **\`${releaseType}\` _(e.g. ${next})_**`;
  }).join('\n');
}

export function getSkippedCommitsText({
  commitsWithoutLanguageScope,
  commitsWithUnknownLanguageScope,
}: {
  commitsWithoutLanguageScope: string[];
  commitsWithUnknownLanguageScope: string[];
}): string {
  if (
    commitsWithoutLanguageScope.length === 0 &&
    commitsWithUnknownLanguageScope.length === 0
  ) {
    return '_(None)_';
  }

  // GitHub API restrict the size of a PR body, if we send too many commits
  // we might end up with 502 errors when trying to send the pull request
  // So we limit the size of the missed commits
  return `
<p>${TEXT.skippedCommitsDesc}</p>

<details>
  <summary>
    <i>Commits without language scope:</i>
  </summary>

  ${commitsWithoutLanguageScope
    .slice(0, 15)
    .map((commit) => `- ${commit}`)
    .join('\n')}
</details>

<details>
  <summary>
    <i>Commits with unknown language scope:</i>
  </summary>

  ${commitsWithUnknownLanguageScope
    .slice(0, 15)
    .map((commit) => `- ${commit}`)
    .join('\n')}
</details>`;
}

export async function parseCommit(commit: string): Promise<Commit> {
  const [hash, authorEmail, message] = commit.split('|');
  const commitScope = message.slice(0, message.indexOf(':'));
  const typeAndScope = commitScope.match(/(.+)\((.+)\)/);
  const prNumberMatch = message.match(/#(\d+)/);
  const prNumber = prNumberMatch ? parseInt(prNumberMatch[1], 10) : 0;
  let commitMessage = message;

  if (prNumber) {
    commitMessage = message.replace(`(#${prNumber})`, '').trim();
  }

  // We skip generation commits as they do not appear in changelogs
  if (
    message
      .toLocaleLowerCase()
      .startsWith(generationCommitText.commitStartMessage)
  ) {
    return {
      error: 'generation-commit',
    };
  }
  if (!typeAndScope) {
    return {
      error: 'missing-language-scope',
      message,
    };
  }

  const scope = typeAndScope[2] as Scope;
  if (![...LANGUAGES, ...COMMON_SCOPES].includes(scope)) {
    return { error: 'unknown-language-scope', message };
  }

  // Retrieve the author GitHub username if publicly available
  if (!fetchedUsers[authorEmail] && prNumber) {
    const octokit = getOctokit();
    const { data } = await octokit.pulls.get({
      owner: OWNER,
      repo: REPO,
      pull_number: prNumber,
    });

    if (data.user) {
      fetchedUsers[
        authorEmail
      ] = `[@${data.user.login}](https://github.com/${data.user.login}/)`;
    }
  }

  return {
    hash,
    type: typeAndScope[1], // `fix` | `feat` | `chore` | ...
    scope, // `clients` | `specs` | `javascript` | `php` | `java` | ...
    message: commitMessage,
    prNumber,
    raw: commit,
    author: fetchedUsers[authorEmail],
  };
}

/**
 * Returns the next version of the client.
 */
export function getNextVersion(
  current: string,
  releaseType: semver.ReleaseType | null
): string {
  if (releaseType === null) {
    return current;
  }

  let nextVersion: string | null = current;

  // snapshots should not be bumped
  if (current.endsWith('-SNAPSHOT')) {
    nextVersion = current;
  } else {
    nextVersion = semver.inc(current, releaseType);
  }

  if (!nextVersion) {
    throw new Error(
      `Unable to bump version: '${current}' with release type: '${releaseType}'`
    );
  }

  console.log(
    `    > Next version is '${nextVersion}', release type: '${releaseType}'`
  );

  return nextVersion;
}

/* eslint-disable no-param-reassign */
export function decideReleaseStrategy({
  versions,
  commits,
}: {
  versions: VersionsBeforeBump;
  commits: PassedCommit[];
}): Versions {
  return Object.entries(versions).reduce(
    (versionsWithReleaseType: Versions, [lang, version]) => {
      const commitsPerLang = commits.filter(
        (commit) =>
          commit.scope === lang || COMMON_SCOPES.includes(commit.scope)
      );
      const currentVersion = versions[lang].current;

      if (commitsPerLang.length === 0) {
        versionsWithReleaseType[lang] = {
          ...version,
          noCommit: true,
          releaseType: null,
          next: getNextVersion(currentVersion, null),
        };
        return versionsWithReleaseType;
      }

      console.log(`Deciding next version bump for ${lang}.`);

      // snapshots should not be bumped as prerelease
      if (
        semver.prerelease(currentVersion) &&
        !currentVersion.endsWith('-SNAPSHOT')
      ) {
        // if version is like 0.1.2-beta.1, it increases to 0.1.2-beta.2, even if there's a breaking change.
        versionsWithReleaseType[lang] = {
          ...version,
          releaseType: 'prerelease',
          next: getNextVersion(currentVersion, 'prerelease'),
        };
        return versionsWithReleaseType;
      }

      if (
        commitsPerLang.some((commit) =>
          commit.message.includes('BREAKING CHANGE')
        )
      ) {
        versionsWithReleaseType[lang] = {
          ...version,
          releaseType: 'major',
          next: getNextVersion(currentVersion, 'major'),
        };
        return versionsWithReleaseType;
      }

      const commitTypes = new Set(commitsPerLang.map(({ type }) => type));
      if (commitTypes.has('feat')) {
        versionsWithReleaseType[lang] = {
          ...version,
          releaseType: 'minor',
          next: getNextVersion(currentVersion, 'minor'),
        };
        return versionsWithReleaseType;
      }

      versionsWithReleaseType[lang] = {
        ...version,
        releaseType: 'patch',
        ...(commitTypes.has('fix') ? undefined : { skipRelease: true }),
        next: getNextVersion(currentVersion, 'patch'),
      };
      return versionsWithReleaseType;
    },
    {}
  );
}
/* eslint-enable no-param-reassign */

/**
 * Returns commits separated in categories used to compute the next release version.
 *
 * Gracefully exits if there is none.
 */
async function getCommits(): Promise<{
  validCommits: PassedCommit[];
  skippedCommits: string;
}> {
  // Reading commits since last release
  const latestCommits = (
    await run(
      `git log --pretty=format:"%h|%ae|%s" ${RELEASED_TAG}..${MAIN_BRANCH}`
    )
  )
    .split('\n')
    .filter(Boolean);

  const commitsWithoutLanguageScope: string[] = [];
  const commitsWithUnknownLanguageScope: string[] = [];
  const validCommits: PassedCommit[] = [];

  for (const commitMessage of latestCommits) {
    const commit = await parseCommit(commitMessage);

    if ('error' in commit) {
      if (commit.error === 'missing-language-scope') {
        commitsWithoutLanguageScope.push(commit.message);
      }

      if (commit.error === 'unknown-language-scope') {
        commitsWithUnknownLanguageScope.push(commit.message);
      }

      continue;
    }

    validCommits.push(commit);
  }

  if (validCommits.length === 0) {
    console.log(
      chalk.black.bgYellow('[INFO]'),
      `Skipping release because no valid commit has been added since \`released\` tag.`
    );
    // eslint-disable-next-line no-process-exit
    process.exit(0);
  }

  return {
    validCommits,
    skippedCommits: getSkippedCommitsText({
      commitsWithoutLanguageScope,
      commitsWithUnknownLanguageScope,
    }),
  };
}

/**
 * Ensure the release environment is correct before triggering.
 */
async function prepareGitEnvironment(): Promise<void> {
  ensureGitHubToken();

  // We allow bypassing those requirements for local tests
  if (process.env.LOCAL_TEST_DEV) {
    return;
  }

  if (CI) {
    await configureGitHubAuthor();
  }

  if ((await run('git rev-parse --abbrev-ref HEAD')) !== MAIN_BRANCH) {
    throw new Error(
      `You can run this script only from \`${MAIN_BRANCH}\` branch.`
    );
  }

  if (
    (await getNbGitDiff({
      head: null,
    })) !== 0
  ) {
    throw new Error(
      'Working directory is not clean. Commit all the changes first.'
    );
  }

  await run(`git rev-parse --verify refs/tags/${RELEASED_TAG}`, {
    errorMessage: '`released` tag is missing in this repository.',
  });

  console.log('Pulling from origin...');
  await run('git fetch origin');
  await run('git pull');

  // Remove the local tag, and fetch it from the remote.
  // We move the `released` tag as we release, so we need to make it up-to-date.
  await run(`git tag -d ${RELEASED_TAG}`);
  await run(
    `git fetch origin refs/tags/${RELEASED_TAG}:refs/tags/${RELEASED_TAG}`
  );
}

async function createReleasePR(): Promise<void> {
  await prepareGitEnvironment();

  console.log('Searching for commits since last release...');
  const { validCommits, skippedCommits } = await getCommits();

  const versions = decideReleaseStrategy({
    versions: readVersions(),
    commits: validCommits,
  });
  const versionChanges = getVersionChangesText(versions);

  console.log('Creating changelogs for all languages...');
  const changelog: Changelog = LANGUAGES.filter(
    (lang) => lang !== 'dart'
  ).reduce((newChangelog, lang) => {
    if (versions[lang].noCommit) {
      return newChangelog;
    }

    const changelogCommits: string[] = [];
    for (const validCommit of validCommits) {
      if (
        validCommit.scope !== lang &&
        !COMMON_SCOPES.includes(validCommit.scope)
      ) {
        continue;
      }

      const changelogCommit = [
        `[${validCommit.hash}](https://github.com/${OWNER}/${REPO}/commit/${validCommit.hash})`,
        validCommit.message,
        validCommit.prNumber
          ? `([#${validCommit.prNumber}](https://github.com/${OWNER}/${REPO}/pull/${validCommit.prNumber}))`
          : undefined,
        validCommit.author ? `by ${validCommit.author}` : undefined,
      ]
        .filter(Boolean)
        .join(' ');

      changelogCommits.push(`- ${changelogCommit}`);
    }

    return {
      ...newChangelog,
      [lang]: changelogCommits.join('\n'),
    };
  }, {} as Changelog);

  console.log('Updating config files...');
  await updateAPIVersions(versions, changelog);
  await updateDartPackages();

  const headBranch = `chore/prepare-release-${TODAY}`;
  console.log(`Switching to branch: ${headBranch}`);
  if (await gitBranchExists(headBranch)) {
    await run(`git fetch origin ${headBranch}`);
    await run(`git push -d origin ${headBranch}`);
  }

  await run(`git checkout -b ${headBranch}`);

  setVerbose(true);
  console.log(`Pushing updated changes to: ${headBranch}`);
  const commitMessage = generationCommitText.commitPrepareReleaseMessage;
  await run('git add .');
  if (process.env.LOCAL_TEST_DEV) {
    await run(`git commit -m "${commitMessage} [skip ci]"`);
  } else {
    await run(`CI=false git commit -m "${commitMessage}"`);
  }

  // cleanup all the changes to the generated files (the ones not commited because of the pre-commit hook)
  await run(`git checkout .`);

  await run(`git push origin ${headBranch}`);
  await run(`git checkout ${MAIN_BRANCH}`);

  console.log('Creating prepare release pull request...');
  const octokit = getOctokit();
  const { data } = await octokit.pulls.create({
    owner: OWNER,
    repo: REPO,
    title: generationCommitText.commitPrepareReleaseMessage,
    body: [
      TEXT.header,
      TEXT.summary,
      TEXT.versionChangeHeader,
      versionChanges,
      TEXT.skippedCommitsHeader,
      skippedCommits,
    ].join('\n\n'),
    base: 'main',
    head: headBranch,
  });

  console.log('Assigning team members to the PR...');
  await octokit.pulls.requestReviewers({
    owner: OWNER,
    repo: REPO,
    pull_number: data.number,
    team_reviewers: ['api-clients-automation'],
  });

  console.log(`Release PR #${data.number} is ready for review.`);
  console.log(`  > ${data.url}`);
}

if (import.meta.url.endsWith(process.argv[1])) {
  setVerbose(false);
  createReleasePR();
}
