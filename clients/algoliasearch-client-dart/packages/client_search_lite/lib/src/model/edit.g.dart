// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'edit.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Edit _$EditFromJson(Map<String, dynamic> json) => Edit(
      type: $enumDecodeNullable(_$EditTypeEnumMap, json['type']),
      delete: json['delete'] as String?,
      insert: json['insert'] as String?,
    );

Map<String, dynamic> _$EditToJson(Edit instance) => <String, dynamic>{
      'type': _$EditTypeEnumMap[instance.type],
      'delete': instance.delete,
      'insert': instance.insert,
    };

const _$EditTypeEnumMap = {
  EditType.remove: 'remove',
  EditType.replace: 'replace',
};
