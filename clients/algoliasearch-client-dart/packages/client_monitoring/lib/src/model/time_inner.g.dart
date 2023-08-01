// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'time_inner.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TimeInner _$TimeInnerFromJson(Map<String, dynamic> json) => $checkedCreate(
      'TimeInner',
      json,
      ($checkedConvert) {
        final val = TimeInner(
          t: $checkedConvert('t', (v) => v as int?),
          v: $checkedConvert('v', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$TimeInnerToJson(TimeInner instance) {
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
