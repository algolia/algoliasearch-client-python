// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'browse_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BrowseResponse _$BrowseResponseFromJson(Map<String, dynamic> json) =>
    BrowseResponse(
      abTestID: json['abTestID'] as int?,
      abTestVariantID: json['abTestVariantID'] as int?,
      aroundLatLng: json['aroundLatLng'] as String?,
      automaticRadius: json['automaticRadius'] as String?,
      exhaustiveFacetsCount: json['exhaustiveFacetsCount'] as bool?,
      exhaustiveNbHits: json['exhaustiveNbHits'] as bool,
      exhaustiveTypo: json['exhaustiveTypo'] as bool?,
      facets: (json['facets'] as Map<String, dynamic>?)?.map(
        (k, e) => MapEntry(k, Map<String, int>.from(e as Map)),
      ),
      facetsStats: (json['facets_stats'] as Map<String, dynamic>?)?.map(
        (k, e) => MapEntry(k, FacetsStats.fromJson(e as Map<String, dynamic>)),
      ),
      hitsPerPage: json['hitsPerPage'] as int,
      index: json['index'] as String?,
      indexUsed: json['indexUsed'] as String?,
      message: json['message'] as String?,
      nbHits: json['nbHits'] as int,
      nbPages: json['nbPages'] as int,
      nbSortedHits: json['nbSortedHits'] as int?,
      page: json['page'] as int,
      params: json['params'] as String,
      redirect: json['redirect'] == null
          ? null
          : BaseSearchResponseRedirect.fromJson(
              json['redirect'] as Map<String, dynamic>),
      parsedQuery: json['parsedQuery'] as String?,
      processingTimeMS: json['processingTimeMS'] as int,
      query: json['query'] as String,
      queryAfterRemoval: json['queryAfterRemoval'] as String?,
      serverUsed: json['serverUsed'] as String?,
      userData: json['userData'],
      renderingContent: json['renderingContent'] == null
          ? null
          : RenderingContent.fromJson(
              json['renderingContent'] as Map<String, dynamic>),
      hits: (json['hits'] as List<dynamic>)
          .map((e) => Hit.fromJson(e as Map<String, dynamic>))
          .toList(),
      cursor: json['cursor'] as String?,
    );

Map<String, dynamic> _$BrowseResponseToJson(BrowseResponse instance) =>
    <String, dynamic>{
      'abTestID': instance.abTestID,
      'abTestVariantID': instance.abTestVariantID,
      'aroundLatLng': instance.aroundLatLng,
      'automaticRadius': instance.automaticRadius,
      'exhaustiveFacetsCount': instance.exhaustiveFacetsCount,
      'exhaustiveNbHits': instance.exhaustiveNbHits,
      'exhaustiveTypo': instance.exhaustiveTypo,
      'facets': instance.facets,
      'facets_stats': instance.facetsStats,
      'hitsPerPage': instance.hitsPerPage,
      'index': instance.index,
      'indexUsed': instance.indexUsed,
      'message': instance.message,
      'nbHits': instance.nbHits,
      'nbPages': instance.nbPages,
      'nbSortedHits': instance.nbSortedHits,
      'page': instance.page,
      'params': instance.params,
      'redirect': instance.redirect,
      'parsedQuery': instance.parsedQuery,
      'processingTimeMS': instance.processingTimeMS,
      'query': instance.query,
      'queryAfterRemoval': instance.queryAfterRemoval,
      'serverUsed': instance.serverUsed,
      'userData': instance.userData,
      'renderingContent': instance.renderingContent,
      'hits': instance.hits,
      'cursor': instance.cursor,
    };
