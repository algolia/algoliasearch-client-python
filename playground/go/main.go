package main

import (
	"fmt"
	"os"

	"github.com/joho/godotenv"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/ingestion"
	"github.com/algolia/algoliasearch-client-go/v4/algolia/search"
)

func main() {
	fmt.Println("Go playground")
	godotenv.Load("../.env")
	appID := os.Getenv("ALGOLIA_APPLICATION_ID")
	apiKey := os.Getenv("ALGOLIA_ADMIN_KEY")

	//debug.Enable()

	// ingestion
	ingestionClient := ingestion.NewClient(appID, apiKey, ingestion.US)

	auths, err := ingestionClient.GetAuthentications(
		ingestionClient.NewApiGetAuthenticationsRequest().WithItemsPerPage(2),
		ingestion.QueryParamOption("myQueryParam1", "myQueryParamValue1"),
		ingestion.HeaderParamOption("myHeaderParam1", "myHeaderParamValue2"),
	)
	fmt.Println(auths, err)

	// search
	indexName := "test_index"
	searchClient := search.NewClient(appID, apiKey)

	searchParams := search.SearchParamsStringAsSearchParams(search.NewSearchParamsString(search.WithSearchParamsStringParams("query=jeans&hitsPerPage=2")))
	searchRes, err := searchClient.SearchSingleIndex(searchClient.NewApiSearchSingleIndexRequest(indexName).WithSearchParams(searchParams))
	fmt.Println(searchRes, err)
}
