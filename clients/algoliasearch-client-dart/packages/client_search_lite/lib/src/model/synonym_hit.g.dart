// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'synonym_hit.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SynonymHit _$SynonymHitFromJson(Map<String, dynamic> json) => SynonymHit(
      objectID: json['objectID'] as String,
      type: $enumDecode(_$SynonymTypeEnumMap, json['type']),
      synonyms: (json['synonyms'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      input: json['input'] as String?,
      word: json['word'] as String?,
      corrections: (json['corrections'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      placeholder: json['placeholder'] as String?,
      replacements: (json['replacements'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
    );

Map<String, dynamic> _$SynonymHitToJson(SynonymHit instance) =>
    <String, dynamic>{
      'objectID': instance.objectID,
      'type': _$SynonymTypeEnumMap[instance.type]!,
      'synonyms': instance.synonyms,
      'input': instance.input,
      'word': instance.word,
      'corrections': instance.corrections,
      'placeholder': instance.placeholder,
      'replacements': instance.replacements,
    };

const _$SynonymTypeEnumMap = {
  SynonymType.synonym: 'synonym',
  SynonymType.onewaysynonym: 'onewaysynonym',
  SynonymType.altcorrection1: 'altcorrection1',
  SynonymType.altcorrection2: 'altcorrection2',
  SynonymType.placeholder: 'placeholder',
};
