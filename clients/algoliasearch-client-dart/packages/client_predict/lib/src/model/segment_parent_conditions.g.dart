// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'segment_parent_conditions.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SegmentParentConditions _$SegmentParentConditionsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SegmentParentConditions',
      json,
      ($checkedConvert) {
        final val = SegmentParentConditions(
          operator: $checkedConvert('operator',
              (v) => $enumDecode(_$SegmentConditionOperatorEnumMap, v)),
          operands: $checkedConvert('operands', (v) => v as List<dynamic>),
        );
        return val;
      },
    );

Map<String, dynamic> _$SegmentParentConditionsToJson(
        SegmentParentConditions instance) =>
    <String, dynamic>{
      'operator': instance.operator.toJson(),
      'operands': instance.operands.toList(),
    };

const _$SegmentConditionOperatorEnumMap = {
  SegmentConditionOperator.and: 'AND',
  SegmentConditionOperator.or: 'OR',
};
