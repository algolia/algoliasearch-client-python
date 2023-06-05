// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'user_id.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

UserId _$UserIdFromJson(Map<String, dynamic> json) => $checkedCreate(
      'UserId',
      json,
      ($checkedConvert) {
        final val = UserId(
          userID: $checkedConvert('userID', (v) => v as String),
          clusterName: $checkedConvert('clusterName', (v) => v as String),
          nbRecords: $checkedConvert('nbRecords', (v) => v as int),
          dataSize: $checkedConvert('dataSize', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$UserIdToJson(UserId instance) => <String, dynamic>{
      'userID': instance.userID,
      'clusterName': instance.clusterName,
      'nbRecords': instance.nbRecords,
      'dataSize': instance.dataSize,
    };
