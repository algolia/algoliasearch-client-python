package main

import (
	"fmt"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/ingestion"
)

func testIngestion(appID, apiKey string) int {
	ingestionClient := ingestion.NewClient(appID, apiKey, ingestion.US)

	listAuthenticationsResponse, err := ingestionClient.GetAuthentications(
		ingestionClient.NewApiGetAuthenticationsRequest().WithItemsPerPage(2),
	)
	if err != nil {
		fmt.Printf("request error with GetAuthentications: %v\n", err)
		return 1
	}

	printResponse(listAuthenticationsResponse)

	return 0
}
