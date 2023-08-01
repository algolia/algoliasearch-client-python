// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'average_click_event.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AverageClickEvent _$AverageClickEventFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'AverageClickEvent',
      json,
      ($checkedConvert) {
        final val = AverageClickEvent(
          average: $checkedConvert('average', (v) => (v as num).toDouble()),
          clickCount: $checkedConvert('clickCount', (v) => v as int),
          date: $checkedConvert('date', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$AverageClickEventToJson(AverageClickEvent instance) =>
    <String, dynamic>{
      'average': instance.average,
      'clickCount': instance.clickCount,
      'date': instance.date,
    };
