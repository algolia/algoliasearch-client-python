package main

import (
	"fmt"
	"time"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/ingestion"
)

func testIngestion(appID, apiKey string) int {
	ingestionClient := ingestion.NewClient(appID, apiKey, ingestion.US)

	// another example to generate payload for a request.
	createAuthenticationResponse, err := ingestionClient.CreateAuthentication(ingestionClient.NewApiCreateAuthenticationRequest(
		&ingestion.AuthenticationCreate{
			Type: ingestion.AUTHENTICATIONTYPE_BASIC,
			Name: fmt.Sprintf("my-authentication-%d", time.Now().Unix()),
			Input: ingestion.AuthInput{
				AuthBasic: &ingestion.AuthBasic{
					Username: "username",
					Password: "password",
				},
			},
		}))

	if err != nil {
		fmt.Printf("request error with CreateAuthentication: %v\n", err)
		return 1
	}

	printResponse(createAuthenticationResponse)

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
