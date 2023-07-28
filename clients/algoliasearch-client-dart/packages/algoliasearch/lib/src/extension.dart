import 'package:algoliasearch/algoliasearch_lite.dart';

extension SearchClientExt on SearchClient {
  /// Perform a search operation targeting one index.
  Future<SearchResponse> searchIndex({
    required SearchForHits request,
    RequestOptions? requestOptions,
  }) async {
    final response = await search(
      searchMethodParams: SearchMethodParams(requests: [request]),
      requestOptions: requestOptions,
    );
    return SearchResponse.fromJson(response.results.first);
  }

  /// Perform a search operation targeting one index.
  Future<Iterable<SearchResponse>> searchMultiIndex({
    required List<SearchForHits> queries,
    SearchStrategy? strategy,
    RequestOptions? requestOptions,
  }) {
    final request = SearchMethodParams(requests: queries, strategy: strategy);
    return search(searchMethodParams: request, requestOptions: requestOptions)
        .then((res) => res.results.map((e) => SearchResponse.fromJson(e)));
  }
}
