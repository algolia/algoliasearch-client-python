// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'base_trending_items_query.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BaseTrendingItemsQuery _$BaseTrendingItemsQueryFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'BaseTrendingItemsQuery',
      json,
      ($checkedConvert) {
        final val = BaseTrendingItemsQuery(
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
        );
        return val;
      },
    );

Map<String, dynamic> _$BaseTrendingItemsQueryToJson(
    BaseTrendingItemsQuery instance) {
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
  return val;
}

const _$TrendingItemsModelEnumMap = {
  TrendingItemsModel.trendingItems: 'trending-items',
};
