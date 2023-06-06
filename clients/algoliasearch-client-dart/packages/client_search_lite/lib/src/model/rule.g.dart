// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'rule.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Rule _$RuleFromJson(Map<String, dynamic> json) => Rule(
      objectID: json['objectID'] as String,
      conditions: (json['conditions'] as List<dynamic>?)
          ?.map((e) => Condition.fromJson(e as Map<String, dynamic>))
          .toList(),
      consequence: json['consequence'] == null
          ? null
          : Consequence.fromJson(json['consequence'] as Map<String, dynamic>),
      description: json['description'] as String?,
      enabled: json['enabled'] as bool?,
      validity: (json['validity'] as List<dynamic>?)
          ?.map((e) => TimeRange.fromJson(e as Map<String, dynamic>))
          .toList(),
    );

Map<String, dynamic> _$RuleToJson(Rule instance) => <String, dynamic>{
      'objectID': instance.objectID,
      'conditions': instance.conditions,
      'consequence': instance.consequence,
      'description': instance.description,
      'enabled': instance.enabled,
      'validity': instance.validity,
    };
