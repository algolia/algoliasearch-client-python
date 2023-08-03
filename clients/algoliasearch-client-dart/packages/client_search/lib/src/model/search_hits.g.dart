// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_hits.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchHits _$SearchHitsFromJson(Map<String, dynamic> json) => $checkedCreate(
      'SearchHits',
      json,
      ($checkedConvert) {
        final val = SearchHits(
          hits: $checkedConvert(
              'hits',
              (v) => (v as List<dynamic>)
                  .map((e) => Hit.fromJson(e as Map<String, dynamic>))
                  .toList()),
          query: $checkedConvert('query', (v) => v as String),
          params: $checkedConvert('params', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchHitsToJson(SearchHits instance) =>
    <String, dynamic>{
      'hits': instance.hits.map((e) => e.toJson()).toList(),
      'query': instance.query,
      'params': instance.params,
    };
