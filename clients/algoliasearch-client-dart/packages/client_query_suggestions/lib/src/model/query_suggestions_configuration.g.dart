// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'query_suggestions_configuration.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

QuerySuggestionsConfiguration _$QuerySuggestionsConfigurationFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'QuerySuggestionsConfiguration',
      json,
      ($checkedConvert) {
        final val = QuerySuggestionsConfiguration(
          sourceIndices: $checkedConvert(
              'sourceIndices',
              (v) => (v as List<dynamic>)
                  .map((e) => SourceIndex.fromJson(e as Map<String, dynamic>))
                  .toList()),
          languages: $checkedConvert('languages', (v) => v),
          exclude: $checkedConvert('exclude',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          enablePersonalization:
              $checkedConvert('enablePersonalization', (v) => v as bool?),
          allowSpecialCharacters:
              $checkedConvert('allowSpecialCharacters', (v) => v as bool?),
        );
        return val;
      },
    );

Map<String, dynamic> _$QuerySuggestionsConfigurationToJson(
    QuerySuggestionsConfiguration instance) {
  final val = <String, dynamic>{
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
