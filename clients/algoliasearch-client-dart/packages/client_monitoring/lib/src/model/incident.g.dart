// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'incident.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Incident _$IncidentFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Incident',
      json,
      ($checkedConvert) {
        final val = Incident(
          title: $checkedConvert('title', (v) => v as String?),
          status: $checkedConvert(
              'status', (v) => $enumDecodeNullable(_$StatusEnumMap, v)),
        );
        return val;
      },
    );

Map<String, dynamic> _$IncidentToJson(Incident instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('title', instance.title);
  writeNotNull('status', instance.status?.toJson());
  return val;
}

const _$StatusEnumMap = {
  Status.operational: 'operational',
  Status.degradedPerformance: 'degraded_performance',
  Status.partialOutage: 'partial_outage',
  Status.majorOutage: 'major_outage',
};
