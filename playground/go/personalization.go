package main

import (
	"fmt"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/personalization"
)

func testPersonalization(appID, apiKey string) int {
	personalizationClient := personalization.NewClient(appID, apiKey, personalization.US)

	deleteUserProfileResponse, err := personalizationClient.DeleteUserProfile(
		personalizationClient.NewApiDeleteUserProfileRequest("userToken"),
	)
	if err != nil {
		fmt.Printf("request error with DeleteUserProfile: %v\n", err)
		return 1
	}

	printResponse(deleteUserProfileResponse)

	return 0
}
