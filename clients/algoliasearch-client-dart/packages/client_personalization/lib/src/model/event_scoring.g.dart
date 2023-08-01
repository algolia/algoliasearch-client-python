// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'event_scoring.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

EventScoring _$EventScoringFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'EventScoring',
      json,
      ($checkedConvert) {
        final val = EventScoring(
          score: $checkedConvert('score', (v) => v as int),
          eventName: $checkedConvert('eventName', (v) => v as String),
          eventType: $checkedConvert('eventType', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$EventScoringToJson(EventScoring instance) =>
    <String, dynamic>{
      'score': instance.score,
      'eventName': instance.eventName,
      'eventType': instance.eventType,
    };
