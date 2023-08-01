// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'recommend_hit.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RecommendHit _$RecommendHitFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'RecommendHit',
      json,
      ($checkedConvert) {
        final val = RecommendHit(
          objectID: $checkedConvert('objectID', (v) => v as String),
          highlightResult: $checkedConvert(
              '_highlightResult', (v) => v as Map<String, dynamic>?),
          snippetResult: $checkedConvert(
              '_snippetResult', (v) => v as Map<String, dynamic>?),
          rankingInfo: $checkedConvert(
              '_rankingInfo',
              (v) => v == null
                  ? null
                  : RankingInfo.fromJson(v as Map<String, dynamic>)),
          distinctSeqID: $checkedConvert('_distinctSeqID', (v) => v as int?),
          score: $checkedConvert('_score', (v) => (v as num).toDouble()),
        );
        return val;
      },
      fieldKeyMap: const {
        'highlightResult': '_highlightResult',
        'snippetResult': '_snippetResult',
        'rankingInfo': '_rankingInfo',
        'distinctSeqID': '_distinctSeqID',
        'score': '_score'
      },
    );

const _$RecommendHitFieldMap = <String, String>{
  'objectID': 'objectID',
  'highlightResult': '_highlightResult',
  'snippetResult': '_snippetResult',
  'rankingInfo': '_rankingInfo',
  'distinctSeqID': '_distinctSeqID',
  'score': '_score',
};

Map<String, dynamic> _$RecommendHitToJson(RecommendHit instance) {
  final val = <String, dynamic>{
    'objectID': instance.objectID,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('_highlightResult', instance.highlightResult);
  writeNotNull('_snippetResult', instance.snippetResult);
  writeNotNull('_rankingInfo', instance.rankingInfo?.toJson());
  writeNotNull('_distinctSeqID', instance.distinctSeqID);
  val['_score'] = instance.score;
  return val;
}
