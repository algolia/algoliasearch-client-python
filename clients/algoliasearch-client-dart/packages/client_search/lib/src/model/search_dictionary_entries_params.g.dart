// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_dictionary_entries_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchDictionaryEntriesParams _$SearchDictionaryEntriesParamsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SearchDictionaryEntriesParams',
      json,
      ($checkedConvert) {
        final val = SearchDictionaryEntriesParams(
          query: $checkedConvert('query', (v) => v as String),
          page: $checkedConvert('page', (v) => v as int?),
          hitsPerPage: $checkedConvert('hitsPerPage', (v) => v as int?),
          language: $checkedConvert('language', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchDictionaryEntriesParamsToJson(
    SearchDictionaryEntriesParams instance) {
  final val = <String, dynamic>{
    'query': instance.query,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('page', instance.page);
  writeNotNull('hitsPerPage', instance.hitsPerPage);
  writeNotNull('language', instance.language);
  return val;
}
