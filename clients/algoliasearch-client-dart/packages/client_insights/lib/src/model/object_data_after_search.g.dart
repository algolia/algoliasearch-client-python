// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'object_data_after_search.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ObjectDataAfterSearch _$ObjectDataAfterSearchFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'ObjectDataAfterSearch',
      json,
      ($checkedConvert) {
        final val = ObjectDataAfterSearch(
          queryID: $checkedConvert('queryID', (v) => v as String?),
          price: $checkedConvert('price', (v) => v),
          quantity: $checkedConvert('quantity', (v) => v as int?),
          discount: $checkedConvert('discount', (v) => v),
        );
        return val;
      },
    );

Map<String, dynamic> _$ObjectDataAfterSearchToJson(
    ObjectDataAfterSearch instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('queryID', instance.queryID);
  writeNotNull('price', instance.price);
  writeNotNull('quantity', instance.quantity);
  writeNotNull('discount', instance.discount);
  return val;
}
