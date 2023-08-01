// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_recommend_task_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetRecommendTaskResponse _$GetRecommendTaskResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetRecommendTaskResponse',
      json,
      ($checkedConvert) {
        final val = GetRecommendTaskResponse(
          status: $checkedConvert(
              'status', (v) => $enumDecode(_$TaskStatusEnumMap, v)),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetRecommendTaskResponseToJson(
        GetRecommendTaskResponse instance) =>
    <String, dynamic>{
      'status': instance.status.toJson(),
    };

const _$TaskStatusEnumMap = {
  TaskStatus.published: 'published',
  TaskStatus.notPublished: 'notPublished',
};
