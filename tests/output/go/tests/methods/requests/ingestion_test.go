package tests

import (
	"encoding/json"
	"net/url"
	"testing"

	"github.com/kinbiko/jsonassert"
	"github.com/stretchr/testify/require"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/ingestion"
)

func createIngestionClient() (*ingestion.APIClient, *echoRequester) {
	echo := &echoRequester{}
	cfg := ingestion.Configuration{
		AppID:     "appID",
		ApiKey:    "apiKey",
		Region:    ingestion.US,
		Requester: echo,
	}
	client := ingestion.NewClientWithConfig(cfg)

	// so that the linter doesn't complain
	_ = jsonassert.New(nil)

	return client, echo
}

func TestIngestion_CreateAuthentication(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "createAuthenticationOAuth",
			testFunc: func(t *testing.T) {
				parametersStr := `{"type":"oauth","name":"authName","input":{"url":"http://test.oauth","client_id":"myID","client_secret":"mySecret"}}`
				req := ingestion.ApiCreateAuthenticationRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.CreateAuthentication(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/authentications")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"type":"oauth","name":"authName","input":{"url":"http://test.oauth","client_id":"myID","client_secret":"mySecret"}}`)
			},
		},
		{
			name: "createAuthenticationAlgolia",
			testFunc: func(t *testing.T) {
				parametersStr := `{"type":"algolia","name":"authName","input":{"appID":"myappID","apiKey":"randomApiKey"}}`
				req := ingestion.ApiCreateAuthenticationRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.CreateAuthentication(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/authentications")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"type":"algolia","name":"authName","input":{"appID":"myappID","apiKey":"randomApiKey"}}`)
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

func TestIngestion_CreateDestination(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "createDestination",
			testFunc: func(t *testing.T) {
				parametersStr := `{"type":"search","name":"destinationName","input":{"indexPrefix":"prefix_"},"authenticationID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`
				req := ingestion.ApiCreateDestinationRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.CreateDestination(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/destinations")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"type":"search","name":"destinationName","input":{"indexPrefix":"prefix_"},"authenticationID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`)
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

func TestIngestion_CreateSource(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "createSource",
			testFunc: func(t *testing.T) {
				parametersStr := `{"type":"commercetools","name":"sourceName","input":{"storeKeys":["myStore"],"locales":["de"],"url":"http://commercetools.com","projectKey":"keyID"},"authenticationID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`
				req := ingestion.ApiCreateSourceRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.CreateSource(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/sources")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"type":"commercetools","name":"sourceName","input":{"storeKeys":["myStore"],"locales":["de"],"url":"http://commercetools.com","projectKey":"keyID"},"authenticationID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`)
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

func TestIngestion_CreateTask(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "createTaskOnDemand",
			testFunc: func(t *testing.T) {
				parametersStr := `{"sourceID":"search","destinationID":"destinationName","trigger":{"type":"onDemand"},"action":"replace"}`
				req := ingestion.ApiCreateTaskRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.CreateTask(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/tasks")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"sourceID":"search","destinationID":"destinationName","trigger":{"type":"onDemand"},"action":"replace"}`)
			},
		},
		{
			name: "createTaskSchedule",
			testFunc: func(t *testing.T) {
				parametersStr := `{"sourceID":"search","destinationID":"destinationName","trigger":{"type":"schedule","cron":"* * * * *"},"action":"replace"}`
				req := ingestion.ApiCreateTaskRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.CreateTask(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/tasks")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"sourceID":"search","destinationID":"destinationName","trigger":{"type":"schedule","cron":"* * * * *"},"action":"replace"}`)
			},
		},
		{
			name: "createTaskSubscription",
			testFunc: func(t *testing.T) {
				parametersStr := `{"sourceID":"search","destinationID":"destinationName","trigger":{"type":"onDemand"},"action":"replace"}`
				req := ingestion.ApiCreateTaskRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.CreateTask(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/tasks")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"sourceID":"search","destinationID":"destinationName","trigger":{"type":"onDemand"},"action":"replace"}`)
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

func TestIngestion_Del(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow del method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := ingestion.ApiDelRequest{}
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
				req := ingestion.ApiDelRequest{}
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

func TestIngestion_DeleteAuthentication(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "deleteAuthentication",
			testFunc: func(t *testing.T) {
				parametersStr := `{"authenticationID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`
				req := ingestion.ApiDeleteAuthenticationRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DeleteAuthentication(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/authentications/6c02aeb1-775e-418e-870b-1faccd4b2c0f")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "DELETE", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_DeleteDestination(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "deleteDestination",
			testFunc: func(t *testing.T) {
				parametersStr := `{"destinationID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`
				req := ingestion.ApiDeleteDestinationRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DeleteDestination(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/destinations/6c02aeb1-775e-418e-870b-1faccd4b2c0f")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "DELETE", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_DeleteSource(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "deleteSource",
			testFunc: func(t *testing.T) {
				parametersStr := `{"sourceID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`
				req := ingestion.ApiDeleteSourceRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DeleteSource(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/sources/6c02aeb1-775e-418e-870b-1faccd4b2c0f")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "DELETE", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_DeleteTask(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "deleteTask",
			testFunc: func(t *testing.T) {
				parametersStr := `{"taskID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`
				req := ingestion.ApiDeleteTaskRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DeleteTask(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/tasks/6c02aeb1-775e-418e-870b-1faccd4b2c0f")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "DELETE", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_DisableTask(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "disableTask",
			testFunc: func(t *testing.T) {
				parametersStr := `{"taskID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`
				req := ingestion.ApiDisableTaskRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DisableTask(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/tasks/6c02aeb1-775e-418e-870b-1faccd4b2c0f/disable")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				require.Empty(t, echo.body)
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

func TestIngestion_EnableTask(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "enableTask",
			testFunc: func(t *testing.T) {
				parametersStr := `{"taskID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`
				req := ingestion.ApiEnableTaskRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.EnableTask(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/tasks/6c02aeb1-775e-418e-870b-1faccd4b2c0f/enable")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				require.Empty(t, echo.body)
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

func TestIngestion_Get(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow get method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := ingestion.ApiGetRequest{}
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
				req := ingestion.ApiGetRequest{}
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

func TestIngestion_GetAuthentication(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getAuthentication",
			testFunc: func(t *testing.T) {
				parametersStr := `{"authenticationID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`
				req := ingestion.ApiGetAuthenticationRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetAuthentication(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/authentications/6c02aeb1-775e-418e-870b-1faccd4b2c0f")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_GetAuthentications(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getAuthentications",
			testFunc: func(t *testing.T) {
				parametersStr := `{}`
				req := ingestion.ApiGetAuthenticationsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetAuthentications(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/authentications")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_GetDestination(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getDestination",
			testFunc: func(t *testing.T) {
				parametersStr := `{"destinationID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`
				req := ingestion.ApiGetDestinationRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetDestination(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/destinations/6c02aeb1-775e-418e-870b-1faccd4b2c0f")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_GetDestinations(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getDestinations",
			testFunc: func(t *testing.T) {
				parametersStr := `{}`
				req := ingestion.ApiGetDestinationsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetDestinations(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/destinations")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_GetEvent(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getEvent",
			testFunc: func(t *testing.T) {
				parametersStr := `{"runID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f","eventID":"6c02aeb1-775e-418e-870b-1faccd4b2c0c"}`
				req := ingestion.ApiGetEventRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetEvent(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/runs/6c02aeb1-775e-418e-870b-1faccd4b2c0f/events/6c02aeb1-775e-418e-870b-1faccd4b2c0c")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_GetEvents(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getEvents",
			testFunc: func(t *testing.T) {
				parametersStr := `{"runID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`
				req := ingestion.ApiGetEventsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetEvents(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/runs/6c02aeb1-775e-418e-870b-1faccd4b2c0f/events")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_GetRun(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getRun",
			testFunc: func(t *testing.T) {
				parametersStr := `{"runID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`
				req := ingestion.ApiGetRunRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetRun(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/runs/6c02aeb1-775e-418e-870b-1faccd4b2c0f")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_GetRuns(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getRuns",
			testFunc: func(t *testing.T) {
				parametersStr := `{}`
				req := ingestion.ApiGetRunsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetRuns(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/runs")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_GetSource(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getSource",
			testFunc: func(t *testing.T) {
				parametersStr := `{"sourceID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`
				req := ingestion.ApiGetSourceRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetSource(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/sources/6c02aeb1-775e-418e-870b-1faccd4b2c0f")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_GetSources(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getSources",
			testFunc: func(t *testing.T) {
				parametersStr := `{}`
				req := ingestion.ApiGetSourcesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetSources(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/sources")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_GetTask(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getTask",
			testFunc: func(t *testing.T) {
				parametersStr := `{"taskID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`
				req := ingestion.ApiGetTaskRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTask(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/tasks/6c02aeb1-775e-418e-870b-1faccd4b2c0f")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_GetTasks(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getTasks",
			testFunc: func(t *testing.T) {
				parametersStr := `{}`
				req := ingestion.ApiGetTasksRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTasks(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/tasks")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
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

func TestIngestion_Post(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow post method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := ingestion.ApiPostRequest{}
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
				req := ingestion.ApiPostRequest{}
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
				req := ingestion.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []ingestion.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"myQueryParameter"}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, ingestion.QueryParamOption(k, v))
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
				req := ingestion.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []ingestion.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"query2":"myQueryParameter"}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, ingestion.QueryParamOption(k, v))
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
				req := ingestion.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []ingestion.Option
				requestOptionHeaders := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"x-algolia-api-key":"myApiKey"}`), &requestOptionHeaders))
				for k, v := range requestOptionHeaders {
					opts = append(opts, ingestion.HeaderParamOption(k, v))
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
				req := ingestion.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []ingestion.Option
				requestOptionHeaders := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"x-algolia-api-key":"myApiKey"}`), &requestOptionHeaders))
				for k, v := range requestOptionHeaders {
					opts = append(opts, ingestion.HeaderParamOption(k, v))
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
				req := ingestion.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []ingestion.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"isItWorking":true}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, ingestion.QueryParamOption(k, v))
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
				req := ingestion.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []ingestion.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":2}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, ingestion.QueryParamOption(k, v))
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
				req := ingestion.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []ingestion.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":["c","d"]}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, ingestion.QueryParamOption(k, v))
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
				req := ingestion.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []ingestion.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":[true,true,false]}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, ingestion.QueryParamOption(k, v))
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
				req := ingestion.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []ingestion.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":[1,2]}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, ingestion.QueryParamOption(k, v))
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

func TestIngestion_Put(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow put method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := ingestion.ApiPutRequest{}
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
				req := ingestion.ApiPutRequest{}
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

func TestIngestion_RunTask(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "runTask",
			testFunc: func(t *testing.T) {
				parametersStr := `{"taskID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f"}`
				req := ingestion.ApiRunTaskRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.RunTask(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/tasks/6c02aeb1-775e-418e-870b-1faccd4b2c0f/run")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				require.Empty(t, echo.body)
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

func TestIngestion_SearchAuthentications(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "searchAuthentications",
			testFunc: func(t *testing.T) {
				parametersStr := `{"authenticationIDs":["6c02aeb1-775e-418e-870b-1faccd4b2c0f","947ac9c4-7e58-4c87-b1e7-14a68e99699a"]}`
				req := ingestion.ApiSearchAuthenticationsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SearchAuthentications(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/authentications/search")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"authenticationIDs":["6c02aeb1-775e-418e-870b-1faccd4b2c0f","947ac9c4-7e58-4c87-b1e7-14a68e99699a"]}`)
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

func TestIngestion_SearchDestinations(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "searchDestinations",
			testFunc: func(t *testing.T) {
				parametersStr := `{"destinationIDs":["6c02aeb1-775e-418e-870b-1faccd4b2c0f","947ac9c4-7e58-4c87-b1e7-14a68e99699a"]}`
				req := ingestion.ApiSearchDestinationsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SearchDestinations(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/destinations/search")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"destinationIDs":["6c02aeb1-775e-418e-870b-1faccd4b2c0f","947ac9c4-7e58-4c87-b1e7-14a68e99699a"]}`)
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

func TestIngestion_SearchSources(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "searchSources",
			testFunc: func(t *testing.T) {
				parametersStr := `{"sourceIDs":["6c02aeb1-775e-418e-870b-1faccd4b2c0f","947ac9c4-7e58-4c87-b1e7-14a68e99699a"]}`
				req := ingestion.ApiSearchSourcesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SearchSources(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/sources/search")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"sourceIDs":["6c02aeb1-775e-418e-870b-1faccd4b2c0f","947ac9c4-7e58-4c87-b1e7-14a68e99699a"]}`)
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

func TestIngestion_SearchTasks(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "searchTasks",
			testFunc: func(t *testing.T) {
				parametersStr := `{"taskIDs":["6c02aeb1-775e-418e-870b-1faccd4b2c0f","947ac9c4-7e58-4c87-b1e7-14a68e99699a"]}`
				req := ingestion.ApiSearchTasksRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SearchTasks(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/tasks/search")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"taskIDs":["6c02aeb1-775e-418e-870b-1faccd4b2c0f","947ac9c4-7e58-4c87-b1e7-14a68e99699a"]}`)
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

func TestIngestion_UpdateAuthentication(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "updateAuthentication",
			testFunc: func(t *testing.T) {
				parametersStr := `{"authenticationID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f","authenticationUpdate":{"name":"newName"}}`
				req := ingestion.ApiUpdateAuthenticationRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.UpdateAuthentication(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/authentications/6c02aeb1-775e-418e-870b-1faccd4b2c0f")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PATCH", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"name":"newName"}`)
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

func TestIngestion_UpdateDestination(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "updateDestination",
			testFunc: func(t *testing.T) {
				parametersStr := `{"destinationID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f","destinationUpdate":{"name":"newName"}}`
				req := ingestion.ApiUpdateDestinationRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.UpdateDestination(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/destinations/6c02aeb1-775e-418e-870b-1faccd4b2c0f")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PATCH", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"name":"newName"}`)
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

func TestIngestion_UpdateSource(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "updateSource",
			testFunc: func(t *testing.T) {
				parametersStr := `{"sourceID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f","sourceUpdate":{"name":"newName"}}`
				req := ingestion.ApiUpdateSourceRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.UpdateSource(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/sources/6c02aeb1-775e-418e-870b-1faccd4b2c0f")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PATCH", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"name":"newName"}`)
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

func TestIngestion_UpdateTask(t *testing.T) {
	client, echo := createIngestionClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "updateTask",
			testFunc: func(t *testing.T) {
				parametersStr := `{"taskID":"6c02aeb1-775e-418e-870b-1faccd4b2c0f","taskUpdate":{"enabled":false}}`
				req := ingestion.ApiUpdateTaskRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.UpdateTask(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/tasks/6c02aeb1-775e-418e-870b-1faccd4b2c0f")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PATCH", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"enabled":false}`)
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
