export default {
  header: `## Summary`,
  summary:
    'This PR has been created using the `yarn release` script. Once merged, the clients will try to release their new version if their version has changed.',

  versionChangeHeader: `## Version Changes`,
  skippedCommitsHeader: `### Skipped Commits`,
  skippedCommitsDesc: `It doesn't mean these commits are being excluded from the release. It means they're not taken into account when the release process figured out the next version number, and updated the changelog.`,
  noCommit: `no commit`,
  currentVersionNotFound: `current version not found`,
  indenpendentVersioning: `
  <details>
    <summary>
      <i>The JavaScript repository consists of several packages with independent versioning. Release type is applied to each version.</i>
    </summary>

    For example, if the release type is \`patch\`,

    * algoliasearch@5.0.0 -> 5.0.1
    * @algolia/client-search@5.0.0 -> 5.0.1
    * @algolia/client-abtesting@5.0.0 -> 5.0.1
    * ...
    * @algolia/ingestion@0.0.1 -> 0.0.2
    * ...
    * @algolia/requester-browser-xhr@0.0.5 -> 0.0.6.
  </details>
  `,
  descriptionForSkippedLang: `  - No \`feat\` or \`fix\` commit, thus unchecked by default.`,

  changelogHeader: `## CHANGELOG`,
};
