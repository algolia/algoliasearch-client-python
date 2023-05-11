package main

import (
	"fmt"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/insights"
)

func testInsights(appID, apiKey string) int {
	insightsClient := insights.NewClient(appID, apiKey, insights.US)

	events := insights.NewInsightEvents([]insights.InsightEvent{
		*insights.NewInsightEvent("click",
			"myEvent",
			"test_index",
			"myToken",
			insights.WithInsightEventPositions([]int32{1, 2, 3}),
			insights.WithInsightEventQueryID("myQueryID")),
	})
	pushEventsResponse, err := insightsClient.PushEvents(
		insightsClient.NewApiPushEventsRequest(events),
	)
	if err != nil {
		fmt.Printf("request error with PushEvents: %v\n", err)
		return 1
	}

	printResponse(pushEventsResponse)

	return 0
}
