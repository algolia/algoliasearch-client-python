// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_for_facets_options.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchForFacetsOptions _$SearchForFacetsOptionsFromJson(
        Map<String, dynamic> json) =>
    SearchForFacetsOptions(
      facet: json['facet'] as String,
      indexName: json['indexName'] as String,
      facetQuery: json['facetQuery'] as String?,
      maxFacetHits: json['maxFacetHits'] as int?,
      type: $enumDecode(_$SearchTypeFacetEnumMap, json['type']),
    );

Map<String, dynamic> _$SearchForFacetsOptionsToJson(
        SearchForFacetsOptions instance) =>
    <String, dynamic>{
      'facet': instance.facet,
      'indexName': instance.indexName,
      'facetQuery': instance.facetQuery,
      'maxFacetHits': instance.maxFacetHits,
      'type': _$SearchTypeFacetEnumMap[instance.type]!,
    };

const _$SearchTypeFacetEnumMap = {
  SearchTypeFacet.facet: 'facet',
};
