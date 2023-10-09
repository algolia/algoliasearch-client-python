package tests

import (
	"encoding/json"
	"net/url"
	"testing"

	"github.com/kinbiko/jsonassert"
	"github.com/stretchr/testify/require"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/search"
)

func createSearchClient() (*search.APIClient, *echoRequester) {
	echo := &echoRequester{}
	cfg := search.Configuration{
		AppID:     "appID",
		ApiKey:    "apiKey",
		Requester: echo,
	}
	client := search.NewClientWithConfig(cfg)

	// so that the linter doesn't complain
	_ = jsonassert.New(nil)

	return client, echo
}

func TestSearch_AddApiKey(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "addApiKey",
			testFunc: func(t *testing.T) {
				parametersStr := `{"acl":["search","addObject"],"description":"my new api key","validity":300,"maxQueriesPerIPPerHour":100,"maxHitsPerQuery":20}`
				req := search.ApiAddApiKeyRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.AddApiKey(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/keys")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"acl":["search","addObject"],"description":"my new api key","validity":300,"maxQueriesPerIPPerHour":100,"maxHitsPerQuery":20}`)
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

func TestSearch_AddOrUpdateObject(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "addOrUpdateObject",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","objectID":"uniqueID","body":{"key":"value"}}`
				req := search.ApiAddOrUpdateObjectRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.AddOrUpdateObject(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/uniqueID")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"key":"value"}`)
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

func TestSearch_AppendSource(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "appendSource",
			testFunc: func(t *testing.T) {
				parametersStr := `{"source":"theSource","description":"theDescription"}`
				req := search.ApiAppendSourceRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.AppendSource(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/security/sources/append")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"source":"theSource","description":"theDescription"}`)
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

func TestSearch_AssignUserId(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "assignUserId",
			testFunc: func(t *testing.T) {
				parametersStr := `{"xAlgoliaUserID":"userID","assignUserIdParams":{"cluster":"theCluster"}}`
				req := search.ApiAssignUserIdRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.AssignUserId(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/clusters/mapping")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"cluster":"theCluster"}`)
				headers := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"x-algolia-user-id":"userID"}`), &headers))
				for k, v := range headers {
					require.Equal(t, v, echo.header.Get(k))
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

func TestSearch_Batch(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allows batch method with `addObject` action",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","batchWriteParams":{"requests":[{"action":"addObject","body":{"key":"value"}}]}}`
				req := search.ApiBatchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Batch(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/batch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"action":"addObject","body":{"key":"value"}}]}`)
			},
		},
		{
			name: "allows batch method with `clear` action",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","batchWriteParams":{"requests":[{"action":"clear","body":{"key":"value"}}]}}`
				req := search.ApiBatchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Batch(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/batch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"action":"clear","body":{"key":"value"}}]}`)
			},
		},
		{
			name: "allows batch method with `delete` action",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","batchWriteParams":{"requests":[{"action":"delete","body":{"key":"value"}}]}}`
				req := search.ApiBatchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Batch(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/batch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"action":"delete","body":{"key":"value"}}]}`)
			},
		},
		{
			name: "allows batch method with `deleteObject` action",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","batchWriteParams":{"requests":[{"action":"deleteObject","body":{"key":"value"}}]}}`
				req := search.ApiBatchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Batch(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/batch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"action":"deleteObject","body":{"key":"value"}}]}`)
			},
		},
		{
			name: "allows batch method with `partialUpdateObject` action",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","batchWriteParams":{"requests":[{"action":"partialUpdateObject","body":{"key":"value"}}]}}`
				req := search.ApiBatchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Batch(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/batch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"action":"partialUpdateObject","body":{"key":"value"}}]}`)
			},
		},
		{
			name: "allows batch method with `partialUpdateObjectNoCreate` action",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","batchWriteParams":{"requests":[{"action":"partialUpdateObjectNoCreate","body":{"key":"value"}}]}}`
				req := search.ApiBatchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Batch(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/batch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"action":"partialUpdateObjectNoCreate","body":{"key":"value"}}]}`)
			},
		},
		{
			name: "allows batch method with `updateObject` action",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","batchWriteParams":{"requests":[{"action":"updateObject","body":{"key":"value"}}]}}`
				req := search.ApiBatchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Batch(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/batch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"action":"updateObject","body":{"key":"value"}}]}`)
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

func TestSearch_BatchAssignUserIds(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "batchAssignUserIds",
			testFunc: func(t *testing.T) {
				parametersStr := `{"xAlgoliaUserID":"userID","batchAssignUserIdsParams":{"cluster":"theCluster","users":["user1","user2"]}}`
				req := search.ApiBatchAssignUserIdsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.BatchAssignUserIds(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/clusters/mapping/batch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"cluster":"theCluster","users":["user1","user2"]}`)
				headers := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"x-algolia-user-id":"userID"}`), &headers))
				for k, v := range headers {
					require.Equal(t, v, echo.header.Get(k))
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

func TestSearch_BatchDictionaryEntries(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get batchDictionaryEntries results with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"dictionaryName":"compounds","batchDictionaryEntriesParams":{"requests":[{"action":"addEntry","body":{"objectID":"1","language":"en"}},{"action":"deleteEntry","body":{"objectID":"2","language":"fr"}}]}}`
				req := search.ApiBatchDictionaryEntriesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.BatchDictionaryEntries(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/dictionaries/compounds/batch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"action":"addEntry","body":{"objectID":"1","language":"en"}},{"action":"deleteEntry","body":{"objectID":"2","language":"fr"}}]}`)
			},
		},
		{
			name: "get batchDictionaryEntries results with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"dictionaryName":"compounds","batchDictionaryEntriesParams":{"clearExistingDictionaryEntries":false,"requests":[{"action":"addEntry","body":{"objectID":"1","language":"en","word":"fancy","words":["believe","algolia"],"decomposition":["trust","algolia"],"state":"enabled"}},{"action":"deleteEntry","body":{"objectID":"2","language":"fr","word":"humility","words":["candor","algolia"],"decomposition":["grit","algolia"],"state":"enabled"}}]}}`
				req := search.ApiBatchDictionaryEntriesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.BatchDictionaryEntries(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/dictionaries/compounds/batch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"clearExistingDictionaryEntries":false,"requests":[{"action":"addEntry","body":{"objectID":"1","language":"en","word":"fancy","words":["believe","algolia"],"decomposition":["trust","algolia"],"state":"enabled"}},{"action":"deleteEntry","body":{"objectID":"2","language":"fr","word":"humility","words":["candor","algolia"],"decomposition":["grit","algolia"],"state":"enabled"}}]}`)
			},
		},
		{
			name: "get batchDictionaryEntries results additional properties",
			testFunc: func(t *testing.T) {
				parametersStr := `{"dictionaryName":"compounds","batchDictionaryEntriesParams":{"requests":[{"action":"addEntry","body":{"objectID":"1","language":"en","additional":"try me"}}]}}`
				req := search.ApiBatchDictionaryEntriesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.BatchDictionaryEntries(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/dictionaries/compounds/batch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"action":"addEntry","body":{"objectID":"1","language":"en","additional":"try me"}}]}`)
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

func TestSearch_Browse(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "browse with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName"}`
				req := search.ApiBrowseRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Browse(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/browse")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{}`)
			},
		},
		{
			name: "browse with search parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","browseParams":{"query":"myQuery","facetFilters":["tags:algolia"]}}`
				req := search.ApiBrowseRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Browse(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/browse")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"query":"myQuery","facetFilters":["tags:algolia"]}`)
			},
		},
		{
			name: "browse allow a cursor in parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","browseParams":{"cursor":"test"}}`
				req := search.ApiBrowseRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Browse(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/browse")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"cursor":"test"}`)
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

func TestSearch_ClearAllSynonyms(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "clearAllSynonyms",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName"}`
				req := search.ApiClearAllSynonymsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.ClearAllSynonyms(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/synonyms/clear")
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

func TestSearch_ClearObjects(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "clearObjects",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName"}`
				req := search.ApiClearObjectsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.ClearObjects(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/clear")
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

func TestSearch_ClearRules(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "clearRules",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName"}`
				req := search.ApiClearRulesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.ClearRules(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/rules/clear")
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

func TestSearch_Del(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow del method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := search.ApiDelRequest{}
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
				req := search.ApiDelRequest{}
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

func TestSearch_DeleteApiKey(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "deleteApiKey",
			testFunc: func(t *testing.T) {
				parametersStr := `{"key":"myTestApiKey"}`
				req := search.ApiDeleteApiKeyRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DeleteApiKey(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/keys/myTestApiKey")
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

func TestSearch_DeleteBy(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "deleteBy",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","deleteByParams":{"filters":"brand:brandName"}}`
				req := search.ApiDeleteByRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DeleteBy(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/deleteByQuery")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"filters":"brand:brandName"}`)
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

func TestSearch_DeleteIndex(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "deleteIndex",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName"}`
				req := search.ApiDeleteIndexRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DeleteIndex(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName")
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

func TestSearch_DeleteObject(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "deleteObject",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","objectID":"uniqueID"}`
				req := search.ApiDeleteObjectRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DeleteObject(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/uniqueID")
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

func TestSearch_DeleteRule(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "deleteRule",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","objectID":"id1"}`
				req := search.ApiDeleteRuleRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DeleteRule(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/rules/id1")
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

func TestSearch_DeleteSource(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "deleteSource",
			testFunc: func(t *testing.T) {
				parametersStr := `{"source":"theSource"}`
				req := search.ApiDeleteSourceRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DeleteSource(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/security/sources/theSource")
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

func TestSearch_DeleteSynonym(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "deleteSynonym",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","objectID":"id1"}`
				req := search.ApiDeleteSynonymRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.DeleteSynonym(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/synonyms/id1")
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

func TestSearch_Get(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow get method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := search.ApiGetRequest{}
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
				req := search.ApiGetRequest{}
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

func TestSearch_GetApiKey(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getApiKey",
			testFunc: func(t *testing.T) {
				parametersStr := `{"key":"myTestApiKey"}`
				req := search.ApiGetApiKeyRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetApiKey(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/keys/myTestApiKey")
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

func TestSearch_GetDictionaryLanguages(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getDictionaryLanguages",
			testFunc: func(t *testing.T) {
				_, err := client.GetDictionaryLanguages()
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/dictionaries/*/languages")
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

func TestSearch_GetDictionarySettings(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get getDictionarySettings results",
			testFunc: func(t *testing.T) {
				_, err := client.GetDictionarySettings()
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/dictionaries/*/settings")
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

func TestSearch_GetLogs(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getLogs with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{}`
				req := search.ApiGetLogsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetLogs(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/logs")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
			},
		},
		{
			name: "getLogs with parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"offset":5,"length":10,"indexName":"theIndexName","type":"all"}`
				req := search.ApiGetLogsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetLogs(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/logs")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"offset":"5","length":"10","indexName":"theIndexName","type":"all"}`), &queryParams))
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

func TestSearch_GetObject(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getObject",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","objectID":"uniqueID","attributesToRetrieve":["attr1","attr2"]}`
				req := search.ApiGetObjectRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetObject(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/uniqueID")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"attributesToRetrieve":"attr1,attr2"}`), &queryParams))
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

func TestSearch_GetObjects(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getObjects",
			testFunc: func(t *testing.T) {
				parametersStr := `{"requests":[{"attributesToRetrieve":["attr1","attr2"],"objectID":"uniqueID","indexName":"theIndexName"}]}`
				req := search.ApiGetObjectsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetObjects(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/*/objects")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"attributesToRetrieve":["attr1","attr2"],"objectID":"uniqueID","indexName":"theIndexName"}]}`)
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

func TestSearch_GetRule(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getRule",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","objectID":"id1"}`
				req := search.ApiGetRuleRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetRule(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/rules/id1")
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

func TestSearch_GetSettings(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getSettings",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName"}`
				req := search.ApiGetSettingsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetSettings(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/settings")
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

func TestSearch_GetSources(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getSources",
			testFunc: func(t *testing.T) {
				_, err := client.GetSources()
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/security/sources")
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

func TestSearch_GetSynonym(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getSynonym",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","objectID":"id1"}`
				req := search.ApiGetSynonymRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetSynonym(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/synonyms/id1")
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

func TestSearch_GetTask(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getTask",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","taskID":123}`
				req := search.ApiGetTaskRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetTask(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/task/123")
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

func TestSearch_GetTopUserIds(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getTopUserIds",
			testFunc: func(t *testing.T) {
				_, err := client.GetTopUserIds()
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/clusters/mapping/top")
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

func TestSearch_GetUserId(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "getUserId",
			testFunc: func(t *testing.T) {
				parametersStr := `{"userID":"uniqueID"}`
				req := search.ApiGetUserIdRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.GetUserId(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/clusters/mapping/uniqueID")
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

func TestSearch_HasPendingMappings(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "hasPendingMappings with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{}`
				req := search.ApiHasPendingMappingsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.HasPendingMappings(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/clusters/mapping/pending")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
			},
		},
		{
			name: "hasPendingMappings with parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"getClusters":true}`
				req := search.ApiHasPendingMappingsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.HasPendingMappings(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/clusters/mapping/pending")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"getClusters":"true"}`), &queryParams))
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

func TestSearch_ListApiKeys(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "listApiKeys",
			testFunc: func(t *testing.T) {
				_, err := client.ListApiKeys()
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/keys")
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

func TestSearch_ListClusters(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "listClusters",
			testFunc: func(t *testing.T) {
				_, err := client.ListClusters()
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/clusters")
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

func TestSearch_ListIndices(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "listIndices with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{}`
				req := search.ApiListIndicesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.ListIndices(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
			},
		},
		{
			name: "listIndices with parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"page":8,"hitsPerPage":3}`
				req := search.ApiListIndicesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.ListIndices(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"page":"8","hitsPerPage":"3"}`), &queryParams))
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

func TestSearch_ListUserIds(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "listUserIds with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{}`
				req := search.ApiListUserIdsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.ListUserIds(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/clusters/mapping")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
			},
		},
		{
			name: "listUserIds with parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"page":8,"hitsPerPage":100}`
				req := search.ApiListUserIdsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.ListUserIds(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/clusters/mapping")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "GET", echo.method)

				require.Nil(t, echo.body)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"page":"8","hitsPerPage":"100"}`), &queryParams))
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

func TestSearch_MultipleBatch(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "multipleBatch",
			testFunc: func(t *testing.T) {
				parametersStr := `{"requests":[{"action":"addObject","body":{"key":"value"},"indexName":"theIndexName"}]}`
				req := search.ApiMultipleBatchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.MultipleBatch(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/*/batch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"action":"addObject","body":{"key":"value"},"indexName":"theIndexName"}]}`)
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

func TestSearch_OperationIndex(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "operationIndex",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","operationIndexParams":{"operation":"copy","destination":"dest","scope":["rules","settings"]}}`
				req := search.ApiOperationIndexRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.OperationIndex(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/operation")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"operation":"copy","destination":"dest","scope":["rules","settings"]}`)
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

func TestSearch_PartialUpdateObject(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "partialUpdateObject",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","objectID":"uniqueID","attributesToUpdate":{"id1":"test","id2":{"_operation":"AddUnique","value":"test2"}},"createIfNotExists":true}`
				req := search.ApiPartialUpdateObjectRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.PartialUpdateObject(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/uniqueID/partial")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"id1":"test","id2":{"_operation":"AddUnique","value":"test2"}}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"createIfNotExists":"true"}`), &queryParams))
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

func TestSearch_Post(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow post method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := search.ApiPostRequest{}
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
				req := search.ApiPostRequest{}
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
				req := search.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []search.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"query":"myQueryParameter"}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, search.QueryParamOption(k, v))
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
				req := search.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []search.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"query2":"myQueryParameter"}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, search.QueryParamOption(k, v))
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
				req := search.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []search.Option
				requestOptionHeaders := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"x-algolia-api-key":"myApiKey"}`), &requestOptionHeaders))
				for k, v := range requestOptionHeaders {
					opts = append(opts, search.HeaderParamOption(k, v))
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
				req := search.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []search.Option
				requestOptionHeaders := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"x-algolia-api-key":"myApiKey"}`), &requestOptionHeaders))
				for k, v := range requestOptionHeaders {
					opts = append(opts, search.HeaderParamOption(k, v))
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
				req := search.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []search.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"isItWorking":true}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, search.QueryParamOption(k, v))
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
				req := search.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []search.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":2}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, search.QueryParamOption(k, v))
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
				req := search.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []search.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":["c","d"]}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, search.QueryParamOption(k, v))
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
				req := search.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []search.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":[true,true,false]}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, search.QueryParamOption(k, v))
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
				req := search.ApiPostRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				var opts []search.Option
				requestOptionParameters := map[string]any{}
				require.NoError(t, json.Unmarshal([]byte(`{"myParam":[1,2]}`), &requestOptionParameters))
				for k, v := range requestOptionParameters {
					opts = append(opts, search.QueryParamOption(k, v))
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

func TestSearch_Put(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "allow put method for a custom path with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"path":"/test/minimal"}`
				req := search.ApiPutRequest{}
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
				req := search.ApiPutRequest{}
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

func TestSearch_RemoveUserId(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "removeUserId",
			testFunc: func(t *testing.T) {
				parametersStr := `{"userID":"uniqueID"}`
				req := search.ApiRemoveUserIdRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.RemoveUserId(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/clusters/mapping/uniqueID")
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

func TestSearch_ReplaceSources(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "replaceSources",
			testFunc: func(t *testing.T) {
				parametersStr := `{"source":[{"source":"theSource","description":"theDescription"}]}`
				req := search.ApiReplaceSourcesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.ReplaceSources(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/security/sources")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `[{"source":"theSource","description":"theDescription"}]`)
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

func TestSearch_RestoreApiKey(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "restoreApiKey",
			testFunc: func(t *testing.T) {
				parametersStr := `{"key":"myApiKey"}`
				req := search.ApiRestoreApiKeyRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.RestoreApiKey(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/keys/myApiKey/restore")
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

func TestSearch_SaveObject(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "saveObject",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","body":{"objectID":"id","test":"val"}}`
				req := search.ApiSaveObjectRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SaveObject(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"objectID":"id","test":"val"}`)
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

func TestSearch_SaveRule(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "saveRule with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","objectID":"id1","rule":{"objectID":"id1","conditions":[{"pattern":"apple","anchoring":"contains"}]}}`
				req := search.ApiSaveRuleRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SaveRule(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/rules/id1")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"objectID":"id1","conditions":[{"pattern":"apple","anchoring":"contains"}]}`)
			},
		},
		{
			name: "saveRule with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","objectID":"id1","rule":{"objectID":"id1","conditions":[{"pattern":"apple","anchoring":"contains","alternatives":false,"context":"search"}],"consequence":{"params":{"filters":"brand:apple","query":{"remove":["algolia"],"edits":[{"type":"remove","delete":"abc","insert":"cde"},{"type":"replace","delete":"abc","insert":"cde"}]}},"hide":[{"objectID":"321"}],"filterPromotes":false,"userData":{"algolia":"aloglia"},"promote":[{"objectID":"abc","position":3},{"objectIDs":["abc","def"],"position":1}]},"description":"test","enabled":true,"validity":[{"from":1656670273,"until":1656670277}]},"forwardToReplicas":true}`
				req := search.ApiSaveRuleRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SaveRule(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/rules/id1")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"objectID":"id1","conditions":[{"pattern":"apple","anchoring":"contains","alternatives":false,"context":"search"}],"consequence":{"params":{"filters":"brand:apple","query":{"remove":["algolia"],"edits":[{"type":"remove","delete":"abc","insert":"cde"},{"type":"replace","delete":"abc","insert":"cde"}]}},"hide":[{"objectID":"321"}],"filterPromotes":false,"userData":{"algolia":"aloglia"},"promote":[{"objectID":"abc","position":3},{"objectIDs":["abc","def"],"position":1}]},"description":"test","enabled":true,"validity":[{"from":1656670273,"until":1656670277}]}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"forwardToReplicas":"true"}`), &queryParams))
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

func TestSearch_SaveRules(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "saveRules with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","rules":[{"objectID":"a-rule-id","conditions":[{"pattern":"smartphone","anchoring":"contains"}]},{"objectID":"a-second-rule-id","conditions":[{"pattern":"apple","anchoring":"contains"}]}]}`
				req := search.ApiSaveRulesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SaveRules(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/rules/batch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `[{"objectID":"a-rule-id","conditions":[{"pattern":"smartphone","anchoring":"contains"}]},{"objectID":"a-second-rule-id","conditions":[{"pattern":"apple","anchoring":"contains"}]}]`)
			},
		},
		{
			name: "saveRules with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","rules":[{"objectID":"id1","conditions":[{"pattern":"apple","anchoring":"contains","alternatives":false,"context":"search"}],"consequence":{"params":{"filters":"brand:apple","query":{"remove":["algolia"],"edits":[{"type":"remove","delete":"abc","insert":"cde"},{"type":"replace","delete":"abc","insert":"cde"}]}},"hide":[{"objectID":"321"}],"filterPromotes":false,"userData":{"algolia":"aloglia"},"promote":[{"objectID":"abc","position":3},{"objectIDs":["abc","def"],"position":1}]},"description":"test","enabled":true,"validity":[{"from":1656670273,"until":1656670277}]}],"forwardToReplicas":true,"clearExistingRules":true}`
				req := search.ApiSaveRulesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SaveRules(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/rules/batch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `[{"objectID":"id1","conditions":[{"pattern":"apple","anchoring":"contains","alternatives":false,"context":"search"}],"consequence":{"params":{"filters":"brand:apple","query":{"remove":["algolia"],"edits":[{"type":"remove","delete":"abc","insert":"cde"},{"type":"replace","delete":"abc","insert":"cde"}]}},"hide":[{"objectID":"321"}],"filterPromotes":false,"userData":{"algolia":"aloglia"},"promote":[{"objectID":"abc","position":3},{"objectIDs":["abc","def"],"position":1}]},"description":"test","enabled":true,"validity":[{"from":1656670273,"until":1656670277}]}]`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"forwardToReplicas":"true","clearExistingRules":"true"}`), &queryParams))
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

func TestSearch_SaveSynonym(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "saveSynonym",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","objectID":"id1","synonymHit":{"objectID":"id1","type":"synonym","synonyms":["car","vehicule","auto"]},"forwardToReplicas":true}`
				req := search.ApiSaveSynonymRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SaveSynonym(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/synonyms/id1")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"objectID":"id1","type":"synonym","synonyms":["car","vehicule","auto"]}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"forwardToReplicas":"true"}`), &queryParams))
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

func TestSearch_SaveSynonyms(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "saveSynonyms",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","synonymHit":[{"objectID":"id1","type":"synonym","synonyms":["car","vehicule","auto"]},{"objectID":"id2","type":"onewaysynonym","input":"iphone","synonyms":["ephone","aphone","yphone"]}],"forwardToReplicas":true,"replaceExistingSynonyms":false}`
				req := search.ApiSaveSynonymsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SaveSynonyms(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/synonyms/batch")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `[{"objectID":"id1","type":"synonym","synonyms":["car","vehicule","auto"]},{"objectID":"id2","type":"onewaysynonym","input":"iphone","synonyms":["ephone","aphone","yphone"]}]`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"forwardToReplicas":"true","replaceExistingSynonyms":"false"}`), &queryParams))
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

func TestSearch_Search(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "search for a single hits request with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"requests":[{"indexName":"theIndexName"}]}`
				req := search.ApiSearchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Search(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/*/queries")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"indexName":"theIndexName"}]}`)
			},
		},
		{
			name: "search for a single facet request with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"requests":[{"indexName":"theIndexName","type":"facet","facet":"theFacet"}],"strategy":"stopIfEnoughMatches"}`
				req := search.ApiSearchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Search(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/*/queries")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"indexName":"theIndexName","type":"facet","facet":"theFacet"}],"strategy":"stopIfEnoughMatches"}`)
			},
		},
		{
			name: "search for a single hits request with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"requests":[{"indexName":"theIndexName","query":"myQuery","hitsPerPage":50,"type":"default"}]}`
				req := search.ApiSearchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Search(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/*/queries")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"indexName":"theIndexName","query":"myQuery","hitsPerPage":50,"type":"default"}]}`)
			},
		},
		{
			name: "search for a single facet request with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"requests":[{"indexName":"theIndexName","type":"facet","facet":"theFacet","facetQuery":"theFacetQuery","query":"theQuery","maxFacetHits":50}],"strategy":"stopIfEnoughMatches"}`
				req := search.ApiSearchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Search(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/*/queries")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"indexName":"theIndexName","type":"facet","facet":"theFacet","facetQuery":"theFacetQuery","query":"theQuery","maxFacetHits":50}],"strategy":"stopIfEnoughMatches"}`)
			},
		},
		{
			name: "search for multiple mixed requests in multiple indices with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"requests":[{"indexName":"theIndexName"},{"indexName":"theIndexName2","type":"facet","facet":"theFacet"},{"indexName":"theIndexName","type":"default"}],"strategy":"stopIfEnoughMatches"}`
				req := search.ApiSearchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Search(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/*/queries")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"indexName":"theIndexName"},{"indexName":"theIndexName2","type":"facet","facet":"theFacet"},{"indexName":"theIndexName","type":"default"}],"strategy":"stopIfEnoughMatches"}`)
			},
		},
		{
			name: "search for multiple mixed requests in multiple indices with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"requests":[{"indexName":"theIndexName","type":"facet","facet":"theFacet","facetQuery":"theFacetQuery","query":"theQuery","maxFacetHits":50},{"indexName":"theIndexName","query":"myQuery","hitsPerPage":50,"type":"default"}],"strategy":"stopIfEnoughMatches"}`
				req := search.ApiSearchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Search(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/*/queries")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"indexName":"theIndexName","type":"facet","facet":"theFacet","facetQuery":"theFacetQuery","query":"theQuery","maxFacetHits":50},{"indexName":"theIndexName","query":"myQuery","hitsPerPage":50,"type":"default"}],"strategy":"stopIfEnoughMatches"}`)
			},
		},
		{
			name: "search filters accept all of the possible shapes",
			testFunc: func(t *testing.T) {
				parametersStr := `{"requests":[{"indexName":"theIndexName","facetFilters":"mySearch:filters","reRankingApplyFilter":"mySearch:filters","tagFilters":"mySearch:filters","numericFilters":"mySearch:filters","optionalFilters":"mySearch:filters"},{"indexName":"theIndexName","facetFilters":["mySearch:filters",["mySearch:filters"]],"reRankingApplyFilter":["mySearch:filters",["mySearch:filters"]],"tagFilters":["mySearch:filters",["mySearch:filters"]],"numericFilters":["mySearch:filters",["mySearch:filters"]],"optionalFilters":["mySearch:filters",["mySearch:filters"]]}]}`
				req := search.ApiSearchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Search(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/*/queries")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"indexName":"theIndexName","facetFilters":"mySearch:filters","reRankingApplyFilter":"mySearch:filters","tagFilters":"mySearch:filters","numericFilters":"mySearch:filters","optionalFilters":"mySearch:filters"},{"indexName":"theIndexName","facetFilters":["mySearch:filters",["mySearch:filters"]],"reRankingApplyFilter":["mySearch:filters",["mySearch:filters"]],"tagFilters":["mySearch:filters",["mySearch:filters"]],"numericFilters":["mySearch:filters",["mySearch:filters"]],"optionalFilters":["mySearch:filters",["mySearch:filters"]]}]}`)
			},
		},
		{
			name: "search with all search parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"requests":[{"advancedSyntax":true,"advancedSyntaxFeatures":["exactPhrase"],"allowTyposOnNumericTokens":true,"alternativesAsExact":["multiWordsSynonym"],"analytics":true,"analyticsTags":[""],"aroundLatLng":"","aroundLatLngViaIP":true,"aroundPrecision":0,"aroundRadius":"all","attributeCriteriaComputedByMinProximity":true,"attributesForFaceting":[""],"attributesToHighlight":[""],"attributesToRetrieve":[""],"attributesToSnippet":[""],"clickAnalytics":true,"customRanking":[""],"decompoundQuery":true,"disableExactOnAttributes":[""],"disableTypoToleranceOnAttributes":[""],"distinct":0,"enableABTest":true,"enablePersonalization":true,"enableReRanking":true,"enableRules":true,"exactOnSingleWordQuery":"attribute","explain":["foo","bar"],"facetFilters":[""],"facetingAfterDistinct":true,"facets":[""],"filters":"","getRankingInfo":true,"highlightPostTag":"","highlightPreTag":"","hitsPerPage":0,"ignorePlurals":false,"indexName":"theIndexName","insideBoundingBox":[[47.3165,4.9665,47.3424,5.0201],[40.9234,2.1185,38.643,1.9916]],"insidePolygon":[[47.3165,4.9665,47.3424,5.0201,47.32,4.9],[40.9234,2.1185,38.643,1.9916,39.2587,2.0104]],"keepDiacriticsOnCharacters":"","length":0,"maxValuesPerFacet":0,"minProximity":0,"minWordSizefor1Typo":0,"minWordSizefor2Typos":0,"minimumAroundRadius":0,"naturalLanguages":[""],"numericFilters":[""],"offset":0,"optionalFilters":[""],"optionalWords":[""],"page":0,"percentileComputation":true,"personalizationImpact":0,"query":"","queryLanguages":[""],"queryType":"prefixAll","ranking":[""],"reRankingApplyFilter":[""],"relevancyStrictness":0,"removeStopWords":true,"removeWordsIfNoResults":"allOptional","renderingContent":{"facetOrdering":{"facets":{"order":["a","b"]},"values":{"a":{"order":["b"],"sortRemainingBy":"count"}}}},"replaceSynonymsInHighlight":true,"responseFields":[""],"restrictHighlightAndSnippetArrays":true,"restrictSearchableAttributes":[""],"ruleContexts":[""],"similarQuery":"","snippetEllipsisText":"","sortFacetValuesBy":"","sumOrFiltersScores":true,"synonyms":true,"tagFilters":[""],"type":"default","typoTolerance":"min","userToken":""}]}`
				req := search.ApiSearchRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.Search(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/*/queries")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"requests":[{"advancedSyntax":true,"advancedSyntaxFeatures":["exactPhrase"],"allowTyposOnNumericTokens":true,"alternativesAsExact":["multiWordsSynonym"],"analytics":true,"analyticsTags":[""],"aroundLatLng":"","aroundLatLngViaIP":true,"aroundPrecision":0,"aroundRadius":"all","attributeCriteriaComputedByMinProximity":true,"attributesForFaceting":[""],"attributesToHighlight":[""],"attributesToRetrieve":[""],"attributesToSnippet":[""],"clickAnalytics":true,"customRanking":[""],"decompoundQuery":true,"disableExactOnAttributes":[""],"disableTypoToleranceOnAttributes":[""],"distinct":0,"enableABTest":true,"enablePersonalization":true,"enableReRanking":true,"enableRules":true,"exactOnSingleWordQuery":"attribute","explain":["foo","bar"],"facetFilters":[""],"facetingAfterDistinct":true,"facets":[""],"filters":"","getRankingInfo":true,"highlightPostTag":"","highlightPreTag":"","hitsPerPage":0,"ignorePlurals":false,"indexName":"theIndexName","insideBoundingBox":[[47.3165,4.9665,47.3424,5.0201],[40.9234,2.1185,38.643,1.9916]],"insidePolygon":[[47.3165,4.9665,47.3424,5.0201,47.32,4.9],[40.9234,2.1185,38.643,1.9916,39.2587,2.0104]],"keepDiacriticsOnCharacters":"","length":0,"maxValuesPerFacet":0,"minProximity":0,"minWordSizefor1Typo":0,"minWordSizefor2Typos":0,"minimumAroundRadius":0,"naturalLanguages":[""],"numericFilters":[""],"offset":0,"optionalFilters":[""],"optionalWords":[""],"page":0,"percentileComputation":true,"personalizationImpact":0,"query":"","queryLanguages":[""],"queryType":"prefixAll","ranking":[""],"reRankingApplyFilter":[""],"relevancyStrictness":0,"removeStopWords":true,"removeWordsIfNoResults":"allOptional","renderingContent":{"facetOrdering":{"facets":{"order":["a","b"]},"values":{"a":{"order":["b"],"sortRemainingBy":"count"}}}},"replaceSynonymsInHighlight":true,"responseFields":[""],"restrictHighlightAndSnippetArrays":true,"restrictSearchableAttributes":[""],"ruleContexts":[""],"similarQuery":"","snippetEllipsisText":"","sortFacetValuesBy":"","sumOrFiltersScores":true,"synonyms":true,"tagFilters":[""],"type":"default","typoTolerance":"min","userToken":""}]}`)
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

func TestSearch_SearchDictionaryEntries(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get searchDictionaryEntries results with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"dictionaryName":"compounds","searchDictionaryEntriesParams":{"query":"foo"}}`
				req := search.ApiSearchDictionaryEntriesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SearchDictionaryEntries(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/dictionaries/compounds/search")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"query":"foo"}`)
			},
		},
		{
			name: "get searchDictionaryEntries results with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"dictionaryName":"compounds","searchDictionaryEntriesParams":{"query":"foo","page":4,"hitsPerPage":2,"language":"fr"}}`
				req := search.ApiSearchDictionaryEntriesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SearchDictionaryEntries(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/dictionaries/compounds/search")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"query":"foo","page":4,"hitsPerPage":2,"language":"fr"}`)
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

func TestSearch_SearchForFacetValues(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get searchForFacetValues results with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","facetName":"facetName"}`
				req := search.ApiSearchForFacetValuesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SearchForFacetValues(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/facets/facetName/query")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{}`)
			},
		},
		{
			name: "get searchForFacetValues results with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","facetName":"facetName","searchForFacetValuesRequest":{"params":"query=foo&facetFilters=['bar']","facetQuery":"foo","maxFacetHits":42}}`
				req := search.ApiSearchForFacetValuesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SearchForFacetValues(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/facets/facetName/query")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"params":"query=foo&facetFilters=['bar']","facetQuery":"foo","maxFacetHits":42}`)
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

func TestSearch_SearchRules(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "searchRules",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","searchRulesParams":{"query":"something"}}`
				req := search.ApiSearchRulesRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SearchRules(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/rules/search")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"query":"something"}`)
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

func TestSearch_SearchSingleIndex(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "search with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName"}`
				req := search.ApiSearchSingleIndexRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SearchSingleIndex(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/query")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{}`)
			},
		},
		{
			name: "search with searchParams",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","searchParams":{"query":"myQuery","facetFilters":["tags:algolia"]}}`
				req := search.ApiSearchSingleIndexRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SearchSingleIndex(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/query")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"query":"myQuery","facetFilters":["tags:algolia"]}`)
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

func TestSearch_SearchSynonyms(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "searchSynonyms with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName"}`
				req := search.ApiSearchSynonymsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SearchSynonyms(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/synonyms/search")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{}`)
			},
		},
		{
			name: "searchSynonyms with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"indexName","type":"altcorrection1","page":10,"hitsPerPage":10,"searchSynonymsParams":{"query":"myQuery"}}`
				req := search.ApiSearchSynonymsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SearchSynonyms(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/indexName/synonyms/search")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"query":"myQuery"}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"type":"altcorrection1","page":"10","hitsPerPage":"10"}`), &queryParams))
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

func TestSearch_SearchUserIds(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "searchUserIds",
			testFunc: func(t *testing.T) {
				parametersStr := `{"query":"test","clusterName":"theClusterName","page":5,"hitsPerPage":10}`
				req := search.ApiSearchUserIdsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SearchUserIds(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/clusters/mapping/search")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "POST", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"query":"test","clusterName":"theClusterName","page":5,"hitsPerPage":10}`)
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

func TestSearch_SetDictionarySettings(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "get setDictionarySettings results with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"disableStandardEntries":{"plurals":{"fr":false,"en":false,"ru":true}}}`
				req := search.ApiSetDictionarySettingsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SetDictionarySettings(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/dictionaries/*/settings")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"disableStandardEntries":{"plurals":{"fr":false,"en":false,"ru":true}}}`)
			},
		},
		{
			name: "get setDictionarySettings results with all parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"disableStandardEntries":{"plurals":{"fr":false,"en":false,"ru":true},"stopwords":{"fr":false},"compounds":{"ru":true}}}`
				req := search.ApiSetDictionarySettingsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SetDictionarySettings(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/dictionaries/*/settings")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"disableStandardEntries":{"plurals":{"fr":false,"en":false,"ru":true},"stopwords":{"fr":false},"compounds":{"ru":true}}}`)
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

func TestSearch_SetSettings(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "setSettings with minimal parameters",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","indexSettings":{"paginationLimitedTo":10},"forwardToReplicas":true}`
				req := search.ApiSetSettingsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SetSettings(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/settings")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"paginationLimitedTo":10}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"forwardToReplicas":"true"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "setSettings allow boolean `typoTolerance`",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","indexSettings":{"typoTolerance":true},"forwardToReplicas":true}`
				req := search.ApiSetSettingsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SetSettings(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/settings")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"typoTolerance":true}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"forwardToReplicas":"true"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "setSettings allow enum `typoTolerance`",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","indexSettings":{"typoTolerance":"min"},"forwardToReplicas":true}`
				req := search.ApiSetSettingsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SetSettings(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/settings")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"typoTolerance":"min"}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"forwardToReplicas":"true"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "setSettings allow boolean `ignorePlurals`",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","indexSettings":{"ignorePlurals":true},"forwardToReplicas":true}`
				req := search.ApiSetSettingsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SetSettings(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/settings")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"ignorePlurals":true}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"forwardToReplicas":"true"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "setSettings allow list of string `ignorePlurals`",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","indexSettings":{"ignorePlurals":["algolia"]},"forwardToReplicas":true}`
				req := search.ApiSetSettingsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SetSettings(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/settings")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"ignorePlurals":["algolia"]}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"forwardToReplicas":"true"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "setSettings allow boolean `removeStopWords`",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","indexSettings":{"removeStopWords":true},"forwardToReplicas":true}`
				req := search.ApiSetSettingsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SetSettings(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/settings")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"removeStopWords":true}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"forwardToReplicas":"true"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "setSettings allow list of string `removeStopWords`",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","indexSettings":{"removeStopWords":["algolia"]},"forwardToReplicas":true}`
				req := search.ApiSetSettingsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SetSettings(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/settings")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"removeStopWords":["algolia"]}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"forwardToReplicas":"true"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "setSettings allow boolean `distinct`",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","indexSettings":{"distinct":true},"forwardToReplicas":true}`
				req := search.ApiSetSettingsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SetSettings(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/settings")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"distinct":true}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"forwardToReplicas":"true"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "setSettings allow integers for `distinct`",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","indexSettings":{"distinct":1},"forwardToReplicas":true}`
				req := search.ApiSetSettingsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SetSettings(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/settings")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"distinct":1}`)
				queryParams := map[string]string{}
				require.NoError(t, json.Unmarshal([]byte(`{"forwardToReplicas":"true"}`), &queryParams))
				for k, v := range queryParams {
					require.Equal(t, v, echo.query.Get(k))
				}
			},
		},
		{
			name: "setSettings allow all `indexSettings`",
			testFunc: func(t *testing.T) {
				parametersStr := `{"indexName":"theIndexName","indexSettings":{"advancedSyntax":true,"advancedSyntaxFeatures":["exactPhrase"],"allowCompressionOfIntegerArray":true,"allowTyposOnNumericTokens":true,"alternativesAsExact":["singleWordSynonym"],"attributeCriteriaComputedByMinProximity":true,"attributeForDistinct":"test","attributesForFaceting":["algolia"],"attributesToHighlight":["algolia"],"attributesToRetrieve":["algolia"],"attributesToSnippet":["algolia"],"attributesToTransliterate":["algolia"],"camelCaseAttributes":["algolia"],"customNormalization":{"algolia":{"aloglia":"aglolia"}},"customRanking":["algolia"],"decompoundQuery":false,"decompoundedAttributes":{"algolia":"aloglia"},"disableExactOnAttributes":["algolia"],"disablePrefixOnAttributes":["algolia"],"disableTypoToleranceOnAttributes":["algolia"],"disableTypoToleranceOnWords":["algolia"],"distinct":3,"enablePersonalization":true,"enableReRanking":false,"enableRules":true,"exactOnSingleWordQuery":"attribute","highlightPreTag":"<span>","highlightPostTag":"</span>","hitsPerPage":10,"ignorePlurals":false,"indexLanguages":["algolia"],"keepDiacriticsOnCharacters":"abc","maxFacetHits":20,"maxValuesPerFacet":30,"minProximity":6,"minWordSizefor1Typo":5,"minWordSizefor2Typos":11,"mode":"neuralSearch","numericAttributesForFiltering":["algolia"],"optionalWords":["myspace"],"paginationLimitedTo":0,"queryLanguages":["algolia"],"queryType":"prefixLast","ranking":["geo"],"reRankingApplyFilter":"mySearch:filters","relevancyStrictness":10,"removeStopWords":false,"removeWordsIfNoResults":"lastWords","renderingContent":{"facetOrdering":{"facets":{"order":["a","b"]},"values":{"a":{"order":["b"],"sortRemainingBy":"count"}}}},"replaceSynonymsInHighlight":true,"replicas":[""],"responseFields":["algolia"],"restrictHighlightAndSnippetArrays":true,"searchableAttributes":["foo"],"semanticSearch":{"eventSources":["foo"]},"separatorsToIndex":"bar","snippetEllipsisText":"---","sortFacetValuesBy":"date","typoTolerance":false,"unretrievableAttributes":["foo"],"userData":{"user":"data"}}}`
				req := search.ApiSetSettingsRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.SetSettings(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/indexes/theIndexName/settings")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"advancedSyntax":true,"advancedSyntaxFeatures":["exactPhrase"],"allowCompressionOfIntegerArray":true,"allowTyposOnNumericTokens":true,"alternativesAsExact":["singleWordSynonym"],"attributeCriteriaComputedByMinProximity":true,"attributeForDistinct":"test","attributesForFaceting":["algolia"],"attributesToHighlight":["algolia"],"attributesToRetrieve":["algolia"],"attributesToSnippet":["algolia"],"attributesToTransliterate":["algolia"],"camelCaseAttributes":["algolia"],"customNormalization":{"algolia":{"aloglia":"aglolia"}},"customRanking":["algolia"],"decompoundQuery":false,"decompoundedAttributes":{"algolia":"aloglia"},"disableExactOnAttributes":["algolia"],"disablePrefixOnAttributes":["algolia"],"disableTypoToleranceOnAttributes":["algolia"],"disableTypoToleranceOnWords":["algolia"],"distinct":3,"enablePersonalization":true,"enableReRanking":false,"enableRules":true,"exactOnSingleWordQuery":"attribute","highlightPreTag":"<span>","highlightPostTag":"</span>","hitsPerPage":10,"ignorePlurals":false,"indexLanguages":["algolia"],"keepDiacriticsOnCharacters":"abc","maxFacetHits":20,"maxValuesPerFacet":30,"minProximity":6,"minWordSizefor1Typo":5,"minWordSizefor2Typos":11,"mode":"neuralSearch","numericAttributesForFiltering":["algolia"],"optionalWords":["myspace"],"paginationLimitedTo":0,"queryLanguages":["algolia"],"queryType":"prefixLast","ranking":["geo"],"reRankingApplyFilter":"mySearch:filters","relevancyStrictness":10,"removeStopWords":false,"removeWordsIfNoResults":"lastWords","renderingContent":{"facetOrdering":{"facets":{"order":["a","b"]},"values":{"a":{"order":["b"],"sortRemainingBy":"count"}}}},"replaceSynonymsInHighlight":true,"replicas":[""],"responseFields":["algolia"],"restrictHighlightAndSnippetArrays":true,"searchableAttributes":["foo"],"semanticSearch":{"eventSources":["foo"]},"separatorsToIndex":"bar","snippetEllipsisText":"---","sortFacetValuesBy":"date","typoTolerance":false,"unretrievableAttributes":["foo"],"userData":{"user":"data"}}`)
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

func TestSearch_UpdateApiKey(t *testing.T) {
	client, echo := createSearchClient()

	tests := []struct {
		name     string
		testFunc func(t *testing.T)
	}{
		{
			name: "updateApiKey",
			testFunc: func(t *testing.T) {
				parametersStr := `{"key":"myApiKey","apiKey":{"acl":["search","addObject"],"validity":300,"maxQueriesPerIPPerHour":100,"maxHitsPerQuery":20}}`
				req := search.ApiUpdateApiKeyRequest{}
				require.NoError(t, json.Unmarshal([]byte(parametersStr), &req))
				_, err := client.UpdateApiKey(req)
				require.NoError(t, err)

				expectedPath, err := url.QueryUnescape("/1/keys/myApiKey")
				require.NoError(t, err)
				require.Equal(t, expectedPath, echo.path)
				require.Equal(t, "PUT", echo.method)

				ja := jsonassert.New(t)
				ja.Assertf(*echo.body, `{"acl":["search","addObject"],"validity":300,"maxQueriesPerIPPerHour":100,"maxHitsPerQuery":20}`)
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
