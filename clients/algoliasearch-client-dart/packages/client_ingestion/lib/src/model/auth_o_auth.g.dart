// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'auth_o_auth.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AuthOAuth _$AuthOAuthFromJson(Map<String, dynamic> json) => $checkedCreate(
      'AuthOAuth',
      json,
      ($checkedConvert) {
        final val = AuthOAuth(
          url: $checkedConvert('url', (v) => v as String),
          clientId: $checkedConvert('client_id', (v) => v as String),
          clientSecret: $checkedConvert('client_secret', (v) => v as String),
        );
        return val;
      },
      fieldKeyMap: const {
        'clientId': 'client_id',
        'clientSecret': 'client_secret'
      },
    );

Map<String, dynamic> _$AuthOAuthToJson(AuthOAuth instance) => <String, dynamic>{
      'url': instance.url,
      'client_id': instance.clientId,
      'client_secret': instance.clientSecret,
    };
