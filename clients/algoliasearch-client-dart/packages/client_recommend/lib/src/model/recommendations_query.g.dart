// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'recommendations_query.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RecommendationsQuery _$RecommendationsQueryFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'RecommendationsQuery',
      json,
      ($checkedConvert) {
        final val = RecommendationsQuery(
          model: $checkedConvert(
              'model', (v) => $enumDecode(_$RecommendationModelsEnumMap, v)),
          objectID: $checkedConvert('objectID', (v) => v as String),
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

Map<String, dynamic> _$RecommendationsQueryToJson(
    RecommendationsQuery instance) {
  final val = <String, dynamic>{
    'model': instance.model.toJson(),
    'objectID': instance.objectID,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('queryParameters', instance.queryParameters?.toJson());
  writeNotNull('fallbackParameters', instance.fallbackParameters?.toJson());
  val['indexName'] = instance.indexName;
  writeNotNull('threshold', instance.threshold);
  writeNotNull('maxRecommendations', instance.maxRecommendations);
  return val;
}

const _$RecommendationModelsEnumMap = {
  RecommendationModels.relatedProducts: 'related-products',
  RecommendationModels.boughtTogether: 'bought-together',
};
