// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'snippet_result_option.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SnippetResultOption _$SnippetResultOptionFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SnippetResultOption',
      json,
      ($checkedConvert) {
        final val = SnippetResultOption(
          value: $checkedConvert('value', (v) => v as String),
          matchLevel: $checkedConvert(
              'matchLevel', (v) => $enumDecode(_$MatchLevelEnumMap, v)),
        );
        return val;
      },
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
