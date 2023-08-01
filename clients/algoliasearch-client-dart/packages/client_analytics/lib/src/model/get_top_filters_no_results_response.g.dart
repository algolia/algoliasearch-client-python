// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_top_filters_no_results_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetTopFiltersNoResultsResponse _$GetTopFiltersNoResultsResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetTopFiltersNoResultsResponse',
      json,
      ($checkedConvert) {
        final val = GetTopFiltersNoResultsResponse(
          values: $checkedConvert(
              'values',
              (v) => (v as List<dynamic>)
                  .map((e) => GetTopFiltersNoResultsValues.fromJson(
                      e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetTopFiltersNoResultsResponseToJson(
        GetTopFiltersNoResultsResponse instance) =>
    <String, dynamic>{
      'values': instance.values.map((e) => e.toJson()).toList(),
    };
