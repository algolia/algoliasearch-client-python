// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_no_result_event.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchNoResultEvent _$SearchNoResultEventFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SearchNoResultEvent',
      json,
      ($checkedConvert) {
        final val = SearchNoResultEvent(
          search: $checkedConvert('search', (v) => v as String),
          count: $checkedConvert('count', (v) => v as int),
          nbHits: $checkedConvert('nbHits', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchNoResultEventToJson(
        SearchNoResultEvent instance) =>
    <String, dynamic>{
      'search': instance.search,
      'count': instance.count,
      'nbHits': instance.nbHits,
    };
