// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'authentication_create_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AuthenticationCreateResponse _$AuthenticationCreateResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'AuthenticationCreateResponse',
      json,
      ($checkedConvert) {
        final val = AuthenticationCreateResponse(
          authenticationID:
              $checkedConvert('authenticationID', (v) => v as String),
          name: $checkedConvert('name', (v) => v as String),
          createdAt: $checkedConvert('createdAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$AuthenticationCreateResponseToJson(
        AuthenticationCreateResponse instance) =>
    <String, dynamic>{
      'authenticationID': instance.authenticationID,
      'name': instance.name,
      'createdAt': instance.createdAt,
    };
