// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'auth_algolia.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AuthAlgolia _$AuthAlgoliaFromJson(Map<String, dynamic> json) => $checkedCreate(
      'AuthAlgolia',
      json,
      ($checkedConvert) {
        final val = AuthAlgolia(
          appID: $checkedConvert('appID', (v) => v as String),
          apiKey: $checkedConvert('apiKey', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$AuthAlgoliaToJson(AuthAlgolia instance) =>
    <String, dynamic>{
      'appID': instance.appID,
      'apiKey': instance.apiKey,
    };
