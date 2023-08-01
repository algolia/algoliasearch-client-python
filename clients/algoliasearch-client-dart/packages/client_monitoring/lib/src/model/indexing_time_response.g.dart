// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'indexing_time_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

IndexingTimeResponse _$IndexingTimeResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'IndexingTimeResponse',
      json,
      ($checkedConvert) {
        final val = IndexingTimeResponse(
          metrics: $checkedConvert(
              'metrics',
              (v) => v == null
                  ? null
                  : IndexingTimeResponseMetrics.fromJson(
                      v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$IndexingTimeResponseToJson(
    IndexingTimeResponse instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('metrics', instance.metrics?.toJson());
  return val;
}
