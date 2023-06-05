// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_user_ids_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchUserIdsResponse _$SearchUserIdsResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SearchUserIdsResponse',
      json,
      ($checkedConvert) {
        final val = SearchUserIdsResponse(
          hits: $checkedConvert(
              'hits',
              (v) => (v as List<dynamic>)
                  .map((e) => UserHit.fromJson(e as Map<String, dynamic>))
                  .toList()),
          nbHits: $checkedConvert('nbHits', (v) => v as int),
          page: $checkedConvert('page', (v) => v as int),
          hitsPerPage: $checkedConvert('hitsPerPage', (v) => v as int),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchUserIdsResponseToJson(
        SearchUserIdsResponse instance) =>
    <String, dynamic>{
      'hits': instance.hits.map((e) => e.toJson()).toList(),
      'nbHits': instance.nbHits,
      'page': instance.page,
      'hitsPerPage': instance.hitsPerPage,
      'updatedAt': instance.updatedAt,
    };
