// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_task_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetTaskResponse _$GetTaskResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'GetTaskResponse',
      json,
      ($checkedConvert) {
        final val = GetTaskResponse(
          status: $checkedConvert(
              'status', (v) => $enumDecode(_$TaskStatusEnumMap, v)),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetTaskResponseToJson(GetTaskResponse instance) =>
    <String, dynamic>{
      'status': instance.status.toJson(),
    };

const _$TaskStatusEnumMap = {
  TaskStatus.published: 'published',
  TaskStatus.notPublished: 'notPublished',
};
