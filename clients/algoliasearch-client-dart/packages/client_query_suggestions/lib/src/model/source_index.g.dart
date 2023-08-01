// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'source_index.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SourceIndex _$SourceIndexFromJson(Map<String, dynamic> json) => $checkedCreate(
      'SourceIndex',
      json,
      ($checkedConvert) {
        final val = SourceIndex(
          indexName: $checkedConvert('indexName', (v) => v as String),
          replicas: $checkedConvert('replicas', (v) => v as bool?),
          analyticsTags: $checkedConvert('analyticsTags',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          facets: $checkedConvert(
              'facets',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => Facet.fromJson(e as Map<String, dynamic>))
                  .toList()),
          minHits: $checkedConvert('minHits', (v) => v as int?),
          minLetters: $checkedConvert('minLetters', (v) => v as int?),
          generate: $checkedConvert(
              'generate',
              (v) => (v as List<dynamic>?)
                  ?.map((e) =>
                      (e as List<dynamic>).map((e) => e as String).toList())
                  .toList()),
          external_: $checkedConvert('external',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
        );
        return val;
      },
      fieldKeyMap: const {'external_': 'external'},
    );

Map<String, dynamic> _$SourceIndexToJson(SourceIndex instance) {
  final val = <String, dynamic>{
    'indexName': instance.indexName,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('replicas', instance.replicas);
  writeNotNull('analyticsTags', instance.analyticsTags);
  writeNotNull('facets', instance.facets?.map((e) => e.toJson()).toList());
  writeNotNull('minHits', instance.minHits);
  writeNotNull('minLetters', instance.minLetters);
  writeNotNull('generate', instance.generate);
  writeNotNull('external', instance.external_);
  return val;
}
