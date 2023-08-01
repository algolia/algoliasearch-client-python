// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'personalization_strategy_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

PersonalizationStrategyParams _$PersonalizationStrategyParamsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'PersonalizationStrategyParams',
      json,
      ($checkedConvert) {
        final val = PersonalizationStrategyParams(
          eventScoring: $checkedConvert(
              'eventScoring',
              (v) => (v as List<dynamic>)
                  .map((e) => EventScoring.fromJson(e as Map<String, dynamic>))
                  .toList()),
          facetScoring: $checkedConvert(
              'facetScoring',
              (v) => (v as List<dynamic>)
                  .map((e) => FacetScoring.fromJson(e as Map<String, dynamic>))
                  .toList()),
          personalizationImpact:
              $checkedConvert('personalizationImpact', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$PersonalizationStrategyParamsToJson(
        PersonalizationStrategyParams instance) =>
    <String, dynamic>{
      'eventScoring': instance.eventScoring.map((e) => e.toJson()).toList(),
      'facetScoring': instance.facetScoring.map((e) => e.toJson()).toList(),
      'personalizationImpact': instance.personalizationImpact,
    };
