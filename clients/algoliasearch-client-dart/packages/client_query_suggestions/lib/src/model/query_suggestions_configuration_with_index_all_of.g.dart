// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'query_suggestions_configuration_with_index_all_of.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

QuerySuggestionsConfigurationWithIndexAllOf
    _$QuerySuggestionsConfigurationWithIndexAllOfFromJson(
            Map<String, dynamic> json) =>
        $checkedCreate(
          'QuerySuggestionsConfigurationWithIndexAllOf',
          json,
          ($checkedConvert) {
            final val = QuerySuggestionsConfigurationWithIndexAllOf(
              indexName: $checkedConvert('indexName', (v) => v as String),
            );
            return val;
          },
        );

Map<String, dynamic> _$QuerySuggestionsConfigurationWithIndexAllOfToJson(
        QuerySuggestionsConfigurationWithIndexAllOf instance) =>
    <String, dynamic>{
      'indexName': instance.indexName,
    };
