// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'on_demand_trigger.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

OnDemandTrigger _$OnDemandTriggerFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'OnDemandTrigger',
      json,
      ($checkedConvert) {
        final val = OnDemandTrigger(
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$OnDemandTriggerTypeEnumMap, v)),
          lastRun: $checkedConvert('lastRun', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$OnDemandTriggerToJson(OnDemandTrigger instance) {
  final val = <String, dynamic>{
    'type': instance.type.toJson(),
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('lastRun', instance.lastRun);
  return val;
}

const _$OnDemandTriggerTypeEnumMap = {
  OnDemandTriggerType.onDemand: 'onDemand',
};
