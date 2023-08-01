// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_top_filters_no_results_value.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetTopFiltersNoResultsValue _$GetTopFiltersNoResultsValueFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetTopFiltersNoResultsValue',
      json,
      ($checkedConvert) {
        final val = GetTopFiltersNoResultsValue(
          attribute: $checkedConvert('attribute', (v) => v as String),
          operator: $checkedConvert('operator', (v) => v as String),
          value: $checkedConvert('value', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetTopFiltersNoResultsValueToJson(
        GetTopFiltersNoResultsValue instance) =>
    <String, dynamic>{
      'attribute': instance.attribute,
      'operator': instance.operator,
      'value': instance.value,
    };
