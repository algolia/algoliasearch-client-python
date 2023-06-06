// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'hit.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Hit _$HitFromJson(Map<String, dynamic> json) => Hit(
      objectID: json['objectID'] as String,
      highlightResult: json['_highlightResult'] as Map<String, dynamic>?,
      snippetResult: json['_snippetResult'] as Map<String, dynamic>?,
      rankingInfo: json['_rankingInfo'] == null
          ? null
          : RankingInfo.fromJson(json['_rankingInfo'] as Map<String, dynamic>),
      distinctSeqID: json['_distinctSeqID'] as int?,
    );

Map<String, dynamic> _$HitToJson(Hit instance) => <String, dynamic>{
      'objectID': instance.objectID,
      '_highlightResult': instance.highlightResult,
      '_snippetResult': instance.snippetResult,
      '_rankingInfo': instance.rankingInfo,
      '_distinctSeqID': instance.distinctSeqID,
    };
