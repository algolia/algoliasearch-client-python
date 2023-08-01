// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'funnel_stage.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

FunnelStage _$FunnelStageFromJson(Map<String, dynamic> json) => $checkedCreate(
      'FunnelStage',
      json,
      ($checkedConvert) {
        final val = FunnelStage(
          name: $checkedConvert('name', (v) => v as String),
          probability:
              $checkedConvert('probability', (v) => (v as num).toDouble()),
        );
        return val;
      },
    );

Map<String, dynamic> _$FunnelStageToJson(FunnelStage instance) =>
    <String, dynamic>{
      'name': instance.name,
      'probability': instance.probability,
    };
