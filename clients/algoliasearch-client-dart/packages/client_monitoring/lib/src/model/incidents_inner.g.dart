// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'incidents_inner.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

IncidentsInner _$IncidentsInnerFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'IncidentsInner',
      json,
      ($checkedConvert) {
        final val = IncidentsInner(
          t: $checkedConvert('t', (v) => v as int?),
          v: $checkedConvert(
              'v',
              (v) => v == null
                  ? null
                  : Incident.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$IncidentsInnerToJson(IncidentsInner instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('t', instance.t);
  writeNotNull('v', instance.v?.toJson());
  return val;
}
