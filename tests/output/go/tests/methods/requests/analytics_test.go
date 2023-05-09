package tests

import (
	"encoding/json"
	"net/url"
	"testing"

	"github.com/kinbiko/jsonassert"
	"github.com/stretchr/testify/require"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/analytics"
)

func createAnalyticsClient() (*analytics.APIClient, *echoRequester) {
	echo := &echoRequester{}
	cfg := analytics.Configuration{
		AppID:     "appID",
		ApiKey:    "apiKey",
		Region:    analytics.US,
		Requester: echo,
	}
	client := analytics.NewClientWithConfig(cfg)

	return client, echo
}

func TestAnalytics_Del(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow del method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := analytics.ApiDelRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Del(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/minimal")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "DELETE", echo.method)

				require.Nil(t, echo.body)
			},
		},
		{
			name: "allow del method for a custom path with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/all","parameters":{"query":"parameters"}}`
				req := analytics.ApiDelRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Del(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/all")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "DELETE", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"parameters"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_Get(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow get method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := analytics.ApiGetRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Get(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/minimal")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
			},
		},
		{
			name: "allow get method for a custom path with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/all","parameters":{"query":"parameters"}}`
				req := analytics.ApiGetRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Get(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/all")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"parameters"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetAverageClickPosition(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getAverageClickPosition with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetAverageClickPositionRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetAverageClickPosition(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/clicks/averageClickPosition")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getAverageClickPosition with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`
				req := analytics.ApiGetAverageClickPositionRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetAverageClickPosition(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/clicks/averageClickPosition")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetClickPositions(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getClickPositions with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetClickPositionsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetClickPositions(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/clicks/positions")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getClickPositions with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`
				req := analytics.ApiGetClickPositionsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetClickPositions(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/clicks/positions")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetClickThroughRate(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getClickThroughRate with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetClickThroughRateRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetClickThroughRate(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/clicks/clickThroughRate")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getClickThroughRate with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`
				req := analytics.ApiGetClickThroughRateRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetClickThroughRate(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/clicks/clickThroughRate")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetConversationRate(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getConversationRate with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetConversationRateRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetConversationRate(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/conversions/conversionRate")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getConversationRate with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`
				req := analytics.ApiGetConversationRateRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetConversationRate(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/conversions/conversionRate")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetNoClickRate(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getNoClickRate with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetNoClickRateRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetNoClickRate(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/searches/noClickRate")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getNoClickRate with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`
				req := analytics.ApiGetNoClickRateRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetNoClickRate(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/searches/noClickRate")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetNoResultsRate(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getNoResultsRate with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetNoResultsRateRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetNoResultsRate(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/searches/noResultRate")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getNoResultsRate with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`
				req := analytics.ApiGetNoResultsRateRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetNoResultsRate(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/searches/noResultRate")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetSearchesCount(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getSearchesCount with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetSearchesCountRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetSearchesCount(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/searches/count")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getSearchesCount with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`
				req := analytics.ApiGetSearchesCountRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetSearchesCount(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/searches/count")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetSearchesNoClicks(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getSearchesNoClicks with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetSearchesNoClicksRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetSearchesNoClicks(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/searches/noClicks")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getSearchesNoClicks with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","limit":21,"offset":42,"tags":"tag"}`
				req := analytics.ApiGetSearchesNoClicksRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetSearchesNoClicks(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/searches/noClicks")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetSearchesNoResults(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getSearchesNoResults with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetSearchesNoResultsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetSearchesNoResults(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/searches/noResults")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getSearchesNoResults with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","limit":21,"offset":42,"tags":"tag"}`
				req := analytics.ApiGetSearchesNoResultsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetSearchesNoResults(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/searches/noResults")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetStatus(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getStatus with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetStatusRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetStatus(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/status")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetTopCountries(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getTopCountries with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetTopCountriesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTopCountries(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/countries")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getTopCountries with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","limit":21,"offset":42,"tags":"tag"}`
				req := analytics.ApiGetTopCountriesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTopCountries(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/countries")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetTopFilterAttributes(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getTopFilterAttributes with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetTopFilterAttributesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTopFilterAttributes(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/filters")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getTopFilterAttributes with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":21,"offset":42,"tags":"tag"}`
				req := analytics.ApiGetTopFilterAttributesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTopFilterAttributes(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/filters")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetTopFilterForAttribute(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getTopFilterForAttribute with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"attribute":"myAttribute","index":"index"}`
				req := analytics.ApiGetTopFilterForAttributeRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTopFilterForAttribute(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/filters/myAttribute")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getTopFilterForAttribute with minimal parameters and multiple attributes",
			testFunc: func(t *testing.T) {
				parametersStr := `{"attribute":"myAttribute1,myAttribute2","index":"index"}`
				req := analytics.ApiGetTopFilterForAttributeRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTopFilterForAttribute(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/filters/myAttribute1%2CmyAttribute2")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getTopFilterForAttribute with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"attribute":"myAttribute","index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":21,"offset":42,"tags":"tag"}`
				req := analytics.ApiGetTopFilterForAttributeRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTopFilterForAttribute(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/filters/myAttribute")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getTopFilterForAttribute with all parameters and multiple attributes",
			testFunc: func(t *testing.T) {
				parametersStr := `{"attribute":"myAttribute1,myAttribute2","index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":21,"offset":42,"tags":"tag"}`
				req := analytics.ApiGetTopFilterForAttributeRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTopFilterForAttribute(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/filters/myAttribute1%2CmyAttribute2")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetTopFiltersNoResults(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getTopFiltersNoResults with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetTopFiltersNoResultsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTopFiltersNoResults(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/filters/noResults")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getTopFiltersNoResults with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":21,"offset":42,"tags":"tag"}`
				req := analytics.ApiGetTopFiltersNoResultsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTopFiltersNoResults(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/filters/noResults")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetTopHits(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getTopHits with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetTopHitsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTopHits(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/hits")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getTopHits with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index","search":"mySearch","clickAnalytics":true,"startDate":"1999-09-19","endDate":"2001-01-01","limit":21,"offset":42,"tags":"tag"}`
				req := analytics.ApiGetTopHitsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTopHits(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/hits")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","search":"mySearch","clickAnalytics":"true","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetTopSearches(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getTopSearches with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetTopSearchesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTopSearches(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/searches")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getTopSearches with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index","clickAnalytics":true,"startDate":"1999-09-19","endDate":"2001-01-01","orderBy":"searchCount","direction":"asc","limit":21,"offset":42,"tags":"tag"}`
				req := analytics.ApiGetTopSearchesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTopSearches(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/searches")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","clickAnalytics":"true","startDate":"1999-09-19","endDate":"2001-01-01","orderBy":"searchCount","direction":"asc","limit":"21","offset":"42","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_GetUsersCount(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getUsersCount with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index"}`
				req := analytics.ApiGetUsersCountRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetUsersCount(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/users/count")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "get getUsersCount with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`
				req := analytics.ApiGetUsersCountRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetUsersCount(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/2/users/count")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_Post(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow post method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := analytics.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Post(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/minimal")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{}`)
			},
		},
		{
			name: "allow post method for a custom path with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/all","parameters":{"query":"parameters"},"body":{"body":"parameters"}}`
				req := analytics.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Post(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/all")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"body":"parameters"}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"parameters"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "requestOptions can override default query parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/requestOptions","parameters":{"query":"parameters"},"body":{"facet":"filters"}}`
				req := analytics.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []analytics.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"myQueryParameter"}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, analytics.QueryParamOption(k, v))
				}
				_, err := client.Post(req, opts...)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/requestOptions")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"facet":"filters"}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"myQueryParameter"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "requestOptions merges query parameters with default ones",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/requestOptions","parameters":{"query":"parameters"},"body":{"facet":"filters"}}`
				req := analytics.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []analytics.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"query2":"myQueryParameter"}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, analytics.QueryParamOption(k, v))
				}
				_, err := client.Post(req, opts...)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/requestOptions")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"facet":"filters"}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"parameters","query2":"myQueryParameter"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "requestOptions can override default headers",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/requestOptions","parameters":{"query":"parameters"},"body":{"facet":"filters"}}`
				req := analytics.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []analytics.Option
				requestOptionHeaders := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"x-algolia-api-key":"myApiKey"}`), &requestOptionHeaders))
				for k, v := range requestOptionHeaders {
					opts = append(opts, analytics.HeaderParamOption(k, v))
				}
				_, err := client.Post(req, opts...)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/requestOptions")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"facet":"filters"}`)
				headers := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"x-algolia-api-key":"myApiKey"}`), &headers))
				for k, v := range headers {
					require.Equal(t, v, echo.header.Get(k))
				}
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"parameters"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "requestOptions merges headers with default ones",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/requestOptions","parameters":{"query":"parameters"},"body":{"facet":"filters"}}`
				req := analytics.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []analytics.Option
				requestOptionHeaders := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"x-algolia-api-key":"myApiKey"}`), &requestOptionHeaders))
				for k, v := range requestOptionHeaders {
					opts = append(opts, analytics.HeaderParamOption(k, v))
				}
				_, err := client.Post(req, opts...)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/requestOptions")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"facet":"filters"}`)
				headers := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"x-algolia-api-key":"myApiKey"}`), &headers))
				for k, v := range headers {
					require.Equal(t, v, echo.header.Get(k))
				}
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"parameters"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "requestOptions queryParameters accepts booleans",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/requestOptions","parameters":{"query":"parameters"},"body":{"facet":"filters"}}`
				req := analytics.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []analytics.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"isItWorking":true}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, analytics.QueryParamOption(k, v))
				}
				_, err := client.Post(req, opts...)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/requestOptions")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"facet":"filters"}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"parameters","isItWorking":"true"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "requestOptions queryParameters accepts integers",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/requestOptions","parameters":{"query":"parameters"},"body":{"facet":"filters"}}`
				req := analytics.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []analytics.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":2}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, analytics.QueryParamOption(k, v))
				}
				_, err := client.Post(req, opts...)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/requestOptions")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"facet":"filters"}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"parameters","myParam":"2"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "requestOptions queryParameters accepts list of string",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/requestOptions","parameters":{"query":"parameters"},"body":{"facet":"filters"}}`
				req := analytics.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []analytics.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":["c","d"]}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, analytics.QueryParamOption(k, v))
				}
				_, err := client.Post(req, opts...)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/requestOptions")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"facet":"filters"}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"parameters","myParam":"c,d"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "requestOptions queryParameters accepts list of booleans",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/requestOptions","parameters":{"query":"parameters"},"body":{"facet":"filters"}}`
				req := analytics.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []analytics.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":[true,true,false]}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, analytics.QueryParamOption(k, v))
				}
				_, err := client.Post(req, opts...)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/requestOptions")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"facet":"filters"}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"parameters","myParam":"true,true,false"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "requestOptions queryParameters accepts list of integers",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/requestOptions","parameters":{"query":"parameters"},"body":{"facet":"filters"}}`
				req := analytics.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []analytics.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":[1,2]}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, analytics.QueryParamOption(k, v))
				}
				_, err := client.Post(req, opts...)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/requestOptions")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"facet":"filters"}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"parameters","myParam":"1,2"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}

func TestAnalytics_Put(t *testing.T) {
	client, echo := createAnalyticsClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow put method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := analytics.ApiPutRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Put(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/minimal")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{}`)
			},
		},
		{
			name: "allow put method for a custom path with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/all","parameters":{"query":"parameters"},"body":{"body":"parameters"}}`
				req := analytics.ApiPutRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Put(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/test/all")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"body":"parameters"}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"parameters"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
	}
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			test.testFunc(t)
		})
	}
}
