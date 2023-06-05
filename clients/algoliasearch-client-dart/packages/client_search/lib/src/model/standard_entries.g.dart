// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'standard_entries.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

StandardEntries _$StandardEntriesFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'StandardEntries',
      json,
      ($checkedConvert) {
        final val = StandardEntries(
          plurals: $checkedConvert(
              'plurals',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) => MapEntry(k, e as bool),
                  )),
          stopwords: $checkedConvert(
              'stopwords',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) => MapEntry(k, e as bool),
                  )),
          compounds: $checkedConvert(
              'compounds',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) => MapEntry(k, e as bool),
                  )),
        );
        return val;
      },
    );

Map<String, dynamic> _$StandardEntriesToJson(StandardEntries instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('plurals', instance.plurals);
  writeNotNull('stopwords', instance.stopwords);
  writeNotNull('compounds', instance.compounds);
  return val;
}
