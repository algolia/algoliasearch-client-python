// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'query_suggestions_configuration_response_all_of.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

QuerySuggestionsConfigurationResponseAllOf
    _$QuerySuggestionsConfigurationResponseAllOfFromJson(
            Map<String, dynamic> json) =>
        $checkedCreate(
          'QuerySuggestionsConfigurationResponseAllOf',
          json,
          ($checkedConvert) {
            final val = QuerySuggestionsConfigurationResponseAllOf(
              appId: $checkedConvert('appId', (v) => v as String?),
              sourceIndicesAPIKey:
                  $checkedConvert('sourceIndicesAPIKey', (v) => v as String?),
              suggestionsIndicesAPIKey: $checkedConvert(
                  'suggestionsIndicesAPIKey', (v) => v as String?),
              externalIndicesAPIKey:
                  $checkedConvert('externalIndicesAPIKey', (v) => v as String?),
            );
            return val;
          },
        );

Map<String, dynamic> _$QuerySuggestionsConfigurationResponseAllOfToJson(
    QuerySuggestionsConfigurationResponseAllOf instance) {
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
  return val;
}
