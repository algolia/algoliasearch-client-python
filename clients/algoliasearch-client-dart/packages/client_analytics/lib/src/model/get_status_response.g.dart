// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_status_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetStatusResponse _$GetStatusResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'GetStatusResponse',
      json,
      ($checkedConvert) {
        final val = GetStatusResponse(
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetStatusResponseToJson(GetStatusResponse instance) =>
    <String, dynamic>{
      'updatedAt': instance.updatedAt,
    };
