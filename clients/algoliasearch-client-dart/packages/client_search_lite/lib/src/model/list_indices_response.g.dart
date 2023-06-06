// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'list_indices_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ListIndicesResponse _$ListIndicesResponseFromJson(Map<String, dynamic> json) =>
    ListIndicesResponse(
      items: (json['items'] as List<dynamic>)
          .map((e) => FetchedIndex.fromJson(e as Map<String, dynamic>))
          .toList(),
      nbPages: json['nbPages'] as int?,
    );

Map<String, dynamic> _$ListIndicesResponseToJson(
        ListIndicesResponse instance) =>
    <String, dynamic>{
      'items': instance.items,
      'nbPages': instance.nbPages,
    };
