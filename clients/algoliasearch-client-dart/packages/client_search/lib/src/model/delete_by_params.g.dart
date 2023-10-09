// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'delete_by_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DeleteByParams _$DeleteByParamsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'DeleteByParams',
      json,
      ($checkedConvert) {
        final val = DeleteByParams(
          facetFilters: $checkedConvert('facetFilters', (v) => v),
          filters: $checkedConvert('filters', (v) => v as String?),
          numericFilters: $checkedConvert('numericFilters', (v) => v),
          tagFilters: $checkedConvert('tagFilters', (v) => v),
          aroundLatLng: $checkedConvert('aroundLatLng', (v) => v as String?),
          aroundRadius: $checkedConvert('aroundRadius', (v) => v),
          insideBoundingBox: $checkedConvert(
              'insideBoundingBox',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => (e as List<dynamic>)
                      .map((e) => (e as num).toDouble())
                      .toList())
                  .toList()),
          insidePolygon: $checkedConvert(
              'insidePolygon',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => (e as List<dynamic>)
                      .map((e) => (e as num).toDouble())
                      .toList())
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$DeleteByParamsToJson(DeleteByParams instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('facetFilters', instance.facetFilters);
  writeNotNull('filters', instance.filters);
  writeNotNull('numericFilters', instance.numericFilters);
  writeNotNull('tagFilters', instance.tagFilters);
  writeNotNull('aroundLatLng', instance.aroundLatLng);
  writeNotNull('aroundRadius', instance.aroundRadius);
  writeNotNull('insideBoundingBox', instance.insideBoundingBox);
  writeNotNull('insidePolygon', instance.insidePolygon);
  return val;
}
