// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'multiple_batch_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

MultipleBatchResponse _$MultipleBatchResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'MultipleBatchResponse',
      json,
      ($checkedConvert) {
        final val = MultipleBatchResponse(
          taskID:
              $checkedConvert('taskID', (v) => Map<String, int>.from(v as Map)),
          objectIDs: $checkedConvert('objectIDs',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$MultipleBatchResponseToJson(
        MultipleBatchResponse instance) =>
    <String, dynamic>{
      'taskID': instance.taskID,
      'objectIDs': instance.objectIDs,
    };
