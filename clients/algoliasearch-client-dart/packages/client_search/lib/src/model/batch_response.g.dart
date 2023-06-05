// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'batch_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BatchResponse _$BatchResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'BatchResponse',
      json,
      ($checkedConvert) {
        final val = BatchResponse(
          taskID: $checkedConvert('taskID', (v) => v as int),
          objectIDs: $checkedConvert('objectIDs',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$BatchResponseToJson(BatchResponse instance) =>
    <String, dynamic>{
      'taskID': instance.taskID,
      'objectIDs': instance.objectIDs,
    };
