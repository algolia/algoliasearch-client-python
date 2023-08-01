// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'destination_update_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DestinationUpdateResponse _$DestinationUpdateResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'DestinationUpdateResponse',
      json,
      ($checkedConvert) {
        final val = DestinationUpdateResponse(
          destinationID: $checkedConvert('destinationID', (v) => v as String),
          name: $checkedConvert('name', (v) => v as String),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$DestinationUpdateResponseToJson(
        DestinationUpdateResponse instance) =>
    <String, dynamic>{
      'destinationID': instance.destinationID,
      'name': instance.name,
      'updatedAt': instance.updatedAt,
    };
