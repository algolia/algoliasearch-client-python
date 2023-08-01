// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_event.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchEvent _$SearchEventFromJson(Map<String, dynamic> json) => $checkedCreate(
      'SearchEvent',
      json,
      ($checkedConvert) {
        final val = SearchEvent(
          date: $checkedConvert('date', (v) => v as String),
          count: $checkedConvert('count', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchEventToJson(SearchEvent instance) =>
    <String, dynamic>{
      'date': instance.date,
      'count': instance.count,
    };
