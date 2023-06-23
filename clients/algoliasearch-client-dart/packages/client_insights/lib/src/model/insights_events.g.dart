// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'insights_events.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

InsightsEvents _$InsightsEventsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'InsightsEvents',
      json,
      ($checkedConvert) {
        final val = InsightsEvents(
          events: $checkedConvert('events', (v) => v as List<dynamic>),
        );
        return val;
      },
    );

Map<String, dynamic> _$InsightsEventsToJson(InsightsEvents instance) =>
    <String, dynamic>{
      'events': instance.events.toList(),
    };
