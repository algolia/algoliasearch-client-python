// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'segment_property_filter.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SegmentPropertyFilter _$SegmentPropertyFilterFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SegmentPropertyFilter',
      json,
      ($checkedConvert) {
        final val = SegmentPropertyFilter(
          operator: $checkedConvert(
              'operator',
              (v) => $enumDecodeNullable(
                  _$SegmentFilterOperatorNumericalEnumMap, v)),
          value: $checkedConvert('value', (v) => v),
        );
        return val;
      },
    );

Map<String, dynamic> _$SegmentPropertyFilterToJson(
    SegmentPropertyFilter instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('operator', instance.operator?.toJson());
  writeNotNull('value', instance.value);
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
