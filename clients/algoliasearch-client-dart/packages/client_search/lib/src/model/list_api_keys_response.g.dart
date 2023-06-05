// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'list_api_keys_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ListApiKeysResponse _$ListApiKeysResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ListApiKeysResponse',
      json,
      ($checkedConvert) {
        final val = ListApiKeysResponse(
          keys: $checkedConvert(
              'keys',
              (v) => (v as List<dynamic>)
                  .map((e) =>
                      GetApiKeyResponse.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$ListApiKeysResponseToJson(
        ListApiKeysResponse instance) =>
    <String, dynamic>{
      'keys': instance.keys.map((e) => e.toJson()).toList(),
    };
