<!-- centered logo -->
<p align="center">
  <a href="https://www.algolia.com">
    <img alt="Algolia for Dart" src="https://raw.githubusercontent.com/algolia/algoliasearch-client-common/master/banners/dart.png" >
  </a>
</p>

<!-- centered project introduction -->
<h3 align="center">
  The perfect starting point to integrate <a href="https://algolia.com" target="_blank">Algolia</a> within your Dart project
</h3>

<!-- centered badges -->
<p align="center">
  <a href="https://pub.dartlang.org/packages/algoliasearch"><img src="https://img.shields.io/pub/v/algoliasearch.svg" alt="Latest version"/></a>
  <a href="https://pub.dev/packages/algoliasearch/publisher"><img src="https://img.shields.io/pub/publisher/algoliasearch.svg" alt="Publisher"/></a>
</p>

<!-- quick links -->
<p align="center">
  <a href="https://www.algolia.com/doc/guides/building-search-ui/what-is-instantsearch/flutter/" target="_blank">Flutter Guide</a>  •
  <a href="https://discourse.algolia.com" target="_blank">Community Forum</a>  •
  <a href="https://stackoverflow.com/questions/tagged/algolia" target="_blank">Stack Overflow</a>  •
  <a href="https://github.com/algolia/algoliasearch-client-dart/issues" target="_blank">Report a Bug</a>  •
  <a href="https://www.algolia.com/support" target="_blank">Support</a>
</p>

## 📚 Description

`algoliasearch` is a comprehensive Dart package that provides access to Algolia's robust search and insights features. It is an all-in-one solution designed to help you integrate Algolia within your Dart project seamlessly and efficiently.

The package currently offers the following clients:

- **Search Client**: Allows you to leverage Algolia's search capabilities, including instant search results, search-as-you-type, and typo-tolerance.
- **Insights Client**: Enables you to collect events related to your search and discovery experience, providing valuable insights into user behavior. With it, you can unlock powerful features such as recommendations, personalization, and smarter search results.
- **Search Lite Client**: A lighter, search-only version of the library, perfect for projects that require search functionality without the need for features like indexing.

Future updates will include more clients to cover the entirety of Algolia's feature set, providing a complete toolset for building powerful, interactive search experiences in your Dart or Flutter application.

## ✨ Features

- **Low-Level HTTP Client**: Provides a thin and minimal low-level HTTP client to interact directly with Algolia's API, giving you maximum control over your requests.
- **Cross-Platform Compatibility**: Designed to work seamlessly on both native and web platforms, making it ideal for any Dart project.
- **Pure Dart Construction**: Built with pure Dart for superior performance and maximum compatibility across Dart projects.

## 💡 Getting Started

### Step 1: Add Dependency

To use this package in your project, add it as a dependency:

#### For Dart projects:

```shell
dart pub add algoliasearch
```

#### For Flutter projects:

```shell
flutter pub add algoliasearch
```

### Step 2: Import the Package

Now, you can import the `algoliasearch` package in your Dart code for all operations, including indexing, search, and personalization:

```dart
import 'package:algoliasearch/algoliasearch.dart';
```

Alternatively, you can import `algoliasearch_lite`, a **search-only** version of the library, if you do not need the full feature set:

```dart
import 'package:algoliasearch/algoliasearch_lite.dart';
```

## 📄 License

Algolia API Client is an open-sourced software licensed under the [MIT license](LICENSE).
