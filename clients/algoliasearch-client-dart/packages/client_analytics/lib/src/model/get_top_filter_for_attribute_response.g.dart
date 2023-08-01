// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_top_filter_for_attribute_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetTopFilterForAttributeResponse _$GetTopFilterForAttributeResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetTopFilterForAttributeResponse',
      json,
      ($checkedConvert) {
        final val = GetTopFilterForAttributeResponse(
          values: $checkedConvert(
              'values',
              (v) => (v as List<dynamic>)
                  .map((e) => GetTopFilterForAttribute.fromJson(
                      e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetTopFilterForAttributeResponseToJson(
        GetTopFilterForAttributeResponse instance) =>
    <String, dynamic>{
      'values': instance.values.map((e) => e.toJson()).toList(),
    };
