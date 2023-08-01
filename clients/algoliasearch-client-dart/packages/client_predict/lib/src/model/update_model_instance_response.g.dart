// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'update_model_instance_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

UpdateModelInstanceResponse _$UpdateModelInstanceResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'UpdateModelInstanceResponse',
      json,
      ($checkedConvert) {
        final val = UpdateModelInstanceResponse(
          modelID: $checkedConvert('modelID', (v) => v as String),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$UpdateModelInstanceResponseToJson(
        UpdateModelInstanceResponse instance) =>
    <String, dynamic>{
      'modelID': instance.modelID,
      'updatedAt': instance.updatedAt,
    };
