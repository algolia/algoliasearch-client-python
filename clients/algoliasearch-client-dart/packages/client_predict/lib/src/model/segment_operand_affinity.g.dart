// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'segment_operand_affinity.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SegmentOperandAffinity _$SegmentOperandAffinityFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SegmentOperandAffinity',
      json,
      ($checkedConvert) {
        final val = SegmentOperandAffinity(
          name: $checkedConvert('name', (v) => v as String),
          filters: $checkedConvert(
              'filters',
              (v) => (v as List<dynamic>)
                  .map((e) =>
                      SegmentAffinityFilter.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$SegmentOperandAffinityToJson(
        SegmentOperandAffinity instance) =>
    <String, dynamic>{
      'name': instance.name,
      'filters': instance.filters.map((e) => e.toJson()).toList(),
    };
