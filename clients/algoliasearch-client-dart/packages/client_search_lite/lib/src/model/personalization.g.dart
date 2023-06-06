// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'personalization.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Personalization _$PersonalizationFromJson(Map<String, dynamic> json) =>
    Personalization(
      filtersScore: json['filtersScore'] as int?,
      rankingScore: json['rankingScore'] as int?,
      score: json['score'] as int?,
    );

Map<String, dynamic> _$PersonalizationToJson(Personalization instance) =>
    <String, dynamic>{
      'filtersScore': instance.filtersScore,
      'rankingScore': instance.rankingScore,
      'score': instance.score,
    };
