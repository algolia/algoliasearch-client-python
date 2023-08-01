// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'recommendation_request.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RecommendationRequest _$RecommendationRequestFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'RecommendationRequest',
      json,
      ($checkedConvert) {
        final val = RecommendationRequest(
          model: $checkedConvert(
              'model', (v) => $enumDecode(_$RecommendationModelsEnumMap, v)),
          objectID: $checkedConvert('objectID', (v) => v as String),
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

Map<String, dynamic> _$RecommendationRequestToJson(
    RecommendationRequest instance) {
  final val = <String, dynamic>{
    'model': instance.model.toJson(),
    'objectID': instance.objectID,
    'indexName': instance.indexName,
    'threshold': instance.threshold,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('maxRecommendations', instance.maxRecommendations);
  writeNotNull('queryParameters', instance.queryParameters?.toJson());
  writeNotNull('fallbackParameters', instance.fallbackParameters?.toJson());
  return val;
}

const _$RecommendationModelsEnumMap = {
  RecommendationModels.relatedProducts: 'related-products',
  RecommendationModels.boughtTogether: 'bought-together',
};
