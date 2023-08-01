// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'click_through_rate_event.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ClickThroughRateEvent _$ClickThroughRateEventFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'ClickThroughRateEvent',
      json,
      ($checkedConvert) {
        final val = ClickThroughRateEvent(
          rate: $checkedConvert('rate', (v) => (v as num).toDouble()),
          clickCount: $checkedConvert('clickCount', (v) => v as int),
          trackedSearchCount:
              $checkedConvert('trackedSearchCount', (v) => v as int),
          date: $checkedConvert('date', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$ClickThroughRateEventToJson(
        ClickThroughRateEvent instance) =>
    <String, dynamic>{
      'rate': instance.rate,
      'clickCount': instance.clickCount,
      'trackedSearchCount': instance.trackedSearchCount,
      'date': instance.date,
    };
