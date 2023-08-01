// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'infrastructure_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

InfrastructureResponse _$InfrastructureResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'InfrastructureResponse',
      json,
      ($checkedConvert) {
        final val = InfrastructureResponse(
          metrics: $checkedConvert(
              'metrics',
              (v) => v == null
                  ? null
                  : InfrastructureResponseMetrics.fromJson(
                      v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$InfrastructureResponseToJson(
    InfrastructureResponse instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('metrics', instance.metrics?.toJson());
  return val;
}
