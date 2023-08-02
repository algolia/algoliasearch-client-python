package com.algolia.methods.requests

import com.algolia.client.api.SearchClient
import com.algolia.client.configuration.*
import com.algolia.client.model.search.*
import com.algolia.client.transport.*
import com.algolia.utils.*
import io.ktor.http.*
import kotlinx.coroutines.test.*
import kotlinx.serialization.json.*
import kotlin.test.*

class SearchTest {

  val client = SearchClient(
    appId = "appId",
    apiKey = "apiKey",
  )

  // addApiKey

  @Test
  fun `addApiKey`() = runTest {
    client.runTest(
      call = {
        addApiKey(
          apiKey = ApiKey(
            acl = listOf(Acl.values().first { it.value == "search" }, Acl.values().first { it.value == "addObject" }),
            description = "my new api key",
            validity = 300,
            maxQueriesPerIPPerHour = 100,
            maxHitsPerQuery = 20,
          ),
        )
      },
      intercept = {
        assertEquals("/1/keys".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"acl":["search","addObject"],"description":"my new api key","validity":300,"maxQueriesPerIPPerHour":100,"maxHitsPerQuery":20}""", it.body)
      },
    )
  }

  // addOrUpdateObject

  @Test
  fun `addOrUpdateObject`() = runTest {
    client.runTest(
      call = {
        addOrUpdateObject(
          indexName = "indexName",
          objectID = "uniqueID",
          body = buildJsonObject {
            put(
              "key",
              JsonPrimitive("value"),
            )
          },
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/uniqueID".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertJsonBody("""{"key":"value"}""", it.body)
      },
    )
  }

  // appendSource

  @Test
  fun `appendSource`() = runTest {
    client.runTest(
      call = {
        appendSource(
          source = Source(
            source = "theSource",
            description = "theDescription",
          ),
        )
      },
      intercept = {
        assertEquals("/1/security/sources/append".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"source":"theSource","description":"theDescription"}""", it.body)
      },
    )
  }

  // assignUserId

  @Test
  fun `assignUserId`() = runTest {
    client.runTest(
      call = {
        assignUserId(
          xAlgoliaUserID = "userID",
          assignUserIdParams = AssignUserIdParams(
            cluster = "theCluster",
          ),
        )
      },
      intercept = {
        assertEquals("/1/clusters/mapping".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"x-algolia-user-id":"userID"}""", it.headers)
        assertJsonBody("""{"cluster":"theCluster"}""", it.body)
      },
    )
  }

  // batch

  @Test
  fun `allows batch method with 'addObject' action`() = runTest {
    client.runTest(
      call = {
        batch(
          indexName = "theIndexName",
          batchWriteParams = BatchWriteParams(
            requests = listOf(
              BatchRequest(
                action = Action.values().first { it.value == "addObject" },
                body = buildJsonObject {
                  put(
                    "key",
                    JsonPrimitive("value"),
                  )
                },
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/batch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"action":"addObject","body":{"key":"value"}}]}""", it.body)
      },
    )
  }

  @Test
  fun `allows batch method with 'clear' action`() = runTest {
    client.runTest(
      call = {
        batch(
          indexName = "theIndexName",
          batchWriteParams = BatchWriteParams(
            requests = listOf(
              BatchRequest(
                action = Action.values().first { it.value == "clear" },
                body = buildJsonObject {
                  put(
                    "key",
                    JsonPrimitive("value"),
                  )
                },
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/batch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"action":"clear","body":{"key":"value"}}]}""", it.body)
      },
    )
  }

  @Test
  fun `allows batch method with 'delete' action`() = runTest {
    client.runTest(
      call = {
        batch(
          indexName = "theIndexName",
          batchWriteParams = BatchWriteParams(
            requests = listOf(
              BatchRequest(
                action = Action.values().first { it.value == "delete" },
                body = buildJsonObject {
                  put(
                    "key",
                    JsonPrimitive("value"),
                  )
                },
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/batch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"action":"delete","body":{"key":"value"}}]}""", it.body)
      },
    )
  }

  @Test
  fun `allows batch method with 'deleteObject' action`() = runTest {
    client.runTest(
      call = {
        batch(
          indexName = "theIndexName",
          batchWriteParams = BatchWriteParams(
            requests = listOf(
              BatchRequest(
                action = Action.values().first { it.value == "deleteObject" },
                body = buildJsonObject {
                  put(
                    "key",
                    JsonPrimitive("value"),
                  )
                },
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/batch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"action":"deleteObject","body":{"key":"value"}}]}""", it.body)
      },
    )
  }

  @Test
  fun `allows batch method with 'partialUpdateObject' action`() = runTest {
    client.runTest(
      call = {
        batch(
          indexName = "theIndexName",
          batchWriteParams = BatchWriteParams(
            requests = listOf(
              BatchRequest(
                action = Action.values().first { it.value == "partialUpdateObject" },
                body = buildJsonObject {
                  put(
                    "key",
                    JsonPrimitive("value"),
                  )
                },
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/batch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"action":"partialUpdateObject","body":{"key":"value"}}]}""", it.body)
      },
    )
  }

  @Test
  fun `allows batch method with 'partialUpdateObjectNoCreate' action`() = runTest {
    client.runTest(
      call = {
        batch(
          indexName = "theIndexName",
          batchWriteParams = BatchWriteParams(
            requests = listOf(
              BatchRequest(
                action = Action.values().first { it.value == "partialUpdateObjectNoCreate" },
                body = buildJsonObject {
                  put(
                    "key",
                    JsonPrimitive("value"),
                  )
                },
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/batch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"action":"partialUpdateObjectNoCreate","body":{"key":"value"}}]}""", it.body)
      },
    )
  }

  @Test
  fun `allows batch method with 'updateObject' action`() = runTest {
    client.runTest(
      call = {
        batch(
          indexName = "theIndexName",
          batchWriteParams = BatchWriteParams(
            requests = listOf(
              BatchRequest(
                action = Action.values().first { it.value == "updateObject" },
                body = buildJsonObject {
                  put(
                    "key",
                    JsonPrimitive("value"),
                  )
                },
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/batch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"action":"updateObject","body":{"key":"value"}}]}""", it.body)
      },
    )
  }

  // batchAssignUserIds

  @Test
  fun `batchAssignUserIds`() = runTest {
    client.runTest(
      call = {
        batchAssignUserIds(
          xAlgoliaUserID = "userID",
          batchAssignUserIdsParams = BatchAssignUserIdsParams(
            cluster = "theCluster",
            users = listOf("user1", "user2"),
          ),
        )
      },
      intercept = {
        assertEquals("/1/clusters/mapping/batch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"x-algolia-user-id":"userID"}""", it.headers)
        assertJsonBody("""{"cluster":"theCluster","users":["user1","user2"]}""", it.body)
      },
    )
  }

  // batchDictionaryEntries

  @Test
  fun `get batchDictionaryEntries results with minimal parameters`() = runTest {
    client.runTest(
      call = {
        batchDictionaryEntries(
          dictionaryName = DictionaryType.values().first { it.value == "compounds" },
          batchDictionaryEntriesParams = BatchDictionaryEntriesParams(
            requests = listOf(
              BatchDictionaryEntriesRequest(
                action = DictionaryAction.values().first { it.value == "addEntry" },
                body = DictionaryEntry(
                  objectID = "1",
                  language = "en",
                ),
              ),
              BatchDictionaryEntriesRequest(
                action = DictionaryAction.values().first { it.value == "deleteEntry" },
                body = DictionaryEntry(
                  objectID = "2",
                  language = "fr",
                ),
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/dictionaries/compounds/batch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"action":"addEntry","body":{"objectID":"1","language":"en"}},{"action":"deleteEntry","body":{"objectID":"2","language":"fr"}}]}""", it.body)
      },
    )
  }

  @Test
  fun `get batchDictionaryEntries results with all parameters`() = runTest {
    client.runTest(
      call = {
        batchDictionaryEntries(
          dictionaryName = DictionaryType.values().first { it.value == "compounds" },
          batchDictionaryEntriesParams = BatchDictionaryEntriesParams(
            clearExistingDictionaryEntries = false,
            requests = listOf(
              BatchDictionaryEntriesRequest(
                action = DictionaryAction.values().first { it.value == "addEntry" },
                body = DictionaryEntry(
                  objectID = "1",
                  language = "en",
                  word = "fancy",
                  words = listOf("believe", "algolia"),
                  decomposition = listOf("trust", "algolia"),
                  state = DictionaryEntryState.values().first { it.value == "enabled" },
                ),
              ),
              BatchDictionaryEntriesRequest(
                action = DictionaryAction.values().first { it.value == "deleteEntry" },
                body = DictionaryEntry(
                  objectID = "2",
                  language = "fr",
                  word = "humility",
                  words = listOf("candor", "algolia"),
                  decomposition = listOf("grit", "algolia"),
                  state = DictionaryEntryState.values().first { it.value == "enabled" },
                ),
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/dictionaries/compounds/batch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"clearExistingDictionaryEntries":false,"requests":[{"action":"addEntry","body":{"objectID":"1","language":"en","word":"fancy","words":["believe","algolia"],"decomposition":["trust","algolia"],"state":"enabled"}},{"action":"deleteEntry","body":{"objectID":"2","language":"fr","word":"humility","words":["candor","algolia"],"decomposition":["grit","algolia"],"state":"enabled"}}]}""", it.body)
      },
    )
  }

  @Test
  fun `get batchDictionaryEntries results additional properties`() = runTest {
    client.runTest(
      call = {
        batchDictionaryEntries(
          dictionaryName = DictionaryType.values().first { it.value == "compounds" },
          batchDictionaryEntriesParams = BatchDictionaryEntriesParams(
            requests = listOf(
              BatchDictionaryEntriesRequest(
                action = DictionaryAction.values().first { it.value == "addEntry" },
                body = DictionaryEntry(
                  objectID = "1",
                  language = "en",
                  additionalProperties = mapOf(
                    "additional" to JsonPrimitive("try me"),
                  ),
                ),
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/dictionaries/compounds/batch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"action":"addEntry","body":{"objectID":"1","language":"en","additional":"try me"}}]}""", it.body)
      },
    )
  }

  // browse

  @Test
  fun `browse with minimal parameters`() = runTest {
    client.runTest(
      call = {
        browse(
          indexName = "indexName",
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/browse".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{}""", it.body)
      },
    )
  }

  @Test
  fun `browse with search parameters`() = runTest {
    client.runTest(
      call = {
        browse(
          indexName = "indexName",
          browseParams = BrowseParamsObject(
            query = "myQuery",
            facetFilters = FacetFilters.ListOfMixedSearchFilters(listOf(MixedSearchFilters.String("tags:algolia"))),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/browse".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"query":"myQuery","facetFilters":["tags:algolia"]}""", it.body)
      },
    )
  }

  @Test
  fun `browse allow a cursor in parameters`() = runTest {
    client.runTest(
      call = {
        browse(
          indexName = "indexName",
          browseParams = BrowseParamsObject(
            cursor = "test",
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/browse".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"cursor":"test"}""", it.body)
      },
    )
  }

  // clearAllSynonyms

  @Test
  fun `clearAllSynonyms`() = runTest {
    client.runTest(
      call = {
        clearAllSynonyms(
          indexName = "indexName",
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/synonyms/clear".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertEmptyBody(it.body)
      },
    )
  }

  // clearObjects

  @Test
  fun `clearObjects`() = runTest {
    client.runTest(
      call = {
        clearObjects(
          indexName = "theIndexName",
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/clear".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertEmptyBody(it.body)
      },
    )
  }

  // clearRules

  @Test
  fun `clearRules`() = runTest {
    client.runTest(
      call = {
        clearRules(
          indexName = "indexName",
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/rules/clear".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertEmptyBody(it.body)
      },
    )
  }

  // del

  @Test
  fun `allow del method for a custom path with minimal parameters`() = runTest {
    client.runTest(
      call = {
        del(
          path = "/test/minimal",
        )
      },
      intercept = {
        assertEquals("/1/test/minimal".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("DELETE"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `allow del method for a custom path with all parameters`() = runTest {
    client.runTest(
      call = {
        del(
          path = "/test/all",
          parameters = mapOf("query" to "parameters"),
        )
      },
      intercept = {
        assertEquals("/1/test/all".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("DELETE"), it.method)
        assertContainsAll("""{"query":"parameters"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // deleteApiKey

  @Test
  fun `deleteApiKey`() = runTest {
    client.runTest(
      call = {
        deleteApiKey(
          key = "myTestApiKey",
        )
      },
      intercept = {
        assertEquals("/1/keys/myTestApiKey".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("DELETE"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // deleteBy

  @Test
  fun `deleteBy`() = runTest {
    client.runTest(
      call = {
        deleteBy(
          indexName = "theIndexName",
          deleteByParams = DeleteByParams(
            filters = "brand:brandName",
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/deleteByQuery".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"filters":"brand:brandName"}""", it.body)
      },
    )
  }

  // deleteIndex

  @Test
  fun `deleteIndex`() = runTest {
    client.runTest(
      call = {
        deleteIndex(
          indexName = "theIndexName",
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("DELETE"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // deleteObject

  @Test
  fun `deleteObject`() = runTest {
    client.runTest(
      call = {
        deleteObject(
          indexName = "theIndexName",
          objectID = "uniqueID",
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/uniqueID".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("DELETE"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // deleteRule

  @Test
  fun `deleteRule`() = runTest {
    client.runTest(
      call = {
        deleteRule(
          indexName = "indexName",
          objectID = "id1",
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/rules/id1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("DELETE"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // deleteSource

  @Test
  fun `deleteSource`() = runTest {
    client.runTest(
      call = {
        deleteSource(
          source = "theSource",
        )
      },
      intercept = {
        assertEquals("/1/security/sources/theSource".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("DELETE"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // deleteSynonym

  @Test
  fun `deleteSynonym`() = runTest {
    client.runTest(
      call = {
        deleteSynonym(
          indexName = "indexName",
          objectID = "id1",
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/synonyms/id1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("DELETE"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // get

  @Test
  fun `allow get method for a custom path with minimal parameters`() = runTest {
    client.runTest(
      call = {
        get(
          path = "/test/minimal",
        )
      },
      intercept = {
        assertEquals("/1/test/minimal".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `allow get method for a custom path with all parameters`() = runTest {
    client.runTest(
      call = {
        get(
          path = "/test/all",
          parameters = mapOf("query" to "parameters"),
        )
      },
      intercept = {
        assertEquals("/1/test/all".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"query":"parameters"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getApiKey

  @Test
  fun `getApiKey`() = runTest {
    client.runTest(
      call = {
        getApiKey(
          key = "myTestApiKey",
        )
      },
      intercept = {
        assertEquals("/1/keys/myTestApiKey".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // getDictionaryLanguages

  @Test
  fun `get getDictionaryLanguages`() = runTest {
    client.runTest(
      call = {
        getDictionaryLanguages()
      },
      intercept = {
        assertEquals("/1/dictionaries/*/languages".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // getDictionarySettings

  @Test
  fun `get getDictionarySettings results`() = runTest {
    client.runTest(
      call = {
        getDictionarySettings()
      },
      intercept = {
        assertEquals("/1/dictionaries/*/settings".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // getLogs

  @Test
  fun `getLogs with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getLogs()
      },
      intercept = {
        assertEquals("/1/logs".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `getLogs with parameters`() = runTest {
    client.runTest(
      call = {
        getLogs(
          offset = 5,
          length = 10,
          indexName = "theIndexName",
          type = LogType.values().first { it.value == "all" },
        )
      },
      intercept = {
        assertEquals("/1/logs".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"offset":"5","length":"10","indexName":"theIndexName","type":"all"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getObject

  @Test
  fun `getObject`() = runTest {
    client.runTest(
      call = {
        getObject(
          indexName = "theIndexName",
          objectID = "uniqueID",
          attributesToRetrieve = listOf("attr1", "attr2"),
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/uniqueID".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"attributesToRetrieve":"attr1,attr2"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getObjects

  @Test
  fun `getObjects`() = runTest {
    client.runTest(
      call = {
        getObjects(
          getObjectsParams = GetObjectsParams(
            requests = listOf(
              GetObjectsRequest(
                attributesToRetrieve = listOf("attr1", "attr2"),
                objectID = "uniqueID",
                indexName = "theIndexName",
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/*/objects".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"attributesToRetrieve":["attr1","attr2"],"objectID":"uniqueID","indexName":"theIndexName"}]}""", it.body)
      },
    )
  }

  // getRule

  @Test
  fun `getRule`() = runTest {
    client.runTest(
      call = {
        getRule(
          indexName = "indexName",
          objectID = "id1",
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/rules/id1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // getSettings

  @Test
  fun `getSettings`() = runTest {
    client.runTest(
      call = {
        getSettings(
          indexName = "theIndexName",
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/settings".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // getSources

  @Test
  fun `getSources`() = runTest {
    client.runTest(
      call = {
        getSources()
      },
      intercept = {
        assertEquals("/1/security/sources".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // getSynonym

  @Test
  fun `getSynonym`() = runTest {
    client.runTest(
      call = {
        getSynonym(
          indexName = "indexName",
          objectID = "id1",
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/synonyms/id1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // getTask

  @Test
  fun `getTask`() = runTest {
    client.runTest(
      call = {
        getTask(
          indexName = "theIndexName",
          taskID = 123L,
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/task/123".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // getTopUserIds

  @Test
  fun `getTopUserIds`() = runTest {
    client.runTest(
      call = {
        getTopUserIds()
      },
      intercept = {
        assertEquals("/1/clusters/mapping/top".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // getUserId

  @Test
  fun `getUserId`() = runTest {
    client.runTest(
      call = {
        getUserId(
          userID = "uniqueID",
        )
      },
      intercept = {
        assertEquals("/1/clusters/mapping/uniqueID".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // hasPendingMappings

  @Test
  fun `hasPendingMappings with minimal parameters`() = runTest {
    client.runTest(
      call = {
        hasPendingMappings()
      },
      intercept = {
        assertEquals("/1/clusters/mapping/pending".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `hasPendingMappings with parameters`() = runTest {
    client.runTest(
      call = {
        hasPendingMappings(
          getClusters = true,
        )
      },
      intercept = {
        assertEquals("/1/clusters/mapping/pending".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"getClusters":"true"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // listApiKeys

  @Test
  fun `listApiKeys`() = runTest {
    client.runTest(
      call = {
        listApiKeys()
      },
      intercept = {
        assertEquals("/1/keys".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // listClusters

  @Test
  fun `listClusters`() = runTest {
    client.runTest(
      call = {
        listClusters()
      },
      intercept = {
        assertEquals("/1/clusters".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // listIndices

  @Test
  fun `listIndices with minimal parameters`() = runTest {
    client.runTest(
      call = {
        listIndices()
      },
      intercept = {
        assertEquals("/1/indexes".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `listIndices with parameters`() = runTest {
    client.runTest(
      call = {
        listIndices(
          page = 8,
          hitsPerPage = 3,
        )
      },
      intercept = {
        assertEquals("/1/indexes".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"page":"8","hitsPerPage":"3"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // listUserIds

  @Test
  fun `listUserIds with minimal parameters`() = runTest {
    client.runTest(
      call = {
        listUserIds()
      },
      intercept = {
        assertEquals("/1/clusters/mapping".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `listUserIds with parameters`() = runTest {
    client.runTest(
      call = {
        listUserIds(
          page = 8,
          hitsPerPage = 100,
        )
      },
      intercept = {
        assertEquals("/1/clusters/mapping".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"page":"8","hitsPerPage":"100"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // multipleBatch

  @Test
  fun `multipleBatch`() = runTest {
    client.runTest(
      call = {
        multipleBatch(
          batchParams = BatchParams(
            requests = listOf(
              MultipleBatchRequest(
                action = Action.values().first { it.value == "addObject" },
                body = buildJsonObject {
                  put(
                    "key",
                    JsonPrimitive("value"),
                  )
                },
                indexName = "theIndexName",
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/*/batch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"action":"addObject","body":{"key":"value"},"indexName":"theIndexName"}]}""", it.body)
      },
    )
  }

  // operationIndex

  @Test
  fun `operationIndex`() = runTest {
    client.runTest(
      call = {
        operationIndex(
          indexName = "theIndexName",
          operationIndexParams = OperationIndexParams(
            operation = OperationType.values().first { it.value == "copy" },
            destination = "dest",
            scope = listOf(ScopeType.values().first { it.value == "rules" }, ScopeType.values().first { it.value == "settings" }),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/operation".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"operation":"copy","destination":"dest","scope":["rules","settings"]}""", it.body)
      },
    )
  }

  // partialUpdateObject

  @Test
  fun `partialUpdateObject`() = runTest {
    client.runTest(
      call = {
        partialUpdateObject(
          indexName = "theIndexName",
          objectID = "uniqueID",
          attributesToUpdate = mapOf(
            "id1" to AttributeToUpdate.String("test"),
            "id2" to BuiltInOperation(
              operation = BuiltInOperationType.values().first { it.value == "AddUnique" },
              value = "test2",
            ),
          ),
          createIfNotExists = true,
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/uniqueID/partial".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"createIfNotExists":"true"}""", it.url.parameters)
        assertJsonBody("""{"id1":"test","id2":{"_operation":"AddUnique","value":"test2"}}""", it.body)
      },
    )
  }

  // post

  @Test
  fun `allow post method for a custom path with minimal parameters`() = runTest {
    client.runTest(
      call = {
        post(
          path = "/test/minimal",
        )
      },
      intercept = {
        assertEquals("/1/test/minimal".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{}""", it.body)
      },
    )
  }

  @Test
  fun `allow post method for a custom path with all parameters`() = runTest {
    client.runTest(
      call = {
        post(
          path = "/test/all",
          parameters = mapOf("query" to "parameters"),
          body = buildJsonObject {
            put(
              "body",
              JsonPrimitive("parameters"),
            )
          },
        )
      },
      intercept = {
        assertEquals("/1/test/all".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"query":"parameters"}""", it.url.parameters)
        assertJsonBody("""{"body":"parameters"}""", it.body)
      },
    )
  }

  @Test
  fun `requestOptions can override default query parameters`() = runTest {
    client.runTest(
      call = {
        post(
          path = "/test/requestOptions",
          parameters = mapOf("query" to "parameters"),
          body = buildJsonObject {
            put(
              "facet",
              JsonPrimitive("filters"),
            )
          },
          requestOptions = RequestOptions(
            urlParameters = buildMap {
              put("query", "myQueryParameter")
            },
          ),
        )
      },
      intercept = {
        assertEquals("/1/test/requestOptions".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"query":"myQueryParameter"}""", it.url.parameters)
        assertJsonBody("""{"facet":"filters"}""", it.body)
      },
    )
  }

  @Test
  fun `requestOptions merges query parameters with default ones`() = runTest {
    client.runTest(
      call = {
        post(
          path = "/test/requestOptions",
          parameters = mapOf("query" to "parameters"),
          body = buildJsonObject {
            put(
              "facet",
              JsonPrimitive("filters"),
            )
          },
          requestOptions = RequestOptions(
            urlParameters = buildMap {
              put("query2", "myQueryParameter")
            },
          ),
        )
      },
      intercept = {
        assertEquals("/1/test/requestOptions".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"query":"parameters","query2":"myQueryParameter"}""", it.url.parameters)
        assertJsonBody("""{"facet":"filters"}""", it.body)
      },
    )
  }

  @Test
  fun `requestOptions can override default headers`() = runTest {
    client.runTest(
      call = {
        post(
          path = "/test/requestOptions",
          parameters = mapOf("query" to "parameters"),
          body = buildJsonObject {
            put(
              "facet",
              JsonPrimitive("filters"),
            )
          },
          requestOptions = RequestOptions(
            headers = buildMap {
              put("x-algolia-api-key", "myApiKey")
            },
          ),
        )
      },
      intercept = {
        assertEquals("/1/test/requestOptions".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"x-algolia-api-key":"myApiKey"}""", it.headers)
        assertContainsAll("""{"query":"parameters"}""", it.url.parameters)
        assertJsonBody("""{"facet":"filters"}""", it.body)
      },
    )
  }

  @Test
  fun `requestOptions merges headers with default ones`() = runTest {
    client.runTest(
      call = {
        post(
          path = "/test/requestOptions",
          parameters = mapOf("query" to "parameters"),
          body = buildJsonObject {
            put(
              "facet",
              JsonPrimitive("filters"),
            )
          },
          requestOptions = RequestOptions(
            headers = buildMap {
              put("x-algolia-api-key", "myApiKey")
            },
          ),
        )
      },
      intercept = {
        assertEquals("/1/test/requestOptions".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"x-algolia-api-key":"myApiKey"}""", it.headers)
        assertContainsAll("""{"query":"parameters"}""", it.url.parameters)
        assertJsonBody("""{"facet":"filters"}""", it.body)
      },
    )
  }

  @Test
  fun `requestOptions queryParameters accepts booleans`() = runTest {
    client.runTest(
      call = {
        post(
          path = "/test/requestOptions",
          parameters = mapOf("query" to "parameters"),
          body = buildJsonObject {
            put(
              "facet",
              JsonPrimitive("filters"),
            )
          },
          requestOptions = RequestOptions(
            urlParameters = buildMap {
              put("isItWorking", true)
            },
          ),
        )
      },
      intercept = {
        assertEquals("/1/test/requestOptions".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"query":"parameters","isItWorking":"true"}""", it.url.parameters)
        assertJsonBody("""{"facet":"filters"}""", it.body)
      },
    )
  }

  @Test
  fun `requestOptions queryParameters accepts integers`() = runTest {
    client.runTest(
      call = {
        post(
          path = "/test/requestOptions",
          parameters = mapOf("query" to "parameters"),
          body = buildJsonObject {
            put(
              "facet",
              JsonPrimitive("filters"),
            )
          },
          requestOptions = RequestOptions(
            urlParameters = buildMap {
              put("myParam", 2)
            },
          ),
        )
      },
      intercept = {
        assertEquals("/1/test/requestOptions".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"query":"parameters","myParam":"2"}""", it.url.parameters)
        assertJsonBody("""{"facet":"filters"}""", it.body)
      },
    )
  }

  @Test
  fun `requestOptions queryParameters accepts list of string`() = runTest {
    client.runTest(
      call = {
        post(
          path = "/test/requestOptions",
          parameters = mapOf("query" to "parameters"),
          body = buildJsonObject {
            put(
              "facet",
              JsonPrimitive("filters"),
            )
          },
          requestOptions = RequestOptions(
            urlParameters = buildMap {
              put("myParam", listOf("c", "d"))
            },
          ),
        )
      },
      intercept = {
        assertEquals("/1/test/requestOptions".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"query":"parameters","myParam":"c,d"}""", it.url.parameters)
        assertJsonBody("""{"facet":"filters"}""", it.body)
      },
    )
  }

  @Test
  fun `requestOptions queryParameters accepts list of booleans`() = runTest {
    client.runTest(
      call = {
        post(
          path = "/test/requestOptions",
          parameters = mapOf("query" to "parameters"),
          body = buildJsonObject {
            put(
              "facet",
              JsonPrimitive("filters"),
            )
          },
          requestOptions = RequestOptions(
            urlParameters = buildMap {
              put("myParam", listOf(true, true, false))
            },
          ),
        )
      },
      intercept = {
        assertEquals("/1/test/requestOptions".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"query":"parameters","myParam":"true,true,false"}""", it.url.parameters)
        assertJsonBody("""{"facet":"filters"}""", it.body)
      },
    )
  }

  @Test
  fun `requestOptions queryParameters accepts list of integers`() = runTest {
    client.runTest(
      call = {
        post(
          path = "/test/requestOptions",
          parameters = mapOf("query" to "parameters"),
          body = buildJsonObject {
            put(
              "facet",
              JsonPrimitive("filters"),
            )
          },
          requestOptions = RequestOptions(
            urlParameters = buildMap {
              put("myParam", listOf(1, 2))
            },
          ),
        )
      },
      intercept = {
        assertEquals("/1/test/requestOptions".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"query":"parameters","myParam":"1,2"}""", it.url.parameters)
        assertJsonBody("""{"facet":"filters"}""", it.body)
      },
    )
  }

  // put

  @Test
  fun `allow put method for a custom path with minimal parameters`() = runTest {
    client.runTest(
      call = {
        put(
          path = "/test/minimal",
        )
      },
      intercept = {
        assertEquals("/1/test/minimal".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertJsonBody("""{}""", it.body)
      },
    )
  }

  @Test
  fun `allow put method for a custom path with all parameters`() = runTest {
    client.runTest(
      call = {
        put(
          path = "/test/all",
          parameters = mapOf("query" to "parameters"),
          body = buildJsonObject {
            put(
              "body",
              JsonPrimitive("parameters"),
            )
          },
        )
      },
      intercept = {
        assertEquals("/1/test/all".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertContainsAll("""{"query":"parameters"}""", it.url.parameters)
        assertJsonBody("""{"body":"parameters"}""", it.body)
      },
    )
  }

  // removeUserId

  @Test
  fun `removeUserId`() = runTest {
    client.runTest(
      call = {
        removeUserId(
          userID = "uniqueID",
        )
      },
      intercept = {
        assertEquals("/1/clusters/mapping/uniqueID".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("DELETE"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // replaceSources

  @Test
  fun `replaceSources`() = runTest {
    client.runTest(
      call = {
        replaceSources(
          source = listOf(
            Source(
              source = "theSource",
              description = "theDescription",
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/security/sources".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertJsonBody("""[{"source":"theSource","description":"theDescription"}]""", it.body)
      },
    )
  }

  // restoreApiKey

  @Test
  fun `restoreApiKey`() = runTest {
    client.runTest(
      call = {
        restoreApiKey(
          key = "myApiKey",
        )
      },
      intercept = {
        assertEquals("/1/keys/myApiKey/restore".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertEmptyBody(it.body)
      },
    )
  }

  // saveObject

  @Test
  fun `saveObject`() = runTest {
    client.runTest(
      call = {
        saveObject(
          indexName = "theIndexName",
          body = buildJsonObject {
            put(
              "objectID",
              JsonPrimitive("id"),
            )
            put(
              "test",
              JsonPrimitive("val"),
            )
          },
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"objectID":"id","test":"val"}""", it.body)
      },
    )
  }

  // saveRule

  @Test
  fun `saveRule with minimal parameters`() = runTest {
    client.runTest(
      call = {
        saveRule(
          indexName = "indexName",
          objectID = "id1",
          rule = Rule(
            objectID = "id1",
            conditions = listOf(
              Condition(
                pattern = "apple",
                anchoring = Anchoring.values().first { it.value == "contains" },
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/rules/id1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertJsonBody("""{"objectID":"id1","conditions":[{"pattern":"apple","anchoring":"contains"}]}""", it.body)
      },
    )
  }

  @Test
  fun `saveRule with all parameters`() = runTest {
    client.runTest(
      call = {
        saveRule(
          indexName = "indexName",
          objectID = "id1",
          rule = Rule(
            objectID = "id1",
            conditions = listOf(
              Condition(
                pattern = "apple",
                anchoring = Anchoring.values().first { it.value == "contains" },
                alternatives = false,
                context = "search",
              ),
            ),
            consequence = Consequence(
              params = ConsequenceParams(
                filters = "brand:apple",
                query = ConsequenceQueryObject(
                  remove = listOf("algolia"),
                  edits = listOf(
                    Edit(
                      type = EditType.values().first { it.value == "remove" },
                      delete = "abc",
                      insert = "cde",
                    ),
                    Edit(
                      type = EditType.values().first { it.value == "replace" },
                      delete = "abc",
                      insert = "cde",
                    ),
                  ),
                ),
              ),
              hide = listOf(
                ConsequenceHide(
                  objectID = "321",
                ),
              ),
              filterPromotes = false,
              userData = buildJsonObject {
                put(
                  "algolia",
                  JsonPrimitive("aloglia"),
                )
              },
              promote = listOf(
                PromoteObjectID(
                  objectID = "abc",
                  position = 3,
                ),
                PromoteObjectIDs(
                  objectIDs = listOf("abc", "def"),
                  position = 1,
                ),
              ),
            ),
            description = "test",
            enabled = true,
            validity = listOf(
              TimeRange(
                from = 1656670273,
                until = 1656670277,
              ),
            ),
          ),
          forwardToReplicas = true,
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/rules/id1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertContainsAll("""{"forwardToReplicas":"true"}""", it.url.parameters)
        assertJsonBody("""{"objectID":"id1","conditions":[{"pattern":"apple","anchoring":"contains","alternatives":false,"context":"search"}],"consequence":{"params":{"filters":"brand:apple","query":{"remove":["algolia"],"edits":[{"type":"remove","delete":"abc","insert":"cde"},{"type":"replace","delete":"abc","insert":"cde"}]}},"hide":[{"objectID":"321"}],"filterPromotes":false,"userData":{"algolia":"aloglia"},"promote":[{"objectID":"abc","position":3},{"objectIDs":["abc","def"],"position":1}]},"description":"test","enabled":true,"validity":[{"from":1656670273,"until":1656670277}]}""", it.body)
      },
    )
  }

  // saveRules

  @Test
  fun `saveRules with minimal parameters`() = runTest {
    client.runTest(
      call = {
        saveRules(
          indexName = "indexName",
          rules = listOf(
            Rule(
              objectID = "a-rule-id",
              conditions = listOf(
                Condition(
                  pattern = "smartphone",
                  anchoring = Anchoring.values().first { it.value == "contains" },
                ),
              ),
            ),
            Rule(
              objectID = "a-second-rule-id",
              conditions = listOf(
                Condition(
                  pattern = "apple",
                  anchoring = Anchoring.values().first { it.value == "contains" },
                ),
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/rules/batch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""[{"objectID":"a-rule-id","conditions":[{"pattern":"smartphone","anchoring":"contains"}]},{"objectID":"a-second-rule-id","conditions":[{"pattern":"apple","anchoring":"contains"}]}]""", it.body)
      },
    )
  }

  @Test
  fun `saveRules with all parameters`() = runTest {
    client.runTest(
      call = {
        saveRules(
          indexName = "indexName",
          rules = listOf(
            Rule(
              objectID = "id1",
              conditions = listOf(
                Condition(
                  pattern = "apple",
                  anchoring = Anchoring.values().first { it.value == "contains" },
                  alternatives = false,
                  context = "search",
                ),
              ),
              consequence = Consequence(
                params = ConsequenceParams(
                  filters = "brand:apple",
                  query = ConsequenceQueryObject(
                    remove = listOf("algolia"),
                    edits = listOf(
                      Edit(
                        type = EditType.values().first { it.value == "remove" },
                        delete = "abc",
                        insert = "cde",
                      ),
                      Edit(
                        type = EditType.values().first { it.value == "replace" },
                        delete = "abc",
                        insert = "cde",
                      ),
                    ),
                  ),
                ),
                hide = listOf(
                  ConsequenceHide(
                    objectID = "321",
                  ),
                ),
                filterPromotes = false,
                userData = buildJsonObject {
                  put(
                    "algolia",
                    JsonPrimitive("aloglia"),
                  )
                },
                promote = listOf(
                  PromoteObjectID(
                    objectID = "abc",
                    position = 3,
                  ),
                  PromoteObjectIDs(
                    objectIDs = listOf("abc", "def"),
                    position = 1,
                  ),
                ),
              ),
              description = "test",
              enabled = true,
              validity = listOf(
                TimeRange(
                  from = 1656670273,
                  until = 1656670277,
                ),
              ),
            ),
          ),
          forwardToReplicas = true,
          clearExistingRules = true,
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/rules/batch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"forwardToReplicas":"true","clearExistingRules":"true"}""", it.url.parameters)
        assertJsonBody("""[{"objectID":"id1","conditions":[{"pattern":"apple","anchoring":"contains","alternatives":false,"context":"search"}],"consequence":{"params":{"filters":"brand:apple","query":{"remove":["algolia"],"edits":[{"type":"remove","delete":"abc","insert":"cde"},{"type":"replace","delete":"abc","insert":"cde"}]}},"hide":[{"objectID":"321"}],"filterPromotes":false,"userData":{"algolia":"aloglia"},"promote":[{"objectID":"abc","position":3},{"objectIDs":["abc","def"],"position":1}]},"description":"test","enabled":true,"validity":[{"from":1656670273,"until":1656670277}]}]""", it.body)
      },
    )
  }

  // saveSynonym

  @Test
  fun `saveSynonym`() = runTest {
    client.runTest(
      call = {
        saveSynonym(
          indexName = "indexName",
          objectID = "id1",
          synonymHit = SynonymHit(
            objectID = "id1",
            type = SynonymType.values().first { it.value == "synonym" },
            synonyms = listOf("car", "vehicule", "auto"),
          ),
          forwardToReplicas = true,
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/synonyms/id1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertContainsAll("""{"forwardToReplicas":"true"}""", it.url.parameters)
        assertJsonBody("""{"objectID":"id1","type":"synonym","synonyms":["car","vehicule","auto"]}""", it.body)
      },
    )
  }

  // saveSynonyms

  @Test
  fun `saveSynonyms`() = runTest {
    client.runTest(
      call = {
        saveSynonyms(
          indexName = "indexName",
          synonymHit = listOf(
            SynonymHit(
              objectID = "id1",
              type = SynonymType.values().first { it.value == "synonym" },
              synonyms = listOf("car", "vehicule", "auto"),
            ),
            SynonymHit(
              objectID = "id2",
              type = SynonymType.values().first { it.value == "onewaysynonym" },
              input = "iphone",
              synonyms = listOf("ephone", "aphone", "yphone"),
            ),
          ),
          forwardToReplicas = true,
          replaceExistingSynonyms = false,
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/synonyms/batch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"forwardToReplicas":"true","replaceExistingSynonyms":"false"}""", it.url.parameters)
        assertJsonBody("""[{"objectID":"id1","type":"synonym","synonyms":["car","vehicule","auto"]},{"objectID":"id2","type":"onewaysynonym","input":"iphone","synonyms":["ephone","aphone","yphone"]}]""", it.body)
      },
    )
  }

  // search

  @Test
  fun `search for a single hits request with minimal parameters`() = runTest {
    client.runTest(
      call = {
        search(
          searchMethodParams = SearchMethodParams(
            requests = listOf(
              SearchForHits(
                indexName = "theIndexName",
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/*/queries".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"indexName":"theIndexName"}]}""", it.body)
      },
    )
  }

  @Test
  fun `search for a single facet request with minimal parameters`() = runTest {
    client.runTest(
      call = {
        search(
          searchMethodParams = SearchMethodParams(
            requests = listOf(
              SearchForFacets(
                indexName = "theIndexName",
                type = SearchTypeFacet.values().first { it.value == "facet" },
                facet = "theFacet",
              ),
            ),
            strategy = SearchStrategy.values().first { it.value == "stopIfEnoughMatches" },
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/*/queries".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"indexName":"theIndexName","type":"facet","facet":"theFacet"}],"strategy":"stopIfEnoughMatches"}""", it.body)
      },
    )
  }

  @Test
  fun `search for a single hits request with all parameters`() = runTest {
    client.runTest(
      call = {
        search(
          searchMethodParams = SearchMethodParams(
            requests = listOf(
              SearchForHits(
                indexName = "theIndexName",
                query = "myQuery",
                hitsPerPage = 50,
                type = SearchTypeDefault.values().first { it.value == "default" },
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/*/queries".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"indexName":"theIndexName","query":"myQuery","hitsPerPage":50,"type":"default"}]}""", it.body)
      },
    )
  }

  @Test
  fun `search for a single facet request with all parameters`() = runTest {
    client.runTest(
      call = {
        search(
          searchMethodParams = SearchMethodParams(
            requests = listOf(
              SearchForFacets(
                indexName = "theIndexName",
                type = SearchTypeFacet.values().first { it.value == "facet" },
                facet = "theFacet",
                facetQuery = "theFacetQuery",
                query = "theQuery",
                maxFacetHits = 50,
              ),
            ),
            strategy = SearchStrategy.values().first { it.value == "stopIfEnoughMatches" },
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/*/queries".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"indexName":"theIndexName","type":"facet","facet":"theFacet","facetQuery":"theFacetQuery","query":"theQuery","maxFacetHits":50}],"strategy":"stopIfEnoughMatches"}""", it.body)
      },
    )
  }

  @Test
  fun `search for multiple mixed requests in multiple indices with minimal parameters`() = runTest {
    client.runTest(
      call = {
        search(
          searchMethodParams = SearchMethodParams(
            requests = listOf(
              SearchForHits(
                indexName = "theIndexName",
              ),
              SearchForFacets(
                indexName = "theIndexName2",
                type = SearchTypeFacet.values().first { it.value == "facet" },
                facet = "theFacet",
              ),
              SearchForHits(
                indexName = "theIndexName",
                type = SearchTypeDefault.values().first { it.value == "default" },
              ),
            ),
            strategy = SearchStrategy.values().first { it.value == "stopIfEnoughMatches" },
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/*/queries".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"indexName":"theIndexName"},{"indexName":"theIndexName2","type":"facet","facet":"theFacet"},{"indexName":"theIndexName","type":"default"}],"strategy":"stopIfEnoughMatches"}""", it.body)
      },
    )
  }

  @Test
  fun `search for multiple mixed requests in multiple indices with all parameters`() = runTest {
    client.runTest(
      call = {
        search(
          searchMethodParams = SearchMethodParams(
            requests = listOf(
              SearchForFacets(
                indexName = "theIndexName",
                type = SearchTypeFacet.values().first { it.value == "facet" },
                facet = "theFacet",
                facetQuery = "theFacetQuery",
                query = "theQuery",
                maxFacetHits = 50,
              ),
              SearchForHits(
                indexName = "theIndexName",
                query = "myQuery",
                hitsPerPage = 50,
                type = SearchTypeDefault.values().first { it.value == "default" },
              ),
            ),
            strategy = SearchStrategy.values().first { it.value == "stopIfEnoughMatches" },
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/*/queries".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"indexName":"theIndexName","type":"facet","facet":"theFacet","facetQuery":"theFacetQuery","query":"theQuery","maxFacetHits":50},{"indexName":"theIndexName","query":"myQuery","hitsPerPage":50,"type":"default"}],"strategy":"stopIfEnoughMatches"}""", it.body)
      },
    )
  }

  @Test
  fun `search filters accept all of the possible shapes`() = runTest {
    client.runTest(
      call = {
        search(
          searchMethodParams = SearchMethodParams(
            requests = listOf(
              SearchForHits(
                indexName = "theIndexName",
                facetFilters = FacetFilters.String("mySearch:filters"),
                reRankingApplyFilter = ReRankingApplyFilter.String("mySearch:filters"),
                tagFilters = TagFilters.String("mySearch:filters"),
                numericFilters = NumericFilters.String("mySearch:filters"),
                optionalFilters = OptionalFilters.String("mySearch:filters"),
              ),
              SearchForHits(
                indexName = "theIndexName",
                facetFilters = FacetFilters.ListOfMixedSearchFilters(listOf(MixedSearchFilters.String("mySearch:filters"), MixedSearchFilters.ListOfString(listOf("mySearch:filters")))),
                reRankingApplyFilter = ReRankingApplyFilter.ListOfMixedSearchFilters(listOf(MixedSearchFilters.String("mySearch:filters"), MixedSearchFilters.ListOfString(listOf("mySearch:filters")))),
                tagFilters = TagFilters.ListOfMixedSearchFilters(listOf(MixedSearchFilters.String("mySearch:filters"), MixedSearchFilters.ListOfString(listOf("mySearch:filters")))),
                numericFilters = NumericFilters.ListOfMixedSearchFilters(listOf(MixedSearchFilters.String("mySearch:filters"), MixedSearchFilters.ListOfString(listOf("mySearch:filters")))),
                optionalFilters = OptionalFilters.ListOfMixedSearchFilters(listOf(MixedSearchFilters.String("mySearch:filters"), MixedSearchFilters.ListOfString(listOf("mySearch:filters")))),
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/*/queries".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"indexName":"theIndexName","facetFilters":"mySearch:filters","reRankingApplyFilter":"mySearch:filters","tagFilters":"mySearch:filters","numericFilters":"mySearch:filters","optionalFilters":"mySearch:filters"},{"indexName":"theIndexName","facetFilters":["mySearch:filters",["mySearch:filters"]],"reRankingApplyFilter":["mySearch:filters",["mySearch:filters"]],"tagFilters":["mySearch:filters",["mySearch:filters"]],"numericFilters":["mySearch:filters",["mySearch:filters"]],"optionalFilters":["mySearch:filters",["mySearch:filters"]]}]}""", it.body)
      },
    )
  }

  @Test
  fun `search with all search parameters`() = runTest {
    client.runTest(
      call = {
        search(
          searchMethodParams = SearchMethodParams(
            requests = listOf(
              SearchForHits(
                indexName = "theIndexName",
                query = "",
                similarQuery = "",
                filters = "",
                facetFilters = FacetFilters.ListOfMixedSearchFilters(listOf(MixedSearchFilters.String(""))),
                optionalFilters = OptionalFilters.ListOfMixedSearchFilters(listOf(MixedSearchFilters.String(""))),
                numericFilters = NumericFilters.ListOfMixedSearchFilters(listOf(MixedSearchFilters.String(""))),
                tagFilters = TagFilters.ListOfMixedSearchFilters(listOf(MixedSearchFilters.String(""))),
                sumOrFiltersScores = true,
                facets = listOf(""),
                maxValuesPerFacet = 0,
                facetingAfterDistinct = true,
                sortFacetValuesBy = "",
                page = 0,
                offset = 0,
                length = 0,
                aroundLatLng = "",
                aroundLatLngViaIP = true,
                aroundRadius = AroundRadiusAll.values().first { it.value == "all" },
                aroundPrecision = 0,
                minimumAroundRadius = 0,
                insideBoundingBox = listOf(47.3165, 4.9665),
                insidePolygon = listOf(47.3165, 4.9665),
                naturalLanguages = listOf(""),
                ruleContexts = listOf(""),
                personalizationImpact = 0,
                userToken = "",
                getRankingInfo = true,
                clickAnalytics = true,
                analytics = true,
                analyticsTags = listOf(""),
                percentileComputation = true,
                enableABTest = true,
                enableReRanking = true,
                reRankingApplyFilter = ReRankingApplyFilter.ListOfMixedSearchFilters(listOf(MixedSearchFilters.String(""))),
                attributesForFaceting = listOf(""),
                attributesToRetrieve = listOf(""),
                restrictSearchableAttributes = listOf(""),
                ranking = listOf(""),
                customRanking = listOf(""),
                relevancyStrictness = 0,
                attributesToHighlight = listOf(""),
                attributesToSnippet = listOf(""),
                highlightPreTag = "",
                highlightPostTag = "",
                snippetEllipsisText = "",
                restrictHighlightAndSnippetArrays = true,
                hitsPerPage = 0,
                minWordSizefor1Typo = 0,
                minWordSizefor2Typos = 0,
                typoTolerance = TypoToleranceEnum.values().first { it.value == "min" },
                allowTyposOnNumericTokens = true,
                disableTypoToleranceOnAttributes = listOf(""),
                ignorePlurals = IgnorePlurals.Boolean(false),
                removeStopWords = RemoveStopWords.Boolean(true),
                keepDiacriticsOnCharacters = "",
                queryLanguages = listOf(""),
                decompoundQuery = true,
                enableRules = true,
                enablePersonalization = true,
                queryType = QueryType.values().first { it.value == "prefixAll" },
                removeWordsIfNoResults = RemoveWordsIfNoResults.values().first { it.value == "allOptional" },
                advancedSyntax = true,
                optionalWords = listOf(""),
                disableExactOnAttributes = listOf(""),
                exactOnSingleWordQuery = ExactOnSingleWordQuery.values().first { it.value == "attribute" },
                alternativesAsExact = listOf(AlternativesAsExact.values().first { it.value == "multiWordsSynonym" }),
                advancedSyntaxFeatures = listOf(AdvancedSyntaxFeatures.values().first { it.value == "exactPhrase" }),
                distinct = Distinct.Number(0.toNumberType()),
                synonyms = true,
                replaceSynonymsInHighlight = true,
                minProximity = 0,
                responseFields = listOf(""),
                attributeCriteriaComputedByMinProximity = true,
                renderingContent = RenderingContent(
                  facetOrdering = FacetOrdering(
                    facets = Facets(
                      order = listOf("a", "b"),
                    ),
                    values = mapOf(
                      "a" to Value(
                        order = listOf("b"),
                        sortRemainingBy = SortRemainingBy.values().first { it.value == "count" },
                      ),
                    ),
                  ),
                ),
                type = SearchTypeDefault.values().first { it.value == "default" },
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/*/queries".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"requests":[{"indexName":"theIndexName","query":"","similarQuery":"","filters":"","facetFilters":[""],"optionalFilters":[""],"numericFilters":[""],"tagFilters":[""],"sumOrFiltersScores":true,"facets":[""],"maxValuesPerFacet":0,"facetingAfterDistinct":true,"sortFacetValuesBy":"","page":0,"offset":0,"length":0,"aroundLatLng":"","aroundLatLngViaIP":true,"aroundRadius":"all","aroundPrecision":0,"minimumAroundRadius":0,"insideBoundingBox":[47.3165,4.9665],"insidePolygon":[47.3165,4.9665],"naturalLanguages":[""],"ruleContexts":[""],"personalizationImpact":0,"userToken":"","getRankingInfo":true,"clickAnalytics":true,"analytics":true,"analyticsTags":[""],"percentileComputation":true,"enableABTest":true,"enableReRanking":true,"reRankingApplyFilter":[""],"attributesForFaceting":[""],"attributesToRetrieve":[""],"restrictSearchableAttributes":[""],"ranking":[""],"customRanking":[""],"relevancyStrictness":0,"attributesToHighlight":[""],"attributesToSnippet":[""],"highlightPreTag":"","highlightPostTag":"","snippetEllipsisText":"","restrictHighlightAndSnippetArrays":true,"hitsPerPage":0,"minWordSizefor1Typo":0,"minWordSizefor2Typos":0,"typoTolerance":"min","allowTyposOnNumericTokens":true,"disableTypoToleranceOnAttributes":[""],"ignorePlurals":false,"removeStopWords":true,"keepDiacriticsOnCharacters":"","queryLanguages":[""],"decompoundQuery":true,"enableRules":true,"enablePersonalization":true,"queryType":"prefixAll","removeWordsIfNoResults":"allOptional","advancedSyntax":true,"optionalWords":[""],"disableExactOnAttributes":[""],"exactOnSingleWordQuery":"attribute","alternativesAsExact":["multiWordsSynonym"],"advancedSyntaxFeatures":["exactPhrase"],"distinct":0,"synonyms":true,"replaceSynonymsInHighlight":true,"minProximity":0,"responseFields":[""],"attributeCriteriaComputedByMinProximity":true,"renderingContent":{"facetOrdering":{"facets":{"order":["a","b"]},"values":{"a":{"order":["b"],"sortRemainingBy":"count"}}}},"type":"default"}]}""", it.body)
      },
    )
  }

  // searchDictionaryEntries

  @Test
  fun `get searchDictionaryEntries results with minimal parameters`() = runTest {
    client.runTest(
      call = {
        searchDictionaryEntries(
          dictionaryName = DictionaryType.values().first { it.value == "compounds" },
          searchDictionaryEntriesParams = SearchDictionaryEntriesParams(
            query = "foo",
          ),
        )
      },
      intercept = {
        assertEquals("/1/dictionaries/compounds/search".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"query":"foo"}""", it.body)
      },
    )
  }

  @Test
  fun `get searchDictionaryEntries results with all parameters`() = runTest {
    client.runTest(
      call = {
        searchDictionaryEntries(
          dictionaryName = DictionaryType.values().first { it.value == "compounds" },
          searchDictionaryEntriesParams = SearchDictionaryEntriesParams(
            query = "foo",
            page = 4,
            hitsPerPage = 2,
            language = "fr",
          ),
        )
      },
      intercept = {
        assertEquals("/1/dictionaries/compounds/search".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"query":"foo","page":4,"hitsPerPage":2,"language":"fr"}""", it.body)
      },
    )
  }

  // searchForFacetValues

  @Test
  fun `get searchForFacetValues results with minimal parameters`() = runTest {
    client.runTest(
      call = {
        searchForFacetValues(
          indexName = "indexName",
          facetName = "facetName",
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/facets/facetName/query".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{}""", it.body)
      },
    )
  }

  @Test
  fun `get searchForFacetValues results with all parameters`() = runTest {
    client.runTest(
      call = {
        searchForFacetValues(
          indexName = "indexName",
          facetName = "facetName",
          searchForFacetValuesRequest = SearchForFacetValuesRequest(
            params = "query=foo&facetFilters=['bar']",
            facetQuery = "foo",
            maxFacetHits = 42,
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/facets/facetName/query".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"params":"query=foo&facetFilters=['bar']","facetQuery":"foo","maxFacetHits":42}""", it.body)
      },
    )
  }

  // searchRules

  @Test
  fun `searchRules`() = runTest {
    client.runTest(
      call = {
        searchRules(
          indexName = "indexName",
          searchRulesParams = SearchRulesParams(
            query = "something",
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/rules/search".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"query":"something"}""", it.body)
      },
    )
  }

  // searchSingleIndex

  @Test
  fun `search with minimal parameters`() = runTest {
    client.runTest(
      call = {
        searchSingleIndex(
          indexName = "indexName",
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/query".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{}""", it.body)
      },
    )
  }

  @Test
  fun `search with searchParams`() = runTest {
    client.runTest(
      call = {
        searchSingleIndex(
          indexName = "indexName",
          searchParams = SearchParamsObject(
            query = "myQuery",
            facetFilters = FacetFilters.ListOfMixedSearchFilters(listOf(MixedSearchFilters.String("tags:algolia"))),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/query".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"query":"myQuery","facetFilters":["tags:algolia"]}""", it.body)
      },
    )
  }

  // searchSynonyms

  @Test
  fun `searchSynonyms with minimal parameters`() = runTest {
    client.runTest(
      call = {
        searchSynonyms(
          indexName = "indexName",
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/synonyms/search".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{}""", it.body)
      },
    )
  }

  @Test
  fun `searchSynonyms with all parameters`() = runTest {
    client.runTest(
      call = {
        searchSynonyms(
          indexName = "indexName",
          type = SynonymType.values().first { it.value == "altcorrection1" },
          page = 10,
          hitsPerPage = 10,
          searchSynonymsParams = SearchSynonymsParams(
            query = "myQuery",
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/indexName/synonyms/search".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertContainsAll("""{"type":"altcorrection1","page":"10","hitsPerPage":"10"}""", it.url.parameters)
        assertJsonBody("""{"query":"myQuery"}""", it.body)
      },
    )
  }

  // searchUserIds

  @Test
  fun `searchUserIds`() = runTest {
    client.runTest(
      call = {
        searchUserIds(
          searchUserIdsParams = SearchUserIdsParams(
            query = "test",
            clusterName = "theClusterName",
            page = 5,
            hitsPerPage = 10,
          ),
        )
      },
      intercept = {
        assertEquals("/1/clusters/mapping/search".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"query":"test","clusterName":"theClusterName","page":5,"hitsPerPage":10}""", it.body)
      },
    )
  }

  // setDictionarySettings

  @Test
  fun `get setDictionarySettings results with minimal parameters`() = runTest {
    client.runTest(
      call = {
        setDictionarySettings(
          dictionarySettingsParams = DictionarySettingsParams(
            disableStandardEntries = StandardEntries(
              plurals = mapOf("fr" to false, "en" to false, "ru" to true),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/dictionaries/*/settings".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertJsonBody("""{"disableStandardEntries":{"plurals":{"fr":false,"en":false,"ru":true}}}""", it.body)
      },
    )
  }

  @Test
  fun `get setDictionarySettings results with all parameters`() = runTest {
    client.runTest(
      call = {
        setDictionarySettings(
          dictionarySettingsParams = DictionarySettingsParams(
            disableStandardEntries = StandardEntries(
              plurals = mapOf("fr" to false, "en" to false, "ru" to true),
              stopwords = mapOf("fr" to false),
              compounds = mapOf("ru" to true),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/dictionaries/*/settings".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertJsonBody("""{"disableStandardEntries":{"plurals":{"fr":false,"en":false,"ru":true},"stopwords":{"fr":false},"compounds":{"ru":true}}}""", it.body)
      },
    )
  }

  // setSettings

  @Test
  fun `setSettings with minimal parameters`() = runTest {
    client.runTest(
      call = {
        setSettings(
          indexName = "theIndexName",
          indexSettings = IndexSettings(
            paginationLimitedTo = 10,
          ),
          forwardToReplicas = true,
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/settings".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertContainsAll("""{"forwardToReplicas":"true"}""", it.url.parameters)
        assertJsonBody("""{"paginationLimitedTo":10}""", it.body)
      },
    )
  }

  @Test
  fun `setSettings allow boolean 'typoTolerance'`() = runTest {
    client.runTest(
      call = {
        setSettings(
          indexName = "theIndexName",
          indexSettings = IndexSettings(
            typoTolerance = TypoTolerance.Boolean(true),
          ),
          forwardToReplicas = true,
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/settings".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertContainsAll("""{"forwardToReplicas":"true"}""", it.url.parameters)
        assertJsonBody("""{"typoTolerance":true}""", it.body)
      },
    )
  }

  @Test
  fun `setSettings allow enum 'typoTolerance'`() = runTest {
    client.runTest(
      call = {
        setSettings(
          indexName = "theIndexName",
          indexSettings = IndexSettings(
            typoTolerance = TypoToleranceEnum.values().first { it.value == "min" },
          ),
          forwardToReplicas = true,
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/settings".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertContainsAll("""{"forwardToReplicas":"true"}""", it.url.parameters)
        assertJsonBody("""{"typoTolerance":"min"}""", it.body)
      },
    )
  }

  @Test
  fun `setSettings allow boolean 'ignorePlurals'`() = runTest {
    client.runTest(
      call = {
        setSettings(
          indexName = "theIndexName",
          indexSettings = IndexSettings(
            ignorePlurals = IgnorePlurals.Boolean(true),
          ),
          forwardToReplicas = true,
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/settings".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertContainsAll("""{"forwardToReplicas":"true"}""", it.url.parameters)
        assertJsonBody("""{"ignorePlurals":true}""", it.body)
      },
    )
  }

  @Test
  fun `setSettings allow list of string 'ignorePlurals'`() = runTest {
    client.runTest(
      call = {
        setSettings(
          indexName = "theIndexName",
          indexSettings = IndexSettings(
            ignorePlurals = IgnorePlurals.ListOfString(listOf("algolia")),
          ),
          forwardToReplicas = true,
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/settings".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertContainsAll("""{"forwardToReplicas":"true"}""", it.url.parameters)
        assertJsonBody("""{"ignorePlurals":["algolia"]}""", it.body)
      },
    )
  }

  @Test
  fun `setSettings allow boolean 'removeStopWords'`() = runTest {
    client.runTest(
      call = {
        setSettings(
          indexName = "theIndexName",
          indexSettings = IndexSettings(
            removeStopWords = RemoveStopWords.Boolean(true),
          ),
          forwardToReplicas = true,
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/settings".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertContainsAll("""{"forwardToReplicas":"true"}""", it.url.parameters)
        assertJsonBody("""{"removeStopWords":true}""", it.body)
      },
    )
  }

  @Test
  fun `setSettings allow list of string 'removeStopWords'`() = runTest {
    client.runTest(
      call = {
        setSettings(
          indexName = "theIndexName",
          indexSettings = IndexSettings(
            removeStopWords = RemoveStopWords.ListOfString(listOf("algolia")),
          ),
          forwardToReplicas = true,
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/settings".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertContainsAll("""{"forwardToReplicas":"true"}""", it.url.parameters)
        assertJsonBody("""{"removeStopWords":["algolia"]}""", it.body)
      },
    )
  }

  @Test
  fun `setSettings allow boolean 'distinct'`() = runTest {
    client.runTest(
      call = {
        setSettings(
          indexName = "theIndexName",
          indexSettings = IndexSettings(
            distinct = Distinct.Boolean(true),
          ),
          forwardToReplicas = true,
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/settings".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertContainsAll("""{"forwardToReplicas":"true"}""", it.url.parameters)
        assertJsonBody("""{"distinct":true}""", it.body)
      },
    )
  }

  @Test
  fun `setSettings allow integers for 'distinct'`() = runTest {
    client.runTest(
      call = {
        setSettings(
          indexName = "theIndexName",
          indexSettings = IndexSettings(
            distinct = Distinct.Number(1.toNumberType()),
          ),
          forwardToReplicas = true,
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/settings".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertContainsAll("""{"forwardToReplicas":"true"}""", it.url.parameters)
        assertJsonBody("""{"distinct":1}""", it.body)
      },
    )
  }

  @Test
  fun `setSettings allow all 'indexSettings'`() = runTest {
    client.runTest(
      call = {
        setSettings(
          indexName = "theIndexName",
          indexSettings = IndexSettings(
            replicas = listOf(""),
            paginationLimitedTo = 0,
            disableTypoToleranceOnWords = listOf("algolia"),
            attributesToTransliterate = listOf("algolia"),
            camelCaseAttributes = listOf("algolia"),
            decompoundedAttributes = buildJsonObject {
              put(
                "algolia",
                JsonPrimitive("aloglia"),
              )
            },
            indexLanguages = listOf("algolia"),
            disablePrefixOnAttributes = listOf("algolia"),
            allowCompressionOfIntegerArray = true,
            numericAttributesForFiltering = listOf("algolia"),
            separatorsToIndex = "algolia",
            searchableAttributes = listOf("algolia"),
            userData = buildJsonObject {
              put(
                "user",
                JsonPrimitive("data"),
              )
            },
            customNormalization = mapOf("algolia" to mapOf("aloglia" to "aglolia")),
            attributesForFaceting = listOf("algolia"),
            unretrievableAttributes = listOf("algolia"),
            attributesToRetrieve = listOf("algolia"),
            restrictSearchableAttributes = listOf("algolia"),
            ranking = listOf("geo"),
            customRanking = listOf("algolia"),
            relevancyStrictness = 10,
            attributesToHighlight = listOf("algolia"),
            attributesToSnippet = listOf("algolia"),
            highlightPreTag = "<span>",
            highlightPostTag = "</span>",
            snippetEllipsisText = "---",
            restrictHighlightAndSnippetArrays = true,
            hitsPerPage = 10,
            minWordSizefor1Typo = 5,
            minWordSizefor2Typos = 11,
            typoTolerance = TypoTolerance.Boolean(false),
            allowTyposOnNumericTokens = true,
            disableTypoToleranceOnAttributes = listOf("algolia"),
            ignorePlurals = IgnorePlurals.Boolean(false),
            removeStopWords = RemoveStopWords.Boolean(false),
            keepDiacriticsOnCharacters = "abc",
            queryLanguages = listOf("algolia"),
            decompoundQuery = false,
            enableRules = false,
            enablePersonalization = true,
            queryType = QueryType.values().first { it.value == "prefixLast" },
            removeWordsIfNoResults = RemoveWordsIfNoResults.values().first { it.value == "lastWords" },
            advancedSyntax = true,
            optionalWords = listOf("algolia"),
            disableExactOnAttributes = listOf("algolia"),
            exactOnSingleWordQuery = ExactOnSingleWordQuery.values().first { it.value == "attribute" },
            alternativesAsExact = listOf(AlternativesAsExact.values().first { it.value == "singleWordSynonym" }),
            advancedSyntaxFeatures = listOf(AdvancedSyntaxFeatures.values().first { it.value == "exactPhrase" }),
            distinct = Distinct.Number(3.toNumberType()),
            attributeForDistinct = "test",
            synonyms = false,
            replaceSynonymsInHighlight = true,
            minProximity = 6,
            responseFields = listOf("algolia"),
            maxFacetHits = 50,
            attributeCriteriaComputedByMinProximity = true,
            renderingContent = RenderingContent(
              facetOrdering = FacetOrdering(
                facets = Facets(
                  order = listOf("a", "b"),
                ),
                values = mapOf(
                  "a" to Value(
                    order = listOf("b"),
                    sortRemainingBy = SortRemainingBy.values().first { it.value == "count" },
                  ),
                ),
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/indexes/theIndexName/settings".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertJsonBody("""{"replicas":[""],"paginationLimitedTo":0,"disableTypoToleranceOnWords":["algolia"],"attributesToTransliterate":["algolia"],"camelCaseAttributes":["algolia"],"decompoundedAttributes":{"algolia":"aloglia"},"indexLanguages":["algolia"],"disablePrefixOnAttributes":["algolia"],"allowCompressionOfIntegerArray":true,"numericAttributesForFiltering":["algolia"],"separatorsToIndex":"algolia","searchableAttributes":["algolia"],"userData":{"user":"data"},"customNormalization":{"algolia":{"aloglia":"aglolia"}},"attributesForFaceting":["algolia"],"unretrievableAttributes":["algolia"],"attributesToRetrieve":["algolia"],"restrictSearchableAttributes":["algolia"],"ranking":["geo"],"customRanking":["algolia"],"relevancyStrictness":10,"attributesToHighlight":["algolia"],"attributesToSnippet":["algolia"],"highlightPreTag":"<span>","highlightPostTag":"</span>","snippetEllipsisText":"---","restrictHighlightAndSnippetArrays":true,"hitsPerPage":10,"minWordSizefor1Typo":5,"minWordSizefor2Typos":11,"typoTolerance":false,"allowTyposOnNumericTokens":true,"disableTypoToleranceOnAttributes":["algolia"],"ignorePlurals":false,"removeStopWords":false,"keepDiacriticsOnCharacters":"abc","queryLanguages":["algolia"],"decompoundQuery":false,"enableRules":false,"enablePersonalization":true,"queryType":"prefixLast","removeWordsIfNoResults":"lastWords","advancedSyntax":true,"optionalWords":["algolia"],"disableExactOnAttributes":["algolia"],"exactOnSingleWordQuery":"attribute","alternativesAsExact":["singleWordSynonym"],"advancedSyntaxFeatures":["exactPhrase"],"distinct":3,"attributeForDistinct":"test","synonyms":false,"replaceSynonymsInHighlight":true,"minProximity":6,"responseFields":["algolia"],"maxFacetHits":50,"attributeCriteriaComputedByMinProximity":true,"renderingContent":{"facetOrdering":{"facets":{"order":["a","b"]},"values":{"a":{"order":["b"],"sortRemainingBy":"count"}}}}}""", it.body)
      },
    )
  }

  // updateApiKey

  @Test
  fun `updateApiKey`() = runTest {
    client.runTest(
      call = {
        updateApiKey(
          key = "myApiKey",
          apiKey = ApiKey(
            acl = listOf(Acl.values().first { it.value == "search" }, Acl.values().first { it.value == "addObject" }),
            validity = 300,
            maxQueriesPerIPPerHour = 100,
            maxHitsPerQuery = 20,
          ),
        )
      },
      intercept = {
        assertEquals("/1/keys/myApiKey".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("PUT"), it.method)
        assertJsonBody("""{"acl":["search","addObject"],"validity":300,"maxQueriesPerIPPerHour":100,"maxHitsPerQuery":20}""", it.body)
      },
    )
  }
}
