// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'base_recommendation_request.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BaseRecommendationRequest _$BaseRecommendationRequestFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'BaseRecommendationRequest',
      json,
      ($checkedConvert) {
        final val = BaseRecommendationRequest(
          model: $checkedConvert(
              'model', (v) => $enumDecode(_$RecommendationModelsEnumMap, v)),
          objectID: $checkedConvert('objectID', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$BaseRecommendationRequestToJson(
        BaseRecommendationRequest instance) =>
    <String, dynamic>{
      'model': instance.model.toJson(),
      'objectID': instance.objectID,
    };

const _$RecommendationModelsEnumMap = {
  RecommendationModels.relatedProducts: 'related-products',
  RecommendationModels.boughtTogether: 'bought-together',
};
