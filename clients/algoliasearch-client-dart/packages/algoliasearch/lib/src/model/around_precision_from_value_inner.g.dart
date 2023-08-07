// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'around_precision_from_value_inner.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AroundPrecisionFromValueInner _$AroundPrecisionFromValueInnerFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'AroundPrecisionFromValueInner',
      json,
      ($checkedConvert) {
        final val = AroundPrecisionFromValueInner(
          from: $checkedConvert('from', (v) => v as int?),
          value: $checkedConvert('value', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$AroundPrecisionFromValueInnerToJson(
    AroundPrecisionFromValueInner instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('from', instance.from);
  writeNotNull('value', instance.value);
  return val;
}
