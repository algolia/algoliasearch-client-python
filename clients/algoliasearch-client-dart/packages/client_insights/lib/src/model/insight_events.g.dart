// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'insight_events.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

InsightEvents _$InsightEventsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'InsightEvents',
      json,
      ($checkedConvert) {
        final val = InsightEvents(
          events: $checkedConvert(
              'events',
              (v) => (v as List<dynamic>)
                  .map((e) => InsightEvent.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$InsightEventsToJson(InsightEvents instance) =>
    <String, dynamic>{
      'events': instance.events.map((e) => e.toJson()).toList(),
    };
