// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'deleted_at_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DeletedAtResponse _$DeletedAtResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'DeletedAtResponse',
      json,
      ($checkedConvert) {
        final val = DeletedAtResponse(
          taskID: $checkedConvert('taskID', (v) => v as int),
          deletedAt: $checkedConvert('deletedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$DeletedAtResponseToJson(DeletedAtResponse instance) =>
    <String, dynamic>{
      'taskID': instance.taskID,
      'deletedAt': instance.deletedAt,
    };
