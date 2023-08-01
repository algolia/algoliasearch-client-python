// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_top_filter_attributes_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetTopFilterAttributesResponse _$GetTopFilterAttributesResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetTopFilterAttributesResponse',
      json,
      ($checkedConvert) {
        final val = GetTopFilterAttributesResponse(
          attributes: $checkedConvert(
              'attributes',
              (v) => (v as List<dynamic>)
                  .map((e) =>
                      GetTopFilterAttribute.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetTopFilterAttributesResponseToJson(
        GetTopFilterAttributesResponse instance) =>
    <String, dynamic>{
      'attributes': instance.attributes.map((e) => e.toJson()).toList(),
    };
