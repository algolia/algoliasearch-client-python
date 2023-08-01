// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_config_status200_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetConfigStatus200Response _$GetConfigStatus200ResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetConfigStatus200Response',
      json,
      ($checkedConvert) {
        final val = GetConfigStatus200Response(
          indexName: $checkedConvert('indexName', (v) => v as String?),
          isRunning: $checkedConvert('isRunning', (v) => v as bool?),
          lastBuiltAt: $checkedConvert('lastBuiltAt', (v) => v as String?),
          lastSuccessfulBuiltAt:
              $checkedConvert('lastSuccessfulBuiltAt', (v) => v as String?),
          lastSuccessfulBuildDuration: $checkedConvert(
              'lastSuccessfulBuildDuration', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetConfigStatus200ResponseToJson(
    GetConfigStatus200Response instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('indexName', instance.indexName);
  writeNotNull('isRunning', instance.isRunning);
  writeNotNull('lastBuiltAt', instance.lastBuiltAt);
  writeNotNull('lastSuccessfulBuiltAt', instance.lastSuccessfulBuiltAt);
  writeNotNull(
      'lastSuccessfulBuildDuration', instance.lastSuccessfulBuildDuration);
  return val;
}
