import 'package:algolia_client_core/algolia_client_core.dart';
import 'package:algolia_search_lite/src/api/search_client.dart';
import 'package:algolia_search_lite/src/model/search_for_hits.dart';
import 'package:algolia_search_lite/src/model/search_method_params.dart';
import 'package:algolia_search_lite/src/model/search_response.dart';
import 'package:algolia_search_lite/src/model/search_responses.dart';
import 'package:algolia_search_lite/src/model/search_strategy.dart';

extension SearchClientExt on SearchClient {
  /// Perform a search operation targeting one index.
  Future<SearchResponse> searchIndex({
    required SearchForHits request,
    RequestOptions? requestOptions,
  }) async {
    final params = SearchMethodParams(requests: [request]);
    final responses = await search(
      searchMethodParams: params,
      requestOptions: requestOptions,
    );
    return responses.results.first;
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
