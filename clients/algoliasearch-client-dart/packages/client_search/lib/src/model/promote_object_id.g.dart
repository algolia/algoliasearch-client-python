// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'promote_object_id.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

PromoteObjectID _$PromoteObjectIDFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'PromoteObjectID',
      json,
      ($checkedConvert) {
        final val = PromoteObjectID(
          objectID: $checkedConvert('objectID', (v) => v as String),
          position: $checkedConvert('position', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$PromoteObjectIDToJson(PromoteObjectID instance) =>
    <String, dynamic>{
      'objectID': instance.objectID,
      'position': instance.position,
    };
