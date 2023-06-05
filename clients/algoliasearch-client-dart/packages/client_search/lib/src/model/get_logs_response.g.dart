// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_logs_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetLogsResponse _$GetLogsResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'GetLogsResponse',
      json,
      ($checkedConvert) {
        final val = GetLogsResponse(
          logs: $checkedConvert(
              'logs',
              (v) => (v as List<dynamic>)
                  .map((e) => Log.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetLogsResponseToJson(GetLogsResponse instance) =>
    <String, dynamic>{
      'logs': instance.logs.map((e) => e.toJson()).toList(),
    };
