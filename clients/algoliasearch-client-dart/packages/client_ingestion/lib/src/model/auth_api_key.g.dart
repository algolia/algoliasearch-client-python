// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'auth_api_key.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AuthAPIKey _$AuthAPIKeyFromJson(Map<String, dynamic> json) => $checkedCreate(
      'AuthAPIKey',
      json,
      ($checkedConvert) {
        final val = AuthAPIKey(
          key: $checkedConvert('key', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$AuthAPIKeyToJson(AuthAPIKey instance) =>
    <String, dynamic>{
      'key': instance.key,
    };
