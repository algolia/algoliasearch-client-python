// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_user_ids_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchUserIdsParams _$SearchUserIdsParamsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SearchUserIdsParams',
      json,
      ($checkedConvert) {
        final val = SearchUserIdsParams(
          query: $checkedConvert('query', (v) => v as String),
          clusterName: $checkedConvert('clusterName', (v) => v as String?),
          page: $checkedConvert('page', (v) => v as int?),
          hitsPerPage: $checkedConvert('hitsPerPage', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchUserIdsParamsToJson(SearchUserIdsParams instance) {
  final val = <String, dynamic>{
    'query': instance.query,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('clusterName', instance.clusterName);
  writeNotNull('page', instance.page);
  writeNotNull('hitsPerPage', instance.hitsPerPage);
  return val;
}
