// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'add_ab_tests_request.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AddABTestsRequest _$AddABTestsRequestFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'AddABTestsRequest',
      json,
      ($checkedConvert) {
        final val = AddABTestsRequest(
          name: $checkedConvert('name', (v) => v as String),
          variants: $checkedConvert('variants', (v) => v as List<dynamic>),
          endAt: $checkedConvert('endAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$AddABTestsRequestToJson(AddABTestsRequest instance) =>
    <String, dynamic>{
      'name': instance.name,
      'variants': instance.variants.toList(),
      'endAt': instance.endAt,
    };
