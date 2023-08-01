// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'ab_tests_variant_search_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AbTestsVariantSearchParams _$AbTestsVariantSearchParamsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'AbTestsVariantSearchParams',
      json,
      ($checkedConvert) {
        final val = AbTestsVariantSearchParams(
          index: $checkedConvert('index', (v) => v as String),
          trafficPercentage:
              $checkedConvert('trafficPercentage', (v) => v as int),
          description: $checkedConvert('description', (v) => v as String?),
          customSearchParameters:
              $checkedConvert('customSearchParameters', (v) => v as Object),
        );
        return val;
      },
    );

Map<String, dynamic> _$AbTestsVariantSearchParamsToJson(
    AbTestsVariantSearchParams instance) {
  final val = <String, dynamic>{
    'index': instance.index,
    'trafficPercentage': instance.trafficPercentage,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('description', instance.description);
  val['customSearchParameters'] = instance.customSearchParameters;
  return val;
}
