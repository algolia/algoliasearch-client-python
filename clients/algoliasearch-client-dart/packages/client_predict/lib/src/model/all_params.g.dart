// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'all_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AllParams _$AllParamsFromJson(Map<String, dynamic> json) => $checkedCreate(
      'AllParams',
      json,
      ($checkedConvert) {
        final val = AllParams(
          modelsToRetrieve: $checkedConvert(
              'modelsToRetrieve',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => $enumDecode(_$ModelsToRetrieveEnumMap, e))
                  .toList()),
          typesToRetrieve: $checkedConvert(
              'typesToRetrieve',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => $enumDecode(_$TypesToRetrieveEnumMap, e))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$AllParamsToJson(AllParams instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('modelsToRetrieve',
      instance.modelsToRetrieve?.map((e) => e.toJson()).toList());
  writeNotNull('typesToRetrieve',
      instance.typesToRetrieve?.map((e) => e.toJson()).toList());
  return val;
}

const _$ModelsToRetrieveEnumMap = {
  ModelsToRetrieve.funnelStage: 'funnel_stage',
  ModelsToRetrieve.orderValue: 'order_value',
  ModelsToRetrieve.affinities: 'affinities',
};

const _$TypesToRetrieveEnumMap = {
  TypesToRetrieve.properties: 'properties',
  TypesToRetrieve.segments: 'segments',
};
