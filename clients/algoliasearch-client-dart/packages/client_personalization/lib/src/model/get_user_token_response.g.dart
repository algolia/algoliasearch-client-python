// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_user_token_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetUserTokenResponse _$GetUserTokenResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetUserTokenResponse',
      json,
      ($checkedConvert) {
        final val = GetUserTokenResponse(
          userToken: $checkedConvert('userToken', (v) => v as String),
          lastEventAt: $checkedConvert('lastEventAt', (v) => v as String),
          scores: $checkedConvert('scores', (v) => v as Object),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetUserTokenResponseToJson(
        GetUserTokenResponse instance) =>
    <String, dynamic>{
      'userToken': instance.userToken,
      'lastEventAt': instance.lastEventAt,
      'scores': instance.scores,
    };
