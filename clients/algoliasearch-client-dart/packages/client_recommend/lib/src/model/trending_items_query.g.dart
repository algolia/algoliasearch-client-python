// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'trending_items_query.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TrendingItemsQuery _$TrendingItemsQueryFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'TrendingItemsQuery',
      json,
      ($checkedConvert) {
        final val = TrendingItemsQuery(
          facetName: $checkedConvert('facetName', (v) => v as String?),
          facetValue: $checkedConvert('facetValue', (v) => v as String?),
          model: $checkedConvert('model',
              (v) => $enumDecodeNullable(_$TrendingItemsModelEnumMap, v)),
          queryParameters: $checkedConvert(
              'queryParameters',
              (v) => v == null
                  ? null
                  : SearchParamsObject.fromJson(v as Map<String, dynamic>)),
          fallbackParameters: $checkedConvert(
              'fallbackParameters',
              (v) => v == null
                  ? null
                  : SearchParamsObject.fromJson(v as Map<String, dynamic>)),
          indexName: $checkedConvert('indexName', (v) => v as String),
          threshold: $checkedConvert('threshold', (v) => v as int?),
          maxRecommendations:
              $checkedConvert('maxRecommendations', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$TrendingItemsQueryToJson(TrendingItemsQuery instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('facetName', instance.facetName);
  writeNotNull('facetValue', instance.facetValue);
  writeNotNull('model', instance.model?.toJson());
  writeNotNull('queryParameters', instance.queryParameters?.toJson());
  writeNotNull('fallbackParameters', instance.fallbackParameters?.toJson());
  val['indexName'] = instance.indexName;
  writeNotNull('threshold', instance.threshold);
  writeNotNull('maxRecommendations', instance.maxRecommendations);
  return val;
}

const _$TrendingItemsModelEnumMap = {
  TrendingItemsModel.trendingItems: 'trending-items',
};
