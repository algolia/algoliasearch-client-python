// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'object_data.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ObjectData _$ObjectDataFromJson(Map<String, dynamic> json) => $checkedCreate(
      'ObjectData',
      json,
      ($checkedConvert) {
        final val = ObjectData(
          price: $checkedConvert('price', (v) => v),
          quantity: $checkedConvert('quantity', (v) => v as int?),
          discount: $checkedConvert('discount', (v) => v),
        );
        return val;
      },
    );

Map<String, dynamic> _$ObjectDataToJson(ObjectData instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('price', instance.price);
  writeNotNull('quantity', instance.quantity);
  writeNotNull('discount', instance.discount);
  return val;
}
