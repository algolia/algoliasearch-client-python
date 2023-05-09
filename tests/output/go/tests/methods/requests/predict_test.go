package tests

import (
	"encoding/json"
	"net/url"
	"testing"

	"github.com/kinbiko/jsonassert"
	"github.com/stretchr/testify/require"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/predict"
)

func createPredictClient() (*predict.APIClient, *echoRequester) {
	echo := &echoRequester{}
	cfg := predict.Configuration{
		AppID:     "appID",
		ApiKey:    "apiKey",
		Region:    predict.EU,
		Requester: echo,
	}
	client := predict.NewClientWithConfig(cfg)

	return client, echo
}

func TestPredict_ActivateModelInstance(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "activate a model instance",
			testFunc: func(t *testing.T) {
				parametersStr := `{"type":"funnel_stage","name":"Shopping stage for EU users","sourceID":"0200030-129930","index":"Products Production","modelAttributes":[]}`
				req := predict.ApiActivateModelInstanceRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.ActivateModelInstance(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/predict/models")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"type":"funnel_stage","name":"Shopping stage for EU users","sourceID":"0200030-129930","index":"Products Production","modelAttributes":[]}`)
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

func TestPredict_CreateSegment(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "create segment with required params",
			testFunc: func(t *testing.T) {
				t.Skip("skipping test for go client")
				parametersStr := `{"name":"segment1","conditions":{"operator":"AND","operands":[{"name":"predictions.order_value","filters":[{"operator":"GT","value":200}]}]}}`
				req := predict.ApiCreateSegmentRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.CreateSegment(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"name":"segment1","conditions":{"operator":"AND","operands":[{"name":"predictions.order_value","filters":[{"operator":"GT","value":200}]}]}}`)
			},
		},
		{
			name: "create segment with filter probability",
			testFunc: func(t *testing.T) {
				parametersStr := `{"name":"segment1","conditions":{"operator":"AND","operands":[{"name":"predictions.affinities.color","filters":[{"operator":"EQ","value":"red","probability":{"GTE":0.5,"LTE":1}}]}]}}`
				req := predict.ApiCreateSegmentRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.CreateSegment(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"name":"segment1","conditions":{"operator":"AND","operands":[{"name":"predictions.affinities.color","filters":[{"operator":"EQ","value":"red","probability":{"GTE":0.5,"LTE":1}}]}]}}`)
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

func TestPredict_Del(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow del method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := predict.ApiDelRequest{}
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
				req := predict.ApiDelRequest{}
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

func TestPredict_DeleteModelInstance(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "delete a model instance",
			testFunc: func(t *testing.T) {
				parametersStr := `{"modelID":"model1"}`
				req := predict.ApiDeleteModelInstanceRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DeleteModelInstance(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/predict/models/model1")
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

func TestPredict_DeleteSegment(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "delete a segments configuration",
			testFunc: func(t *testing.T) {
				parametersStr := `{"segmentID":"segment1"}`
				req := predict.ApiDeleteSegmentRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DeleteSegment(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments/segment1")
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

func TestPredict_DeleteUserProfile(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "deleteUserProfile",
			testFunc: func(t *testing.T) {
				parametersStr := `{"userID":"user1"}`
				req := predict.ApiDeleteUserProfileRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DeleteUserProfile(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/users/user1")
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

func TestPredict_FetchAllSegments(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "fetchAllSegments with no segmentType",
			testFunc: func(t *testing.T) {
				parametersStr := `{}`
				req := predict.ApiFetchAllSegmentsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.FetchAllSegments(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
			},
		},
		{
			name: "fetchAllSegments with segmentType custom",
			testFunc: func(t *testing.T) {
				parametersStr := `{"type":"custom"}`
				req := predict.ApiFetchAllSegmentsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.FetchAllSegments(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"type":"custom"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "fetchAllSegments with segmentType computed",
			testFunc: func(t *testing.T) {
				parametersStr := `{"type":"computed"}`
				req := predict.ApiFetchAllSegmentsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.FetchAllSegments(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"type":"computed"}`), &queryParams))
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

func TestPredict_FetchAllUserProfiles(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "fetchAllUserProfiles with minimal parameters for modelsToRetrieve",
			testFunc: func(t *testing.T) {
				parametersStr := `{"modelsToRetrieve":["funnel_stage","order_value","affinities"]}`
				req := predict.ApiFetchAllUserProfilesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.FetchAllUserProfiles(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/users")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"modelsToRetrieve":["funnel_stage","order_value","affinities"]}`)
			},
		},
		{
			name: "fetchAllUserProfiles with minimal parameters for typesToRetrieve",
			testFunc: func(t *testing.T) {
				parametersStr := `{"typesToRetrieve":["properties","segments"]}`
				req := predict.ApiFetchAllUserProfilesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.FetchAllUserProfiles(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/users")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"typesToRetrieve":["properties","segments"]}`)
			},
		},
		{
			name: "fetchAllUserProfiles with a limit",
			testFunc: func(t *testing.T) {
				parametersStr := `{"limit":10}`
				req := predict.ApiFetchAllUserProfilesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.FetchAllUserProfiles(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/users")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"limit":10}`)
			},
		},
		{
			name: "fetchAllUserProfiles with a nextPageToken",
			testFunc: func(t *testing.T) {
				parametersStr := `{"nextPageToken":"nextPageTokenExample123"}`
				req := predict.ApiFetchAllUserProfilesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.FetchAllUserProfiles(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/users")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"nextPageToken":"nextPageTokenExample123"}`)
			},
		},
		{
			name: "fetchAllUserProfiles with a previousPageToken",
			testFunc: func(t *testing.T) {
				parametersStr := `{"previousPageToken":"previousPageTokenExample123"}`
				req := predict.ApiFetchAllUserProfilesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.FetchAllUserProfiles(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/users")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"previousPageToken":"previousPageTokenExample123"}`)
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

func TestPredict_FetchSegment(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "fetchSegment with user ID",
			testFunc: func(t *testing.T) {
				parametersStr := `{"segmentID":"segment1"}`
				req := predict.ApiFetchSegmentRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.FetchSegment(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments/segment1")
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

func TestPredict_FetchUserProfile(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "fetchUserProfile with minimal parameters for modelsToRetrieve",
			testFunc: func(t *testing.T) {
				parametersStr := `{"userID":"user1","params":{"modelsToRetrieve":["funnel_stage","order_value","affinities"]}}`
				req := predict.ApiFetchUserProfileRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.FetchUserProfile(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/users/user1/fetch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"modelsToRetrieve":["funnel_stage","order_value","affinities"]}`)
			},
		},
		{
			name: "fetchUserProfile with minimal parameters for typesToRetrieve",
			testFunc: func(t *testing.T) {
				parametersStr := `{"userID":"user1","params":{"typesToRetrieve":["properties","segments"]}}`
				req := predict.ApiFetchUserProfileRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.FetchUserProfile(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/users/user1/fetch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"typesToRetrieve":["properties","segments"]}`)
			},
		},
		{
			name: "fetchUserProfile with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"userID":"user1","params":{"modelsToRetrieve":["funnel_stage","order_value","affinities"],"typesToRetrieve":["properties","segments"]}}`
				req := predict.ApiFetchUserProfileRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.FetchUserProfile(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/users/user1/fetch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"modelsToRetrieve":["funnel_stage","order_value","affinities"],"typesToRetrieve":["properties","segments"]}`)
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

func TestPredict_Get(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow get method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := predict.ApiGetRequest{}
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
				req := predict.ApiGetRequest{}
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

func TestPredict_GetAvailableModelTypes(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get available model types",
			testFunc: func(t *testing.T) {
				parametersStr := `{}`
				req := predict.ApiGetAvailableModelTypesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetAvailableModelTypes(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/predict/modeltypes")
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

func TestPredict_GetModelInstanceConfig(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get configurations for a model instance",
			testFunc: func(t *testing.T) {
				parametersStr := `{"modelID":"model1"}`
				req := predict.ApiGetModelInstanceConfigRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetModelInstanceConfig(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/predict/models/model1")
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

func TestPredict_GetModelInstances(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get a list of model instances",
			testFunc: func(t *testing.T) {
				parametersStr := `{}`
				req := predict.ApiGetModelInstancesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetModelInstances(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/predict/models")
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

func TestPredict_GetModelMetrics(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get metrics for a model instance",
			testFunc: func(t *testing.T) {
				parametersStr := `{"modelID":"model1"}`
				req := predict.ApiGetModelMetricsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetModelMetrics(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/predict/models/model1/metrics")
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

func TestPredict_GetSegmentUsers(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getSegmentUsers with minimal parameters for modelsToRetrieve",
			testFunc: func(t *testing.T) {
				parametersStr := `{"segmentID":"segmentID1","fetchAllUserProfilesParams":{"modelsToRetrieve":["funnel_stage"]}}`
				req := predict.ApiGetSegmentUsersRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetSegmentUsers(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments/segmentID1/users")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"modelsToRetrieve":["funnel_stage"]}`)
			},
		},
		{
			name: "getSegmentUsers with minimal parameters for typesToRetrieve",
			testFunc: func(t *testing.T) {
				parametersStr := `{"segmentID":"segmentID1","fetchAllUserProfilesParams":{"typesToRetrieve":["properties"]}}`
				req := predict.ApiGetSegmentUsersRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetSegmentUsers(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments/segmentID1/users")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"typesToRetrieve":["properties"]}`)
			},
		},
		{
			name: "getSegmentUsers with a limit",
			testFunc: func(t *testing.T) {
				parametersStr := `{"segmentID":"segmentID1","fetchAllUserProfilesParams":{"limit":10}}`
				req := predict.ApiGetSegmentUsersRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetSegmentUsers(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments/segmentID1/users")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"limit":10}`)
			},
		},
		{
			name: "getSegmentUsers with a nextPageToken",
			testFunc: func(t *testing.T) {
				parametersStr := `{"segmentID":"segmentID1","fetchAllUserProfilesParams":{"nextPageToken":"nextPageTokenExample123"}}`
				req := predict.ApiGetSegmentUsersRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetSegmentUsers(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments/segmentID1/users")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"nextPageToken":"nextPageTokenExample123"}`)
			},
		},
		{
			name: "getSegmentUsers with a previousPageToken",
			testFunc: func(t *testing.T) {
				parametersStr := `{"segmentID":"segmentID1","fetchAllUserProfilesParams":{"previousPageToken":"previousPageTokenExample123"}}`
				req := predict.ApiGetSegmentUsersRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetSegmentUsers(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments/segmentID1/users")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"previousPageToken":"previousPageTokenExample123"}`)
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

func TestPredict_Post(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow post method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := predict.ApiPostRequest{}
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
				req := predict.ApiPostRequest{}
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
				req := predict.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []predict.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"myQueryParameter"}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, predict.QueryParamOption(k, v))
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
				req := predict.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []predict.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"query2":"myQueryParameter"}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, predict.QueryParamOption(k, v))
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
				req := predict.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []predict.Option
				requestOptionHeaders := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"x-algolia-api-key":"myApiKey"}`), &requestOptionHeaders))
				for k, v := range requestOptionHeaders {
					opts = append(opts, predict.HeaderParamOption(k, v))
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
				req := predict.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []predict.Option
				requestOptionHeaders := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"x-algolia-api-key":"myApiKey"}`), &requestOptionHeaders))
				for k, v := range requestOptionHeaders {
					opts = append(opts, predict.HeaderParamOption(k, v))
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
				req := predict.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []predict.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"isItWorking":true}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, predict.QueryParamOption(k, v))
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
				req := predict.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []predict.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":2}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, predict.QueryParamOption(k, v))
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
				req := predict.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []predict.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":["c","d"]}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, predict.QueryParamOption(k, v))
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
				req := predict.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []predict.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":[true,true,false]}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, predict.QueryParamOption(k, v))
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
				req := predict.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []predict.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":[1,2]}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, predict.QueryParamOption(k, v))
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

func TestPredict_Put(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow put method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := predict.ApiPutRequest{}
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
				req := predict.ApiPutRequest{}
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

func TestPredict_UpdateModelInstance(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "update a model instance",
			testFunc: func(t *testing.T) {
				parametersStr := `{"modelID":"model1","updateModelParams":{"name":"Shopping stage for EU users","modelAttributes":["brand","color","category_level0","category_level1"],"modelStatus":"inactive"}}`
				req := predict.ApiUpdateModelInstanceRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.UpdateModelInstance(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/predict/models/model1")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"name":"Shopping stage for EU users","modelAttributes":["brand","color","category_level0","category_level1"],"modelStatus":"inactive"}`)
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

func TestPredict_UpdateSegment(t *testing.T) {
	client, echo := createPredictClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "updateSegment with name",
			testFunc: func(t *testing.T) {
				parametersStr := `{"segmentID":"segment1","updateSegmentParams":{"name":"example segment name"}}`
				req := predict.ApiUpdateSegmentRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.UpdateSegment(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments/segment1")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"name":"example segment name"}`)
			},
		},
		{
			name: "updateSegment with conditions",
			testFunc: func(t *testing.T) {
				t.Skip("skipping test for go client")
				parametersStr := `{"segmentID":"segment1","updateSegmentParams":{"conditions":{"operator":"AND","operands":[{"name":"predictions.order_value","filters":[{"operator":"GT","value":200}]}]}}}`
				req := predict.ApiUpdateSegmentRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.UpdateSegment(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments/segment1")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"conditions":{"operator":"AND","operands":[{"name":"predictions.order_value","filters":[{"operator":"GT","value":200}]}]}}`)
			},
		},
		{
			name: "updateSegment with name and conditions",
			testFunc: func(t *testing.T) {
				t.Skip("skipping test for go client")
				parametersStr := `{"segmentID":"segment1","updateSegmentParams":{"name":"example segment name","conditions":{"operator":"AND","operands":[{"name":"predictions.order_value","filters":[{"operator":"GT","value":200}]}]}}}`
				req := predict.ApiUpdateSegmentRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.UpdateSegment(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments/segment1")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"name":"example segment name","conditions":{"operator":"AND","operands":[{"name":"predictions.order_value","filters":[{"operator":"GT","value":200}]}]}}`)
			},
		},
		{
			name: "updateSegment with filter probability",
			testFunc: func(t *testing.T) {
				parametersStr := `{"segmentID":"segment1","updateSegmentParams":{"conditions":{"operator":"AND","operands":[{"name":"predictions.affinities.color","filters":[{"operator":"EQ","value":"red","probability":{"GTE":0.5,"LTE":1}}]}]}}}`
				req := predict.ApiUpdateSegmentRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.UpdateSegment(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/segments/segment1")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"conditions":{"operator":"AND","operands":[{"name":"predictions.affinities.color","filters":[{"operator":"EQ","value":"red","probability":{"GTE":0.5,"LTE":1}}]}]}}`)
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
