package main

import (
	"fmt"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/search"
)

func testSearch(appID, apiKey string) int {
	indexName := getEnvWithDefault("SEARCH_INDEX", "test_index")
	searchClient := search.NewClient(appID, apiKey)

	searchParams := search.SearchParamsStringAsSearchParams(search.NewSearchParamsString(search.WithSearchParamsStringParams("query=jeans&hitsPerPage=2")))
	_, err := searchClient.SearchSingleIndex(searchClient.NewApiSearchSingleIndexRequest(indexName).WithSearchParams(&searchParams))
	if err != nil {
		fmt.Printf("request error with SearchSingleIndex: %v\n", err)
		return 1
	}

	apiKeyStruct := search.NewApiKey([]search.Acl{"search"})

	addApiKeyResponse, err := searchClient.AddApiKey(searchClient.NewApiAddApiKeyRequest(apiKeyStruct))
	if err != nil {
		panic(err)
	}

	taskResponse, err := searchClient.WaitForApiKey(
		addApiKeyResponse.Key,
		apiKeyStruct,
		"add",
		nil,
		nil,
		nil,
	)
	if err != nil {
		panic(err)
	}

	printResponse(taskResponse)

	apiKeyStruct.SetAcl([]search.Acl{"search", "addObject"})

	_, err = searchClient.UpdateApiKey(searchClient.NewApiUpdateApiKeyRequest(addApiKeyResponse.Key, apiKeyStruct))
	if err != nil {
		panic(err)
	}

	taskResponse, err = searchClient.WaitForApiKey(
		addApiKeyResponse.Key,
		apiKeyStruct,
		"update",
		nil,
		nil,
		nil,
	)
	if err != nil {
		panic(err)
	}

	printResponse(taskResponse)

	apiKeyStruct.SetAcl([]search.Acl{"search", "addObject"})

	_, err = searchClient.UpdateApiKey(searchClient.NewApiUpdateApiKeyRequest(addApiKeyResponse.Key, apiKeyStruct))
	if err != nil {
		panic(err)
	}

	taskResponse, err = searchClient.WaitForApiKey(
		addApiKeyResponse.Key,
		apiKeyStruct,
		"update",
		nil,
		nil,
		nil,
	)
	if err != nil {
		panic(err)
	}

	printResponse(taskResponse)

	_, err = searchClient.DeleteApiKey(searchClient.NewApiDeleteApiKeyRequest(addApiKeyResponse.Key))
	if err != nil {
		panic(err)
	}

	taskResponse, err = searchClient.WaitForApiKey(
		addApiKeyResponse.Key,
		apiKeyStruct,
		"delete",
		nil,
		nil,
		nil,
	)
	if err != nil {
		panic(err)
	}

	printResponse(taskResponse)

	return 0
}
