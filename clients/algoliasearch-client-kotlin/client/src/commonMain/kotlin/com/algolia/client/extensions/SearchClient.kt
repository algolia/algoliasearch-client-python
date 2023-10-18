package com.algolia.client.extensions

import com.algolia.client.api.SearchClient
import com.algolia.client.model.search.*
import com.algolia.client.transport.RequestOptions

/**
 * Calls the `search` method but with certainty that we will only request Algolia records (hits).
 */
public suspend fun SearchClient.searchForHits(
    requests: List<SearchForHits>,
    strategy: SearchStrategy? = null,
    requestOptions: RequestOptions? = null,
): List<SearchResponse> {
    val request = SearchMethodParams(requests = requests, strategy = strategy)
    return search(searchMethodParams = request, requestOptions = requestOptions).results.map { it as SearchResponse }
}

/**
 * Calls the `search` method but with certainty that we will only request Algolia facets.
 */
public suspend fun SearchClient.searchForFacets(
    requests: List<SearchForFacets>,
    strategy: SearchStrategy? = null,
    requestOptions: RequestOptions? = null,
): List<SearchForFacetValuesResponse> {
    val request = SearchMethodParams(requests = requests, strategy = strategy)
    return search(
        searchMethodParams = request,
        requestOptions = requestOptions
    ).results.map { it as SearchForFacetValuesResponse }
}
