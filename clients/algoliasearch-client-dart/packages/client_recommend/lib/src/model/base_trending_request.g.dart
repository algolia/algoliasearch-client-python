// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'base_trending_request.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BaseTrendingRequest _$BaseTrendingRequestFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'BaseTrendingRequest',
      json,
      ($checkedConvert) {
        final val = BaseTrendingRequest(
          model: $checkedConvert(
              'model', (v) => $enumDecode(_$TrendingModelsEnumMap, v)),
          facetName: $checkedConvert('facetName', (v) => v as String?),
          facetValue: $checkedConvert('facetValue', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$BaseTrendingRequestToJson(BaseTrendingRequest instance) {
  final val = <String, dynamic>{
    'model': instance.model.toJson(),
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('facetName', instance.facetName);
  writeNotNull('facetValue', instance.facetValue);
  return val;
}

const _$TrendingModelsEnumMap = {
  TrendingModels.facets: 'trending-facets',
  TrendingModels.items: 'trending-items',
};
