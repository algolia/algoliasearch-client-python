// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'segment_conditions_param.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SegmentConditionsParam _$SegmentConditionsParamFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SegmentConditionsParam',
      json,
      ($checkedConvert) {
        final val = SegmentConditionsParam(
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

Map<String, dynamic> _$SegmentConditionsParamToJson(
    SegmentConditionsParam instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('conditions', instance.conditions?.toJson());
  return val;
}
