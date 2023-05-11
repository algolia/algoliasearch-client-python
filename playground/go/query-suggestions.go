package main

import (
	"fmt"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/query-suggestions"
)

func testQuerySuggestions(appID, apiKey string) int {
	suggestionsClient := suggestions.NewClient(appID, apiKey, suggestions.US)

	// if there is no params for the requests, we don't need to give empty request instance such as `suggestionsClient.NewApiGetAllConfigsRequest()`.
	querySuggestionsIndex, err := suggestionsClient.GetAllConfigs()
	if err != nil {
		fmt.Printf("request error with GetAllConfigs: %v\n", err)
		return 1
	}

	printResponse(querySuggestionsIndex)

	return 0
}
