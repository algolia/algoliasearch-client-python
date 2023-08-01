// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'query_suggestions_configuration_with_index.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

QuerySuggestionsConfigurationWithIndex
    _$QuerySuggestionsConfigurationWithIndexFromJson(
            Map<String, dynamic> json) =>
        $checkedCreate(
          'QuerySuggestionsConfigurationWithIndex',
          json,
          ($checkedConvert) {
            final val = QuerySuggestionsConfigurationWithIndex(
              indexName: $checkedConvert('indexName', (v) => v as String),
              sourceIndices: $checkedConvert(
                  'sourceIndices',
                  (v) => (v as List<dynamic>)
                      .map((e) =>
                          SourceIndex.fromJson(e as Map<String, dynamic>))
                      .toList()),
              languages: $checkedConvert('languages', (v) => v),
              exclude: $checkedConvert(
                  'exclude',
                  (v) =>
                      (v as List<dynamic>?)?.map((e) => e as String).toList()),
              enablePersonalization:
                  $checkedConvert('enablePersonalization', (v) => v as bool?),
              allowSpecialCharacters:
                  $checkedConvert('allowSpecialCharacters', (v) => v as bool?),
            );
            return val;
          },
        );

Map<String, dynamic> _$QuerySuggestionsConfigurationWithIndexToJson(
    QuerySuggestionsConfigurationWithIndex instance) {
  final val = <String, dynamic>{
    'indexName': instance.indexName,
    'sourceIndices': instance.sourceIndices.map((e) => e.toJson()).toList(),
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('languages', instance.languages);
  writeNotNull('exclude', instance.exclude);
  writeNotNull('enablePersonalization', instance.enablePersonalization);
  writeNotNull('allowSpecialCharacters', instance.allowSpecialCharacters);
  return val;
}
