package tests

import (
	"encoding/json"
	"net/url"
	"testing"

	"github.com/kinbiko/jsonassert"
	"github.com/stretchr/testify/require"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/personalization"
)

func createPersonalizationClient() (*personalization.APIClient, *echoRequester) {
	echo := &echoRequester{}
	cfg := personalization.Configuration{
		AppID:     "appID",
		ApiKey:    "apiKey",
		Region:    personalization.US,
		Requester: echo,
	}
	client := personalization.NewClientWithConfig(cfg)

	// so that the linter doesn't complain
	_ = jsonassert.New(nil)

	return client, echo
}

func TestPersonalization_Del(t *testing.T) {
	client, echo := createPersonalizationClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow del method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := personalization.ApiDelRequest{}
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
				req := personalization.ApiDelRequest{}
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

func TestPersonalization_DeleteUserProfile(t *testing.T) {
	client, echo := createPersonalizationClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "delete deleteUserProfile",
			testFunc: func(t *testing.T) {
				parametersStr := `{"userToken":"UserToken"}`
				req := personalization.ApiDeleteUserProfileRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DeleteUserProfile(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/profiles/UserToken")
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

func TestPersonalization_Get(t *testing.T) {
	client, echo := createPersonalizationClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow get method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := personalization.ApiGetRequest{}
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
				req := personalization.ApiGetRequest{}
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

func TestPersonalization_GetPersonalizationStrategy(t *testing.T) {
	client, echo := createPersonalizationClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getPersonalizationStrategy",
			testFunc: func(t *testing.T) {
				_, err := client.GetPersonalizationStrategy()
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/strategies/personalization")
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

func TestPersonalization_GetUserTokenProfile(t *testing.T) {
	client, echo := createPersonalizationClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getUserTokenProfile",
			testFunc: func(t *testing.T) {
				parametersStr := `{"userToken":"UserToken"}`
				req := personalization.ApiGetUserTokenProfileRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetUserTokenProfile(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/profiles/personalization/UserToken")
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

func TestPersonalization_Post(t *testing.T) {
	client, echo := createPersonalizationClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow post method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := personalization.ApiPostRequest{}
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
				req := personalization.ApiPostRequest{}
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
				req := personalization.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []personalization.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"myQueryParameter"}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, personalization.QueryParamOption(k, v))
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
				req := personalization.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []personalization.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"query2":"myQueryParameter"}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, personalization.QueryParamOption(k, v))
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
				req := personalization.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []personalization.Option
				requestOptionHeaders := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"x-algolia-api-key":"myApiKey"}`), &requestOptionHeaders))
				for k, v := range requestOptionHeaders {
					opts = append(opts, personalization.HeaderParamOption(k, v))
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
				req := personalization.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []personalization.Option
				requestOptionHeaders := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"x-algolia-api-key":"myApiKey"}`), &requestOptionHeaders))
				for k, v := range requestOptionHeaders {
					opts = append(opts, personalization.HeaderParamOption(k, v))
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
				req := personalization.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []personalization.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"isItWorking":true}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, personalization.QueryParamOption(k, v))
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
				req := personalization.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []personalization.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":2}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, personalization.QueryParamOption(k, v))
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
				req := personalization.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []personalization.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":["c","d"]}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, personalization.QueryParamOption(k, v))
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
				req := personalization.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []personalization.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":[true,true,false]}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, personalization.QueryParamOption(k, v))
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
				req := personalization.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []personalization.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":[1,2]}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, personalization.QueryParamOption(k, v))
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

func TestPersonalization_Put(t *testing.T) {
	client, echo := createPersonalizationClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow put method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := personalization.ApiPutRequest{}
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
				req := personalization.ApiPutRequest{}
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

func TestPersonalization_SetPersonalizationStrategy(t *testing.T) {
	client, echo := createPersonalizationClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "set setPersonalizationStrategy",
			testFunc: func(t *testing.T) {
				parametersStr := `{"eventScoring":[{"score":42,"eventName":"Algolia","eventType":"Event"}],"facetScoring":[{"score":42,"facetName":"Event"}],"personalizationImpact":42}`
				req := personalization.ApiSetPersonalizationStrategyRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SetPersonalizationStrategy(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/strategies/personalization")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"eventScoring":[{"score":42,"eventName":"Algolia","eventType":"Event"}],"facetScoring":[{"score":42,"facetName":"Event"}],"personalizationImpact":42}`)
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
