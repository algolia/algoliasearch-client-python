// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'built_in_operation.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BuiltInOperation _$BuiltInOperationFromJson(Map<String, dynamic> json) =>
    BuiltInOperation(
      operation: $enumDecode(_$BuiltInOperationTypeEnumMap, json['_operation']),
      value: json['value'] as String,
    );

Map<String, dynamic> _$BuiltInOperationToJson(BuiltInOperation instance) =>
    <String, dynamic>{
      '_operation': _$BuiltInOperationTypeEnumMap[instance.operation]!,
      'value': instance.value,
    };

const _$BuiltInOperationTypeEnumMap = {
  BuiltInOperationType.increment: 'Increment',
  BuiltInOperationType.decrement: 'Decrement',
  BuiltInOperationType.add: 'Add',
  BuiltInOperationType.remove: 'Remove',
  BuiltInOperationType.addUnique: 'AddUnique',
  BuiltInOperationType.incrementFrom: 'IncrementFrom',
  BuiltInOperationType.incrementSet: 'IncrementSet',
};
