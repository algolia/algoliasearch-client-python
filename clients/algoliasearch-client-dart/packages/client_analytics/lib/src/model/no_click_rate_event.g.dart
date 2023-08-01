// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'no_click_rate_event.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

NoClickRateEvent _$NoClickRateEventFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'NoClickRateEvent',
      json,
      ($checkedConvert) {
        final val = NoClickRateEvent(
          rate: $checkedConvert('rate', (v) => (v as num).toDouble()),
          count: $checkedConvert('count', (v) => v as int),
          noClickCount: $checkedConvert('noClickCount', (v) => v as int),
          date: $checkedConvert('date', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$NoClickRateEventToJson(NoClickRateEvent instance) =>
    <String, dynamic>{
      'rate': instance.rate,
      'count': instance.count,
      'noClickCount': instance.noClickCount,
      'date': instance.date,
    };
