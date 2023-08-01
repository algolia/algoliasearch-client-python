// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'authentication_search.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AuthenticationSearch _$AuthenticationSearchFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'AuthenticationSearch',
      json,
      ($checkedConvert) {
        final val = AuthenticationSearch(
          authenticationIDs: $checkedConvert('authenticationIDs',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$AuthenticationSearchToJson(
        AuthenticationSearch instance) =>
    <String, dynamic>{
      'authenticationIDs': instance.authenticationIDs,
    };
