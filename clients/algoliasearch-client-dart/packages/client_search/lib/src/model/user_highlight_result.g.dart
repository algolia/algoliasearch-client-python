// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'user_highlight_result.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

UserHighlightResult _$UserHighlightResultFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'UserHighlightResult',
      json,
      ($checkedConvert) {
        final val = UserHighlightResult(
          userID: $checkedConvert('userID', (v) => v as Map<String, dynamic>),
          clusterName:
              $checkedConvert('clusterName', (v) => v as Map<String, dynamic>),
        );
        return val;
      },
    );

Map<String, dynamic> _$UserHighlightResultToJson(
        UserHighlightResult instance) =>
    <String, dynamic>{
      'userID': instance.userID,
      'clusterName': instance.clusterName,
    };
