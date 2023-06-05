// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'personalization.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Personalization _$PersonalizationFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'Personalization',
      json,
      ($checkedConvert) {
        final val = Personalization(
          filtersScore: $checkedConvert('filtersScore', (v) => v as int?),
          rankingScore: $checkedConvert('rankingScore', (v) => v as int?),
          score: $checkedConvert('score', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$PersonalizationToJson(Personalization instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('filtersScore', instance.filtersScore);
  writeNotNull('rankingScore', instance.rankingScore);
  writeNotNull('score', instance.score);
  return val;
}
