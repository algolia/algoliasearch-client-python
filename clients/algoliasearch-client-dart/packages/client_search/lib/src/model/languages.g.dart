// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'languages.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Languages _$LanguagesFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Languages',
      json,
      ($checkedConvert) {
        final val = Languages(
          plurals: $checkedConvert(
              'plurals',
              (v) => v == null
                  ? null
                  : DictionaryLanguage.fromJson(v as Map<String, dynamic>)),
          stopwords: $checkedConvert(
              'stopwords',
              (v) => v == null
                  ? null
                  : DictionaryLanguage.fromJson(v as Map<String, dynamic>)),
          compounds: $checkedConvert(
              'compounds',
              (v) => v == null
                  ? null
                  : DictionaryLanguage.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$LanguagesToJson(Languages instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('plurals', instance.plurals?.toJson());
  writeNotNull('stopwords', instance.stopwords?.toJson());
  writeNotNull('compounds', instance.compounds?.toJson());
  return val;
}
