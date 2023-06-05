// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'update_api_key_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

UpdateApiKeyResponse _$UpdateApiKeyResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'UpdateApiKeyResponse',
      json,
      ($checkedConvert) {
        final val = UpdateApiKeyResponse(
          key: $checkedConvert('key', (v) => v as String),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$UpdateApiKeyResponseToJson(
        UpdateApiKeyResponse instance) =>
    <String, dynamic>{
      'key': instance.key,
      'updatedAt': instance.updatedAt,
    };
