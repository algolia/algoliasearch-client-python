// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Params _$ParamsFromJson(Map<String, dynamic> json) => Params(
      query: json['query'],
      automaticFacetFilters: json['automaticFacetFilters'],
      automaticOptionalFacetFilters: json['automaticOptionalFacetFilters'],
      renderingContent: json['renderingContent'] == null
          ? null
          : RenderingContent.fromJson(
              json['renderingContent'] as Map<String, dynamic>),
    );

Map<String, dynamic> _$ParamsToJson(Params instance) => <String, dynamic>{
      'query': instance.query,
      'automaticFacetFilters': instance.automaticFacetFilters,
      'automaticOptionalFacetFilters': instance.automaticOptionalFacetFilters,
      'renderingContent': instance.renderingContent,
    };
