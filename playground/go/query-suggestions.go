package main

import (
	"fmt"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/query-suggestions"
)

func testQuerySuggestions(appID, apiKey string) int {
	suggestionsClient := suggestions.NewClient(appID, apiKey, suggestions.US)

	querySuggestionsIndex, err := suggestionsClient.GetAllConfigs(
		suggestionsClient.NewApiGetAllConfigsRequest(),
	)
	if err != nil {
		fmt.Printf("request error with GetAllConfigs: %v\n", err)
		return 1
	}

	printResponse(querySuggestionsIndex)

	return 0
}
