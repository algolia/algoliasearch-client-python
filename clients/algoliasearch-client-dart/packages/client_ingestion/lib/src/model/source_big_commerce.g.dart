// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'source_big_commerce.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SourceBigCommerce _$SourceBigCommerceFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SourceBigCommerce',
      json,
      ($checkedConvert) {
        final val = SourceBigCommerce(
          storeHash: $checkedConvert('storeHash', (v) => v as String?),
          channel: $checkedConvert(
              'channel',
              (v) => v == null
                  ? null
                  : BigCommerceChannel.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$SourceBigCommerceToJson(SourceBigCommerce instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('storeHash', instance.storeHash);
  writeNotNull('channel', instance.channel?.toJson());
  return val;
}
