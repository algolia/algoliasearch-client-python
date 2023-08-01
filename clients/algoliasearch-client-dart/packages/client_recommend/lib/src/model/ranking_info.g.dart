// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'ranking_info.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RankingInfo _$RankingInfoFromJson(Map<String, dynamic> json) => $checkedCreate(
      'RankingInfo',
      json,
      ($checkedConvert) {
        final val = RankingInfo(
          filters: $checkedConvert('filters', (v) => v as int),
          firstMatchedWord:
              $checkedConvert('firstMatchedWord', (v) => v as int),
          geoDistance: $checkedConvert('geoDistance', (v) => v as int),
          geoPrecision: $checkedConvert('geoPrecision', (v) => v as int?),
          matchedGeoLocation: $checkedConvert(
              'matchedGeoLocation',
              (v) => v == null
                  ? null
                  : MatchedGeoLocation.fromJson(v as Map<String, dynamic>)),
          personalization: $checkedConvert(
              'personalization',
              (v) => v == null
                  ? null
                  : Personalization.fromJson(v as Map<String, dynamic>)),
          nbExactWords: $checkedConvert('nbExactWords', (v) => v as int),
          nbTypos: $checkedConvert('nbTypos', (v) => v as int),
          promoted: $checkedConvert('promoted', (v) => v as bool),
          proximityDistance:
              $checkedConvert('proximityDistance', (v) => v as int?),
          userScore: $checkedConvert('userScore', (v) => v as int),
          words: $checkedConvert('words', (v) => v as int),
          promotedByReRanking:
              $checkedConvert('promotedByReRanking', (v) => v as bool?),
        );
        return val;
      },
    );

Map<String, dynamic> _$RankingInfoToJson(RankingInfo instance) {
  final val = <String, dynamic>{
    'filters': instance.filters,
    'firstMatchedWord': instance.firstMatchedWord,
    'geoDistance': instance.geoDistance,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('geoPrecision', instance.geoPrecision);
  writeNotNull('matchedGeoLocation', instance.matchedGeoLocation?.toJson());
  writeNotNull('personalization', instance.personalization?.toJson());
  val['nbExactWords'] = instance.nbExactWords;
  val['nbTypos'] = instance.nbTypos;
  val['promoted'] = instance.promoted;
  writeNotNull('proximityDistance', instance.proximityDistance);
  val['userScore'] = instance.userScore;
  val['words'] = instance.words;
  writeNotNull('promotedByReRanking', instance.promotedByReRanking);
  return val;
}
