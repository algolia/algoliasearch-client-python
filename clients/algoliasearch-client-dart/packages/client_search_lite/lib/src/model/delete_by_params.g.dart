// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'delete_by_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DeleteByParams _$DeleteByParamsFromJson(Map<String, dynamic> json) =>
    DeleteByParams(
      facetFilters: json['facetFilters'],
      filters: json['filters'] as String?,
      numericFilters: json['numericFilters'],
      tagFilters: json['tagFilters'],
      aroundLatLng: json['aroundLatLng'] as String?,
      aroundRadius: json['aroundRadius'],
      insideBoundingBox: (json['insideBoundingBox'] as List<dynamic>?)
          ?.map((e) => (e as num).toDouble())
          .toList(),
      insidePolygon: (json['insidePolygon'] as List<dynamic>?)
          ?.map((e) => (e as num).toDouble())
          .toList(),
    );

Map<String, dynamic> _$DeleteByParamsToJson(DeleteByParams instance) =>
    <String, dynamic>{
      'facetFilters': instance.facetFilters,
      'filters': instance.filters,
      'numericFilters': instance.numericFilters,
      'tagFilters': instance.tagFilters,
      'aroundLatLng': instance.aroundLatLng,
      'aroundRadius': instance.aroundRadius,
      'insideBoundingBox': instance.insideBoundingBox,
      'insidePolygon': instance.insidePolygon,
    };
