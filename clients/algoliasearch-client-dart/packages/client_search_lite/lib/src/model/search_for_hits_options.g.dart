// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_for_hits_options.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchForHitsOptions _$SearchForHitsOptionsFromJson(
        Map<String, dynamic> json) =>
    SearchForHitsOptions(
      indexName: json['indexName'] as String,
      type: $enumDecodeNullable(_$SearchTypeDefaultEnumMap, json['type']),
    );

Map<String, dynamic> _$SearchForHitsOptionsToJson(
        SearchForHitsOptions instance) =>
    <String, dynamic>{
      'indexName': instance.indexName,
      'type': _$SearchTypeDefaultEnumMap[instance.type],
    };

const _$SearchTypeDefaultEnumMap = {
  SearchTypeDefault.default_: 'default',
};
