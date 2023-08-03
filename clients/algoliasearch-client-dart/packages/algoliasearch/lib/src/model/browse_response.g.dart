// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'browse_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BrowseResponse _$BrowseResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'BrowseResponse',
      json,
      ($checkedConvert) {
        final val = BrowseResponse(
          abTestID: $checkedConvert('abTestID', (v) => v as int?),
          abTestVariantID: $checkedConvert('abTestVariantID', (v) => v as int?),
          aroundLatLng: $checkedConvert('aroundLatLng', (v) => v as String?),
          automaticRadius:
              $checkedConvert('automaticRadius', (v) => v as String?),
          exhaustiveFacetsCount:
              $checkedConvert('exhaustiveFacetsCount', (v) => v as bool?),
          exhaustiveNbHits:
              $checkedConvert('exhaustiveNbHits', (v) => v as bool),
          exhaustiveTypo: $checkedConvert('exhaustiveTypo', (v) => v as bool?),
          facets: $checkedConvert(
              'facets',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) => MapEntry(k, Map<String, int>.from(e as Map)),
                  )),
          facetsStats: $checkedConvert(
              'facets_stats',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) => MapEntry(
                        k, FacetsStats.fromJson(e as Map<String, dynamic>)),
                  )),
          hitsPerPage: $checkedConvert('hitsPerPage', (v) => v as int),
          index: $checkedConvert('index', (v) => v as String?),
          indexUsed: $checkedConvert('indexUsed', (v) => v as String?),
          message: $checkedConvert('message', (v) => v as String?),
          nbHits: $checkedConvert('nbHits', (v) => v as int),
          nbPages: $checkedConvert('nbPages', (v) => v as int),
          nbSortedHits: $checkedConvert('nbSortedHits', (v) => v as int?),
          page: $checkedConvert('page', (v) => v as int),
          redirect: $checkedConvert(
              'redirect',
              (v) => v == null
                  ? null
                  : BaseSearchResponseRedirect.fromJson(
                      v as Map<String, dynamic>)),
          parsedQuery: $checkedConvert('parsedQuery', (v) => v as String?),
          processingTimeMS:
              $checkedConvert('processingTimeMS', (v) => v as int),
          queryAfterRemoval:
              $checkedConvert('queryAfterRemoval', (v) => v as String?),
          serverUsed: $checkedConvert('serverUsed', (v) => v as String?),
          userData: $checkedConvert('userData', (v) => v),
          renderingContent: $checkedConvert(
              'renderingContent',
              (v) => v == null
                  ? null
                  : RenderingContent.fromJson(v as Map<String, dynamic>)),
          hits: $checkedConvert(
              'hits',
              (v) => (v as List<dynamic>)
                  .map((e) => Hit.fromJson(e as Map<String, dynamic>))
                  .toList()),
          query: $checkedConvert('query', (v) => v as String),
          params: $checkedConvert('params', (v) => v as String),
          cursor: $checkedConvert('cursor', (v) => v as String?),
        );
        return val;
      },
      fieldKeyMap: const {'facetsStats': 'facets_stats'},
    );

Map<String, dynamic> _$BrowseResponseToJson(BrowseResponse instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('abTestID', instance.abTestID);
  writeNotNull('abTestVariantID', instance.abTestVariantID);
  writeNotNull('aroundLatLng', instance.aroundLatLng);
  writeNotNull('automaticRadius', instance.automaticRadius);
  writeNotNull('exhaustiveFacetsCount', instance.exhaustiveFacetsCount);
  val['exhaustiveNbHits'] = instance.exhaustiveNbHits;
  writeNotNull('exhaustiveTypo', instance.exhaustiveTypo);
  writeNotNull('facets', instance.facets);
  writeNotNull('facets_stats',
      instance.facetsStats?.map((k, e) => MapEntry(k, e.toJson())));
  val['hitsPerPage'] = instance.hitsPerPage;
  writeNotNull('index', instance.index);
  writeNotNull('indexUsed', instance.indexUsed);
  writeNotNull('message', instance.message);
  val['nbHits'] = instance.nbHits;
  val['nbPages'] = instance.nbPages;
  writeNotNull('nbSortedHits', instance.nbSortedHits);
  val['page'] = instance.page;
  writeNotNull('redirect', instance.redirect?.toJson());
  writeNotNull('parsedQuery', instance.parsedQuery);
  val['processingTimeMS'] = instance.processingTimeMS;
  writeNotNull('queryAfterRemoval', instance.queryAfterRemoval);
  writeNotNull('serverUsed', instance.serverUsed);
  writeNotNull('userData', instance.userData);
  writeNotNull('renderingContent', instance.renderingContent?.toJson());
  val['hits'] = instance.hits.map((e) => e.toJson()).toList();
  val['query'] = instance.query;
  val['params'] = instance.params;
  writeNotNull('cursor', instance.cursor);
  return val;
}
