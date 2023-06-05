// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'base_get_api_key_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BaseGetApiKeyResponse _$BaseGetApiKeyResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'BaseGetApiKeyResponse',
      json,
      ($checkedConvert) {
        final val = BaseGetApiKeyResponse(
          value: $checkedConvert('value', (v) => v as String?),
          createdAt: $checkedConvert('createdAt', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$BaseGetApiKeyResponseToJson(
    BaseGetApiKeyResponse instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('value', instance.value);
  val['createdAt'] = instance.createdAt;
  return val;
}
