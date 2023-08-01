// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'inventory_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

InventoryResponse _$InventoryResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'InventoryResponse',
      json,
      ($checkedConvert) {
        final val = InventoryResponse(
          inventory: $checkedConvert(
              'inventory',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => Server.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$InventoryResponseToJson(InventoryResponse instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull(
      'inventory', instance.inventory?.map((e) => e.toJson()).toList());
  return val;
}
