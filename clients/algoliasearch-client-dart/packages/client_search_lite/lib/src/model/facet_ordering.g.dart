// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'facet_ordering.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

FacetOrdering _$FacetOrderingFromJson(Map<String, dynamic> json) =>
    FacetOrdering(
      facets: json['facets'] == null
          ? null
          : Facets.fromJson(json['facets'] as Map<String, dynamic>),
      values: (json['values'] as Map<String, dynamic>?)?.map(
        (k, e) => MapEntry(k, Value.fromJson(e as Map<String, dynamic>)),
      ),
    );

Map<String, dynamic> _$FacetOrderingToJson(FacetOrdering instance) =>
    <String, dynamic>{
      'facets': instance.facets,
      'values': instance.values,
    };
