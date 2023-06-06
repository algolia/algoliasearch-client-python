// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'base_index_settings.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BaseIndexSettings _$BaseIndexSettingsFromJson(Map<String, dynamic> json) =>
    BaseIndexSettings(
      replicas: (json['replicas'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      paginationLimitedTo: json['paginationLimitedTo'] as int?,
      unretrievableAttributes:
          (json['unretrievableAttributes'] as List<dynamic>?)
              ?.map((e) => e as String)
              .toList(),
      disableTypoToleranceOnWords:
          (json['disableTypoToleranceOnWords'] as List<dynamic>?)
              ?.map((e) => e as String)
              .toList(),
      attributesToTransliterate:
          (json['attributesToTransliterate'] as List<dynamic>?)
              ?.map((e) => e as String)
              .toList(),
      camelCaseAttributes: (json['camelCaseAttributes'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      decompoundedAttributes: json['decompoundedAttributes'],
      indexLanguages: (json['indexLanguages'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      disablePrefixOnAttributes:
          (json['disablePrefixOnAttributes'] as List<dynamic>?)
              ?.map((e) => e as String)
              .toList(),
      allowCompressionOfIntegerArray:
          json['allowCompressionOfIntegerArray'] as bool?,
      numericAttributesForFiltering:
          (json['numericAttributesForFiltering'] as List<dynamic>?)
              ?.map((e) => e as String)
              .toList(),
      separatorsToIndex: json['separatorsToIndex'] as String?,
      searchableAttributes: (json['searchableAttributes'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      userData: json['userData'],
      customNormalization:
          (json['customNormalization'] as Map<String, dynamic>?)?.map(
        (k, e) => MapEntry(k, Map<String, String>.from(e as Map)),
      ),
    );

Map<String, dynamic> _$BaseIndexSettingsToJson(BaseIndexSettings instance) =>
    <String, dynamic>{
      'replicas': instance.replicas,
      'paginationLimitedTo': instance.paginationLimitedTo,
      'unretrievableAttributes': instance.unretrievableAttributes,
      'disableTypoToleranceOnWords': instance.disableTypoToleranceOnWords,
      'attributesToTransliterate': instance.attributesToTransliterate,
      'camelCaseAttributes': instance.camelCaseAttributes,
      'decompoundedAttributes': instance.decompoundedAttributes,
      'indexLanguages': instance.indexLanguages,
      'disablePrefixOnAttributes': instance.disablePrefixOnAttributes,
      'allowCompressionOfIntegerArray': instance.allowCompressionOfIntegerArray,
      'numericAttributesForFiltering': instance.numericAttributesForFiltering,
      'separatorsToIndex': instance.separatorsToIndex,
      'searchableAttributes': instance.searchableAttributes,
      'userData': instance.userData,
      'customNormalization': instance.customNormalization,
    };
