// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'user_id.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

UserId _$UserIdFromJson(Map<String, dynamic> json) => UserId(
      userID: json['userID'] as String,
      clusterName: json['clusterName'] as String,
      nbRecords: json['nbRecords'] as int,
      dataSize: json['dataSize'] as int,
    );

Map<String, dynamic> _$UserIdToJson(UserId instance) => <String, dynamic>{
      'userID': instance.userID,
      'clusterName': instance.clusterName,
      'nbRecords': instance.nbRecords,
      'dataSize': instance.dataSize,
    };
