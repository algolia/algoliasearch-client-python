// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_top_filters_no_results_values.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetTopFiltersNoResultsValues _$GetTopFiltersNoResultsValuesFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetTopFiltersNoResultsValues',
      json,
      ($checkedConvert) {
        final val = GetTopFiltersNoResultsValues(
          count: $checkedConvert('count', (v) => v as int),
          values: $checkedConvert(
              'values',
              (v) => (v as List<dynamic>)
                  .map((e) => GetTopFiltersNoResultsValue.fromJson(
                      e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetTopFiltersNoResultsValuesToJson(
        GetTopFiltersNoResultsValues instance) =>
    <String, dynamic>{
      'count': instance.count,
      'values': instance.values.map((e) => e.toJson()).toList(),
    };
