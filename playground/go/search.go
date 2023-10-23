package main

import (
	"fmt"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/search"
)

func testSearch(appID, apiKey string) int {
	indexName := getEnvWithDefault("SEARCH_INDEX", "test_index")
	searchClient := search.NewClient(appID, apiKey)

	response, err := searchClient.AddOrUpdateObject(
		searchClient.NewApiAddOrUpdateObjectRequest(
			indexName,
			"1",
			map[string]interface{}{
				"name": "Foo",
				"age":  42,
				"city": "Paris",
			},
		),
	)
	if err != nil {
		panic(err)
	}

	_, err = searchClient.WaitForTask(
		indexName,
		*response.TaskID,
		nil,
		nil,
		nil,
	)
	if err != nil {
		panic(err)
	}

	searchResponse, err := searchClient.Search(
		searchClient.NewApiSearchRequest(
			search.NewSearchMethodParams(
				[]search.SearchQuery{
					search.SearchForHitsAsSearchQuery(
						search.NewSearchForHits(
							indexName,
							search.WithSearchForHitsQuery("foo"),
						),
					),
				},
			),
		),
	)
	if err != nil {
		panic(err)
	}

	for _, result := range searchResponse.Results {
		fmt.Printf("Result: %v", result.SearchResponse)
	}

	return 0
}
