// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'auth_api_key_partial.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AuthAPIKeyPartial _$AuthAPIKeyPartialFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'AuthAPIKeyPartial',
      json,
      ($checkedConvert) {
        final val = AuthAPIKeyPartial(
          key: $checkedConvert('key', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$AuthAPIKeyPartialToJson(AuthAPIKeyPartial instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('key', instance.key);
  return val;
}
