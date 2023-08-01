// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_top_filter_for_attribute.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetTopFilterForAttribute _$GetTopFilterForAttributeFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetTopFilterForAttribute',
      json,
      ($checkedConvert) {
        final val = GetTopFilterForAttribute(
          attribute: $checkedConvert('attribute', (v) => v as String),
          operator: $checkedConvert('operator', (v) => v as String),
          value: $checkedConvert('value', (v) => v as String),
          count: $checkedConvert('count', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetTopFilterForAttributeToJson(
        GetTopFilterForAttribute instance) =>
    <String, dynamic>{
      'attribute': instance.attribute,
      'operator': instance.operator,
      'value': instance.value,
      'count': instance.count,
    };
