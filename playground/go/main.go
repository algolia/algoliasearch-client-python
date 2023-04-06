package main

import (
	"flag"
	"fmt"
	"os"

	"github.com/joho/godotenv"
)

func main() {
	fmt.Println("Go playground")
	godotenv.Load("../.env")
	appID := os.Getenv("ALGOLIA_APPLICATION_ID")
	apiKey := os.Getenv("ALGOLIA_ADMIN_KEY")

	var client string
	var returnCode int

	flag.StringVar(&client, "client", "", "client name")
	flag.Parse()

	if client == "" {
		fmt.Println("Please specify a client name")
		os.Exit(1)
	}

	//debug.Enable()

	switch client {
	case "ingestion":
		returnCode = testIngestion(appID, apiKey)
	case "search":
		returnCode = testSearch(appID, apiKey)
	case "analytics":
		returnCode = testAnalytics(appID, apiKey)
	case "insights":
		returnCode = testInsights(appID, apiKey)
	case "personalization":
		returnCode = testPersonalization(appID, apiKey)
	case "predict":
		returnCode = testPredict(appID, apiKey)
	case "query-suggestions":
		returnCode = testQuerySuggestions(appID, apiKey)
	case "recommend":
		returnCode = testRecommend(appID, apiKey)
	default:
		fmt.Println("Please specify a valid client name")
		os.Exit(1)
	}

	os.Exit(returnCode)
}
