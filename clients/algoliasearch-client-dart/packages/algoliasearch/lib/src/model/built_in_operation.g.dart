// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'built_in_operation.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BuiltInOperation _$BuiltInOperationFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'BuiltInOperation',
      json,
      ($checkedConvert) {
        final val = BuiltInOperation(
          operation: $checkedConvert('_operation',
              (v) => $enumDecode(_$BuiltInOperationTypeEnumMap, v)),
          value: $checkedConvert('value', (v) => v as String),
        );
        return val;
      },
      fieldKeyMap: const {'operation': '_operation'},
    );

Map<String, dynamic> _$BuiltInOperationToJson(BuiltInOperation instance) =>
    <String, dynamic>{
      '_operation': instance.operation.toJson(),
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
