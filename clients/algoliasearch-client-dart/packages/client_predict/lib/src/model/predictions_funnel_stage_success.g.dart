// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'predictions_funnel_stage_success.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

PredictionsFunnelStageSuccess _$PredictionsFunnelStageSuccessFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'PredictionsFunnelStageSuccess',
      json,
      ($checkedConvert) {
        final val = PredictionsFunnelStageSuccess(
          value: $checkedConvert(
              'value',
              (v) => (v as List<dynamic>)
                  .map((e) => FunnelStage.fromJson(e as Map<String, dynamic>))
                  .toList()),
          lastUpdatedAt: $checkedConvert('lastUpdatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$PredictionsFunnelStageSuccessToJson(
        PredictionsFunnelStageSuccess instance) =>
    <String, dynamic>{
      'value': instance.value.map((e) => e.toJson()).toList(),
      'lastUpdatedAt': instance.lastUpdatedAt,
    };
