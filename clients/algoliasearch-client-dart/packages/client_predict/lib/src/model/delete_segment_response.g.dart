// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'delete_segment_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DeleteSegmentResponse _$DeleteSegmentResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'DeleteSegmentResponse',
      json,
      ($checkedConvert) {
        final val = DeleteSegmentResponse(
          segmentID: $checkedConvert('segmentID', (v) => v as String),
          deletedUntil: $checkedConvert('deletedUntil', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$DeleteSegmentResponseToJson(
        DeleteSegmentResponse instance) =>
    <String, dynamic>{
      'segmentID': instance.segmentID,
      'deletedUntil': instance.deletedUntil,
    };
