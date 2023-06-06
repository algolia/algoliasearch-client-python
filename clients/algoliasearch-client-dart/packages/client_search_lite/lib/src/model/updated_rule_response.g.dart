// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'updated_rule_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

UpdatedRuleResponse _$UpdatedRuleResponseFromJson(Map<String, dynamic> json) =>
    UpdatedRuleResponse(
      objectID: json['objectID'] as String,
      updatedAt: json['updatedAt'] as String,
      taskID: json['taskID'] as int,
    );

Map<String, dynamic> _$UpdatedRuleResponseToJson(
        UpdatedRuleResponse instance) =>
    <String, dynamic>{
      'objectID': instance.objectID,
      'updatedAt': instance.updatedAt,
      'taskID': instance.taskID,
    };
