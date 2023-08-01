// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'predictions_order_value_success.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

PredictionsOrderValueSuccess _$PredictionsOrderValueSuccessFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'PredictionsOrderValueSuccess',
      json,
      ($checkedConvert) {
        final val = PredictionsOrderValueSuccess(
          value: $checkedConvert('value', (v) => (v as num).toDouble()),
          lastUpdatedAt: $checkedConvert('lastUpdatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$PredictionsOrderValueSuccessToJson(
        PredictionsOrderValueSuccess instance) =>
    <String, dynamic>{
      'value': instance.value,
      'lastUpdatedAt': instance.lastUpdatedAt,
    };
