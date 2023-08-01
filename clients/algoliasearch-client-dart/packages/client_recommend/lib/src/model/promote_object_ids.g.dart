// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'promote_object_ids.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

PromoteObjectIDs _$PromoteObjectIDsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'PromoteObjectIDs',
      json,
      ($checkedConvert) {
        final val = PromoteObjectIDs(
          objectIDs: $checkedConvert('objectIDs',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
          position: $checkedConvert('position', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$PromoteObjectIDsToJson(PromoteObjectIDs instance) =>
    <String, dynamic>{
      'objectIDs': instance.objectIDs,
      'position': instance.position,
    };
