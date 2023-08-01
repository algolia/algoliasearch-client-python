// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'create_segment_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

CreateSegmentParams _$CreateSegmentParamsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'CreateSegmentParams',
      json,
      ($checkedConvert) {
        final val = CreateSegmentParams(
          name: $checkedConvert('name', (v) => v as String),
          conditions: $checkedConvert(
              'conditions',
              (v) =>
                  SegmentParentConditions.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$CreateSegmentParamsToJson(
        CreateSegmentParams instance) =>
    <String, dynamic>{
      'name': instance.name,
      'conditions': instance.conditions.toJson(),
    };
