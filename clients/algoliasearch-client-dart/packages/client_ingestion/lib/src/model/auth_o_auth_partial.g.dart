// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'auth_o_auth_partial.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AuthOAuthPartial _$AuthOAuthPartialFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'AuthOAuthPartial',
      json,
      ($checkedConvert) {
        final val = AuthOAuthPartial(
          url: $checkedConvert('url', (v) => v as String?),
          clientId: $checkedConvert('client_id', (v) => v as String?),
          clientSecret: $checkedConvert('client_secret', (v) => v as String?),
        );
        return val;
      },
      fieldKeyMap: const {
        'clientId': 'client_id',
        'clientSecret': 'client_secret'
      },
    );

Map<String, dynamic> _$AuthOAuthPartialToJson(AuthOAuthPartial instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('url', instance.url);
  writeNotNull('client_id', instance.clientId);
  writeNotNull('client_secret', instance.clientSecret);
  return val;
}
