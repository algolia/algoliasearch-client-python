// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'updated_rule_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

UpdatedRuleResponse _$UpdatedRuleResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'UpdatedRuleResponse',
      json,
      ($checkedConvert) {
        final val = UpdatedRuleResponse(
          objectID: $checkedConvert('objectID', (v) => v as String),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
          taskID: $checkedConvert('taskID', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$UpdatedRuleResponseToJson(
        UpdatedRuleResponse instance) =>
    <String, dynamic>{
      'objectID': instance.objectID,
      'updatedAt': instance.updatedAt,
      'taskID': instance.taskID,
    };
