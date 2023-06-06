// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'consequence_query_object.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ConsequenceQueryObject _$ConsequenceQueryObjectFromJson(
        Map<String, dynamic> json) =>
    ConsequenceQueryObject(
      remove:
          (json['remove'] as List<dynamic>?)?.map((e) => e as String).toList(),
      edits: (json['edits'] as List<dynamic>?)
          ?.map((e) => Edit.fromJson(e as Map<String, dynamic>))
          .toList(),
    );

Map<String, dynamic> _$ConsequenceQueryObjectToJson(
        ConsequenceQueryObject instance) =>
    <String, dynamic>{
      'remove': instance.remove,
      'edits': instance.edits,
    };
