// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_for_hits_options.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchForHitsOptions _$SearchForHitsOptionsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'SearchForHitsOptions',
      json,
      ($checkedConvert) {
        final val = SearchForHitsOptions(
          indexName: $checkedConvert('indexName', (v) => v as String),
          type: $checkedConvert('type',
              (v) => $enumDecodeNullable(_$SearchTypeDefaultEnumMap, v)),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchForHitsOptionsToJson(
    SearchForHitsOptions instance) {
  final val = <String, dynamic>{
    'indexName': instance.indexName,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('type', instance.type?.toJson());
  return val;
}

const _$SearchTypeDefaultEnumMap = {
  SearchTypeDefault.default_: 'default',
};
