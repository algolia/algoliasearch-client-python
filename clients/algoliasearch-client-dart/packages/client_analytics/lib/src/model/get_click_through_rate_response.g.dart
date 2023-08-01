// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_click_through_rate_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetClickThroughRateResponse _$GetClickThroughRateResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetClickThroughRateResponse',
      json,
      ($checkedConvert) {
        final val = GetClickThroughRateResponse(
          rate: $checkedConvert('rate', (v) => (v as num).toDouble()),
          clickCount: $checkedConvert('clickCount', (v) => v as int),
          trackedSearchCount:
              $checkedConvert('trackedSearchCount', (v) => v as int),
          dates: $checkedConvert(
              'dates',
              (v) => (v as List<dynamic>)
                  .map((e) =>
                      ClickThroughRateEvent.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetClickThroughRateResponseToJson(
        GetClickThroughRateResponse instance) =>
    <String, dynamic>{
      'rate': instance.rate,
      'clickCount': instance.clickCount,
      'trackedSearchCount': instance.trackedSearchCount,
      'dates': instance.dates.map((e) => e.toJson()).toList(),
    };
