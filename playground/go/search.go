package main

import (
	"fmt"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/search"
)

func testSearch(appID, apiKey string) int {
	indexName := getEnvWithDefault("SEARCH_INDEX", "test_index")
	searchClient := search.NewClient(appID, apiKey)

	searchParams := search.SearchParamsStringAsSearchParams(search.NewSearchParamsString(search.WithSearchParamsStringParams("query=jeans&hitsPerPage=2")))
	searchResponse, err := searchClient.SearchSingleIndex(searchClient.NewApiSearchSingleIndexRequest(indexName).WithSearchParams(searchParams))
	if err != nil {
		fmt.Printf("request error with SearchSingleIndex: %v\n", err)
		return 1
	}

	printResponse(searchResponse)

	return 0
}
