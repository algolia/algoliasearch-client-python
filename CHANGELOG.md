# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

# Release Notes

## [Unreleased](https://github.com/algolia/algoliasearch-client-python/compare/v2.6.3...master)

## [v3.0.0](https://github.com/algolia/algoliasearch-client-python/compare/v2.6.2...v3.0.0)

### Changed

- Major version: Python 2.7 is no longer supported, adds support until Python 3.11

### Fixed
 - Unable to initialize SearchClient on Python 3.11 ([#549](https://github.com/algolia/algoliasearch-client-python/issues/549))

## [v2.6.3](https://github.com/algolia/algoliasearch-client-python/compare/v2.6.2...v2.6.3)

### Fixed

- prevent KeyError when popping an unknown property ([#552](https://github.com/algolia/algoliasearch-client-python/pull/552))

## [v2.6.2](https://github.com/algolia/algoliasearch-client-python/compare/v2.6.1...v2.6.2)

### Fixed

- Encode path parameters ([#546](https://github.com/algolia/algoliasearch-client-python/pull/546))

## [v2.6.1](https://github.com/algolia/algoliasearch-client-python/compare/v2.6.0...v2.6.1)

### Fixed

- Prevent recursion issue with `browse_rules` method ([#542](https://github.com/algolia/algoliasearch-client-python/pull/542))

## [v2.6.0](https://github.com/algolia/algoliasearch-client-python/compare/v2.5.0...v2.6.0)

### Added

- Provide `RecommendClient` class for Algolia Recommend ([#539](https://github.com/algolia/algoliasearch-client-python/pull/539))
- Provide `PersonalizationClient` class in favor of `RecommendationClient` ([#536](https://github.com/algolia/algoliasearch-client-python/pull/536))
- Dockerize repository ([#538](https://github.com/algolia/algoliasearch-client-python/pull/538))

### Changed

- Deprecate `RecommendationClient` in favor of `PersonalizationClient` ([#536](https://github.com/algolia/algoliasearch-client-python/pull/536))

## [v2.5.0](https://github.com/algolia/algoliasearch-client-python/compare/v2.4.0...v2.5.0)

### Added

- Bring support custom dictionaries ([#522](https://github.com/algolia/algoliasearch-client-python/pull/522))

## [v2.4.0](https://github.com/algolia/algoliasearch-client-python/compare/v2.3.1...v2.4.0)

### Added

- Bring support for HTTP_PROXY / HTTPS_PROXY ([#505](https://github.com/algolia/algoliasearch-client-python/pull/505))

## [v2.3.1](https://github.com/algolia/algoliasearch-client-python/compare/v2.3.0...v2.3.1)

### Fixed

- Invalid format in `setup.cfg` -> `python_requires`. ([#500](https://github.com/algolia/algoliasearch-client-python/pull/500))

## [v2.3.0](https://github.com/algolia/algoliasearch-client-python/compare/v2.2.0...v2.3.0)

### Added

- Closeable http sessions directly from the clients ([#492](https://github.com/algolia/algoliasearch-client-python/pull/492))

### Fixed

- Replace all objects could get blocked on the replace all objects method while using safe parameter with async dependencies. ([#479](https://github.com/algolia/algoliasearch-client-python/pull/479), [493](https://github.com/algolia/algoliasearch-client-python/pull/493))

## [v2.2.0](https://github.com/algolia/algoliasearch-client-python/compare/2.1.0...2.2.0)

### Added

- Method `RecommendationClient.set_personalization_strategy` and Method `RecommendationClient.get_personalization_strategy` ([#471](https://github.com/algolia/algoliasearch-client-python/pull/471))
- Method `SearchClient.has_pending_mappings` ([#463](https://github.com/algolia/algoliasearch-client-python/pull/463))
- Method `SearchClient.assign_user_ids` ([#473](https://github.com/algolia/algoliasearch-client-python/pull/473))

### Changed

- Deprecates method `SearchClient.set_personalization_strategy` and method `SearchClient.get_personalization_strategy` ([#471](https://github.com/algolia/algoliasearch-client-python/pull/471))

## [v2.1.0](https://github.com/algolia/algoliasearch-client-python/compare/2.0.4...2.1.0)

### Added

- Method `SearchClient.get_secured_api_key_remaining_validity` ([#455](https://github.com/algolia/algoliasearch-client-python/pull/455))
- Method `SearchIndex.exists` ([#444](https://github.com/algolia/algoliasearch-client-python/pull/444)) ([#454](https://github.com/algolia/algoliasearch-client-python/pull/454))
- Method `SearchIndex.find_object` and `SearchIndex.get_object_position` ([#449](https://github.com/algolia/algoliasearch-client-python/pull/449))

## [v2.0.4](https://github.com/algolia/algoliasearch-client-python/compare/2.0.3...2.0.4)

### Fixed

- On `getVersion` param used by `search_index.get_settings` ([#426](https://github.com/algolia/algoliasearch-client-python/pull/426))

## [v2.0.3](https://github.com/algolia/algoliasearch-client-python/compare/2.0.2...2.0.3)

### Fixed

- Missing `attributesToRetrieve` data on multiple `get_objects` ([#424](https://github.com/algolia/algoliasearch-client-python/pull/424))

## [v2.0.2](https://github.com/algolia/algoliasearch-client-python/compare/2.0.1...2.0.2)

### Fixed

- Conflict with `typing` standard library ([#423](https://github.com/algolia/algoliasearch-client-python/pull/423))

## [v2.0.1](https://github.com/algolia/algoliasearch-client-python/compare/2.0.0...2.0.1)

### Fixed

- Batching algorithm when reaching the `batch_size` ([#421](https://github.com/algolia/algoliasearch-client-python/pull/421))

## [v2.0.0](https://github.com/algolia/algoliasearch-client-python/compare/1.20.0...2.0.0)

### Changed

- Major version - [Upgrade Guide](https://www.algolia.com/doc/api-client/getting-started/upgrade-guides/python)
