// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_for_facets_options.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchForFacetsOptions _$SearchForFacetsOptionsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SearchForFacetsOptions',
      json,
      ($checkedConvert) {
        final val = SearchForFacetsOptions(
          facet: $checkedConvert('facet', (v) => v as String),
          indexName: $checkedConvert('indexName', (v) => v as String),
          facetQuery: $checkedConvert('facetQuery', (v) => v as String?),
          maxFacetHits: $checkedConvert('maxFacetHits', (v) => v as int?),
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$SearchTypeFacetEnumMap, v)),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchForFacetsOptionsToJson(
    SearchForFacetsOptions instance) {
  final val = <String, dynamic>{
    'facet': instance.facet,
    'indexName': instance.indexName,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('facetQuery', instance.facetQuery);
  writeNotNull('maxFacetHits', instance.maxFacetHits);
  val['type'] = _$SearchTypeFacetEnumMap[instance.type]!;
  return val;
}

const _$SearchTypeFacetEnumMap = {
  SearchTypeFacet.facet: 'facet',
};
