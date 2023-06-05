// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'remove_user_id_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RemoveUserIdResponse _$RemoveUserIdResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'RemoveUserIdResponse',
      json,
      ($checkedConvert) {
        final val = RemoveUserIdResponse(
          deletedAt: $checkedConvert('deletedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$RemoveUserIdResponseToJson(
        RemoveUserIdResponse instance) =>
    <String, dynamic>{
      'deletedAt': instance.deletedAt,
    };
