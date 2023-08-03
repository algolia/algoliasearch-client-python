// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'recommend_hits.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RecommendHits _$RecommendHitsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'RecommendHits',
      json,
      ($checkedConvert) {
        final val = RecommendHits(
          hits: $checkedConvert(
              'hits',
              (v) => (v as List<dynamic>)
                  .map((e) => RecommendHit.fromJson(e as Map<String, dynamic>))
                  .toList()),
          query: $checkedConvert('query', (v) => v as String?),
          params: $checkedConvert('params', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$RecommendHitsToJson(RecommendHits instance) {
  final val = <String, dynamic>{
    'hits': instance.hits.map((e) => e.toJson()).toList(),
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('query', instance.query);
  writeNotNull('params', instance.params);
  return val;
}
