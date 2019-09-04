# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

# Release Notes

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
