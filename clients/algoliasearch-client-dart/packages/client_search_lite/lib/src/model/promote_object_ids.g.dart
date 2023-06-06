// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'promote_object_ids.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

PromoteObjectIDs _$PromoteObjectIDsFromJson(Map<String, dynamic> json) =>
    PromoteObjectIDs(
      objectIDs:
          (json['objectIDs'] as List<dynamic>).map((e) => e as String).toList(),
      position: json['position'] as int,
    );

Map<String, dynamic> _$PromoteObjectIDsToJson(PromoteObjectIDs instance) =>
    <String, dynamic>{
      'objectIDs': instance.objectIDs,
      'position': instance.position,
    };
