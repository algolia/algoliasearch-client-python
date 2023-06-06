// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'base_get_api_key_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BaseGetApiKeyResponse _$BaseGetApiKeyResponseFromJson(
        Map<String, dynamic> json) =>
    BaseGetApiKeyResponse(
      value: json['value'] as String?,
      createdAt: json['createdAt'] as int,
    );

Map<String, dynamic> _$BaseGetApiKeyResponseToJson(
        BaseGetApiKeyResponse instance) =>
    <String, dynamic>{
      'value': instance.value,
      'createdAt': instance.createdAt,
    };
