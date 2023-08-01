// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'authentication_update.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AuthenticationUpdate _$AuthenticationUpdateFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'AuthenticationUpdate',
      json,
      ($checkedConvert) {
        final val = AuthenticationUpdate(
          type: $checkedConvert('type',
              (v) => $enumDecodeNullable(_$AuthenticationTypeEnumMap, v)),
          name: $checkedConvert('name', (v) => v as String?),
          platform: $checkedConvert(
              'platform', (v) => $enumDecodeNullable(_$PlatformEnumMap, v)),
          input: $checkedConvert('input', (v) => v),
        );
        return val;
      },
    );

Map<String, dynamic> _$AuthenticationUpdateToJson(
    AuthenticationUpdate instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('type', instance.type?.toJson());
  writeNotNull('name', instance.name);
  writeNotNull('platform', instance.platform?.toJson());
  writeNotNull('input', instance.input);
  return val;
}

const _$AuthenticationTypeEnumMap = {
  AuthenticationType.googleServiceAccount: 'googleServiceAccount',
  AuthenticationType.basic: 'basic',
  AuthenticationType.apiKey: 'apiKey',
  AuthenticationType.oauth: 'oauth',
  AuthenticationType.algolia: 'algolia',
};

const _$PlatformEnumMap = {
  Platform.bigcommerce: 'bigcommerce',
  Platform.commercetools: 'commercetools',
};
