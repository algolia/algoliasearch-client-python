// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'facets_stats.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

FacetsStats _$FacetsStatsFromJson(Map<String, dynamic> json) => FacetsStats(
      min: json['min'] as int?,
      max: json['max'] as int?,
      avg: json['avg'] as int?,
      sum: json['sum'] as int?,
    );

Map<String, dynamic> _$FacetsStatsToJson(FacetsStats instance) =>
    <String, dynamic>{
      'min': instance.min,
      'max': instance.max,
      'avg': instance.avg,
      'sum': instance.sum,
    };
