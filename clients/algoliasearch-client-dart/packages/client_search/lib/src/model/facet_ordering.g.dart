// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'facet_ordering.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

FacetOrdering _$FacetOrderingFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'FacetOrdering',
      json,
      ($checkedConvert) {
        final val = FacetOrdering(
          facets: $checkedConvert(
              'facets',
              (v) => v == null
                  ? null
                  : Facets.fromJson(v as Map<String, dynamic>)),
          values: $checkedConvert(
              'values',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) =>
                        MapEntry(k, Value.fromJson(e as Map<String, dynamic>)),
                  )),
        );
        return val;
      },
    );

Map<String, dynamic> _$FacetOrderingToJson(FacetOrdering instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('facets', instance.facets?.toJson());
  writeNotNull(
      'values', instance.values?.map((k, e) => MapEntry(k, e.toJson())));
  return val;
}
