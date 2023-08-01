// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'status_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

StatusResponse _$StatusResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'StatusResponse',
      json,
      ($checkedConvert) {
        final val = StatusResponse(
          status: $checkedConvert(
              'status',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) => MapEntry(k, $enumDecode(_$StatusEnumMap, e)),
                  )),
        );
        return val;
      },
    );

Map<String, dynamic> _$StatusResponseToJson(StatusResponse instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull(
      'status', instance.status?.map((k, e) => MapEntry(k, e.toJson())));
  return val;
}

const _$StatusEnumMap = {
  Status.operational: 'operational',
  Status.degradedPerformance: 'degraded_performance',
  Status.partialOutage: 'partial_outage',
  Status.majorOutage: 'major_outage',
};
