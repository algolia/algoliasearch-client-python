// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'auth_basic.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AuthBasic _$AuthBasicFromJson(Map<String, dynamic> json) => $checkedCreate(
      'AuthBasic',
      json,
      ($checkedConvert) {
        final val = AuthBasic(
          username: $checkedConvert('username', (v) => v as String),
          password: $checkedConvert('password', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$AuthBasicToJson(AuthBasic instance) => <String, dynamic>{
      'username': instance.username,
      'password': instance.password,
    };
