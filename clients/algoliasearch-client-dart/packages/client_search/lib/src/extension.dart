import 'package:algolia_search/algolia_search.dart';

extension SearchClientExt on SearchClient {
  /// Perform a search operation targeting one index.
  Future<SearchResponse> searchIndex({
    required String indexName,
    required SearchParamsObject request,
    RequestOptions? requestOptions,
  }) async {
    return searchSingleIndex(
      searchParams: request,
      requestOptions: requestOptions,
      indexName: indexName,
    );
  }

  /// Perform a search operation targeting one index.
  Future<SearchResponses> searchMultiIndex({
    required List<SearchForHits> queries,
    SearchStrategy? strategy,
    RequestOptions? requestOptions,
  }) async {
    final request = SearchMethodParams(requests: queries, strategy: strategy);
    return search(searchMethodParams: request, requestOptions: requestOptions);
  }
}
