// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'condition.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Condition _$ConditionFromJson(Map<String, dynamic> json) => Condition(
      pattern: json['pattern'] as String?,
      anchoring: $enumDecodeNullable(_$AnchoringEnumMap, json['anchoring']),
      alternatives: json['alternatives'] as bool?,
      context: json['context'] as String?,
    );

Map<String, dynamic> _$ConditionToJson(Condition instance) => <String, dynamic>{
      'pattern': instance.pattern,
      'anchoring': _$AnchoringEnumMap[instance.anchoring],
      'alternatives': instance.alternatives,
      'context': instance.context,
    };

const _$AnchoringEnumMap = {
  Anchoring.is_: 'is',
  Anchoring.startsWith: 'startsWith',
  Anchoring.endsWith: 'endsWith',
  Anchoring.contains: 'contains',
};
