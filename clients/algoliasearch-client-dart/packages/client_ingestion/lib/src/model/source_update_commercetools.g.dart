// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'source_update_commercetools.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SourceUpdateCommercetools _$SourceUpdateCommercetoolsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SourceUpdateCommercetools',
      json,
      ($checkedConvert) {
        final val = SourceUpdateCommercetools(
          storeKeys: $checkedConvert('storeKeys',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          locales: $checkedConvert('locales',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$SourceUpdateCommercetoolsToJson(
    SourceUpdateCommercetools instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('storeKeys', instance.storeKeys);
  writeNotNull('locales', instance.locales);
  return val;
}
