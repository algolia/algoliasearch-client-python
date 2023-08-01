// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'schedule_trigger.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ScheduleTrigger _$ScheduleTriggerFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ScheduleTrigger',
      json,
      ($checkedConvert) {
        final val = ScheduleTrigger(
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$ScheduleTriggerTypeEnumMap, v)),
          cron: $checkedConvert('cron', (v) => v as String),
          lastRun: $checkedConvert('lastRun', (v) => v as String?),
          nextRun: $checkedConvert('nextRun', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$ScheduleTriggerToJson(ScheduleTrigger instance) {
  final val = <String, dynamic>{
    'type': instance.type.toJson(),
    'cron': instance.cron,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('lastRun', instance.lastRun);
  val['nextRun'] = instance.nextRun;
  return val;
}

const _$ScheduleTriggerTypeEnumMap = {
  ScheduleTriggerType.schedule: 'schedule',
};
