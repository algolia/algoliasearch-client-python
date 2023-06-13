import 'dart:convert';

import 'package:algolia_test/algolia_test.dart';
import 'package:collection/collection.dart';
import 'package:test/test.dart';
import 'package:test_api/hooks.dart';

/// Checks if the [actual] JSON object matches the [expected] JSON string,
/// disregarding the order of elements.
void expectBody(dynamic actual, String expected) {
  final expectedJson = jsonDecode(expected);
  final jsonObj = jsonEncode(actual);
  final actualJson = jsonDecode(jsonObj);
  expect(
    const DeepCollectionEquality.unordered().equals(expectedJson, actualJson),
    true,
    reason: "expected body: $expectedJson, \nactual body: $actual",
  );
}

/// Verifies that the [actual] map of HTTP headers matches the [expected]
/// headers given as a JSON string, with case-insensitive comparison.
void expectHeaders(Map<String, dynamic>? actual, String expected) {
  final expectedMap = _normalizeKeys(
    jsonDecode(expected) as Map<String, dynamic>,
  );
  final actualMap = _normalizeKeys(actual);
  expect(
    const DeepCollectionEquality.unordered().equals(actualMap, expectedMap),
    true,
    reason: "expected map: $expectedMap, \nactual map: $actualMap",
  );
}

/// Normalizes a map by converting all keys to lowercase, making comparison
/// case-insensitive.
Map<String, dynamic> _normalizeKeys(Map<String, dynamic>? map) {
  if (map == null) return const {};
  var newMap = <String, dynamic>{};
  map.forEach((key, value) => newMap[key.toLowerCase()] = value);
  return newMap;
}

/// Verifies that the [actual] URI string, once fully decoded, matches the
/// [expected] string.
void expectPath(String actual, String expected) {
  expect(Uri.decodeFull(actual), expected);
}

/// Checks if the [actual] map of query parameters matches the [expected]
/// parameters given as a JSON string.
void expectParams(Map<String, dynamic> actual, String expected) {
  final expectedMap = jsonDecode(expected) as Map<String, dynamic>;
  final actualMap = Map<String, String>.from(actual.map((key, value) =>
      MapEntry(key, value is Iterable ? value.join(",") : value.toString())));
  expect(
    const DeepCollectionEquality.unordered().equals(actualMap, expectedMap),
    true,
    reason: "expected params: $expectedMap, \nactual params: $actualMap",
  );
}

void expectError(String message, Function block) async {
  try {
    await block();
  } on SkipException catch (_) {
    TestHandle.current.markSkipped('Skip non-nullable params test');
  } on AssertionError catch (e) {
    expect(e.message, message);
  }
}
