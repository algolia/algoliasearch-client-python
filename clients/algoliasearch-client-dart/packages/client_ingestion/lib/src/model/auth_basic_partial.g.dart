// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'auth_basic_partial.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AuthBasicPartial _$AuthBasicPartialFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'AuthBasicPartial',
      json,
      ($checkedConvert) {
        final val = AuthBasicPartial(
          username: $checkedConvert('username', (v) => v as String?),
          password: $checkedConvert('password', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$AuthBasicPartialToJson(AuthBasicPartial instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('username', instance.username);
  writeNotNull('password', instance.password);
  return val;
}
