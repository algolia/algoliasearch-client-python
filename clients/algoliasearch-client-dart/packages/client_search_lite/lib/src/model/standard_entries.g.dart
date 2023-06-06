// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'standard_entries.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

StandardEntries _$StandardEntriesFromJson(Map<String, dynamic> json) =>
    StandardEntries(
      plurals: (json['plurals'] as Map<String, dynamic>?)?.map(
        (k, e) => MapEntry(k, e as bool),
      ),
      stopwords: (json['stopwords'] as Map<String, dynamic>?)?.map(
        (k, e) => MapEntry(k, e as bool),
      ),
      compounds: (json['compounds'] as Map<String, dynamic>?)?.map(
        (k, e) => MapEntry(k, e as bool),
      ),
    );

Map<String, dynamic> _$StandardEntriesToJson(StandardEntries instance) =>
    <String, dynamic>{
      'plurals': instance.plurals,
      'stopwords': instance.stopwords,
      'compounds': instance.compounds,
    };
