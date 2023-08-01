// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'ab_test_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ABTestResponse _$ABTestResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ABTestResponse',
      json,
      ($checkedConvert) {
        final val = ABTestResponse(
          index: $checkedConvert('index', (v) => v as String),
          abTestID: $checkedConvert('abTestID', (v) => v as int),
          taskID: $checkedConvert('taskID', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$ABTestResponseToJson(ABTestResponse instance) =>
    <String, dynamic>{
      'index': instance.index,
      'abTestID': instance.abTestID,
      'taskID': instance.taskID,
    };
