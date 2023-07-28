import 'package:algolia_client_search/algolia_client_search.dart';

void main() async {
  // Creating an instance of the search client with the provided App ID and API key.
  final client = SearchClient(
    appId: 'latency',
    apiKey: '6be0576ff61c053d5f9a3225e2a90f76',
  );

  // Constructing a query to search for hits in the 'instant_search' index.
  final queryHits = SearchParamsObject(
    query: 'a',
    hitsPerPage: 5,
  );
  // Execute the search request.
  final responseHits = await client.searchSingleIndex(
    indexName: 'instant_search',
    searchParams: queryHits,
  );
  // Print the search hits.
  printHits(responseHits);

  // Constructing a request to search for facet values in the 'instant_search' index.
  final responseFacets = await client.searchForFacetValues(
    indexName: 'instant_search',
    facetName: 'categories',
    searchForFacetValuesRequest: SearchForFacetValuesRequest(maxFacetHits: 5),
  );
  // Print the facet values.
  printFacets(responseFacets);

  // Close the client and dispose of all underlying resources.
  client.dispose();
}

/// Prints the search hits.
void printHits(SearchResponse response) {
  print(
      "Query: '${response.query}' (${response.nbHits} hits in ${response.processingTimeMS}ms)");
  // Map over the search hits, converting each hit to a product.
  final hits = response.hits.map((e) => product(e));
  for (final (name, brand) in hits) {
    print("* $name ($brand)");
  }
}

/// Converts a JSON object into a product tuple of (name, brand).
/// A data class with json deserialization can also be used.
(String, String) product(Map<String, dynamic> json) =>
    (json['name'] as String, json['brand'] as String);

/// Prints the facet values.
void printFacets(SearchForFacetValuesResponse response) {
  print("Facets:");
  for (FacetHits facetHits in response.facetHits) {
    print("> ${facetHits.value} (${facetHits.count})");
  }
}
