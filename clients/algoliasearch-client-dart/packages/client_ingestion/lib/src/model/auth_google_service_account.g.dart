// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'auth_google_service_account.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AuthGoogleServiceAccount _$AuthGoogleServiceAccountFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'AuthGoogleServiceAccount',
      json,
      ($checkedConvert) {
        final val = AuthGoogleServiceAccount(
          clientEmail: $checkedConvert('clientEmail', (v) => v as String),
          privateKey: $checkedConvert('privateKey', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$AuthGoogleServiceAccountToJson(
        AuthGoogleServiceAccount instance) =>
    <String, dynamic>{
      'clientEmail': instance.clientEmail,
      'privateKey': instance.privateKey,
    };
