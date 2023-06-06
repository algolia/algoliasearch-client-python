// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'languages.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Languages _$LanguagesFromJson(Map<String, dynamic> json) => Languages(
      plurals: json['plurals'] == null
          ? null
          : DictionaryLanguage.fromJson(
              json['plurals'] as Map<String, dynamic>),
      stopwords: json['stopwords'] == null
          ? null
          : DictionaryLanguage.fromJson(
              json['stopwords'] as Map<String, dynamic>),
      compounds: json['compounds'] == null
          ? null
          : DictionaryLanguage.fromJson(
              json['compounds'] as Map<String, dynamic>),
    );

Map<String, dynamic> _$LanguagesToJson(Languages instance) => <String, dynamic>{
      'plurals': instance.plurals,
      'stopwords': instance.stopwords,
      'compounds': instance.compounds,
    };
