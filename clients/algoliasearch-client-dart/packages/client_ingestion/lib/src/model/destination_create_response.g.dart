// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'destination_create_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DestinationCreateResponse _$DestinationCreateResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'DestinationCreateResponse',
      json,
      ($checkedConvert) {
        final val = DestinationCreateResponse(
          destinationID: $checkedConvert('destinationID', (v) => v as String),
          name: $checkedConvert('name', (v) => v as String),
          createdAt: $checkedConvert('createdAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$DestinationCreateResponseToJson(
        DestinationCreateResponse instance) =>
    <String, dynamic>{
      'destinationID': instance.destinationID,
      'name': instance.name,
      'createdAt': instance.createdAt,
    };
