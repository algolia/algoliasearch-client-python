// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'no_results_rate_event.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

NoResultsRateEvent _$NoResultsRateEventFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'NoResultsRateEvent',
      json,
      ($checkedConvert) {
        final val = NoResultsRateEvent(
          date: $checkedConvert('date', (v) => v as String),
          noResultCount: $checkedConvert('noResultCount', (v) => v as int),
          count: $checkedConvert('count', (v) => v as int),
          rate: $checkedConvert('rate', (v) => (v as num).toDouble()),
        );
        return val;
      },
    );

Map<String, dynamic> _$NoResultsRateEventToJson(NoResultsRateEvent instance) =>
    <String, dynamic>{
      'date': instance.date,
      'noResultCount': instance.noResultCount,
      'count': instance.count,
      'rate': instance.rate,
    };
