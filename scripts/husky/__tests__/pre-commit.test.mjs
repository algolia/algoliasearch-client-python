import micromatch from 'micromatch';

import { getPatterns } from '../pre-commit.mjs';

describe('micromatch', () => {
  it('matches correctly the files to remove', () => {
    expect(
      micromatch
        .match(
          [
            'clients/algoliasearch-client-java-2/build.gradle',
            'clients/algoliasearch-client-java-2/.gitignore',
            'clients/algoliasearch-client-java-2/gradle.properties',
            'clients/algoliasearch-client-java-2/algoliasearch-core/src/main/java/com/algolia/api/SearchClient.java',
            'clients/algoliasearch-client-java-2/algoliasearch-core/src/main/java/com/algolia/model/search/Test.java',
            'clients/algoliasearch-client-java-2/algoliasearch-core/src/main/java/com/algolia/utils/AlgoliaAgent.java',

            'clients/algoliasearch-client-javascript/.prettierrc',
            'clients/algoliasearch-client-javascript/lerna.json',
            'clients/algoliasearch-client-javascript/packages/client-common/whatever.test',
            'clients/algoliasearch-client-javascript/packages/client-search/ignore.txt',

            'clients/algoliasearch-client-php/.gitignore',
            'clients/algoliasearch-client-php/lib/Api/SearchClient.php',

            'tests/output/java/build.gradle',
            'tests/output/java/settings.gradle',
            'tests/output/java/src/test/java/com/algolia/EchoResponse.java',
            'tests/output/java/src/test/java/com/algolia/client/test.java',

            'tests/output/javascript/jest.config.ts',
            'tests/output/javascript/package.json',
            'tests/output/javascript/src/client/test.ts',

            'tests/output/php/src/methods/requests/test.php',
          ],
          getPatterns()
        )
        .sort()
    ).toEqual(
      [
        'clients/algoliasearch-client-java-2/gradle.properties',
        'clients/algoliasearch-client-java-2/algoliasearch-core/src/main/java/com/algolia/api/SearchClient.java',
        'clients/algoliasearch-client-java-2/algoliasearch-core/src/main/java/com/algolia/model/search/Test.java',

        'clients/algoliasearch-client-javascript/packages/client-search/ignore.txt',

        'clients/algoliasearch-client-php/lib/Api/SearchClient.php',

        'tests/output/java/build.gradle',
        'tests/output/java/src/test/java/com/algolia/client/test.java',

        'tests/output/javascript/src/client/test.ts',
        'tests/output/javascript/package.json',

        'tests/output/php/src/methods/requests/test.php',
      ].sort()
    );
  });
});
