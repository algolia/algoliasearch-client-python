// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'segment.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Segment _$SegmentFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Segment',
      json,
      ($checkedConvert) {
        final val = Segment(
          segmentID: $checkedConvert('segmentID', (v) => v as String),
          name: $checkedConvert('name', (v) => v as String),
          conditions: $checkedConvert(
              'conditions',
              (v) =>
                  SegmentParentConditions.fromJson(v as Map<String, dynamic>)),
          size: $checkedConvert('size', (v) => v as num),
          segmentStatus: $checkedConvert(
              'segmentStatus', (v) => $enumDecode(_$SegmentStatusEnumMap, v)),
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$SegmentTypeEnumMap, v)),
          lastUpdatedAt: $checkedConvert('lastUpdatedAt', (v) => v as String),
          errorMessage: $checkedConvert('errorMessage', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$SegmentToJson(Segment instance) {
  final val = <String, dynamic>{
    'segmentID': instance.segmentID,
    'name': instance.name,
    'conditions': instance.conditions.toJson(),
    'size': instance.size,
    'segmentStatus': instance.segmentStatus.toJson(),
    'type': instance.type.toJson(),
    'lastUpdatedAt': instance.lastUpdatedAt,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('errorMessage', instance.errorMessage);
  return val;
}

const _$SegmentStatusEnumMap = {
  SegmentStatus.active: 'active',
  SegmentStatus.pending: 'pending',
  SegmentStatus.failed: 'failed',
};

const _$SegmentTypeEnumMap = {
  SegmentType.computed: 'computed',
  SegmentType.custom: 'custom',
};
