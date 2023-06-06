// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'highlight_result_option.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

HighlightResultOption _$HighlightResultOptionFromJson(
        Map<String, dynamic> json) =>
    HighlightResultOption(
      value: json['value'] as String,
      matchLevel: $enumDecode(_$MatchLevelEnumMap, json['matchLevel']),
      matchedWords: (json['matchedWords'] as List<dynamic>)
          .map((e) => e as String)
          .toList(),
      fullyHighlighted: json['fullyHighlighted'] as bool?,
    );

Map<String, dynamic> _$HighlightResultOptionToJson(
        HighlightResultOption instance) =>
    <String, dynamic>{
      'value': instance.value,
      'matchLevel': _$MatchLevelEnumMap[instance.matchLevel]!,
      'matchedWords': instance.matchedWords,
      'fullyHighlighted': instance.fullyHighlighted,
    };

const _$MatchLevelEnumMap = {
  MatchLevel.none: 'none',
  MatchLevel.partial: 'partial',
  MatchLevel.full: 'full',
};
