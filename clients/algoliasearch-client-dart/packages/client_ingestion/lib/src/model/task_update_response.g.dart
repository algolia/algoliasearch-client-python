// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'task_update_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TaskUpdateResponse _$TaskUpdateResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'TaskUpdateResponse',
      json,
      ($checkedConvert) {
        final val = TaskUpdateResponse(
          taskID: $checkedConvert('taskID', (v) => v as String),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$TaskUpdateResponseToJson(TaskUpdateResponse instance) =>
    <String, dynamic>{
      'taskID': instance.taskID,
      'updatedAt': instance.updatedAt,
    };
