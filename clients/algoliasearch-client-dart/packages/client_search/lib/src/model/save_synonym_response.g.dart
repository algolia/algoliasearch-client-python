// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'save_synonym_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SaveSynonymResponse _$SaveSynonymResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SaveSynonymResponse',
      json,
      ($checkedConvert) {
        final val = SaveSynonymResponse(
          taskID: $checkedConvert('taskID', (v) => v as int),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
          id: $checkedConvert('id', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$SaveSynonymResponseToJson(
        SaveSynonymResponse instance) =>
    <String, dynamic>{
      'taskID': instance.taskID,
      'updatedAt': instance.updatedAt,
      'id': instance.id,
    };
