// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'ranking_info.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RankingInfo _$RankingInfoFromJson(Map<String, dynamic> json) => RankingInfo(
      filters: json['filters'] as int,
      firstMatchedWord: json['firstMatchedWord'] as int,
      geoDistance: json['geoDistance'] as int,
      geoPrecision: json['geoPrecision'] as int?,
      matchedGeoLocation: json['matchedGeoLocation'] == null
          ? null
          : MatchedGeoLocation.fromJson(
              json['matchedGeoLocation'] as Map<String, dynamic>),
      personalization: json['personalization'] == null
          ? null
          : Personalization.fromJson(
              json['personalization'] as Map<String, dynamic>),
      nbExactWords: json['nbExactWords'] as int,
      nbTypos: json['nbTypos'] as int,
      promoted: json['promoted'] as bool,
      proximityDistance: json['proximityDistance'] as int?,
      userScore: json['userScore'] as int,
      words: json['words'] as int,
      promotedByReRanking: json['promotedByReRanking'] as bool?,
    );

Map<String, dynamic> _$RankingInfoToJson(RankingInfo instance) =>
    <String, dynamic>{
      'filters': instance.filters,
      'firstMatchedWord': instance.firstMatchedWord,
      'geoDistance': instance.geoDistance,
      'geoPrecision': instance.geoPrecision,
      'matchedGeoLocation': instance.matchedGeoLocation,
      'personalization': instance.personalization,
      'nbExactWords': instance.nbExactWords,
      'nbTypos': instance.nbTypos,
      'promoted': instance.promoted,
      'proximityDistance': instance.proximityDistance,
      'userScore': instance.userScore,
      'words': instance.words,
      'promotedByReRanking': instance.promotedByReRanking,
    };
