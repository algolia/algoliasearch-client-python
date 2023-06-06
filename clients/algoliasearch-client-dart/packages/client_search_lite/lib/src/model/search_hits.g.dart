// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_hits.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchHits _$SearchHitsFromJson(Map<String, dynamic> json) => SearchHits(
      hits: (json['hits'] as List<dynamic>)
          .map((e) => Hit.fromJson(e as Map<String, dynamic>))
          .toList(),
    );

Map<String, dynamic> _$SearchHitsToJson(SearchHits instance) =>
    <String, dynamic>{
      'hits': instance.hits,
    };
