// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'dictionary_entry.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DictionaryEntry _$DictionaryEntryFromJson(Map<String, dynamic> json) =>
    DictionaryEntry(
      objectID: json['objectID'] as String,
      language: json['language'] as String,
      word: json['word'] as String?,
      words:
          (json['words'] as List<dynamic>?)?.map((e) => e as String).toList(),
      decomposition: (json['decomposition'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      state: $enumDecodeNullable(_$DictionaryEntryStateEnumMap, json['state']),
    );

Map<String, dynamic> _$DictionaryEntryToJson(DictionaryEntry instance) =>
    <String, dynamic>{
      'objectID': instance.objectID,
      'language': instance.language,
      'word': instance.word,
      'words': instance.words,
      'decomposition': instance.decomposition,
      'state': _$DictionaryEntryStateEnumMap[instance.state],
    };

const _$DictionaryEntryStateEnumMap = {
  DictionaryEntryState.enabled: 'enabled',
  DictionaryEntryState.disabled: 'disabled',
};
