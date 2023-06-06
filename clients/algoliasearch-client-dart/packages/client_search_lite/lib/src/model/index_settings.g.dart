// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'index_settings.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

IndexSettings _$IndexSettingsFromJson(Map<String, dynamic> json) =>
    IndexSettings(
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
      attributesForFaceting: (json['attributesForFaceting'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      attributesToRetrieve: (json['attributesToRetrieve'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      restrictSearchableAttributes:
          (json['restrictSearchableAttributes'] as List<dynamic>?)
              ?.map((e) => e as String)
              .toList(),
      ranking:
          (json['ranking'] as List<dynamic>?)?.map((e) => e as String).toList(),
      customRanking: (json['customRanking'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      relevancyStrictness: json['relevancyStrictness'] as int?,
      attributesToHighlight: (json['attributesToHighlight'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      attributesToSnippet: (json['attributesToSnippet'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      highlightPreTag: json['highlightPreTag'] as String?,
      highlightPostTag: json['highlightPostTag'] as String?,
      snippetEllipsisText: json['snippetEllipsisText'] as String?,
      restrictHighlightAndSnippetArrays:
          json['restrictHighlightAndSnippetArrays'] as bool?,
      hitsPerPage: json['hitsPerPage'] as int?,
      minWordSizefor1Typo: json['minWordSizefor1Typo'] as int?,
      minWordSizefor2Typos: json['minWordSizefor2Typos'] as int?,
      typoTolerance: json['typoTolerance'],
      allowTyposOnNumericTokens: json['allowTyposOnNumericTokens'] as bool?,
      disableTypoToleranceOnAttributes:
          (json['disableTypoToleranceOnAttributes'] as List<dynamic>?)
              ?.map((e) => e as String)
              .toList(),
      ignorePlurals: json['ignorePlurals'],
      removeStopWords: json['removeStopWords'],
      keepDiacriticsOnCharacters: json['keepDiacriticsOnCharacters'] as String?,
      queryLanguages: (json['queryLanguages'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      decompoundQuery: json['decompoundQuery'] as bool?,
      enableRules: json['enableRules'] as bool?,
      enablePersonalization: json['enablePersonalization'] as bool?,
      queryType: $enumDecodeNullable(_$QueryTypeEnumMap, json['queryType']),
      removeWordsIfNoResults: $enumDecodeNullable(
          _$RemoveWordsIfNoResultsEnumMap, json['removeWordsIfNoResults']),
      mode: $enumDecodeNullable(_$ModeEnumMap, json['mode']),
      semanticSearch: json['semanticSearch'] == null
          ? null
          : IndexSettingsAsSearchParamsSemanticSearch.fromJson(
              json['semanticSearch'] as Map<String, dynamic>),
      advancedSyntax: json['advancedSyntax'] as bool?,
      optionalWords: (json['optionalWords'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      disableExactOnAttributes:
          (json['disableExactOnAttributes'] as List<dynamic>?)
              ?.map((e) => e as String)
              .toList(),
      exactOnSingleWordQuery: $enumDecodeNullable(
          _$ExactOnSingleWordQueryEnumMap, json['exactOnSingleWordQuery']),
      alternativesAsExact: (json['alternativesAsExact'] as List<dynamic>?)
          ?.map((e) => $enumDecode(_$AlternativesAsExactEnumMap, e))
          .toList(),
      advancedSyntaxFeatures: (json['advancedSyntaxFeatures'] as List<dynamic>?)
          ?.map((e) => $enumDecode(_$AdvancedSyntaxFeaturesEnumMap, e))
          .toList(),
      explain:
          (json['explain'] as List<dynamic>?)?.map((e) => e as String).toList(),
      distinct: json['distinct'],
      attributeForDistinct: json['attributeForDistinct'] as String?,
      synonyms: json['synonyms'] as bool?,
      replaceSynonymsInHighlight: json['replaceSynonymsInHighlight'] as bool?,
      minProximity: json['minProximity'] as int?,
      responseFields: (json['responseFields'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      maxFacetHits: json['maxFacetHits'] as int?,
      attributeCriteriaComputedByMinProximity:
          json['attributeCriteriaComputedByMinProximity'] as bool?,
      renderingContent: json['renderingContent'] == null
          ? null
          : RenderingContent.fromJson(
              json['renderingContent'] as Map<String, dynamic>),
    );

Map<String, dynamic> _$IndexSettingsToJson(IndexSettings instance) =>
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
      'attributesForFaceting': instance.attributesForFaceting,
      'attributesToRetrieve': instance.attributesToRetrieve,
      'restrictSearchableAttributes': instance.restrictSearchableAttributes,
      'ranking': instance.ranking,
      'customRanking': instance.customRanking,
      'relevancyStrictness': instance.relevancyStrictness,
      'attributesToHighlight': instance.attributesToHighlight,
      'attributesToSnippet': instance.attributesToSnippet,
      'highlightPreTag': instance.highlightPreTag,
      'highlightPostTag': instance.highlightPostTag,
      'snippetEllipsisText': instance.snippetEllipsisText,
      'restrictHighlightAndSnippetArrays':
          instance.restrictHighlightAndSnippetArrays,
      'hitsPerPage': instance.hitsPerPage,
      'minWordSizefor1Typo': instance.minWordSizefor1Typo,
      'minWordSizefor2Typos': instance.minWordSizefor2Typos,
      'typoTolerance': instance.typoTolerance,
      'allowTyposOnNumericTokens': instance.allowTyposOnNumericTokens,
      'disableTypoToleranceOnAttributes':
          instance.disableTypoToleranceOnAttributes,
      'ignorePlurals': instance.ignorePlurals,
      'removeStopWords': instance.removeStopWords,
      'keepDiacriticsOnCharacters': instance.keepDiacriticsOnCharacters,
      'queryLanguages': instance.queryLanguages,
      'decompoundQuery': instance.decompoundQuery,
      'enableRules': instance.enableRules,
      'enablePersonalization': instance.enablePersonalization,
      'queryType': _$QueryTypeEnumMap[instance.queryType],
      'removeWordsIfNoResults':
          _$RemoveWordsIfNoResultsEnumMap[instance.removeWordsIfNoResults],
      'mode': _$ModeEnumMap[instance.mode],
      'semanticSearch': instance.semanticSearch,
      'advancedSyntax': instance.advancedSyntax,
      'optionalWords': instance.optionalWords,
      'disableExactOnAttributes': instance.disableExactOnAttributes,
      'exactOnSingleWordQuery':
          _$ExactOnSingleWordQueryEnumMap[instance.exactOnSingleWordQuery],
      'alternativesAsExact': instance.alternativesAsExact
          ?.map((e) => _$AlternativesAsExactEnumMap[e]!)
          .toList(),
      'advancedSyntaxFeatures': instance.advancedSyntaxFeatures
          ?.map((e) => _$AdvancedSyntaxFeaturesEnumMap[e]!)
          .toList(),
      'explain': instance.explain,
      'distinct': instance.distinct,
      'attributeForDistinct': instance.attributeForDistinct,
      'synonyms': instance.synonyms,
      'replaceSynonymsInHighlight': instance.replaceSynonymsInHighlight,
      'minProximity': instance.minProximity,
      'responseFields': instance.responseFields,
      'maxFacetHits': instance.maxFacetHits,
      'attributeCriteriaComputedByMinProximity':
          instance.attributeCriteriaComputedByMinProximity,
      'renderingContent': instance.renderingContent,
    };

const _$QueryTypeEnumMap = {
  QueryType.prefixLast: 'prefixLast',
  QueryType.prefixAll: 'prefixAll',
  QueryType.prefixNone: 'prefixNone',
};

const _$RemoveWordsIfNoResultsEnumMap = {
  RemoveWordsIfNoResults.none: 'none',
  RemoveWordsIfNoResults.lastWords: 'lastWords',
  RemoveWordsIfNoResults.firstWords: 'firstWords',
  RemoveWordsIfNoResults.allOptional: 'allOptional',
};

const _$ModeEnumMap = {
  Mode.neuralSearch: 'neuralSearch',
  Mode.keywordSearch: 'keywordSearch',
};

const _$ExactOnSingleWordQueryEnumMap = {
  ExactOnSingleWordQuery.attribute: 'attribute',
  ExactOnSingleWordQuery.none: 'none',
  ExactOnSingleWordQuery.word: 'word',
};

const _$AlternativesAsExactEnumMap = {
  AlternativesAsExact.ignorePlurals: 'ignorePlurals',
  AlternativesAsExact.singleWordSynonym: 'singleWordSynonym',
  AlternativesAsExact.multiWordsSynonym: 'multiWordsSynonym',
};

const _$AdvancedSyntaxFeaturesEnumMap = {
  AdvancedSyntaxFeatures.exactPhrase: 'exactPhrase',
  AdvancedSyntaxFeatures.excludeWords: 'excludeWords',
};
