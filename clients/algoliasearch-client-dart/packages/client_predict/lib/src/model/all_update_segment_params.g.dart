// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'all_update_segment_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AllUpdateSegmentParams _$AllUpdateSegmentParamsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'AllUpdateSegmentParams',
      json,
      ($checkedConvert) {
        final val = AllUpdateSegmentParams(
          name: $checkedConvert('name', (v) => v as String?),
          conditions: $checkedConvert(
              'conditions',
              (v) => v == null
                  ? null
                  : SegmentParentConditions.fromJson(
                      v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$AllUpdateSegmentParamsToJson(
    AllUpdateSegmentParams instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('name', instance.name);
  writeNotNull('conditions', instance.conditions?.toJson());
  return val;
}
