// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'conversion_rate_event.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ConversionRateEvent _$ConversionRateEventFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ConversionRateEvent',
      json,
      ($checkedConvert) {
        final val = ConversionRateEvent(
          rate: $checkedConvert('rate', (v) => (v as num).toDouble()),
          trackedSearchCount:
              $checkedConvert('trackedSearchCount', (v) => v as int),
          conversionCount: $checkedConvert('conversionCount', (v) => v as int),
          date: $checkedConvert('date', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$ConversionRateEventToJson(
        ConversionRateEvent instance) =>
    <String, dynamic>{
      'rate': instance.rate,
      'trackedSearchCount': instance.trackedSearchCount,
      'conversionCount': instance.conversionCount,
      'date': instance.date,
    };
