// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'activate_model_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ActivateModelParams _$ActivateModelParamsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ActivateModelParams',
      json,
      ($checkedConvert) {
        final val = ActivateModelParams(
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$ModelsToRetrieveEnumMap, v)),
          name: $checkedConvert('name', (v) => v as String),
          sourceID: $checkedConvert('sourceID', (v) => v as String),
          index: $checkedConvert('index', (v) => v as String),
          modelAttributes: $checkedConvert('modelAttributes',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$ActivateModelParamsToJson(ActivateModelParams instance) {
  final val = <String, dynamic>{
    'type': instance.type.toJson(),
    'name': instance.name,
    'sourceID': instance.sourceID,
    'index': instance.index,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('modelAttributes', instance.modelAttributes);
  return val;
}

const _$ModelsToRetrieveEnumMap = {
  ModelsToRetrieve.funnelStage: 'funnel_stage',
  ModelsToRetrieve.orderValue: 'order_value',
  ModelsToRetrieve.affinities: 'affinities',
};
