// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'search_for_facets.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SearchForFacets _$SearchForFacetsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SearchForFacets',
      json,
      ($checkedConvert) {
        final val = SearchForFacets(
          params: $checkedConvert('params', (v) => v as String?),
          query: $checkedConvert('query', (v) => v as String?),
          similarQuery: $checkedConvert('similarQuery', (v) => v as String?),
          filters: $checkedConvert('filters', (v) => v as String?),
          facetFilters: $checkedConvert('facetFilters', (v) => v),
          optionalFilters: $checkedConvert('optionalFilters', (v) => v),
          numericFilters: $checkedConvert('numericFilters', (v) => v),
          tagFilters: $checkedConvert('tagFilters', (v) => v),
          sumOrFiltersScores:
              $checkedConvert('sumOrFiltersScores', (v) => v as bool?),
          facets: $checkedConvert('facets',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          maxValuesPerFacet:
              $checkedConvert('maxValuesPerFacet', (v) => v as int?),
          facetingAfterDistinct:
              $checkedConvert('facetingAfterDistinct', (v) => v as bool?),
          sortFacetValuesBy:
              $checkedConvert('sortFacetValuesBy', (v) => v as String?),
          page: $checkedConvert('page', (v) => v as int?),
          offset: $checkedConvert('offset', (v) => v as int?),
          length: $checkedConvert('length', (v) => v as int?),
          aroundLatLng: $checkedConvert('aroundLatLng', (v) => v as String?),
          aroundLatLngViaIP:
              $checkedConvert('aroundLatLngViaIP', (v) => v as bool?),
          aroundRadius: $checkedConvert('aroundRadius', (v) => v),
          aroundPrecision: $checkedConvert('aroundPrecision', (v) => v as int?),
          minimumAroundRadius:
              $checkedConvert('minimumAroundRadius', (v) => v as int?),
          insideBoundingBox: $checkedConvert(
              'insideBoundingBox',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => (e as num).toDouble())
                  .toList()),
          insidePolygon: $checkedConvert(
              'insidePolygon',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => (e as num).toDouble())
                  .toList()),
          naturalLanguages: $checkedConvert('naturalLanguages',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          ruleContexts: $checkedConvert('ruleContexts',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          personalizationImpact:
              $checkedConvert('personalizationImpact', (v) => v as int?),
          userToken: $checkedConvert('userToken', (v) => v as String?),
          getRankingInfo: $checkedConvert('getRankingInfo', (v) => v as bool?),
          clickAnalytics: $checkedConvert('clickAnalytics', (v) => v as bool?),
          analytics: $checkedConvert('analytics', (v) => v as bool?),
          analyticsTags: $checkedConvert('analyticsTags',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          percentileComputation:
              $checkedConvert('percentileComputation', (v) => v as bool?),
          enableABTest: $checkedConvert('enableABTest', (v) => v as bool?),
          enableReRanking:
              $checkedConvert('enableReRanking', (v) => v as bool?),
          reRankingApplyFilter:
              $checkedConvert('reRankingApplyFilter', (v) => v),
          attributesForFaceting: $checkedConvert('attributesForFaceting',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          attributesToRetrieve: $checkedConvert('attributesToRetrieve',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          restrictSearchableAttributes: $checkedConvert(
              'restrictSearchableAttributes',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          ranking: $checkedConvert('ranking',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          customRanking: $checkedConvert('customRanking',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          relevancyStrictness:
              $checkedConvert('relevancyStrictness', (v) => v as int?),
          attributesToHighlight: $checkedConvert('attributesToHighlight',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          attributesToSnippet: $checkedConvert('attributesToSnippet',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          highlightPreTag:
              $checkedConvert('highlightPreTag', (v) => v as String?),
          highlightPostTag:
              $checkedConvert('highlightPostTag', (v) => v as String?),
          snippetEllipsisText:
              $checkedConvert('snippetEllipsisText', (v) => v as String?),
          restrictHighlightAndSnippetArrays: $checkedConvert(
              'restrictHighlightAndSnippetArrays', (v) => v as bool?),
          hitsPerPage: $checkedConvert('hitsPerPage', (v) => v as int?),
          minWordSizefor1Typo:
              $checkedConvert('minWordSizefor1Typo', (v) => v as int?),
          minWordSizefor2Typos:
              $checkedConvert('minWordSizefor2Typos', (v) => v as int?),
          typoTolerance: $checkedConvert('typoTolerance', (v) => v),
          allowTyposOnNumericTokens:
              $checkedConvert('allowTyposOnNumericTokens', (v) => v as bool?),
          disableTypoToleranceOnAttributes: $checkedConvert(
              'disableTypoToleranceOnAttributes',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          ignorePlurals: $checkedConvert('ignorePlurals', (v) => v),
          removeStopWords: $checkedConvert('removeStopWords', (v) => v),
          keepDiacriticsOnCharacters: $checkedConvert(
              'keepDiacriticsOnCharacters', (v) => v as String?),
          queryLanguages: $checkedConvert('queryLanguages',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          decompoundQuery:
              $checkedConvert('decompoundQuery', (v) => v as bool?),
          enableRules: $checkedConvert('enableRules', (v) => v as bool?),
          enablePersonalization:
              $checkedConvert('enablePersonalization', (v) => v as bool?),
          queryType: $checkedConvert(
              'queryType', (v) => $enumDecodeNullable(_$QueryTypeEnumMap, v)),
          removeWordsIfNoResults: $checkedConvert('removeWordsIfNoResults',
              (v) => $enumDecodeNullable(_$RemoveWordsIfNoResultsEnumMap, v)),
          mode: $checkedConvert(
              'mode', (v) => $enumDecodeNullable(_$ModeEnumMap, v)),
          semanticSearch: $checkedConvert(
              'semanticSearch',
              (v) => v == null
                  ? null
                  : IndexSettingsAsSearchParamsSemanticSearch.fromJson(
                      v as Map<String, dynamic>)),
          advancedSyntax: $checkedConvert('advancedSyntax', (v) => v as bool?),
          optionalWords: $checkedConvert('optionalWords',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          disableExactOnAttributes: $checkedConvert('disableExactOnAttributes',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          exactOnSingleWordQuery: $checkedConvert('exactOnSingleWordQuery',
              (v) => $enumDecodeNullable(_$ExactOnSingleWordQueryEnumMap, v)),
          alternativesAsExact: $checkedConvert(
              'alternativesAsExact',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => $enumDecode(_$AlternativesAsExactEnumMap, e))
                  .toList()),
          advancedSyntaxFeatures: $checkedConvert(
              'advancedSyntaxFeatures',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => $enumDecode(_$AdvancedSyntaxFeaturesEnumMap, e))
                  .toList()),
          explain: $checkedConvert('explain',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          distinct: $checkedConvert('distinct', (v) => v),
          attributeForDistinct:
              $checkedConvert('attributeForDistinct', (v) => v as String?),
          synonyms: $checkedConvert('synonyms', (v) => v as bool?),
          replaceSynonymsInHighlight:
              $checkedConvert('replaceSynonymsInHighlight', (v) => v as bool?),
          minProximity: $checkedConvert('minProximity', (v) => v as int?),
          responseFields: $checkedConvert('responseFields',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          maxFacetHits: $checkedConvert('maxFacetHits', (v) => v as int?),
          attributeCriteriaComputedByMinProximity: $checkedConvert(
              'attributeCriteriaComputedByMinProximity', (v) => v as bool?),
          renderingContent: $checkedConvert(
              'renderingContent',
              (v) => v == null
                  ? null
                  : RenderingContent.fromJson(v as Map<String, dynamic>)),
          facet: $checkedConvert('facet', (v) => v as String),
          indexName: $checkedConvert('indexName', (v) => v as String),
          facetQuery: $checkedConvert('facetQuery', (v) => v as String?),
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$SearchTypeFacetEnumMap, v)),
        );
        return val;
      },
    );

Map<String, dynamic> _$SearchForFacetsToJson(SearchForFacets instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('params', instance.params);
  writeNotNull('query', instance.query);
  writeNotNull('similarQuery', instance.similarQuery);
  writeNotNull('filters', instance.filters);
  writeNotNull('facetFilters', instance.facetFilters);
  writeNotNull('optionalFilters', instance.optionalFilters);
  writeNotNull('numericFilters', instance.numericFilters);
  writeNotNull('tagFilters', instance.tagFilters);
  writeNotNull('sumOrFiltersScores', instance.sumOrFiltersScores);
  writeNotNull('facets', instance.facets);
  writeNotNull('maxValuesPerFacet', instance.maxValuesPerFacet);
  writeNotNull('facetingAfterDistinct', instance.facetingAfterDistinct);
  writeNotNull('sortFacetValuesBy', instance.sortFacetValuesBy);
  writeNotNull('page', instance.page);
  writeNotNull('offset', instance.offset);
  writeNotNull('length', instance.length);
  writeNotNull('aroundLatLng', instance.aroundLatLng);
  writeNotNull('aroundLatLngViaIP', instance.aroundLatLngViaIP);
  writeNotNull('aroundRadius', instance.aroundRadius);
  writeNotNull('aroundPrecision', instance.aroundPrecision);
  writeNotNull('minimumAroundRadius', instance.minimumAroundRadius);
  writeNotNull('insideBoundingBox', instance.insideBoundingBox);
  writeNotNull('insidePolygon', instance.insidePolygon);
  writeNotNull('naturalLanguages', instance.naturalLanguages);
  writeNotNull('ruleContexts', instance.ruleContexts);
  writeNotNull('personalizationImpact', instance.personalizationImpact);
  writeNotNull('userToken', instance.userToken);
  writeNotNull('getRankingInfo', instance.getRankingInfo);
  writeNotNull('clickAnalytics', instance.clickAnalytics);
  writeNotNull('analytics', instance.analytics);
  writeNotNull('analyticsTags', instance.analyticsTags);
  writeNotNull('percentileComputation', instance.percentileComputation);
  writeNotNull('enableABTest', instance.enableABTest);
  writeNotNull('enableReRanking', instance.enableReRanking);
  writeNotNull('reRankingApplyFilter', instance.reRankingApplyFilter);
  writeNotNull('attributesForFaceting', instance.attributesForFaceting);
  writeNotNull('attributesToRetrieve', instance.attributesToRetrieve);
  writeNotNull(
      'restrictSearchableAttributes', instance.restrictSearchableAttributes);
  writeNotNull('ranking', instance.ranking);
  writeNotNull('customRanking', instance.customRanking);
  writeNotNull('relevancyStrictness', instance.relevancyStrictness);
  writeNotNull('attributesToHighlight', instance.attributesToHighlight);
  writeNotNull('attributesToSnippet', instance.attributesToSnippet);
  writeNotNull('highlightPreTag', instance.highlightPreTag);
  writeNotNull('highlightPostTag', instance.highlightPostTag);
  writeNotNull('snippetEllipsisText', instance.snippetEllipsisText);
  writeNotNull('restrictHighlightAndSnippetArrays',
      instance.restrictHighlightAndSnippetArrays);
  writeNotNull('hitsPerPage', instance.hitsPerPage);
  writeNotNull('minWordSizefor1Typo', instance.minWordSizefor1Typo);
  writeNotNull('minWordSizefor2Typos', instance.minWordSizefor2Typos);
  writeNotNull('typoTolerance', instance.typoTolerance);
  writeNotNull('allowTyposOnNumericTokens', instance.allowTyposOnNumericTokens);
  writeNotNull('disableTypoToleranceOnAttributes',
      instance.disableTypoToleranceOnAttributes);
  writeNotNull('ignorePlurals', instance.ignorePlurals);
  writeNotNull('removeStopWords', instance.removeStopWords);
  writeNotNull(
      'keepDiacriticsOnCharacters', instance.keepDiacriticsOnCharacters);
  writeNotNull('queryLanguages', instance.queryLanguages);
  writeNotNull('decompoundQuery', instance.decompoundQuery);
  writeNotNull('enableRules', instance.enableRules);
  writeNotNull('enablePersonalization', instance.enablePersonalization);
  writeNotNull('queryType', instance.queryType?.toJson());
  writeNotNull(
      'removeWordsIfNoResults', instance.removeWordsIfNoResults?.toJson());
  writeNotNull('mode', instance.mode?.toJson());
  writeNotNull('semanticSearch', instance.semanticSearch?.toJson());
  writeNotNull('advancedSyntax', instance.advancedSyntax);
  writeNotNull('optionalWords', instance.optionalWords);
  writeNotNull('disableExactOnAttributes', instance.disableExactOnAttributes);
  writeNotNull(
      'exactOnSingleWordQuery', instance.exactOnSingleWordQuery?.toJson());
  writeNotNull('alternativesAsExact',
      instance.alternativesAsExact?.map((e) => e.toJson()).toList());
  writeNotNull('advancedSyntaxFeatures',
      instance.advancedSyntaxFeatures?.map((e) => e.toJson()).toList());
  writeNotNull('explain', instance.explain);
  writeNotNull('distinct', instance.distinct);
  writeNotNull('attributeForDistinct', instance.attributeForDistinct);
  writeNotNull('synonyms', instance.synonyms);
  writeNotNull(
      'replaceSynonymsInHighlight', instance.replaceSynonymsInHighlight);
  writeNotNull('minProximity', instance.minProximity);
  writeNotNull('responseFields', instance.responseFields);
  writeNotNull('maxFacetHits', instance.maxFacetHits);
  writeNotNull('attributeCriteriaComputedByMinProximity',
      instance.attributeCriteriaComputedByMinProximity);
  writeNotNull('renderingContent', instance.renderingContent?.toJson());
  val['facet'] = instance.facet;
  val['indexName'] = instance.indexName;
  writeNotNull('facetQuery', instance.facetQuery);
  val['type'] = instance.type.toJson();
  return val;
}

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

const _$SearchTypeFacetEnumMap = {
  SearchTypeFacet.facet: 'facet',
};
