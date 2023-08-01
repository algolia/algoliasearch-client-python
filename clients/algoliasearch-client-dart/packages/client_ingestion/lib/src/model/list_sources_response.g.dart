// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'list_sources_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ListSourcesResponse _$ListSourcesResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ListSourcesResponse',
      json,
      ($checkedConvert) {
        final val = ListSourcesResponse(
          sources: $checkedConvert(
              'sources',
              (v) => (v as List<dynamic>)
                  .map((e) => Source.fromJson(e as Map<String, dynamic>))
                  .toList()),
          pagination: $checkedConvert('pagination',
              (v) => Pagination.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$ListSourcesResponseToJson(
        ListSourcesResponse instance) =>
    <String, dynamic>{
      'sources': instance.sources.map((e) => e.toJson()).toList(),
      'pagination': instance.pagination.toJson(),
    };
