// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'segment_filter_probability.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SegmentFilterProbability _$SegmentFilterProbabilityFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SegmentFilterProbability',
      json,
      ($checkedConvert) {
        final val = SegmentFilterProbability(
          lt: $checkedConvert('LT', (v) => v as num?),
          lte: $checkedConvert('LTE', (v) => v as num?),
          gt: $checkedConvert('GT', (v) => v as num?),
          gte: $checkedConvert('GTE', (v) => v as num?),
        );
        return val;
      },
      fieldKeyMap: const {'lt': 'LT', 'lte': 'LTE', 'gt': 'GT', 'gte': 'GTE'},
    );

Map<String, dynamic> _$SegmentFilterProbabilityToJson(
    SegmentFilterProbability instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('LT', instance.lt);
  writeNotNull('LTE', instance.lte);
  writeNotNull('GT', instance.gt);
  writeNotNull('GTE', instance.gte);
  return val;
}
