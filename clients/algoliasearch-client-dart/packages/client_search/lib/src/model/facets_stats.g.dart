// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'facets_stats.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

FacetsStats _$FacetsStatsFromJson(Map<String, dynamic> json) => $checkedCreate(
      'FacetsStats',
      json,
      ($checkedConvert) {
        final val = FacetsStats(
          min: $checkedConvert('min', (v) => (v as num?)?.toDouble()),
          max: $checkedConvert('max', (v) => (v as num?)?.toDouble()),
          avg: $checkedConvert('avg', (v) => (v as num?)?.toDouble()),
          sum: $checkedConvert('sum', (v) => (v as num?)?.toDouble()),
        );
        return val;
      },
    );

Map<String, dynamic> _$FacetsStatsToJson(FacetsStats instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('min', instance.min);
  writeNotNull('max', instance.max);
  writeNotNull('avg', instance.avg);
  writeNotNull('sum', instance.sum);
  return val;
}
