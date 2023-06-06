// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'index_settings_as_search_params_semantic_search.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

IndexSettingsAsSearchParamsSemanticSearch
    _$IndexSettingsAsSearchParamsSemanticSearchFromJson(
            Map<String, dynamic> json) =>
        IndexSettingsAsSearchParamsSemanticSearch(
          eventSources: (json['eventSources'] as List<dynamic>?)
              ?.map((e) => e as String)
              .toList(),
        );

Map<String, dynamic> _$IndexSettingsAsSearchParamsSemanticSearchToJson(
        IndexSettingsAsSearchParamsSemanticSearch instance) =>
    <String, dynamic>{
      'eventSources': instance.eventSources,
    };
