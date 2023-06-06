// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'base_search_params_without_query.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BaseSearchParamsWithoutQuery _$BaseSearchParamsWithoutQueryFromJson(
        Map<String, dynamic> json) =>
    BaseSearchParamsWithoutQuery(
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
    );

Map<String, dynamic> _$BaseSearchParamsWithoutQueryToJson(
        BaseSearchParamsWithoutQuery instance) =>
    <String, dynamic>{
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
    };
