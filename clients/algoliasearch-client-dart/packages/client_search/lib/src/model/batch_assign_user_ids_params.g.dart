// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'batch_assign_user_ids_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BatchAssignUserIdsParams _$BatchAssignUserIdsParamsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'BatchAssignUserIdsParams',
      json,
      ($checkedConvert) {
        final val = BatchAssignUserIdsParams(
          cluster: $checkedConvert('cluster', (v) => v as String),
          users: $checkedConvert('users',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$BatchAssignUserIdsParamsToJson(
        BatchAssignUserIdsParams instance) =>
    <String, dynamic>{
      'cluster': instance.cluster,
      'users': instance.users,
    };
