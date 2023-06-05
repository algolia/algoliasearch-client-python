// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_rules_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchRulesResponse _$SearchRulesResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SearchRulesResponse',
      json,
      ($checkedConvert) {
        final val = SearchRulesResponse(
          hits: $checkedConvert(
              'hits',
              (v) => (v as List<dynamic>)
                  .map((e) => Rule.fromJson(e as Map<String, dynamic>))
                  .toList()),
          nbHits: $checkedConvert('nbHits', (v) => v as int),
          page: $checkedConvert('page', (v) => v as int),
          nbPages: $checkedConvert('nbPages', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchRulesResponseToJson(
        SearchRulesResponse instance) =>
    <String, dynamic>{
      'hits': instance.hits.map((e) => e.toJson()).toList(),
      'nbHits': instance.nbHits,
      'page': instance.page,
      'nbPages': instance.nbPages,
    };
