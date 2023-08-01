// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'activate_model_instance_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ActivateModelInstanceResponse _$ActivateModelInstanceResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'ActivateModelInstanceResponse',
      json,
      ($checkedConvert) {
        final val = ActivateModelInstanceResponse(
          modelID: $checkedConvert('modelID', (v) => v as String),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$ActivateModelInstanceResponseToJson(
        ActivateModelInstanceResponse instance) =>
    <String, dynamic>{
      'modelID': instance.modelID,
      'updatedAt': instance.updatedAt,
    };
