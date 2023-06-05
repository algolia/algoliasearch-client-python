// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'add_api_key_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AddApiKeyResponse _$AddApiKeyResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'AddApiKeyResponse',
      json,
      ($checkedConvert) {
        final val = AddApiKeyResponse(
          key: $checkedConvert('key', (v) => v as String),
          createdAt: $checkedConvert('createdAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$AddApiKeyResponseToJson(AddApiKeyResponse instance) =>
    <String, dynamic>{
      'key': instance.key,
      'createdAt': instance.createdAt,
    };
