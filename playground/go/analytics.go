package main

import (
	"fmt"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/analytics"
)

func testAnalytics(appID, apiKey string) int {
	indexName := getEnvWithDefault("ANALYTICS_INDEX", "test_index")
	analyticsClient := analytics.NewClient(appID, apiKey, analytics.US)

	getTopFilterForAttributeResponse, err := analyticsClient.GetTopFilterForAttribute(
		analyticsClient.NewApiGetTopFilterForAttributeRequest("myAttribute1,myAttribute2").WithIndex(indexName),
	)
	if err != nil {
		fmt.Printf("request error with GetTopFilterForAttribute: %v\n", err)
		return 1
	}

	printResponse(getTopFilterForAttributeResponse)

	return 0
}
