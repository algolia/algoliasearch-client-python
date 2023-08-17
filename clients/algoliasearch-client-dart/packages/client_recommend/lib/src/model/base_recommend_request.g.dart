// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'base_recommend_request.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BaseRecommendRequest _$BaseRecommendRequestFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'BaseRecommendRequest',
      json,
      ($checkedConvert) {
        final val = BaseRecommendRequest(
          indexName: $checkedConvert('indexName', (v) => v as String),
          threshold: $checkedConvert('threshold', (v) => v as int?),
          maxRecommendations:
              $checkedConvert('maxRecommendations', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$BaseRecommendRequestToJson(
    BaseRecommendRequest instance) {
  final val = <String, dynamic>{
    'indexName': instance.indexName,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('threshold', instance.threshold);
  writeNotNull('maxRecommendations', instance.maxRecommendations);
  return val;
}
