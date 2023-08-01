// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'trending_request.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TrendingRequest _$TrendingRequestFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'TrendingRequest',
      json,
      ($checkedConvert) {
        final val = TrendingRequest(
          model: $checkedConvert(
              'model', (v) => $enumDecode(_$TrendingModelsEnumMap, v)),
          facetName: $checkedConvert('facetName', (v) => v as String?),
          facetValue: $checkedConvert('facetValue', (v) => v as String?),
          indexName: $checkedConvert('indexName', (v) => v as String),
          threshold: $checkedConvert('threshold', (v) => v as int),
          maxRecommendations:
              $checkedConvert('maxRecommendations', (v) => v as int?),
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

Map<String, dynamic> _$TrendingRequestToJson(TrendingRequest instance) {
  final val = <String, dynamic>{
    'model': instance.model.toJson(),
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('facetName', instance.facetName);
  writeNotNull('facetValue', instance.facetValue);
  val['indexName'] = instance.indexName;
  val['threshold'] = instance.threshold;
  writeNotNull('maxRecommendations', instance.maxRecommendations);
  writeNotNull('queryParameters', instance.queryParameters?.toJson());
  writeNotNull('fallbackParameters', instance.fallbackParameters?.toJson());
  return val;
}

const _$TrendingModelsEnumMap = {
  TrendingModels.facets: 'trending-facets',
  TrendingModels.items: 'trending-items',
};
