// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
// ignore_for_file: unused_element
import 'package:algolia_client_search/src/model/dictionary_entry_state.dart';

import 'package:collection/collection.dart';
import 'package:json_annotation/json_annotation.dart';

part 'dictionary_entry.g.dart';

@JsonSerializable(createToJson: false)
final class DictionaryEntry extends DelegatingMap<String, dynamic> {
  /// Returns a new [DictionaryEntry] instance.
  const DictionaryEntry({
    required this.objectID,
    required this.language,
    this.word,
    this.words,
    this.decomposition,
    this.state,
    Map<String, dynamic> json = const {},
  }) : super(json);

  /// Unique identifier of the object.
  @JsonKey(name: r'objectID')
  final String objectID;

  /// Language ISO code supported by the dictionary (e.g., \"en\" for English).
  @JsonKey(name: r'language')
  final String language;

  /// The word of the dictionary entry.
  @JsonKey(name: r'word')
  final String? word;

  /// The words of the dictionary entry.
  @JsonKey(name: r'words')
  final List<String>? words;

  /// A decomposition of the word of the dictionary entry.
  @JsonKey(name: r'decomposition')
  final List<String>? decomposition;

  @JsonKey(name: r'state')
  final DictionaryEntryState? state;

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      const MapEquality<String, dynamic>().equals(this, this);

  @override
  int get hashCode => const MapEquality<String, dynamic>().hash(this);

  factory DictionaryEntry.fromJson(Map<String, dynamic> json) {
    final instance = _$DictionaryEntryFromJson(json);
    return DictionaryEntry(
      objectID: instance.objectID,
      language: instance.language,
      word: instance.word,
      words: instance.words,
      decomposition: instance.decomposition,
      state: instance.state,
      json: json,
    );
  }

  Map<String, dynamic> toJson() => this;
}