// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_method_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchMethodParams _$SearchMethodParamsFromJson(Map<String, dynamic> json) =>
    SearchMethodParams(
      requests: json['requests'] as List<dynamic>,
      strategy: $enumDecodeNullable(_$SearchStrategyEnumMap, json['strategy']),
    );

Map<String, dynamic> _$SearchMethodParamsToJson(SearchMethodParams instance) =>
    <String, dynamic>{
      'requests': instance.requests.toList(),
      'strategy': _$SearchStrategyEnumMap[instance.strategy],
    };

const _$SearchStrategyEnumMap = {
  SearchStrategy.none: 'none',
  SearchStrategy.stopIfEnoughMatches: 'stopIfEnoughMatches',
};
