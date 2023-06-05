// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'push_events_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

PushEventsResponse _$PushEventsResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'PushEventsResponse',
      json,
      ($checkedConvert) {
        final val = PushEventsResponse(
          message: $checkedConvert('message', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$PushEventsResponseToJson(PushEventsResponse instance) =>
    <String, dynamic>{
      'message': instance.message,
    };
