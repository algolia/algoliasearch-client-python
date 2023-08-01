// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_searches_no_results_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetSearchesNoResultsResponse _$GetSearchesNoResultsResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetSearchesNoResultsResponse',
      json,
      ($checkedConvert) {
        final val = GetSearchesNoResultsResponse(
          searches: $checkedConvert(
              'searches',
              (v) => (v as List<dynamic>)
                  .map((e) =>
                      SearchNoResultEvent.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetSearchesNoResultsResponseToJson(
        GetSearchesNoResultsResponse instance) =>
    <String, dynamic>{
      'searches': instance.searches.map((e) => e.toJson()).toList(),
    };
