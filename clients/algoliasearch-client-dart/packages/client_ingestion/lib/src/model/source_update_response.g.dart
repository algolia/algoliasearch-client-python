// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'source_update_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SourceUpdateResponse _$SourceUpdateResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SourceUpdateResponse',
      json,
      ($checkedConvert) {
        final val = SourceUpdateResponse(
          sourceID: $checkedConvert('sourceID', (v) => v as String),
          name: $checkedConvert('name', (v) => v as String),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$SourceUpdateResponseToJson(
        SourceUpdateResponse instance) =>
    <String, dynamic>{
      'sourceID': instance.sourceID,
      'name': instance.name,
      'updatedAt': instance.updatedAt,
    };
