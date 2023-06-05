// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'log_query.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

LogQuery _$LogQueryFromJson(Map<String, dynamic> json) => $checkedCreate(
      'LogQuery',
      json,
      ($checkedConvert) {
        final val = LogQuery(
          indexName: $checkedConvert('index_name', (v) => v as String?),
          userToken: $checkedConvert('user_token', (v) => v as String?),
          queryId: $checkedConvert('query_id', (v) => v as String?),
        );
        return val;
      },
      fieldKeyMap: const {
        'indexName': 'index_name',
        'userToken': 'user_token',
        'queryId': 'query_id'
      },
    );

Map<String, dynamic> _$LogQueryToJson(LogQuery instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('index_name', instance.indexName);
  writeNotNull('user_token', instance.userToken);
  writeNotNull('query_id', instance.queryId);
  return val;
}
