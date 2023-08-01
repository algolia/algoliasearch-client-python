// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'delete_user_profile_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DeleteUserProfileResponse _$DeleteUserProfileResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'DeleteUserProfileResponse',
      json,
      ($checkedConvert) {
        final val = DeleteUserProfileResponse(
          userToken: $checkedConvert('userToken', (v) => v as String),
          deletedUntil: $checkedConvert('deletedUntil', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$DeleteUserProfileResponseToJson(
        DeleteUserProfileResponse instance) =>
    <String, dynamic>{
      'userToken': instance.userToken,
      'deletedUntil': instance.deletedUntil,
    };
