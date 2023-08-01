// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'segment_name_param.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SegmentNameParam _$SegmentNameParamFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SegmentNameParam',
      json,
      ($checkedConvert) {
        final val = SegmentNameParam(
          name: $checkedConvert('name', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$SegmentNameParamToJson(SegmentNameParam instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('name', instance.name);
  return val;
}
