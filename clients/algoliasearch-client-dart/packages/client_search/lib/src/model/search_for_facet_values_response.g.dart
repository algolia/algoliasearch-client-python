// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_for_facet_values_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchForFacetValuesResponse _$SearchForFacetValuesResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SearchForFacetValuesResponse',
      json,
      ($checkedConvert) {
        final val = SearchForFacetValuesResponse(
          facetHits: $checkedConvert(
              'facetHits',
              (v) => (v as List<dynamic>)
                  .map((e) => FacetHits.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchForFacetValuesResponseToJson(
        SearchForFacetValuesResponse instance) =>
    <String, dynamic>{
      'facetHits': instance.facetHits.map((e) => e.toJson()).toList(),
    };
