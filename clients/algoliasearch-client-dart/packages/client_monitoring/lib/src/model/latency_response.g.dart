// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'latency_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

LatencyResponse _$LatencyResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'LatencyResponse',
      json,
      ($checkedConvert) {
        final val = LatencyResponse(
          metrics: $checkedConvert(
              'metrics',
              (v) => v == null
                  ? null
                  : LatencyResponseMetrics.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$LatencyResponseToJson(LatencyResponse instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('metrics', instance.metrics?.toJson());
  return val;
}
