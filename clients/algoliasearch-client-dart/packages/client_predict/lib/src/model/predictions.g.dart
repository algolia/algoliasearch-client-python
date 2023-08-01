// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'predictions.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Predictions _$PredictionsFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Predictions',
      json,
      ($checkedConvert) {
        final val = Predictions(
          funnelStage: $checkedConvert('funnel_stage', (v) => v),
          orderValue: $checkedConvert('order_value', (v) => v),
          affinities: $checkedConvert('affinities', (v) => v),
        );
        return val;
      },
      fieldKeyMap: const {
        'funnelStage': 'funnel_stage',
        'orderValue': 'order_value'
      },
    );

Map<String, dynamic> _$PredictionsToJson(Predictions instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('funnel_stage', instance.funnelStage);
  writeNotNull('order_value', instance.orderValue);
  writeNotNull('affinities', instance.affinities);
  return val;
}
