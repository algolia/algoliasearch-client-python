import { MAIN_BRANCH, REPO_URL, TODAY } from '../../common.js';

export const commitStartPrepareRelease = 'chore: prepare release';
export const commitStartRelease = 'chore: release';

export default {
  commitStartMessage: 'chore: generated code for commit',
  commitPrepareReleaseMessage: `${commitStartPrepareRelease} ${TODAY}`,
  commitReleaseMessage: `${commitStartRelease} ${TODAY}`,
  notification: {
    header: '### 🔨 The codegen job will run at the end of the CI.',
    body: (): string =>
      '_Make sure your last commit does not contain generated code, it will be automatically pushed by our CI._',
  },
  noGen: {
    header: '### ✗ No code generated.',
    body: (): string =>
      `_If you believe this is an issue on our side, please [open an issue](${REPO_URL}/issues/new?template=Bug_report.md)._`,
  },
  cleanup: {
    header: '### ✗ The generated branch has been deleted.',
    body: (
      generatedCommit: string,
      branch: string
    ): string => `If the PR has been merged, you can check the generated code on the [\`${MAIN_BRANCH}\` branch](${REPO_URL}/tree/${MAIN_BRANCH}).
You can still access the code generated on \`${branch}\` via [this commit](${REPO_URL}/commit/${generatedCommit}).`,
  },
  codegen: {
    header: '### ✔️ Code generated!',
    body: (
      generatedCommit: string,
      branch: string,
      commit: string,
      eventNumber: number
    ): string => `
|  Name | Link |
|---------------------------------|------------------------|
| 🔨 Triggered by | [\`${commit}\`](${REPO_URL}/pull/${eventNumber}/commits/${commit}) |
| 🔍 Generated code | [\`${generatedCommit}\`](${REPO_URL}/commit/${generatedCommit}) |
| 🌲 Generated branch | [\`${branch}\`](${REPO_URL}/tree/${branch}) |
`,
  },
};
