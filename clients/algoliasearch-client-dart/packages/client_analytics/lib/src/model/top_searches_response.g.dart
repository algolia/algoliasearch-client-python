// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'top_searches_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TopSearchesResponse _$TopSearchesResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'TopSearchesResponse',
      json,
      ($checkedConvert) {
        final val = TopSearchesResponse(
          searches: $checkedConvert(
              'searches',
              (v) => (v as List<dynamic>)
                  .map((e) => TopSearch.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$TopSearchesResponseToJson(
        TopSearchesResponse instance) =>
    <String, dynamic>{
      'searches': instance.searches.map((e) => e.toJson()).toList(),
    };
