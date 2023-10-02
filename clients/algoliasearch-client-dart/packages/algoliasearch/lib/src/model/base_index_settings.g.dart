// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'base_index_settings.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BaseIndexSettings _$BaseIndexSettingsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'BaseIndexSettings',
      json,
      ($checkedConvert) {
        final val = BaseIndexSettings(
          replicas: $checkedConvert('replicas',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          paginationLimitedTo:
              $checkedConvert('paginationLimitedTo', (v) => v as int?),
          unretrievableAttributes: $checkedConvert('unretrievableAttributes',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          disableTypoToleranceOnWords: $checkedConvert(
              'disableTypoToleranceOnWords',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          attributesToTransliterate: $checkedConvert(
              'attributesToTransliterate',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          camelCaseAttributes: $checkedConvert('camelCaseAttributes',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          decompoundedAttributes:
              $checkedConvert('decompoundedAttributes', (v) => v),
          indexLanguages: $checkedConvert('indexLanguages',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          disablePrefixOnAttributes: $checkedConvert(
              'disablePrefixOnAttributes',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          allowCompressionOfIntegerArray: $checkedConvert(
              'allowCompressionOfIntegerArray', (v) => v as bool?),
          numericAttributesForFiltering: $checkedConvert(
              'numericAttributesForFiltering',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          separatorsToIndex:
              $checkedConvert('separatorsToIndex', (v) => v as String?),
          searchableAttributes: $checkedConvert('searchableAttributes',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          userData: $checkedConvert('userData', (v) => v),
          customNormalization: $checkedConvert(
              'customNormalization',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) => MapEntry(k, Map<String, String>.from(e as Map)),
                  )),
          attributeForDistinct:
              $checkedConvert('attributeForDistinct', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$BaseIndexSettingsToJson(BaseIndexSettings instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('replicas', instance.replicas);
  writeNotNull('paginationLimitedTo', instance.paginationLimitedTo);
  writeNotNull('unretrievableAttributes', instance.unretrievableAttributes);
  writeNotNull(
      'disableTypoToleranceOnWords', instance.disableTypoToleranceOnWords);
  writeNotNull('attributesToTransliterate', instance.attributesToTransliterate);
  writeNotNull('camelCaseAttributes', instance.camelCaseAttributes);
  writeNotNull('decompoundedAttributes', instance.decompoundedAttributes);
  writeNotNull('indexLanguages', instance.indexLanguages);
  writeNotNull('disablePrefixOnAttributes', instance.disablePrefixOnAttributes);
  writeNotNull('allowCompressionOfIntegerArray',
      instance.allowCompressionOfIntegerArray);
  writeNotNull(
      'numericAttributesForFiltering', instance.numericAttributesForFiltering);
  writeNotNull('separatorsToIndex', instance.separatorsToIndex);
  writeNotNull('searchableAttributes', instance.searchableAttributes);
  writeNotNull('userData', instance.userData);
  writeNotNull('customNormalization', instance.customNormalization);
  writeNotNull('attributeForDistinct', instance.attributeForDistinct);
  return val;
}
