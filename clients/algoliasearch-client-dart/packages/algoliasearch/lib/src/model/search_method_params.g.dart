// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_method_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchMethodParams _$SearchMethodParamsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SearchMethodParams',
      json,
      ($checkedConvert) {
        final val = SearchMethodParams(
          requests: $checkedConvert('requests', (v) => v as List<dynamic>),
          strategy: $checkedConvert('strategy',
              (v) => $enumDecodeNullable(_$SearchStrategyEnumMap, v)),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchMethodParamsToJson(SearchMethodParams instance) {
  final val = <String, dynamic>{
    'requests': instance.requests.toList(),
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('strategy', instance.strategy?.toJson());
  return val;
}

const _$SearchStrategyEnumMap = {
  SearchStrategy.none: 'none',
  SearchStrategy.stopIfEnoughMatches: 'stopIfEnoughMatches',
};
