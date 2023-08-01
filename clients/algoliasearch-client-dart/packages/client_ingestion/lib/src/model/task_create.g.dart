// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'task_create.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TaskCreate _$TaskCreateFromJson(Map<String, dynamic> json) => $checkedCreate(
      'TaskCreate',
      json,
      ($checkedConvert) {
        final val = TaskCreate(
          sourceID: $checkedConvert('sourceID', (v) => v as String),
          destinationID: $checkedConvert('destinationID', (v) => v as String),
          trigger: $checkedConvert('trigger', (v) => v),
          action: $checkedConvert(
              'action', (v) => $enumDecode(_$ActionTypeEnumMap, v)),
          enabled: $checkedConvert('enabled', (v) => v as bool?),
          input: $checkedConvert('input', (v) => v),
        );
        return val;
      },
    );

Map<String, dynamic> _$TaskCreateToJson(TaskCreate instance) {
  final val = <String, dynamic>{
    'sourceID': instance.sourceID,
    'destinationID': instance.destinationID,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('trigger', instance.trigger);
  val['action'] = instance.action.toJson();
  writeNotNull('enabled', instance.enabled);
  writeNotNull('input', instance.input);
  return val;
}

const _$ActionTypeEnumMap = {
  ActionType.replace: 'replace',
  ActionType.save: 'save',
};
