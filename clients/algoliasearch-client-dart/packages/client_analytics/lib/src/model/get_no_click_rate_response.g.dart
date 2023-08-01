// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_no_click_rate_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetNoClickRateResponse _$GetNoClickRateResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetNoClickRateResponse',
      json,
      ($checkedConvert) {
        final val = GetNoClickRateResponse(
          rate: $checkedConvert('rate', (v) => (v as num).toDouble()),
          count: $checkedConvert('count', (v) => v as int),
          noClickCount: $checkedConvert('noClickCount', (v) => v as int),
          dates: $checkedConvert(
              'dates',
              (v) => (v as List<dynamic>)
                  .map((e) =>
                      NoClickRateEvent.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetNoClickRateResponseToJson(
        GetNoClickRateResponse instance) =>
    <String, dynamic>{
      'rate': instance.rate,
      'count': instance.count,
      'noClickCount': instance.noClickCount,
      'dates': instance.dates.map((e) => e.toJson()).toList(),
    };
