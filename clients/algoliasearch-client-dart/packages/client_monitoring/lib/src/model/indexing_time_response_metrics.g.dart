// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'indexing_time_response_metrics.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

IndexingTimeResponseMetrics _$IndexingTimeResponseMetricsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'IndexingTimeResponseMetrics',
      json,
      ($checkedConvert) {
        final val = IndexingTimeResponseMetrics(
          indexing: $checkedConvert(
              'indexing',
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

Map<String, dynamic> _$IndexingTimeResponseMetricsToJson(
    IndexingTimeResponseMetrics instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull(
      'indexing',
      instance.indexing
          ?.map((k, e) => MapEntry(k, e.map((e) => e.toJson()).toList())));
  return val;
}
