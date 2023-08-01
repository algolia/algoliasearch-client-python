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
        );
        return val;
      },
    );

Map<String, dynamic> _$RecommendHitsToJson(RecommendHits instance) =>
    <String, dynamic>{
      'hits': instance.hits.map((e) => e.toJson()).toList(),
    };
