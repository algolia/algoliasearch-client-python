// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'assign_user_id_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AssignUserIdParams _$AssignUserIdParamsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'AssignUserIdParams',
      json,
      ($checkedConvert) {
        final val = AssignUserIdParams(
          cluster: $checkedConvert('cluster', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$AssignUserIdParamsToJson(AssignUserIdParams instance) =>
    <String, dynamic>{
      'cluster': instance.cluster,
    };
