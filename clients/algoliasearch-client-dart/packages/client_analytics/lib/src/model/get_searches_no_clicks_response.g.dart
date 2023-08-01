// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_searches_no_clicks_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetSearchesNoClicksResponse _$GetSearchesNoClicksResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetSearchesNoClicksResponse',
      json,
      ($checkedConvert) {
        final val = GetSearchesNoClicksResponse(
          searches: $checkedConvert(
              'searches',
              (v) => (v as List<dynamic>)
                  .map((e) =>
                      SearchNoClickEvent.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetSearchesNoClicksResponseToJson(
        GetSearchesNoClicksResponse instance) =>
    <String, dynamic>{
      'searches': instance.searches.map((e) => e.toJson()).toList(),
    };
