// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Params _$ParamsFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Params',
      json,
      ($checkedConvert) {
        final val = Params(
          query: $checkedConvert('query', (v) => v),
          automaticFacetFilters:
              $checkedConvert('automaticFacetFilters', (v) => v),
          automaticOptionalFacetFilters:
              $checkedConvert('automaticOptionalFacetFilters', (v) => v),
          renderingContent: $checkedConvert(
              'renderingContent',
              (v) => v == null
                  ? null
                  : RenderingContent.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$ParamsToJson(Params instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('query', instance.query);
  writeNotNull('automaticFacetFilters', instance.automaticFacetFilters);
  writeNotNull(
      'automaticOptionalFacetFilters', instance.automaticOptionalFacetFilters);
  writeNotNull('renderingContent', instance.renderingContent?.toJson());
  return val;
}
