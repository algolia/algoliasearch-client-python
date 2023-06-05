// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_synonyms_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchSynonymsParams _$SearchSynonymsParamsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SearchSynonymsParams',
      json,
      ($checkedConvert) {
        final val = SearchSynonymsParams(
          query: $checkedConvert('query', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchSynonymsParamsToJson(
    SearchSynonymsParams instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('query', instance.query);
  return val;
}
