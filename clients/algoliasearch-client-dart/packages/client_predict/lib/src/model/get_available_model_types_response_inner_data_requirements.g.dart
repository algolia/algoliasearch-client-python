// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_available_model_types_response_inner_data_requirements.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetAvailableModelTypesResponseInnerDataRequirements
    _$GetAvailableModelTypesResponseInnerDataRequirementsFromJson(
            Map<String, dynamic> json) =>
        $checkedCreate(
          'GetAvailableModelTypesResponseInnerDataRequirements',
          json,
          ($checkedConvert) {
            final val = GetAvailableModelTypesResponseInnerDataRequirements(
              minUsers: $checkedConvert('minUsers', (v) => v as int),
              minDays: $checkedConvert('minDays', (v) => v as int),
            );
            return val;
          },
        );

Map<String, dynamic>
    _$GetAvailableModelTypesResponseInnerDataRequirementsToJson(
            GetAvailableModelTypesResponseInnerDataRequirements instance) =>
        <String, dynamic>{
          'minUsers': instance.minUsers,
          'minDays': instance.minDays,
        };
