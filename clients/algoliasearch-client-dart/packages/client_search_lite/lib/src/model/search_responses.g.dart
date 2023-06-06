// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_responses.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchResponses _$SearchResponsesFromJson(Map<String, dynamic> json) =>
    SearchResponses(
      results: (json['results'] as List<dynamic>)
          .map((e) => SearchResponse.fromJson(e as Map<String, dynamic>))
          .toList(),
    );

Map<String, dynamic> _$SearchResponsesToJson(SearchResponses instance) =>
    <String, dynamic>{
      'results': instance.results,
    };
