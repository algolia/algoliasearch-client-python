/* eslint-disable no-console */
import { run, OWNER, REPO, getOctokit } from '../../common.js';

import commentText from './text.js';

const BOT_NAME = 'algolia-bot';
const PR_NUMBER = parseInt(process.env.PR_NUMBER || '0', 10);

const args = process.argv.slice(2);
const allowedTriggers = [
  'notification',
  'codegen',
  'noGen',
  'cleanup',
] as const;

type Trigger = (typeof allowedTriggers)[number];

export async function getCommentBody(trigger: Trigger): Promise<string> {
  let generatedBranch = await run('git branch --show-current');

  // `cleanup` is triggered on PR close, which runs on `main`, so we lose the
  // branch name context at this point
  if (generatedBranch === 'main' && process.env.HEAD_BRANCH) {
    generatedBranch = `generated/${process.env.HEAD_BRANCH}`;
  }

  const baseBranch = generatedBranch.replace('generated/', '');
  const baseCommit = await run(`git show ${baseBranch} -s --format=%H`);
  const generatedCommit = await run(
    `git show ${generatedBranch} -s --format=%H`
  );

  return `${commentText[trigger].header}

${commentText[trigger].body(
  generatedCommit,
  generatedBranch,
  baseCommit,
  PR_NUMBER
)}`;
}

/**
 * Adds or updates a comment on a pull request.
 */
export async function upsertGenerationComment(trigger: Trigger): Promise<void> {
  const octokit = getOctokit();
  if (!trigger || allowedTriggers.includes(trigger) === false) {
    throw new Error(
      `'upsertGenerationComment' requires a 'trigger' parameter (${allowedTriggers.join(
        ' | '
      )}).`
    );
  }

  if (!PR_NUMBER) {
    throw new Error(
      '`upsertGenerationComment` requires a `PR_NUMBER` environment variable.'
    );
  }

  console.log(`Upserting comment for trigger: ${trigger}`);

  try {
    const baseOctokitConfig = {
      owner: OWNER,
      repo: REPO,
      issue_number: PR_NUMBER,
      body: await getCommentBody(trigger),
    };

    // Search for a previous comment from our bot.
    const previousComment = await octokit.rest.issues
      .listComments(baseOctokitConfig)
      .then(
        (res) =>
          res.data.filter(
            (comment) =>
              comment.user?.login === BOT_NAME &&
              (comment.body?.startsWith(commentText.codegen.header) ||
                comment.body?.startsWith(commentText.noGen.header) ||
                comment.body?.startsWith(commentText.notification.header))
          )[0]
      );

    if (previousComment?.id) {
      console.log(`Previous bot comment found ${previousComment.id}.`);

      await octokit.rest.issues.updateComment({
        ...baseOctokitConfig,
        comment_id: previousComment.id,
      });

      return;
    }

    console.log('Creating new comment.');
    await octokit.rest.issues.createComment(baseOctokitConfig);
  } catch (e) {
    throw new Error(`Error with GitHub API: ${e}`);
  }
}

if (import.meta.url.endsWith(process.argv[1])) {
  upsertGenerationComment(args[0] as Trigger);
}
