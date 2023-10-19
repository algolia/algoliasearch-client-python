import 'package:algolia_client_search/algolia_client_search.dart';

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

  /// Calls the `search` method but with certainty that we will only request
  /// Algolia records (hits).
  Future<Iterable<SearchResponse>> searchForHits({
    required List<SearchForHits> requests,
    SearchStrategy? strategy,
    RequestOptions? requestOptions,
  }) async {
    final request = SearchMethodParams(requests: requests, strategy: strategy);
    return search(searchMethodParams: request, requestOptions: requestOptions)
        .then((res) => res.results.map((e) => SearchResponse.fromJson(e)));
  }

  /// Calls the `search` method but with certainty that we will only request
  /// Algolia facets.
  Future<Iterable<SearchForFacetValuesResponse>> searchForFacets({
    required List<SearchForFacets> requests,
    SearchStrategy? strategy,
    RequestOptions? requestOptions,
  }) async {
    final request = SearchMethodParams(requests: requests, strategy: strategy);
    return search(searchMethodParams: request, requestOptions: requestOptions)
        .then((res) =>
            res.results.map((e) => SearchForFacetValuesResponse.fromJson(e)));
  }
}
