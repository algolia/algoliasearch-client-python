// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_synonyms_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchSynonymsResponse _$SearchSynonymsResponseFromJson(
        Map<String, dynamic> json) =>
    SearchSynonymsResponse(
      hits: (json['hits'] as List<dynamic>)
          .map((e) => SynonymHit.fromJson(e as Map<String, dynamic>))
          .toList(),
      nbHits: json['nbHits'] as int,
    );

Map<String, dynamic> _$SearchSynonymsResponseToJson(
        SearchSynonymsResponse instance) =>
    <String, dynamic>{
      'hits': instance.hits,
      'nbHits': instance.nbHits,
    };
