// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'base_recommendations_query.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BaseRecommendationsQuery _$BaseRecommendationsQueryFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'BaseRecommendationsQuery',
      json,
      ($checkedConvert) {
        final val = BaseRecommendationsQuery(
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
        );
        return val;
      },
    );

Map<String, dynamic> _$BaseRecommendationsQueryToJson(
    BaseRecommendationsQuery instance) {
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
  return val;
}

const _$RecommendationModelsEnumMap = {
  RecommendationModels.relatedProducts: 'related-products',
  RecommendationModels.boughtTogether: 'bought-together',
};
