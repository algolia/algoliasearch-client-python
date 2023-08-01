// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'subscription_trigger.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SubscriptionTrigger _$SubscriptionTriggerFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SubscriptionTrigger',
      json,
      ($checkedConvert) {
        final val = SubscriptionTrigger(
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$SubscriptionTriggerTypeEnumMap, v)),
        );
        return val;
      },
    );

Map<String, dynamic> _$SubscriptionTriggerToJson(
        SubscriptionTrigger instance) =>
    <String, dynamic>{
      'type': instance.type.toJson(),
    };

const _$SubscriptionTriggerTypeEnumMap = {
  SubscriptionTriggerType.subscription: 'subscription',
};
