package main

import (
	"fmt"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/recommend"
)

func testRecommend(appID, apiKey string) int {
	recommendClient := recommend.NewClient(appID, apiKey)

	/*
		recommend.NewGetRecommendationsParams([]recommend.RecommendationsRequest{
			recommend.RecommendationRequestAsRecommendationsRequest(recommend.NewRecommendationRequest(recommend.RECOMMENDATIONMODELS_BOUGHT_TOGETHER, "test_query", "test_index", 0)),
		})
	*/
	// alternative way to create the payloads, a similar approach can be used with any of the other clients
	params := &recommend.GetRecommendationsParams{
		Requests: []recommend.RecommendationsRequest{
			{
				RecommendationRequest: &recommend.RecommendationRequest{
					Model:     recommend.RECOMMENDATIONMODELS_BOUGHT_TOGETHER,
					ObjectID:  "test_query",
					IndexName: "test_index",
					Threshold: 0,
				},
			},
		},
	}

	searchResponse, err := recommendClient.GetRecommendations(
		recommendClient.NewApiGetRecommendationsRequest(params),
	)
	if err != nil {
		fmt.Printf("request error with SearchSingleIndex: %v\n", err)
		return 1
	}

	printResponse(searchResponse)

	return 0
}
