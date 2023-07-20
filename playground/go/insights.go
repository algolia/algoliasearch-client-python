package main

import (
	"fmt"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/insights"
)

func testInsights(appID, apiKey string) int {
	insightsClient := insights.NewClient(appID, apiKey, insights.US)

	events := insights.NewInsightsEvents([]insights.EventsItems{
		insights.ClickedObjectIDsAsEventsItems(insights.NewClickedObjectIDs("myEvent",
			insights.CLICKEVENT_CLICK,
			"test_index",
			[]string{"myObjectID"},
			"myToken",
			insights.WithClickedObjectIDsTimestamp(1234567890))),
	})
	eventsResponse, err := insightsClient.PushEvents(
		insightsClient.NewApiPushEventsRequest(events),
	)
	if err != nil {
		fmt.Printf("request error with PushEvents: %v\n", err)
		return 1
	}

	printResponse(eventsResponse)

	return 0
}
