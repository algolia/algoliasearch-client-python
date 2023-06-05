// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_responses.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchResponses _$SearchResponsesFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SearchResponses',
      json,
      ($checkedConvert) {
        final val = SearchResponses(
          results: $checkedConvert(
              'results',
              (v) => (v as List<dynamic>)
                  .map(
                      (e) => SearchResponse.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchResponsesToJson(SearchResponses instance) =>
    <String, dynamic>{
      'results': instance.results.map((e) => e.toJson()).toList(),
    };
