// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'delete_model_instance_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DeleteModelInstanceResponse _$DeleteModelInstanceResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'DeleteModelInstanceResponse',
      json,
      ($checkedConvert) {
        final val = DeleteModelInstanceResponse(
          modelID: $checkedConvert('modelID', (v) => v as String),
          deletedUntil: $checkedConvert('deletedUntil', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$DeleteModelInstanceResponseToJson(
        DeleteModelInstanceResponse instance) =>
    <String, dynamic>{
      'modelID': instance.modelID,
      'deletedUntil': instance.deletedUntil,
    };
