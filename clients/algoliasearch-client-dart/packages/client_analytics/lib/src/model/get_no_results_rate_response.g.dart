// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_no_results_rate_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetNoResultsRateResponse _$GetNoResultsRateResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetNoResultsRateResponse',
      json,
      ($checkedConvert) {
        final val = GetNoResultsRateResponse(
          rate: $checkedConvert('rate', (v) => (v as num).toDouble()),
          count: $checkedConvert('count', (v) => v as int),
          noResultCount: $checkedConvert('noResultCount', (v) => v as int),
          dates: $checkedConvert(
              'dates',
              (v) => (v as List<dynamic>)
                  .map((e) =>
                      NoResultsRateEvent.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetNoResultsRateResponseToJson(
        GetNoResultsRateResponse instance) =>
    <String, dynamic>{
      'rate': instance.rate,
      'count': instance.count,
      'noResultCount': instance.noResultCount,
      'dates': instance.dates.map((e) => e.toJson()).toList(),
    };
