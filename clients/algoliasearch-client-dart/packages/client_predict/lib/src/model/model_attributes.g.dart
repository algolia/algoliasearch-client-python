// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'model_attributes.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ModelAttributes _$ModelAttributesFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ModelAttributes',
      json,
      ($checkedConvert) {
        final val = ModelAttributes(
          name: $checkedConvert('name', (v) => v as String),
          values: $checkedConvert('values',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$ModelAttributesToJson(ModelAttributes instance) {
  final val = <String, dynamic>{
    'name': instance.name,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('values', instance.values);
  return val;
}
