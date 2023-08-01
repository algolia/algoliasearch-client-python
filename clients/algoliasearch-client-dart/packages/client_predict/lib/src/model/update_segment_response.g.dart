// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'update_segment_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

UpdateSegmentResponse _$UpdateSegmentResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'UpdateSegmentResponse',
      json,
      ($checkedConvert) {
        final val = UpdateSegmentResponse(
          segmentID: $checkedConvert('segmentID', (v) => v as String),
          size: $checkedConvert('size', (v) => v as num?),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$UpdateSegmentResponseToJson(
    UpdateSegmentResponse instance) {
  final val = <String, dynamic>{
    'segmentID': instance.segmentID,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('size', instance.size);
  val['updatedAt'] = instance.updatedAt;
  return val;
}
