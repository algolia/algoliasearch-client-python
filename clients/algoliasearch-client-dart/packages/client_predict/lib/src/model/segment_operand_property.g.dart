// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'segment_operand_property.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SegmentOperandProperty _$SegmentOperandPropertyFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SegmentOperandProperty',
      json,
      ($checkedConvert) {
        final val = SegmentOperandProperty(
          name: $checkedConvert('name', (v) => v as String),
          filters: $checkedConvert(
              'filters',
              (v) => (v as List<dynamic>)
                  .map((e) =>
                      SegmentPropertyFilter.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$SegmentOperandPropertyToJson(
        SegmentOperandProperty instance) =>
    <String, dynamic>{
      'name': instance.name,
      'filters': instance.filters.map((e) => e.toJson()).toList(),
    };
