// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_no_click_event.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchNoClickEvent _$SearchNoClickEventFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SearchNoClickEvent',
      json,
      ($checkedConvert) {
        final val = SearchNoClickEvent(
          search: $checkedConvert('search', (v) => v as String),
          count: $checkedConvert('count', (v) => v as int),
          withFilterCount: $checkedConvert('withFilterCount', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchNoClickEventToJson(SearchNoClickEvent instance) =>
    <String, dynamic>{
      'search': instance.search,
      'count': instance.count,
      'withFilterCount': instance.withFilterCount,
    };
