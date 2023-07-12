import { jest } from '@jest/globals';

import * as common from '../../../common.js';
import { cleanGeneratedBranch } from '../cleanGeneratedBranch.js';
import { pushGeneratedCode } from '../pushGeneratedCode.js';
import commentText from '../text.js';

const mockedRun = jest.fn(() => {
  return Promise.resolve('');
});

jest.unstable_mockModule('../../../common.js', () => ({
  ...common,
  run: mockedRun,
}));
const { upsertGenerationComment, getCommentBody } = await import(
  '../upsertGenerationComment.js'
);

describe('codegen', () => {
  describe('cleanGeneratedBranch', () => {
    it('throws without parameters', async () => {
      await expect(
        // @ts-expect-error a parameter is required
        cleanGeneratedBranch()
      ).rejects.toThrow(
        'The base branch should be passed as a cli parameter of the `cleanGeneratedBranch` script.'
      );
    });
  });

  describe('pushGeneratedCode', () => {
    it('throws without GITHUB_TOKEN environment variable', async () => {
      process.env.GITHUB_TOKEN = '';
      await expect(pushGeneratedCode()).rejects.toThrow(
        'Environment variable `GITHUB_TOKEN` does not exist.'
      );
    });
  });

  describe('upsertGenerationComment', () => {
    beforeAll(() => {
      process.env.GITHUB_TOKEN = 'mocked';
    });

    it('throws without parameter', async () => {
      await expect(
        // @ts-expect-error a parameter is required
        upsertGenerationComment()
      ).rejects.toThrow(
        "'upsertGenerationComment' requires a 'trigger' parameter (notification | codegen | noGen | cleanup)."
      );
    });

    it('throws without PR_NUMBER environment variable', async () => {
      await expect(upsertGenerationComment('codegen')).rejects.toThrow(
        '`upsertGenerationComment` requires a `PR_NUMBER` environment variable.'
      );
    });
  });

  describe('getCommentBody', () => {
    describe('setup', () => {
      it('returns the right comment for a `notification` trigger', async () => {
        expect(await getCommentBody('notification')).toMatchInlineSnapshot(`
          "### 🔨 The codegen job will run at the end of the CI.

          _Make sure your last commit does not contain generated code, it will be automatically pushed by our CI._"
        `);
      });

      it('returns the right comment for a `noGen` trigger', async () => {
        expect(await getCommentBody('noGen')).toMatchInlineSnapshot(`
          "### ✗ No code generated.

          _If you believe this is an issue on our side, please [open an issue](https://github.com/algolia/api-clients-automation/issues/new?template=Bug_report.md)._"
        `);
      });
    });

    describe('cleanup', () => {
      afterEach(() => {
        jest.clearAllMocks();
      });

      it('returns the right comment for a `cleanup` trigger', async () => {
        mockedRun.mockResolvedValue('mocked');

        expect(await getCommentBody('cleanup')).toMatchInlineSnapshot(`
          "### ✗ The generated branch has been deleted.

          If the PR has been merged, you can check the generated code on the [\`${common.MAIN_BRANCH}\` branch](https://github.com/algolia/api-clients-automation/tree/${common.MAIN_BRANCH}).
          You can still access the code generated on \`mocked\` via [this commit](https://github.com/algolia/api-clients-automation/commit/mocked)."
          `);
      });

      it('fallbacks to the env variable HEAD_BRANCH if found when we are on `main`', async () => {
        process.env.HEAD_BRANCH = 'myFakeBranch';
        mockedRun.mockResolvedValue('main');

        expect(await getCommentBody('cleanup')).toMatchInlineSnapshot(`
          "### ✗ The generated branch has been deleted.

          If the PR has been merged, you can check the generated code on the [\`${common.MAIN_BRANCH}\` branch](https://github.com/algolia/api-clients-automation/tree/${common.MAIN_BRANCH}).
          You can still access the code generated on \`generated/myFakeBranch\` via [this commit](https://github.com/algolia/api-clients-automation/commit/main)."
        `);
      });
    });

    describe('text', () => {
      it('creates a comment body for the parameters', () => {
        expect(
          commentText.codegen.body(
            'theGeneratedCommit',
            'myBranch',
            'myCommit',
            42
          )
        ).toMatchInlineSnapshot(`
          "
          |  Name | Link |
          |---------------------------------|------------------------|
          | 🔨 Triggered by | [\`myCommit\`](https://github.com/algolia/api-clients-automation/pull/42/commits/myCommit) |
          | 🔍 Generated code | [\`theGeneratedCommit\`](https://github.com/algolia/api-clients-automation/commit/theGeneratedCommit) |
          | 🌲 Generated branch | [\`myBranch\`](https://github.com/algolia/api-clients-automation/tree/myBranch) |
          "
        `);
      });
    });
  });
});
