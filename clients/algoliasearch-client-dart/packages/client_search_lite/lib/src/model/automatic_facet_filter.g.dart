// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'automatic_facet_filter.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AutomaticFacetFilter _$AutomaticFacetFilterFromJson(
        Map<String, dynamic> json) =>
    AutomaticFacetFilter(
      facet: json['facet'] as String,
      score: json['score'] as int?,
      disjunctive: json['disjunctive'] as bool?,
    );

Map<String, dynamic> _$AutomaticFacetFilterToJson(
        AutomaticFacetFilter instance) =>
    <String, dynamic>{
      'facet': instance.facet,
      'score': instance.score,
      'disjunctive': instance.disjunctive,
    };
