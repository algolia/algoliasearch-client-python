// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'task.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Task _$TaskFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Task',
      json,
      ($checkedConvert) {
        final val = Task(
          taskID: $checkedConvert('taskID', (v) => v as String),
          sourceID: $checkedConvert('sourceID', (v) => v as String),
          destinationID: $checkedConvert('destinationID', (v) => v as String),
          trigger: $checkedConvert('trigger', (v) => v),
          input: $checkedConvert('input', (v) => v),
          enabled: $checkedConvert('enabled', (v) => v as bool),
          action: $checkedConvert(
              'action', (v) => $enumDecode(_$ActionTypeEnumMap, v)),
          createdAt: $checkedConvert('createdAt', (v) => v as String),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$TaskToJson(Task instance) {
  final val = <String, dynamic>{
    'taskID': instance.taskID,
    'sourceID': instance.sourceID,
    'destinationID': instance.destinationID,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('trigger', instance.trigger);
  writeNotNull('input', instance.input);
  val['enabled'] = instance.enabled;
  val['action'] = instance.action.toJson();
  val['createdAt'] = instance.createdAt;
  writeNotNull('updatedAt', instance.updatedAt);
  return val;
}

const _$ActionTypeEnumMap = {
  ActionType.replace: 'replace',
  ActionType.save: 'save',
};
