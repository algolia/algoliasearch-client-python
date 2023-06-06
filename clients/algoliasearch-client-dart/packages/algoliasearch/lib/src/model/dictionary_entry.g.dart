// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'dictionary_entry.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DictionaryEntry _$DictionaryEntryFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'DictionaryEntry',
      json,
      ($checkedConvert) {
        final val = DictionaryEntry(
          objectID: $checkedConvert('objectID', (v) => v as String),
          language: $checkedConvert('language', (v) => v as String),
          word: $checkedConvert('word', (v) => v as String?),
          words: $checkedConvert('words',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          decomposition: $checkedConvert('decomposition',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          state: $checkedConvert('state',
              (v) => $enumDecodeNullable(_$DictionaryEntryStateEnumMap, v)),
        );
        return val;
      },
    );

const _$DictionaryEntryStateEnumMap = {
  DictionaryEntryState.enabled: 'enabled',
  DictionaryEntryState.disabled: 'disabled',
};
