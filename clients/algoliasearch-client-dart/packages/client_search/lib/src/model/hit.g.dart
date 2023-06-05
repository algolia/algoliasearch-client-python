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

Map<String, dynamic> _$HitToJson(Hit instance) {
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
  return val;
}
