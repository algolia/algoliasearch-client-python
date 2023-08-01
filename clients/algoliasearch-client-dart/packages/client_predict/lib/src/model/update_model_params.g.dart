// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'update_model_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

UpdateModelParams _$UpdateModelParamsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'UpdateModelParams',
      json,
      ($checkedConvert) {
        final val = UpdateModelParams(
          name: $checkedConvert('name', (v) => v as String?),
          modelAttributes: $checkedConvert('modelAttributes',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          modelStatus: $checkedConvert('modelStatus',
              (v) => $enumDecodeNullable(_$ModelStatusEnumMap, v)),
        );
        return val;
      },
    );

Map<String, dynamic> _$UpdateModelParamsToJson(UpdateModelParams instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('name', instance.name);
  writeNotNull('modelAttributes', instance.modelAttributes);
  writeNotNull('modelStatus', instance.modelStatus?.toJson());
  return val;
}

const _$ModelStatusEnumMap = {
  ModelStatus.active: 'active',
  ModelStatus.inactive: 'inactive',
};
