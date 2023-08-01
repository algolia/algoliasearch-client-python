// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'segment_affinity_filter.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SegmentAffinityFilter _$SegmentAffinityFilterFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SegmentAffinityFilter',
      json,
      ($checkedConvert) {
        final val = SegmentAffinityFilter(
          operator: $checkedConvert('operator',
              (v) => $enumDecode(_$SegmentFilterOperatorNumericalEnumMap, v)),
          value: $checkedConvert('value', (v) => v),
          probability: $checkedConvert(
              'probability',
              (v) => v == null
                  ? null
                  : SegmentFilterProbability.fromJson(
                      v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$SegmentAffinityFilterToJson(
    SegmentAffinityFilter instance) {
  final val = <String, dynamic>{
    'operator': instance.operator.toJson(),
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('value', instance.value);
  writeNotNull('probability', instance.probability?.toJson());
  return val;
}

const _$SegmentFilterOperatorNumericalEnumMap = {
  SegmentFilterOperatorNumerical.eq: 'EQ',
  SegmentFilterOperatorNumerical.neq: 'NEQ',
  SegmentFilterOperatorNumerical.gt: 'GT',
  SegmentFilterOperatorNumerical.gte: 'GTE',
  SegmentFilterOperatorNumerical.lt: 'LT',
  SegmentFilterOperatorNumerical.lte: 'LTE',
};
