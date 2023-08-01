// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'auth_algolia_partial.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AuthAlgoliaPartial _$AuthAlgoliaPartialFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'AuthAlgoliaPartial',
      json,
      ($checkedConvert) {
        final val = AuthAlgoliaPartial(
          appID: $checkedConvert('appID', (v) => v as String?),
          apiKey: $checkedConvert('apiKey', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$AuthAlgoliaPartialToJson(AuthAlgoliaPartial instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('appID', instance.appID);
  writeNotNull('apiKey', instance.apiKey);
  return val;
}
