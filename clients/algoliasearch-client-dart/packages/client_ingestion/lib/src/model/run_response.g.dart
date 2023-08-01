// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'run_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RunResponse _$RunResponseFromJson(Map<String, dynamic> json) => $checkedCreate(
      'RunResponse',
      json,
      ($checkedConvert) {
        final val = RunResponse(
          runID: $checkedConvert('runID', (v) => v as String),
          createdAt: $checkedConvert('createdAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$RunResponseToJson(RunResponse instance) =>
    <String, dynamic>{
      'runID': instance.runID,
      'createdAt': instance.createdAt,
    };
