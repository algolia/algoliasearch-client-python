// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'events_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

EventsResponse _$EventsResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'EventsResponse',
      json,
      ($checkedConvert) {
        final val = EventsResponse(
          message: $checkedConvert('message', (v) => v as String?),
          status: $checkedConvert('status', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$EventsResponseToJson(EventsResponse instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('message', instance.message);
  writeNotNull('status', instance.status);
  return val;
}
