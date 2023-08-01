// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'segment_order_value_filter.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SegmentOrderValueFilter _$SegmentOrderValueFilterFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SegmentOrderValueFilter',
      json,
      ($checkedConvert) {
        final val = SegmentOrderValueFilter(
          operator: $checkedConvert(
              'operator',
              (v) => $enumDecodeNullable(
                  _$SegmentFilterOperatorNumericalEnumMap, v)),
          value: $checkedConvert('value', (v) => v as num),
        );
        return val;
      },
    );

Map<String, dynamic> _$SegmentOrderValueFilterToJson(
    SegmentOrderValueFilter instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('operator', instance.operator?.toJson());
  val['value'] = instance.value;
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
