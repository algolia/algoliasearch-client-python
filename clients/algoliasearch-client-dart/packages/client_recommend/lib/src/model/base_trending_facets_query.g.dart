// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'base_trending_facets_query.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BaseTrendingFacetsQuery _$BaseTrendingFacetsQueryFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'BaseTrendingFacetsQuery',
      json,
      ($checkedConvert) {
        final val = BaseTrendingFacetsQuery(
          facetName: $checkedConvert('facetName', (v) => v as String),
          model: $checkedConvert('model',
              (v) => $enumDecodeNullable(_$TrendingFacetsModelEnumMap, v)),
        );
        return val;
      },
    );

Map<String, dynamic> _$BaseTrendingFacetsQueryToJson(
    BaseTrendingFacetsQuery instance) {
  final val = <String, dynamic>{
    'facetName': instance.facetName,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('model', instance.model?.toJson());
  return val;
}

const _$TrendingFacetsModelEnumMap = {
  TrendingFacetsModel.trendingFacets: 'trending-facets',
};
