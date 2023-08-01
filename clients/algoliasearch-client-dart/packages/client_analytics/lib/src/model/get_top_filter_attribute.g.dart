// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_top_filter_attribute.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetTopFilterAttribute _$GetTopFilterAttributeFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetTopFilterAttribute',
      json,
      ($checkedConvert) {
        final val = GetTopFilterAttribute(
          attribute: $checkedConvert('attribute', (v) => v as String),
          count: $checkedConvert('count', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetTopFilterAttributeToJson(
        GetTopFilterAttribute instance) =>
    <String, dynamic>{
      'attribute': instance.attribute,
      'count': instance.count,
    };
