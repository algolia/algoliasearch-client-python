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
          results: $checkedConvert('results', (v) => v as List<dynamic>),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchResponsesToJson(SearchResponses instance) =>
    <String, dynamic>{
      'results': instance.results.toList(),
    };
