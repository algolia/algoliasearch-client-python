// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'query_suggestions_configuration_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

QuerySuggestionsConfigurationResponse
    _$QuerySuggestionsConfigurationResponseFromJson(
            Map<String, dynamic> json) =>
        $checkedCreate(
          'QuerySuggestionsConfigurationResponse',
          json,
          ($checkedConvert) {
            final val = QuerySuggestionsConfigurationResponse(
              appId: $checkedConvert('appId', (v) => v as String?),
              sourceIndicesAPIKey:
                  $checkedConvert('sourceIndicesAPIKey', (v) => v as String?),
              suggestionsIndicesAPIKey: $checkedConvert(
                  'suggestionsIndicesAPIKey', (v) => v as String?),
              externalIndicesAPIKey:
                  $checkedConvert('externalIndicesAPIKey', (v) => v as String?),
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

Map<String, dynamic> _$QuerySuggestionsConfigurationResponseToJson(
    QuerySuggestionsConfigurationResponse instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('appId', instance.appId);
  writeNotNull('sourceIndicesAPIKey', instance.sourceIndicesAPIKey);
  writeNotNull('suggestionsIndicesAPIKey', instance.suggestionsIndicesAPIKey);
  writeNotNull('externalIndicesAPIKey', instance.externalIndicesAPIKey);
  val['indexName'] = instance.indexName;
  val['sourceIndices'] = instance.sourceIndices.map((e) => e.toJson()).toList();
  writeNotNull('languages', instance.languages);
  writeNotNull('exclude', instance.exclude);
  writeNotNull('enablePersonalization', instance.enablePersonalization);
  writeNotNull('allowSpecialCharacters', instance.allowSpecialCharacters);
  return val;
}
