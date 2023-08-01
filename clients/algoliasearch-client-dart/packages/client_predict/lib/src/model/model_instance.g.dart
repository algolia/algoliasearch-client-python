// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'model_instance.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ModelInstance _$ModelInstanceFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ModelInstance',
      json,
      ($checkedConvert) {
        final val = ModelInstance(
          modelID: $checkedConvert('modelID', (v) => v as String),
          name: $checkedConvert('name', (v) => v as String),
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$ModelsToRetrieveEnumMap, v)),
          sourceID: $checkedConvert('sourceID', (v) => v as String),
          index: $checkedConvert('index', (v) => v as String),
          modelAttributes: $checkedConvert(
              'modelAttributes',
              (v) => (v as List<dynamic>?)
                  ?.map((e) =>
                      ModelAttributes.fromJson(e as Map<String, dynamic>))
                  .toList()),
          lastTrained: $checkedConvert('lastTrained', (v) => v as String),
          lastInference: $checkedConvert('lastInference', (v) => v as String),
          errorMessage: $checkedConvert('errorMessage', (v) => v as String?),
          modelStatus: $checkedConvert('modelStatus',
              (v) => $enumDecode(_$GetModelInstanceConfigStatusEnumMap, v)),
        );
        return val;
      },
    );

Map<String, dynamic> _$ModelInstanceToJson(ModelInstance instance) {
  final val = <String, dynamic>{
    'modelID': instance.modelID,
    'name': instance.name,
    'type': instance.type.toJson(),
    'sourceID': instance.sourceID,
    'index': instance.index,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('modelAttributes',
      instance.modelAttributes?.map((e) => e.toJson()).toList());
  val['lastTrained'] = instance.lastTrained;
  val['lastInference'] = instance.lastInference;
  writeNotNull('errorMessage', instance.errorMessage);
  val['modelStatus'] = instance.modelStatus.toJson();
  return val;
}

const _$ModelsToRetrieveEnumMap = {
  ModelsToRetrieve.funnelStage: 'funnel_stage',
  ModelsToRetrieve.orderValue: 'order_value',
  ModelsToRetrieve.affinities: 'affinities',
};

const _$GetModelInstanceConfigStatusEnumMap = {
  GetModelInstanceConfigStatus.pending: 'pending',
  GetModelInstanceConfigStatus.active: 'active',
  GetModelInstanceConfigStatus.invalid: 'invalid',
  GetModelInstanceConfigStatus.inactive: 'inactive',
};
