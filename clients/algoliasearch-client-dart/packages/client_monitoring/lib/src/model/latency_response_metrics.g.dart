// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'latency_response_metrics.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

LatencyResponseMetrics _$LatencyResponseMetricsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'LatencyResponseMetrics',
      json,
      ($checkedConvert) {
        final val = LatencyResponseMetrics(
          latency: $checkedConvert(
              'latency',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) => MapEntry(
                        k,
                        (e as List<dynamic>)
                            .map((e) =>
                                TimeInner.fromJson(e as Map<String, dynamic>))
                            .toList()),
                  )),
        );
        return val;
      },
    );

Map<String, dynamic> _$LatencyResponseMetricsToJson(
    LatencyResponseMetrics instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull(
      'latency',
      instance.latency
          ?.map((k, e) => MapEntry(k, e.map((e) => e.toJson()).toList())));
  return val;
}
