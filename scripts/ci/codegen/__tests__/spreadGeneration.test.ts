import {  describe, expect, it } from "vitest";
import { cleanUpCommitMessage } from '../spreadGeneration.js';
import text from '../text.js';

describe('spread generation', () => {
  describe('cleanUpCommitMessage', () => {
    it('returns a release commit message with the version', () => {
      expect(
        cleanUpCommitMessage(`${text.commitReleaseMessage} [skip ci]`, '1.0.0')
      ).toEqual('chore: release 1.0.0');
    });

    it('removes pull-request number from commit message', () => {
      expect(
        cleanUpCommitMessage('feat(ci): make ci push generated code (#244)', '')
      ).toEqual(
        `feat(ci): make ci push generated code\n\nhttps://github.com/algolia/api-clients-automation/pull/244`
      );
    });

    it('keeps the commit message even if it does not have PR number', () => {
      const commitMessage = `feat(ci): make ci push generated code`;
      expect(cleanUpCommitMessage(commitMessage, '')).toEqual(commitMessage);
    });

    it('cleans up correctly even if the title contains a url', () => {
      const commitMessage = `fix(java): solve oneOf using a custom generator https://algolia.atlassian.net/browse/APIC-123 (#200)`;
      expect(cleanUpCommitMessage(commitMessage, '')).toMatchInlineSnapshot(`
      "fix(java): solve oneOf using a custom generator https://algolia.atlassian.net/browse/APIC-123

      https://github.com/algolia/api-clients-automation/pull/200"
    `);
    });

    it('provides a link to the automation repo for commit with hash', () => {
      const commitMessage = `${text.commitStartMessage} ed33e02f3e45fd72b4f420a56e4be7c6929fca9f. [skip ci]`;
      expect(cleanUpCommitMessage(commitMessage, '')).toMatchInlineSnapshot(`
      "chore: generated code for commit ed33e02f. [skip ci]

      https://github.com/algolia/api-clients-automation/commit/ed33e02f3e45fd72b4f420a56e4be7c6929fca9f"
    `);
    });
  });
});
