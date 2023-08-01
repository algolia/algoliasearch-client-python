// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'on_demand_trigger_input.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

OnDemandTriggerInput _$OnDemandTriggerInputFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'OnDemandTriggerInput',
      json,
      ($checkedConvert) {
        final val = OnDemandTriggerInput(
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$OnDemandTriggerTypeEnumMap, v)),
        );
        return val;
      },
    );

Map<String, dynamic> _$OnDemandTriggerInputToJson(
        OnDemandTriggerInput instance) =>
    <String, dynamic>{
      'type': instance.type.toJson(),
    };

const _$OnDemandTriggerTypeEnumMap = {
  OnDemandTriggerType.onDemand: 'onDemand',
};
