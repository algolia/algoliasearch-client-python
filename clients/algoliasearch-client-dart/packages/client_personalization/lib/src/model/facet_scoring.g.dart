// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'facet_scoring.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

FacetScoring _$FacetScoringFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'FacetScoring',
      json,
      ($checkedConvert) {
        final val = FacetScoring(
          score: $checkedConvert('score', (v) => v as int),
          facetName: $checkedConvert('facetName', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$FacetScoringToJson(FacetScoring instance) =>
    <String, dynamic>{
      'score': instance.score,
      'facetName': instance.facetName,
    };
