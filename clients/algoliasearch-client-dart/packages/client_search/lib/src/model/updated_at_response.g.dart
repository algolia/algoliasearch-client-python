// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'updated_at_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

UpdatedAtResponse _$UpdatedAtResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'UpdatedAtResponse',
      json,
      ($checkedConvert) {
        final val = UpdatedAtResponse(
          taskID: $checkedConvert('taskID', (v) => v as int),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$UpdatedAtResponseToJson(UpdatedAtResponse instance) =>
    <String, dynamic>{
      'taskID': instance.taskID,
      'updatedAt': instance.updatedAt,
    };
