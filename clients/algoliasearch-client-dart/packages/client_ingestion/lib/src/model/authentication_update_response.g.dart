// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'authentication_update_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AuthenticationUpdateResponse _$AuthenticationUpdateResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'AuthenticationUpdateResponse',
      json,
      ($checkedConvert) {
        final val = AuthenticationUpdateResponse(
          authenticationID:
              $checkedConvert('authenticationID', (v) => v as String),
          name: $checkedConvert('name', (v) => v as String),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$AuthenticationUpdateResponseToJson(
        AuthenticationUpdateResponse instance) =>
    <String, dynamic>{
      'authenticationID': instance.authenticationID,
      'name': instance.name,
      'updatedAt': instance.updatedAt,
    };
