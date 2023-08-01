// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_log_file200_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetLogFile200Response _$GetLogFile200ResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetLogFile200Response',
      json,
      ($checkedConvert) {
        final val = GetLogFile200Response(
          timestamp: $checkedConvert('timestamp', (v) => v as String?),
          level: $checkedConvert(
              'level', (v) => $enumDecodeNullable(_$LogLevelEnumMap, v)),
          message: $checkedConvert('message', (v) => v as String?),
          contextLevel: $checkedConvert('contextLevel', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetLogFile200ResponseToJson(
    GetLogFile200Response instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('timestamp', instance.timestamp);
  writeNotNull('level', instance.level?.toJson());
  writeNotNull('message', instance.message);
  writeNotNull('contextLevel', instance.contextLevel);
  return val;
}

const _$LogLevelEnumMap = {
  LogLevel.skip: 'SKIP',
  LogLevel.info: 'INFO',
  LogLevel.error: 'ERROR',
};
