// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_available_model_types_response_inner.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetAvailableModelTypesResponseInner
    _$GetAvailableModelTypesResponseInnerFromJson(Map<String, dynamic> json) =>
        $checkedCreate(
          'GetAvailableModelTypesResponseInner',
          json,
          ($checkedConvert) {
            final val = GetAvailableModelTypesResponseInner(
              name: $checkedConvert('name', (v) => v as String),
              type: $checkedConvert('type', (v) => v as String),
              compatibleSources: $checkedConvert(
                  'compatibleSources',
                  (v) => (v as List<dynamic>)
                      .map((e) => $enumDecode(_$CompatibleSourcesEnumMap, e))
                      .toList()),
              dataRequirements: $checkedConvert(
                  'dataRequirements',
                  (v) => GetAvailableModelTypesResponseInnerDataRequirements
                      .fromJson(v as Map<String, dynamic>)),
            );
            return val;
          },
        );

Map<String, dynamic> _$GetAvailableModelTypesResponseInnerToJson(
        GetAvailableModelTypesResponseInner instance) =>
    <String, dynamic>{
      'name': instance.name,
      'type': instance.type,
      'compatibleSources':
          instance.compatibleSources.map((e) => e.toJson()).toList(),
      'dataRequirements': instance.dataRequirements.toJson(),
    };

const _$CompatibleSourcesEnumMap = {
  CompatibleSources.bigquery: 'bigquery',
};
