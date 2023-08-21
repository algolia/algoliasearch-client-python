/* eslint-disable no-console */
import chalk from 'chalk';
import { execaCommand } from 'execa';
import micromatch from 'micromatch';

import clientConfig from '../../config/clients.config.json' assert { type: 'json' };
import { patterns } from '../../config/generation.config.mjs';

async function run(command) {
  return (
    (
      await execaCommand(command, {
        shell: 'bash',
        all: true,
      })
    ).all ?? ''
  );
}

export function getPatterns() {
  const entries = patterns;
  for (const [language, { tests }] of Object.entries(clientConfig)) {
    entries.push(`tests/output/${language}/${tests.outputFolder}/client/**`);
    entries.push(`tests/output/${language}/${tests.outputFolder}/methods/**`);
  }
  return entries;
}

async function preCommit(log) {
  // when merging, we want to stage all the files
  try {
    await run('git merge HEAD');
  } catch (e) {
    if (e.exitCode === 128) {
      console.log('Skipping the pre-commit check because a merge is in progress');
      return;
    }
  }

  const stagedFiles = (await run('git diff --name-only --cached')).split('\n');

  const toUnstage = micromatch.match(stagedFiles, getPatterns());
  if (toUnstage.length === 0) {
    return;
  }

  if (log) {
    toUnstage.forEach((file) =>
      console.log(chalk.black.bgYellow('[INFO]'), `Generated file found, unstaging: ${file}`)
    );
  }
  await run(`git restore --staged ${toUnstage.join(' ')}`);
}

if (import.meta.url.endsWith(process.argv[1]) && process.env.CI !== 'true') {
  preCommit(true).then(() => {
    // Run it twice because of renamed files, the first one delete the renamed one and leaves the deleted file, which is removed by this second pass
    preCommit(false);
  });
}
