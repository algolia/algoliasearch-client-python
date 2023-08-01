// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'segment_child_conditions.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SegmentChildConditions _$SegmentChildConditionsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SegmentChildConditions',
      json,
      ($checkedConvert) {
        final val = SegmentChildConditions(
          operator: $checkedConvert('operator',
              (v) => $enumDecode(_$SegmentConditionOperatorEnumMap, v)),
          operands: $checkedConvert('operands', (v) => v as List<dynamic>),
        );
        return val;
      },
    );

Map<String, dynamic> _$SegmentChildConditionsToJson(
        SegmentChildConditions instance) =>
    <String, dynamic>{
      'operator': instance.operator.toJson(),
      'operands': instance.operands.toList(),
    };

const _$SegmentConditionOperatorEnumMap = {
  SegmentConditionOperator.and: 'AND',
  SegmentConditionOperator.or: 'OR',
};
