// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_params_string.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchParamsString _$SearchParamsStringFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SearchParamsString',
      json,
      ($checkedConvert) {
        final val = SearchParamsString(
          params: $checkedConvert('params', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchParamsStringToJson(SearchParamsString instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('params', instance.params);
  return val;
}
