// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'source_create_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SourceCreateResponse _$SourceCreateResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SourceCreateResponse',
      json,
      ($checkedConvert) {
        final val = SourceCreateResponse(
          sourceID: $checkedConvert('sourceID', (v) => v as String),
          name: $checkedConvert('name', (v) => v as String),
          createdAt: $checkedConvert('createdAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$SourceCreateResponseToJson(
        SourceCreateResponse instance) =>
    <String, dynamic>{
      'sourceID': instance.sourceID,
      'name': instance.name,
      'createdAt': instance.createdAt,
    };
