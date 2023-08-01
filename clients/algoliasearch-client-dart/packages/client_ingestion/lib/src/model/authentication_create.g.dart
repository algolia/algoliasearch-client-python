// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'authentication_create.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AuthenticationCreate _$AuthenticationCreateFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'AuthenticationCreate',
      json,
      ($checkedConvert) {
        final val = AuthenticationCreate(
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$AuthenticationTypeEnumMap, v)),
          name: $checkedConvert('name', (v) => v as String),
          platform: $checkedConvert(
              'platform', (v) => $enumDecodeNullable(_$PlatformEnumMap, v)),
          input: $checkedConvert('input', (v) => v),
        );
        return val;
      },
    );

Map<String, dynamic> _$AuthenticationCreateToJson(
    AuthenticationCreate instance) {
  final val = <String, dynamic>{
    'type': instance.type.toJson(),
    'name': instance.name,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

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
