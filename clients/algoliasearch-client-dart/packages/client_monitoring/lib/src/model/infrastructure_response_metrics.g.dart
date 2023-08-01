// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'infrastructure_response_metrics.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

InfrastructureResponseMetrics _$InfrastructureResponseMetricsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'InfrastructureResponseMetrics',
      json,
      ($checkedConvert) {
        final val = InfrastructureResponseMetrics(
          cpuUsage: $checkedConvert(
              'cpu_usage',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) => MapEntry(
                        k,
                        (e as List<dynamic>)
                            .map((e) => ProbesMetric.fromJson(
                                e as Map<String, dynamic>))
                            .toList()),
                  )),
          ramIndexingUsage: $checkedConvert(
              'ram_indexing_usage',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) => MapEntry(
                        k,
                        (e as List<dynamic>)
                            .map((e) => ProbesMetric.fromJson(
                                e as Map<String, dynamic>))
                            .toList()),
                  )),
          ramSearchUsage: $checkedConvert(
              'ram_search_usage',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) => MapEntry(
                        k,
                        (e as List<dynamic>)
                            .map((e) => ProbesMetric.fromJson(
                                e as Map<String, dynamic>))
                            .toList()),
                  )),
          ssdUsage: $checkedConvert(
              'ssd_usage',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) => MapEntry(
                        k,
                        (e as List<dynamic>)
                            .map((e) => ProbesMetric.fromJson(
                                e as Map<String, dynamic>))
                            .toList()),
                  )),
          avgBuildTime: $checkedConvert(
              'avg_build_time',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) => MapEntry(
                        k,
                        (e as List<dynamic>)
                            .map((e) => ProbesMetric.fromJson(
                                e as Map<String, dynamic>))
                            .toList()),
                  )),
        );
        return val;
      },
      fieldKeyMap: const {
        'cpuUsage': 'cpu_usage',
        'ramIndexingUsage': 'ram_indexing_usage',
        'ramSearchUsage': 'ram_search_usage',
        'ssdUsage': 'ssd_usage',
        'avgBuildTime': 'avg_build_time'
      },
    );

Map<String, dynamic> _$InfrastructureResponseMetricsToJson(
    InfrastructureResponseMetrics instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull(
      'cpu_usage',
      instance.cpuUsage
          ?.map((k, e) => MapEntry(k, e.map((e) => e.toJson()).toList())));
  writeNotNull(
      'ram_indexing_usage',
      instance.ramIndexingUsage
          ?.map((k, e) => MapEntry(k, e.map((e) => e.toJson()).toList())));
  writeNotNull(
      'ram_search_usage',
      instance.ramSearchUsage
          ?.map((k, e) => MapEntry(k, e.map((e) => e.toJson()).toList())));
  writeNotNull(
      'ssd_usage',
      instance.ssdUsage
          ?.map((k, e) => MapEntry(k, e.map((e) => e.toJson()).toList())));
  writeNotNull(
      'avg_build_time',
      instance.avgBuildTime
          ?.map((k, e) => MapEntry(k, e.map((e) => e.toJson()).toList())));
  return val;
}
