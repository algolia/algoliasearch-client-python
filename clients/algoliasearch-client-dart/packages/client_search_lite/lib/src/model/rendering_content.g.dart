// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'rendering_content.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RenderingContent _$RenderingContentFromJson(Map<String, dynamic> json) =>
    RenderingContent(
      facetOrdering: json['facetOrdering'] == null
          ? null
          : FacetOrdering.fromJson(
              json['facetOrdering'] as Map<String, dynamic>),
    );

Map<String, dynamic> _$RenderingContentToJson(RenderingContent instance) =>
    <String, dynamic>{
      'facetOrdering': instance.facetOrdering,
    };
