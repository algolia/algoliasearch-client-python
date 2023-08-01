// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'segment_funnel_stage_filter.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SegmentFunnelStageFilter _$SegmentFunnelStageFilterFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SegmentFunnelStageFilter',
      json,
      ($checkedConvert) {
        final val = SegmentFunnelStageFilter(
          operator: $checkedConvert(
              'operator',
              (v) => $enumDecodeNullable(
                  _$SegmentFilterOperatorBooleanEnumMap, v)),
          value: $checkedConvert('value', (v) => v as String),
          probability: $checkedConvert(
              'probability',
              (v) =>
                  SegmentFilterProbability.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$SegmentFunnelStageFilterToJson(
    SegmentFunnelStageFilter instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('operator', instance.operator?.toJson());
  val['value'] = instance.value;
  val['probability'] = instance.probability.toJson();
  return val;
}

const _$SegmentFilterOperatorBooleanEnumMap = {
  SegmentFilterOperatorBoolean.eq: 'EQ',
  SegmentFilterOperatorBoolean.neq: 'NEQ',
};
