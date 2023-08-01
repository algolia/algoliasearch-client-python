// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'task_update.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TaskUpdate _$TaskUpdateFromJson(Map<String, dynamic> json) => $checkedCreate(
      'TaskUpdate',
      json,
      ($checkedConvert) {
        final val = TaskUpdate(
          destinationID: $checkedConvert('destinationID', (v) => v as String?),
          trigger: $checkedConvert(
              'trigger',
              (v) => v == null
                  ? null
                  : TriggerInput.fromJson(v as Map<String, dynamic>)),
          input: $checkedConvert('input', (v) => v),
          enabled: $checkedConvert('enabled', (v) => v as bool?),
        );
        return val;
      },
    );

Map<String, dynamic> _$TaskUpdateToJson(TaskUpdate instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('destinationID', instance.destinationID);
  writeNotNull('trigger', instance.trigger?.toJson());
  writeNotNull('input', instance.input);
  writeNotNull('enabled', instance.enabled);
  return val;
}
