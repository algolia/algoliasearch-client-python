// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'browse_params_object.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BrowseParamsObject _$BrowseParamsObjectFromJson(Map<String, dynamic> json) =>
    BrowseParamsObject(
      query: json['query'] as String?,
      similarQuery: json['similarQuery'] as String?,
      filters: json['filters'] as String?,
      facetFilters: json['facetFilters'],
      optionalFilters: json['optionalFilters'],
      numericFilters: json['numericFilters'],
      tagFilters: json['tagFilters'],
      sumOrFiltersScores: json['sumOrFiltersScores'] as bool?,
      facets:
          (json['facets'] as List<dynamic>?)?.map((e) => e as String).toList(),
      maxValuesPerFacet: json['maxValuesPerFacet'] as int?,
      facetingAfterDistinct: json['facetingAfterDistinct'] as bool?,
      sortFacetValuesBy: json['sortFacetValuesBy'] as String?,
      page: json['page'] as int?,
      offset: json['offset'] as int?,
      length: json['length'] as int?,
      aroundLatLng: json['aroundLatLng'] as String?,
      aroundLatLngViaIP: json['aroundLatLngViaIP'] as bool?,
      aroundRadius: json['aroundRadius'],
      aroundPrecision: json['aroundPrecision'] as int?,
      minimumAroundRadius: json['minimumAroundRadius'] as int?,
      insideBoundingBox: (json['insideBoundingBox'] as List<dynamic>?)
          ?.map((e) => (e as num).toDouble())
          .toList(),
      insidePolygon: (json['insidePolygon'] as List<dynamic>?)
          ?.map((e) => (e as num).toDouble())
          .toList(),
      naturalLanguages: (json['naturalLanguages'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      ruleContexts: (json['ruleContexts'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      personalizationImpact: json['personalizationImpact'] as int?,
      userToken: json['userToken'] as String?,
      getRankingInfo: json['getRankingInfo'] as bool?,
      clickAnalytics: json['clickAnalytics'] as bool?,
      analytics: json['analytics'] as bool?,
      analyticsTags: (json['analyticsTags'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      percentileComputation: json['percentileComputation'] as bool?,
      enableABTest: json['enableABTest'] as bool?,
      enableReRanking: json['enableReRanking'] as bool?,
      reRankingApplyFilter: json['reRankingApplyFilter'],
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
      cursor: json['cursor'] as String?,
    );

Map<String, dynamic> _$BrowseParamsObjectToJson(BrowseParamsObject instance) =>
    <String, dynamic>{
      'query': instance.query,
      'similarQuery': instance.similarQuery,
      'filters': instance.filters,
      'facetFilters': instance.facetFilters,
      'optionalFilters': instance.optionalFilters,
      'numericFilters': instance.numericFilters,
      'tagFilters': instance.tagFilters,
      'sumOrFiltersScores': instance.sumOrFiltersScores,
      'facets': instance.facets,
      'maxValuesPerFacet': instance.maxValuesPerFacet,
      'facetingAfterDistinct': instance.facetingAfterDistinct,
      'sortFacetValuesBy': instance.sortFacetValuesBy,
      'page': instance.page,
      'offset': instance.offset,
      'length': instance.length,
      'aroundLatLng': instance.aroundLatLng,
      'aroundLatLngViaIP': instance.aroundLatLngViaIP,
      'aroundRadius': instance.aroundRadius,
      'aroundPrecision': instance.aroundPrecision,
      'minimumAroundRadius': instance.minimumAroundRadius,
      'insideBoundingBox': instance.insideBoundingBox,
      'insidePolygon': instance.insidePolygon,
      'naturalLanguages': instance.naturalLanguages,
      'ruleContexts': instance.ruleContexts,
      'personalizationImpact': instance.personalizationImpact,
      'userToken': instance.userToken,
      'getRankingInfo': instance.getRankingInfo,
      'clickAnalytics': instance.clickAnalytics,
      'analytics': instance.analytics,
      'analyticsTags': instance.analyticsTags,
      'percentileComputation': instance.percentileComputation,
      'enableABTest': instance.enableABTest,
      'enableReRanking': instance.enableReRanking,
      'reRankingApplyFilter': instance.reRankingApplyFilter,
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
      'cursor': instance.cursor,
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
