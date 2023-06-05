// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_synonyms_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchSynonymsResponse _$SearchSynonymsResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SearchSynonymsResponse',
      json,
      ($checkedConvert) {
        final val = SearchSynonymsResponse(
          hits: $checkedConvert(
              'hits',
              (v) => (v as List<dynamic>)
                  .map((e) => SynonymHit.fromJson(e as Map<String, dynamic>))
                  .toList()),
          nbHits: $checkedConvert('nbHits', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchSynonymsResponseToJson(
        SearchSynonymsResponse instance) =>
    <String, dynamic>{
      'hits': instance.hits.map((e) => e.toJson()).toList(),
      'nbHits': instance.nbHits,
    };
