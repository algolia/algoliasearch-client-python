// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_average_click_position_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetAverageClickPositionResponse _$GetAverageClickPositionResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetAverageClickPositionResponse',
      json,
      ($checkedConvert) {
        final val = GetAverageClickPositionResponse(
          average: $checkedConvert('average', (v) => (v as num).toDouble()),
          clickCount: $checkedConvert('clickCount', (v) => v as int),
          dates: $checkedConvert(
              'dates',
              (v) => (v as List<dynamic>)
                  .map((e) =>
                      AverageClickEvent.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetAverageClickPositionResponseToJson(
        GetAverageClickPositionResponse instance) =>
    <String, dynamic>{
      'average': instance.average,
      'clickCount': instance.clickCount,
      'dates': instance.dates.map((e) => e.toJson()).toList(),
    };
