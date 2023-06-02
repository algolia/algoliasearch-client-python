import 'package:algolia_client_core/algolia_client_core.dart';

void main() async {
  // Creating an instance of the RetryStrategy with necessary parameters.
  // This will retry the failed requests with a backoff strategy.
  final requester = RetryStrategy.create(
    segment: AgentSegment(value: 'CustomClient'),
    appId: 'latency',
    apiKey: '6be0576ff61c053d5f9a3225e2a90f76',
    defaultHosts: () => [
      Host(url: 'latency-dsn.algolia.net'),
      Host(url: 'latency-1.algolianet.com'),
    ],
  );

  // Executing a GET request on the '/1/indexes/instant_search' endpoint.
  final response = await requester.execute(
    request: ApiRequest(
        method: RequestMethod.get,
        path: '/1/indexes/instant_search',
        queryParams: {'query': 'a', 'hitsPerPage': '5'}),
  );

  // Printing json response.
  print(response);

  // Dispose of the requester to clean up its resources.
  requester.dispose();
}
