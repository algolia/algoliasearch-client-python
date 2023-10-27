export const patterns = [
  // Ignore the roots and go down the tree by negating hand written files
  'specs/bundled/*.yml',

  'clients/**',
  '!clients/README.md',
  '!clients/**/.openapi-generator-ignore',

  // Java
  '!clients/algoliasearch-client-java/**',
  'clients/algoliasearch-client-java/gradle.properties',
  'clients/algoliasearch-client-java/algoliasearch/src/main/java/com/algolia/api/**',
  'clients/algoliasearch-client-java/algoliasearch/src/main/java/com/algolia/model/**',
  'clients/algoliasearch-client-java/algoliasearch/src/main/java/com/algolia/BuildConfig.java',

  'tests/output/java/build.gradle',

  // JavaScript
  '!clients/algoliasearch-client-javascript/*',
  '!clients/algoliasearch-client-javascript/.github/**',
  '!clients/algoliasearch-client-javascript/.yarn/**',
  '!clients/algoliasearch-client-javascript/scripts/**',
  '!clients/algoliasearch-client-javascript/tests/**',
  // the release process is allowed to push changes to this file, but in general we don't because those files are generated
  process.env.RELEASE ? '!clients/algoliasearch-client-javascript/packages/**/package.json' : 'clients/algoliasearch-client-javascript/packages/**/package.json',
  '!clients/algoliasearch-client-javascript/packages/requester-*/**',
  '!clients/algoliasearch-client-javascript/packages/client-common/**',
  '!clients/algoliasearch-client-javascript/packages/algoliasearch/__tests__/**',
  '!clients/algoliasearch-client-javascript/packages/algoliasearch/jest.config.cjs',
  '!clients/algoliasearch-client-javascript/packages/algoliasearch/babel.config.cjs',

  'tests/output/javascript/package.json',

  // PHP
  '!clients/algoliasearch-client-php/**',
  'clients/algoliasearch-client-php/lib/Api/*',
  'clients/algoliasearch-client-php/lib/Model/**',
  'clients/algoliasearch-client-php/lib/Configuration/*',
  'clients/algoliasearch-client-php/lib/ApiException.php',
  'clients/algoliasearch-client-php/lib/ObjectSerializer.php',
  'clients/algoliasearch-client-php/lib/Algolia.php',
  'clients/algoliasearch-client-php/composer.json',

  // GO
  'clients/algoliasearch-client-go/algolia/**',
  '!clients/algoliasearch-client-go/.github/**',
  '!clients/algoliasearch-client-go/*',
  '!clients/algoliasearch-client-go/algolia/internal/**',
  '!clients/algoliasearch-client-go/algolia/call/*',
  '!clients/algoliasearch-client-go/algolia/compression/*',
  '!clients/algoliasearch-client-go/algolia/debug/*',

  'tests/output/go/go.sum',

  // Kotlin
  '!clients/algoliasearch-client-kotlin/**',
  'clients/algoliasearch-client-kotlin/gradle.properties',
  'clients/algoliasearch-client-kotlin/client/README.md',
  'clients/algoliasearch-client-kotlin/client-bom/README.md',
  'clients/algoliasearch-client-kotlin/client/src/commonMain/kotlin/com/algolia/client/BuildConfig.kt',
  'clients/algoliasearch-client-kotlin/client/src/commonMain/kotlin/com/algolia/client/api/**',
  'clients/algoliasearch-client-kotlin/client/src/commonMain/kotlin/com/algolia/client/model/**',

  'tests/output/kotlin/src/commonTest/kotlin/com/algolia/client/**',
  'tests/output/kotlin/src/commonTest/kotlin/com/algolia/methods/requests/**',

  // Dart
  '!clients/algoliasearch-client-dart/**',
  'clients/algoliasearch-client-dart/packages/*/pubspec.yaml',
  'clients/algoliasearch-client-dart/packages/*/lib/*.dart',
  'clients/algoliasearch-client-dart/packages/*/lib/src/*.dart',
  'clients/algoliasearch-client-dart/packages/client_core/pubspec.yaml',
  'clients/algoliasearch-client-dart/packages/*/lib/src/api/**',
  'clients/algoliasearch-client-dart/packages/*/lib/src/model/**',
  '!clients/algoliasearch-client-dart/packages/client_core/**',
  'clients/algoliasearch-client-dart/packages/client_core/lib/src/version.dart',
  '!clients/algoliasearch-client-dart/packages/*/lib/src/extension.dart',
  '!clients/algoliasearch-client-dart/packages/algoliasearch/lib/algoliasearch.dart',
];
