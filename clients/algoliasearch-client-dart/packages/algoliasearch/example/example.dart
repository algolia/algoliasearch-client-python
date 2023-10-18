import 'package:algoliasearch/algoliasearch_lite.dart';

void main() async {
  // Creating an instance of the search client with given App ID and API key.
  final client = SearchClient(
    appId: 'latency',
    apiKey: '6be0576ff61c053d5f9a3225e2a90f76',
  );

  // Constructing a query to search for hits in the 'instant_search' index.
  final queryHits = SearchForHits(
    indexName: 'instant_search',
    query: 'a',
    hitsPerPage: 5,
  );
  // Execute the search request.
  final responseHits = await client.searchIndex(request: queryHits);
  // Print the search hits.
  printHits(responseHits);

  // Constructing a request to get query suggestions.
  final querySuggestions = SearchForHits(
    indexName: 'instant_search_demo_query_suggestions',
    query: 'a',
    hitsPerPage: 5,
  );
  // Execute the multi-search request.
  final responseMulti = await client.searchForHits(
    requests: [querySuggestions, queryHits],
  );
  // Decompose the search results into separate results and suggestions.
  final [searchResult, suggestionsResult] = responseMulti.toList();
  // Print the search results and suggestions.
  printQuerySuggestion(searchResult);
  printHits(suggestionsResult);

  // Close the client and dispose of all underlying resources.
  client.dispose();
}

/// Prints the search hits.
void printHits(SearchResponse response) {
  // Print basic search information.
  print(
      "Query: '${response.query}' (${response.nbHits} hits in ${response.processingTimeMS}ms)");
  // Map over the search hits, converting each hit to a product.
  final hits = response.hits.map((e) => product(e));
  // Print each product.
  for (final (name, brand) in hits) {
    print("* $name ($brand)");
  }
}

/// Converts a JSON object into a product tuple of (name, brand).
/// A data class with json deserialization can also be used.
(String, String) product(Map<String, dynamic> json) =>
    (json['name'] as String, json['brand'] as String);

/// Prints query suggestions.
void printQuerySuggestion(SearchResponse response) {
  print("Query suggestions:");
  // Extracting the 'query' fields.
  final suggestions = response.hits.map((e) => e["query"]);
  // Print each suggestion.
  for (String suggestion in suggestions) {
    print("> $suggestion");
  }
}
