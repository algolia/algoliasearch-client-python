// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'probes_metric.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ProbesMetric _$ProbesMetricFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ProbesMetric',
      json,
      ($checkedConvert) {
        final val = ProbesMetric(
          t: $checkedConvert('t', (v) => v as int?),
          v: $checkedConvert('v', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$ProbesMetricToJson(ProbesMetric instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('t', instance.t);
  writeNotNull('v', instance.v);
  return val;
}
