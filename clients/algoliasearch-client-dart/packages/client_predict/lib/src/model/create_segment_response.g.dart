// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'create_segment_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

CreateSegmentResponse _$CreateSegmentResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'CreateSegmentResponse',
      json,
      ($checkedConvert) {
        final val = CreateSegmentResponse(
          segmentID: $checkedConvert('segmentID', (v) => v as String),
          size: $checkedConvert('size', (v) => v as num?),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$CreateSegmentResponseToJson(
    CreateSegmentResponse instance) {
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
