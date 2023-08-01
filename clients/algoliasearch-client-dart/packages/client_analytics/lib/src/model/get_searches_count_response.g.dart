// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_searches_count_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetSearchesCountResponse _$GetSearchesCountResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetSearchesCountResponse',
      json,
      ($checkedConvert) {
        final val = GetSearchesCountResponse(
          count: $checkedConvert('count', (v) => v as int),
          dates: $checkedConvert(
              'dates',
              (v) => (v as List<dynamic>)
                  .map((e) => SearchEvent.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetSearchesCountResponseToJson(
        GetSearchesCountResponse instance) =>
    <String, dynamic>{
      'count': instance.count,
      'dates': instance.dates.map((e) => e.toJson()).toList(),
    };
