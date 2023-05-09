package main

import (
	"context"
	"fmt"
	"time"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/personalization"
)

func testPersonalization(appID, apiKey string) int {
	personalizationClient := personalization.NewClient(appID, apiKey, personalization.US)
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Millisecond)
	defer cancel()

	// it will fail expectedly because of the very short timeout to showcase the context usage.
	deleteUserProfileResponse, err := personalizationClient.DeleteUserProfileWithContext(ctx,
		personalizationClient.NewApiDeleteUserProfileRequest("userToken"),
	)
	if err != nil {
		fmt.Printf("request error with DeleteUserProfile: %v\n", err)
		return 1
	}

	printResponse(deleteUserProfileResponse)

	return 0
}
