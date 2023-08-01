// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_inventory403_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetInventory403Response _$GetInventory403ResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetInventory403Response',
      json,
      ($checkedConvert) {
        final val = GetInventory403Response(
          reason: $checkedConvert('reason', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetInventory403ResponseToJson(
    GetInventory403Response instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('reason', instance.reason);
  return val;
}
