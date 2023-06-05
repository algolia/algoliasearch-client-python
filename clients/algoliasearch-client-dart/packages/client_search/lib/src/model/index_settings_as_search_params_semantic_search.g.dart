// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'index_settings_as_search_params_semantic_search.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

IndexSettingsAsSearchParamsSemanticSearch
    _$IndexSettingsAsSearchParamsSemanticSearchFromJson(
            Map<String, dynamic> json) =>
        $checkedCreate(
          'IndexSettingsAsSearchParamsSemanticSearch',
          json,
          ($checkedConvert) {
            final val = IndexSettingsAsSearchParamsSemanticSearch(
              eventSources: $checkedConvert(
                  'eventSources',
                  (v) =>
                      (v as List<dynamic>?)?.map((e) => e as String).toList()),
            );
            return val;
          },
        );

Map<String, dynamic> _$IndexSettingsAsSearchParamsSemanticSearchToJson(
    IndexSettingsAsSearchParamsSemanticSearch instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('eventSources', instance.eventSources);
  return val;
}
