// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'top_search.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TopSearch _$TopSearchFromJson(Map<String, dynamic> json) => $checkedCreate(
      'TopSearch',
      json,
      ($checkedConvert) {
        final val = TopSearch(
          search: $checkedConvert('search', (v) => v as String),
          count: $checkedConvert('count', (v) => v as int),
          nbHits: $checkedConvert('nbHits', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$TopSearchToJson(TopSearch instance) => <String, dynamic>{
      'search': instance.search,
      'count': instance.count,
      'nbHits': instance.nbHits,
    };
