// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'models_to_retrieve_param.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ModelsToRetrieveParam _$ModelsToRetrieveParamFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'ModelsToRetrieveParam',
      json,
      ($checkedConvert) {
        final val = ModelsToRetrieveParam(
          modelsToRetrieve: $checkedConvert(
              'modelsToRetrieve',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => $enumDecode(_$ModelsToRetrieveEnumMap, e))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$ModelsToRetrieveParamToJson(
    ModelsToRetrieveParam instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('modelsToRetrieve',
      instance.modelsToRetrieve?.map((e) => e.toJson()).toList());
  return val;
}

const _$ModelsToRetrieveEnumMap = {
  ModelsToRetrieve.funnelStage: 'funnel_stage',
  ModelsToRetrieve.orderValue: 'order_value',
  ModelsToRetrieve.affinities: 'affinities',
};
