// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'task_create_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TaskCreateResponse _$TaskCreateResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'TaskCreateResponse',
      json,
      ($checkedConvert) {
        final val = TaskCreateResponse(
          taskID: $checkedConvert('taskID', (v) => v as String),
          createdAt: $checkedConvert('createdAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$TaskCreateResponseToJson(TaskCreateResponse instance) =>
    <String, dynamic>{
      'taskID': instance.taskID,
      'createdAt': instance.createdAt,
    };
