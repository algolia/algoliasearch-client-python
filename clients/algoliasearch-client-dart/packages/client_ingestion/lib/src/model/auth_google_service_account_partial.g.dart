// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'auth_google_service_account_partial.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AuthGoogleServiceAccountPartial _$AuthGoogleServiceAccountPartialFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'AuthGoogleServiceAccountPartial',
      json,
      ($checkedConvert) {
        final val = AuthGoogleServiceAccountPartial(
          clientEmail: $checkedConvert('clientEmail', (v) => v as String?),
          privateKey: $checkedConvert('privateKey', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$AuthGoogleServiceAccountPartialToJson(
    AuthGoogleServiceAccountPartial instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('clientEmail', instance.clientEmail);
  writeNotNull('privateKey', instance.privateKey);
  return val;
}
