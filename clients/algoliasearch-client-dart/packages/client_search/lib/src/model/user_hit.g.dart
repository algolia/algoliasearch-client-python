// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'user_hit.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

UserHit _$UserHitFromJson(Map<String, dynamic> json) => $checkedCreate(
      'UserHit',
      json,
      ($checkedConvert) {
        final val = UserHit(
          userID: $checkedConvert('userID', (v) => v as String),
          clusterName: $checkedConvert('clusterName', (v) => v as String),
          nbRecords: $checkedConvert('nbRecords', (v) => v as int),
          dataSize: $checkedConvert('dataSize', (v) => v as int),
          objectID: $checkedConvert('objectID', (v) => v as String),
          highlightResult: $checkedConvert('_highlightResult',
              (v) => UserHighlightResult.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
      fieldKeyMap: const {'highlightResult': '_highlightResult'},
    );

Map<String, dynamic> _$UserHitToJson(UserHit instance) => <String, dynamic>{
      'userID': instance.userID,
      'clusterName': instance.clusterName,
      'nbRecords': instance.nbRecords,
      'dataSize': instance.dataSize,
      'objectID': instance.objectID,
      '_highlightResult': instance.highlightResult.toJson(),
    };
