// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'big_commerce_channel.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BigCommerceChannel _$BigCommerceChannelFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'BigCommerceChannel',
      json,
      ($checkedConvert) {
        final val = BigCommerceChannel(
          id: $checkedConvert('id', (v) => v as int),
          currencies: $checkedConvert('currencies',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$BigCommerceChannelToJson(BigCommerceChannel instance) {
  final val = <String, dynamic>{
    'id': instance.id,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('currencies', instance.currencies);
  return val;
}
