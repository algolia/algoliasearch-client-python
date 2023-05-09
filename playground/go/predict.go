package main

import (
	"fmt"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/predict"
)

func testPredict(appID, apiKey string) int {
	predictClient := predict.NewClient(appID, apiKey, predict.US)

	params := predict.AllParamsAsParams(predict.NewAllParams(
		predict.WithAllParamsModelsToRetrieve(predict.AllowedModelsToRetrieveEnumValues),
		predict.WithAllParamsTypesToRetrieve(predict.AllowedTypesToRetrieveEnumValues),
	))
	userProfile, err := predictClient.FetchUserProfile(
		predictClient.NewApiFetchUserProfileRequest("userId").WithParams(&params),
	)
	if err != nil {
		fmt.Printf("request error with FetchUserProfile: %v\n", err)
		return 1
	}

	printResponse(userProfile)

	return 0
}
