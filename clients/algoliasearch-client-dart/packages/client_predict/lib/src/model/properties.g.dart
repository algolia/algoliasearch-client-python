// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'properties.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Properties _$PropertiesFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Properties',
      json,
      ($checkedConvert) {
        final val = Properties(
          raw: $checkedConvert('raw', (v) => v),
          computed: $checkedConvert('computed', (v) => v),
          custom: $checkedConvert('custom', (v) => v),
        );
        return val;
      },
    );

Map<String, dynamic> _$PropertiesToJson(Properties instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('raw', instance.raw);
  writeNotNull('computed', instance.computed);
  writeNotNull('custom', instance.custom);
  return val;
}
