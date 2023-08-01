// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'segment_operand_funnel_stage.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SegmentOperandFunnelStage _$SegmentOperandFunnelStageFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SegmentOperandFunnelStage',
      json,
      ($checkedConvert) {
        final val = SegmentOperandFunnelStage(
          name: $checkedConvert('name', (v) => v as String),
          filters: $checkedConvert(
              'filters',
              (v) => (v as List<dynamic>)
                  .map((e) => SegmentFunnelStageFilter.fromJson(
                      e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$SegmentOperandFunnelStageToJson(
        SegmentOperandFunnelStage instance) =>
    <String, dynamic>{
      'name': instance.name,
      'filters': instance.filters.map((e) => e.toJson()).toList(),
    };
