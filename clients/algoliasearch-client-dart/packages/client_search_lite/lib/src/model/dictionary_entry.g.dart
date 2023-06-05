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

Map<String, dynamic> _$DictionaryEntryToJson(DictionaryEntry instance) {
  final val = <String, dynamic>{
    'objectID': instance.objectID,
    'language': instance.language,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('word', instance.word);
  writeNotNull('words', instance.words);
  writeNotNull('decomposition', instance.decomposition);
  writeNotNull('state', _$DictionaryEntryStateEnumMap[instance.state]);
  return val;
}

const _$DictionaryEntryStateEnumMap = {
  DictionaryEntryState.enabled: 'enabled',
  DictionaryEntryState.disabled: 'disabled',
};
