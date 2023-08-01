// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'segment_operand_order_value.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SegmentOperandOrderValue _$SegmentOperandOrderValueFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SegmentOperandOrderValue',
      json,
      ($checkedConvert) {
        final val = SegmentOperandOrderValue(
          name: $checkedConvert('name', (v) => v as String),
          filters: $checkedConvert(
              'filters',
              (v) => (v as List<dynamic>)
                  .map((e) => SegmentOrderValueFilter.fromJson(
                      e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$SegmentOperandOrderValueToJson(
        SegmentOperandOrderValue instance) =>
    <String, dynamic>{
      'name': instance.name,
      'filters': instance.filters.map((e) => e.toJson()).toList(),
    };
