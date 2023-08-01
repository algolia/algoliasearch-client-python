// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_recommendations_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetRecommendationsParams _$GetRecommendationsParamsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetRecommendationsParams',
      json,
      ($checkedConvert) {
        final val = GetRecommendationsParams(
          requests: $checkedConvert('requests', (v) => v as List<dynamic>),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetRecommendationsParamsToJson(
        GetRecommendationsParams instance) =>
    <String, dynamic>{
      'requests': instance.requests.toList(),
    };
