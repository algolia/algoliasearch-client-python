// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'synonym_hit.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SynonymHit _$SynonymHitFromJson(Map<String, dynamic> json) => $checkedCreate(
      'SynonymHit',
      json,
      ($checkedConvert) {
        final val = SynonymHit(
          objectID: $checkedConvert('objectID', (v) => v as String),
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$SynonymTypeEnumMap, v)),
          synonyms: $checkedConvert('synonyms',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          input: $checkedConvert('input', (v) => v as String?),
          word: $checkedConvert('word', (v) => v as String?),
          corrections: $checkedConvert('corrections',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          placeholder: $checkedConvert('placeholder', (v) => v as String?),
          replacements: $checkedConvert('replacements',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$SynonymHitToJson(SynonymHit instance) {
  final val = <String, dynamic>{
    'objectID': instance.objectID,
    'type': _$SynonymTypeEnumMap[instance.type]!,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('synonyms', instance.synonyms);
  writeNotNull('input', instance.input);
  writeNotNull('word', instance.word);
  writeNotNull('corrections', instance.corrections);
  writeNotNull('placeholder', instance.placeholder);
  writeNotNull('replacements', instance.replacements);
  return val;
}

const _$SynonymTypeEnumMap = {
  SynonymType.synonym: 'synonym',
  SynonymType.onewaysynonym: 'onewaysynonym',
  SynonymType.altcorrection1: 'altcorrection1',
  SynonymType.altcorrection2: 'altcorrection2',
  SynonymType.placeholder: 'placeholder',
};
