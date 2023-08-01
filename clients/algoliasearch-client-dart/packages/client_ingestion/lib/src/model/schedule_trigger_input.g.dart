// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'schedule_trigger_input.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ScheduleTriggerInput _$ScheduleTriggerInputFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'ScheduleTriggerInput',
      json,
      ($checkedConvert) {
        final val = ScheduleTriggerInput(
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$ScheduleTriggerTypeEnumMap, v)),
          cron: $checkedConvert('cron', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$ScheduleTriggerInputToJson(
        ScheduleTriggerInput instance) =>
    <String, dynamic>{
      'type': instance.type.toJson(),
      'cron': instance.cron,
    };

const _$ScheduleTriggerTypeEnumMap = {
  ScheduleTriggerType.schedule: 'schedule',
};
