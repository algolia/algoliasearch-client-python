// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'automatic_facet_filter.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AutomaticFacetFilter _$AutomaticFacetFilterFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'AutomaticFacetFilter',
      json,
      ($checkedConvert) {
        final val = AutomaticFacetFilter(
          facet: $checkedConvert('facet', (v) => v as String),
          score: $checkedConvert('score', (v) => v as int?),
          disjunctive: $checkedConvert('disjunctive', (v) => v as bool?),
        );
        return val;
      },
    );

Map<String, dynamic> _$AutomaticFacetFilterToJson(
    AutomaticFacetFilter instance) {
  final val = <String, dynamic>{
    'facet': instance.facet,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('score', instance.score);
  writeNotNull('disjunctive', instance.disjunctive);
  return val;
}
