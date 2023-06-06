// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'hit.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Hit _$HitFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Hit',
      json,
      ($checkedConvert) {
        final val = Hit(
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
        );
        return val;
      },
      fieldKeyMap: const {
        'highlightResult': '_highlightResult',
        'snippetResult': '_snippetResult',
        'rankingInfo': '_rankingInfo',
        'distinctSeqID': '_distinctSeqID'
      },
    );
