// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'dictionary_language.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DictionaryLanguage _$DictionaryLanguageFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'DictionaryLanguage',
      json,
      ($checkedConvert) {
        final val = DictionaryLanguage(
          nbCustomEntries: $checkedConvert('nbCustomEntries', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$DictionaryLanguageToJson(DictionaryLanguage instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('nbCustomEntries', instance.nbCustomEntries);
  return val;
}
