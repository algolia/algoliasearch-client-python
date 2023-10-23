// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'exhaustive.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Exhaustive _$ExhaustiveFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Exhaustive',
      json,
      ($checkedConvert) {
        final val = Exhaustive(
          facetsCount: $checkedConvert('facetsCount', (v) => v as bool?),
          facetValues: $checkedConvert('facetValues', (v) => v as bool?),
          nbHits: $checkedConvert('nbHits', (v) => v as bool?),
          rulesMatch: $checkedConvert('rulesMatch', (v) => v as bool?),
          typo: $checkedConvert('typo', (v) => v as bool?),
        );
        return val;
      },
    );

Map<String, dynamic> _$ExhaustiveToJson(Exhaustive instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('facetsCount', instance.facetsCount);
  writeNotNull('facetValues', instance.facetValues);
  writeNotNull('nbHits', instance.nbHits);
  writeNotNull('rulesMatch', instance.rulesMatch);
  writeNotNull('typo', instance.typo);
  return val;
}
