// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'set_personalization_strategy_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SetPersonalizationStrategyResponse _$SetPersonalizationStrategyResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SetPersonalizationStrategyResponse',
      json,
      ($checkedConvert) {
        final val = SetPersonalizationStrategyResponse(
          message: $checkedConvert('message', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$SetPersonalizationStrategyResponseToJson(
        SetPersonalizationStrategyResponse instance) =>
    <String, dynamic>{
      'message': instance.message,
    };
