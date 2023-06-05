// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'log.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Log _$LogFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Log',
      json,
      ($checkedConvert) {
        final val = Log(
          timestamp: $checkedConvert('timestamp', (v) => v as String),
          method: $checkedConvert('method', (v) => v as String),
          answerCode: $checkedConvert('answer_code', (v) => v as String),
          queryBody: $checkedConvert('query_body', (v) => v as String),
          answer: $checkedConvert('answer', (v) => v as String),
          url: $checkedConvert('url', (v) => v as String),
          ip: $checkedConvert('ip', (v) => v as String),
          queryHeaders: $checkedConvert('query_headers', (v) => v as String),
          sha1: $checkedConvert('sha1', (v) => v as String),
          nbApiCalls: $checkedConvert('nb_api_calls', (v) => v as String),
          processingTimeMs:
              $checkedConvert('processing_time_ms', (v) => v as String),
          index: $checkedConvert('index', (v) => v as String?),
          queryParams: $checkedConvert('query_params', (v) => v as String?),
          queryNbHits: $checkedConvert('query_nb_hits', (v) => v as String?),
          innerQueries: $checkedConvert(
              'inner_queries',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => LogQuery.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
      fieldKeyMap: const {
        'answerCode': 'answer_code',
        'queryBody': 'query_body',
        'queryHeaders': 'query_headers',
        'nbApiCalls': 'nb_api_calls',
        'processingTimeMs': 'processing_time_ms',
        'queryParams': 'query_params',
        'queryNbHits': 'query_nb_hits',
        'innerQueries': 'inner_queries'
      },
    );

Map<String, dynamic> _$LogToJson(Log instance) {
  final val = <String, dynamic>{
    'timestamp': instance.timestamp,
    'method': instance.method,
    'answer_code': instance.answerCode,
    'query_body': instance.queryBody,
    'answer': instance.answer,
    'url': instance.url,
    'ip': instance.ip,
    'query_headers': instance.queryHeaders,
    'sha1': instance.sha1,
    'nb_api_calls': instance.nbApiCalls,
    'processing_time_ms': instance.processingTimeMs,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('index', instance.index);
  writeNotNull('query_params', instance.queryParams);
  writeNotNull('query_nb_hits', instance.queryNbHits);
  writeNotNull(
      'inner_queries', instance.innerQueries?.map((e) => e.toJson()).toList());
  return val;
}
