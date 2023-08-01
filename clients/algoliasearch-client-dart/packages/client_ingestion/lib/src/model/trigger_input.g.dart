// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'trigger_input.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TriggerInput _$TriggerInputFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'TriggerInput',
      json,
      ($checkedConvert) {
        final val = TriggerInput(
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$TriggerTypeEnumMap, v)),
        );
        return val;
      },
    );

Map<String, dynamic> _$TriggerInputToJson(TriggerInput instance) =>
    <String, dynamic>{
      'type': instance.type.toJson(),
    };

const _$TriggerTypeEnumMap = {
  TriggerType.onDemand: 'onDemand',
  TriggerType.schedule: 'schedule',
  TriggerType.subscription: 'subscription',
};
