// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'snippet_result_option.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SnippetResultOption _$SnippetResultOptionFromJson(Map<String, dynamic> json) =>
    SnippetResultOption(
      value: json['value'] as String,
      matchLevel: $enumDecode(_$MatchLevelEnumMap, json['matchLevel']),
    );

Map<String, dynamic> _$SnippetResultOptionToJson(
        SnippetResultOption instance) =>
    <String, dynamic>{
      'value': instance.value,
      'matchLevel': _$MatchLevelEnumMap[instance.matchLevel]!,
    };

const _$MatchLevelEnumMap = {
  MatchLevel.none: 'none',
  MatchLevel.partial: 'partial',
  MatchLevel.full: 'full',
};
