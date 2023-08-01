// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'list_events_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ListEventsResponse _$ListEventsResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ListEventsResponse',
      json,
      ($checkedConvert) {
        final val = ListEventsResponse(
          events: $checkedConvert(
              'events',
              (v) => (v as List<dynamic>)
                  .map((e) => Event.fromJson(e as Map<String, dynamic>))
                  .toList()),
          pagination: $checkedConvert('pagination',
              (v) => Pagination.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$ListEventsResponseToJson(ListEventsResponse instance) =>
    <String, dynamic>{
      'events': instance.events.map((e) => e.toJson()).toList(),
      'pagination': instance.pagination.toJson(),
    };
