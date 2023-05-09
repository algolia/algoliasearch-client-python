package com.algolia.methods.requests

import com.algolia.client.api.PredictClient
import com.algolia.client.configuration.*
import com.algolia.client.model.predict.*
import com.algolia.client.transport.*
import com.algolia.extension.*
import com.algolia.utils.*
import io.ktor.http.*
import kotlinx.coroutines.test.*
import kotlinx.serialization.json.*
import kotlin.test.*

class PredictTest {

  val client = PredictClient(
    appId = "appId",
    apiKey = "apiKey",
    region = "eu",
  )

  // activateModelInstance

  @Test
  fun `activate a model instance`() = runTest {
    client.runTest(
      call = {
        activateModelInstance(
          activateModelParams = ActivateModelParams(
            type = ModelsToRetrieve.values().first { it.value == "funnel_stage" },
            name = "Shopping stage for EU users",
            sourceID = "0200030-129930",
            index = "Products Production",
            modelAttributes = listOf(),
          ),
        )
      },
      intercept = {
        assertEquals("/1/predict/models".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"type":"funnel_stage","name":"Shopping stage for EU users","sourceID":"0200030-129930","index":"Products Production","modelAttributes":[]}""", it.body)
      },
    )
  }

  // createSegment

  @Test
  fun `create segment with required params`() = runTest {
    client.runTest(
      call = {
        createSegment(
          createSegmentParams = CreateSegmentParams(
            name = "segment1",
            conditions = SegmentParentConditions(
              operator = SegmentConditionOperator.values().first { it.value == "AND" },
              operands = listOf(
                SegmentOperandAffinity(
                  name = "predictions.order_value",
                  filters = listOf(
                    SegmentAffinityFilter(
                      operator = SegmentFilterOperatorNumerical.values().first { it.value == "GT" },
                      value = SegmentAffinityFilterValue.Number(200.toNumberType()),
                    ),
                  ),
                ),
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/segments".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"name":"segment1","conditions":{"operator":"AND","operands":[{"name":"predictions.order_value","filters":[{"operator":"GT","value":200}]}]}}""", it.body)
      },
    )
  }

  @Test
  fun `create segment with filter probability`() = runTest {
    client.runTest(
      call = {
        createSegment(
          createSegmentParams = CreateSegmentParams(
            name = "segment1",
            conditions = SegmentParentConditions(
              operator = SegmentConditionOperator.values().first { it.value == "AND" },
              operands = listOf(
                SegmentOperandAffinity(
                  name = "predictions.affinities.color",
                  filters = listOf(
                    SegmentAffinityFilter(
                      operator = SegmentFilterOperatorNumerical.values().first { it.value == "EQ" },
                      value = SegmentAffinityFilterValue.String("red"),
                      probability = SegmentFilterProbability(
                        gte = 0.5,
                        lte = 1,
                      ),
                    ),
                  ),
                ),
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/segments".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"name":"segment1","conditions":{"operator":"AND","operands":[{"name":"predictions.affinities.color","filters":[{"operator":"EQ","value":"red","probability":{"GTE":0.5,"LTE":1}}]}]}}""", it.body)
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

  // deleteModelInstance

  @Test
  fun `delete a model instance`() = runTest {
    client.runTest(
      call = {
        deleteModelInstance(
          modelID = "model1",
        )
      },
      intercept = {
        assertEquals("/1/predict/models/model1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("DELETE"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // deleteSegment

  @Test
  fun `delete a segments configuration`() = runTest {
    client.runTest(
      call = {
        deleteSegment(
          segmentID = "segment1",
        )
      },
      intercept = {
        assertEquals("/1/segments/segment1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("DELETE"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // deleteUserProfile

  @Test
  fun `deleteUserProfile`() = runTest {
    client.runTest(
      call = {
        deleteUserProfile(
          userID = "user1",
        )
      },
      intercept = {
        assertEquals("/1/users/user1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("DELETE"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // fetchAllSegments

  @Test
  fun `fetchAllSegments with no segmentType`() = runTest {
    client.runTest(
      call = {
        fetchAllSegments()
      },
      intercept = {
        assertEquals("/1/segments".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `fetchAllSegments with segmentType custom`() = runTest {
    client.runTest(
      call = {
        fetchAllSegments(
          type = SegmentType.values().first { it.value == "custom" },
        )
      },
      intercept = {
        assertEquals("/1/segments".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"type":"custom"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `fetchAllSegments with segmentType computed`() = runTest {
    client.runTest(
      call = {
        fetchAllSegments(
          type = SegmentType.values().first { it.value == "computed" },
        )
      },
      intercept = {
        assertEquals("/1/segments".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"type":"computed"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // fetchAllUserProfiles

  @Test
  fun `fetchAllUserProfiles with minimal parameters for modelsToRetrieve`() = runTest {
    client.runTest(
      call = {
        fetchAllUserProfiles(
          fetchAllUserProfilesParams = ModelsToRetrieveParam(
            modelsToRetrieve = listOf(ModelsToRetrieve.values().first { it.value == "funnel_stage" }, ModelsToRetrieve.values().first { it.value == "order_value" }, ModelsToRetrieve.values().first { it.value == "affinities" }),
          ),
        )
      },
      intercept = {
        assertEquals("/1/users".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"modelsToRetrieve":["funnel_stage","order_value","affinities"]}""", it.body)
      },
    )
  }

  @Test
  fun `fetchAllUserProfiles with minimal parameters for typesToRetrieve`() = runTest {
    client.runTest(
      call = {
        fetchAllUserProfiles(
          fetchAllUserProfilesParams = TypesToRetrieveParam(
            typesToRetrieve = listOf(TypesToRetrieve.values().first { it.value == "properties" }, TypesToRetrieve.values().first { it.value == "segments" }),
          ),
        )
      },
      intercept = {
        assertEquals("/1/users".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"typesToRetrieve":["properties","segments"]}""", it.body)
      },
    )
  }

  @Test
  fun `fetchAllUserProfiles with a limit`() = runTest {
    client.runTest(
      call = {
        fetchAllUserProfiles(
          fetchAllUserProfilesParams = LimitParam(
            limit = 10,
          ),
        )
      },
      intercept = {
        assertEquals("/1/users".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"limit":10}""", it.body)
      },
    )
  }

  @Test
  fun `fetchAllUserProfiles with a nextPageToken`() = runTest {
    client.runTest(
      call = {
        fetchAllUserProfiles(
          fetchAllUserProfilesParams = NextPageTokenParam(
            nextPageToken = "nextPageTokenExample123",
          ),
        )
      },
      intercept = {
        assertEquals("/1/users".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"nextPageToken":"nextPageTokenExample123"}""", it.body)
      },
    )
  }

  @Test
  fun `fetchAllUserProfiles with a previousPageToken`() = runTest {
    client.runTest(
      call = {
        fetchAllUserProfiles(
          fetchAllUserProfilesParams = PreviousPageTokenParam(
            previousPageToken = "previousPageTokenExample123",
          ),
        )
      },
      intercept = {
        assertEquals("/1/users".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"previousPageToken":"previousPageTokenExample123"}""", it.body)
      },
    )
  }

  // fetchSegment

  @Test
  fun `fetchSegment with user ID`() = runTest {
    client.runTest(
      call = {
        fetchSegment(
          segmentID = "segment1",
        )
      },
      intercept = {
        assertEquals("/1/segments/segment1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // fetchUserProfile

  @Test
  fun `fetchUserProfile with minimal parameters for modelsToRetrieve`() = runTest {
    client.runTest(
      call = {
        fetchUserProfile(
          userID = "user1",
          params = ModelsToRetrieveParam(
            modelsToRetrieve = listOf(ModelsToRetrieve.values().first { it.value == "funnel_stage" }, ModelsToRetrieve.values().first { it.value == "order_value" }, ModelsToRetrieve.values().first { it.value == "affinities" }),
          ),
        )
      },
      intercept = {
        assertEquals("/1/users/user1/fetch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"modelsToRetrieve":["funnel_stage","order_value","affinities"]}""", it.body)
      },
    )
  }

  @Test
  fun `fetchUserProfile with minimal parameters for typesToRetrieve`() = runTest {
    client.runTest(
      call = {
        fetchUserProfile(
          userID = "user1",
          params = TypesToRetrieveParam(
            typesToRetrieve = listOf(TypesToRetrieve.values().first { it.value == "properties" }, TypesToRetrieve.values().first { it.value == "segments" }),
          ),
        )
      },
      intercept = {
        assertEquals("/1/users/user1/fetch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"typesToRetrieve":["properties","segments"]}""", it.body)
      },
    )
  }

  @Test
  fun `fetchUserProfile with all parameters`() = runTest {
    client.runTest(
      call = {
        fetchUserProfile(
          userID = "user1",
          params = AllParams(
            modelsToRetrieve = listOf(ModelsToRetrieve.values().first { it.value == "funnel_stage" }, ModelsToRetrieve.values().first { it.value == "order_value" }, ModelsToRetrieve.values().first { it.value == "affinities" }),
            typesToRetrieve = listOf(TypesToRetrieve.values().first { it.value == "properties" }, TypesToRetrieve.values().first { it.value == "segments" }),
          ),
        )
      },
      intercept = {
        assertEquals("/1/users/user1/fetch".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"modelsToRetrieve":["funnel_stage","order_value","affinities"],"typesToRetrieve":["properties","segments"]}""", it.body)
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

  // getAvailableModelTypes

  @Test
  fun `get available model types`() = runTest {
    client.runTest(
      call = {
        getAvailableModelTypes()
      },
      intercept = {
        assertEquals("/1/predict/modeltypes".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // getModelInstanceConfig

  @Test
  fun `get configurations for a model instance`() = runTest {
    client.runTest(
      call = {
        getModelInstanceConfig(
          modelID = "model1",
        )
      },
      intercept = {
        assertEquals("/1/predict/models/model1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // getModelInstances

  @Test
  fun `get a list of model instances`() = runTest {
    client.runTest(
      call = {
        getModelInstances()
      },
      intercept = {
        assertEquals("/1/predict/models".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // getModelMetrics

  @Test
  fun `get metrics for a model instance`() = runTest {
    client.runTest(
      call = {
        getModelMetrics(
          modelID = "model1",
        )
      },
      intercept = {
        assertEquals("/1/predict/models/model1/metrics".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertNoBody(it.body)
      },
    )
  }

  // getSegmentUsers

  @Test
  fun `getSegmentUsers with minimal parameters for modelsToRetrieve`() = runTest {
    client.runTest(
      call = {
        getSegmentUsers(
          segmentID = "segmentID1",
          fetchAllUserProfilesParams = ModelsToRetrieveParam(
            modelsToRetrieve = listOf(ModelsToRetrieve.values().first { it.value == "funnel_stage" }),
          ),
        )
      },
      intercept = {
        assertEquals("/1/segments/segmentID1/users".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"modelsToRetrieve":["funnel_stage"]}""", it.body)
      },
    )
  }

  @Test
  fun `getSegmentUsers with minimal parameters for typesToRetrieve`() = runTest {
    client.runTest(
      call = {
        getSegmentUsers(
          segmentID = "segmentID1",
          fetchAllUserProfilesParams = TypesToRetrieveParam(
            typesToRetrieve = listOf(TypesToRetrieve.values().first { it.value == "properties" }),
          ),
        )
      },
      intercept = {
        assertEquals("/1/segments/segmentID1/users".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"typesToRetrieve":["properties"]}""", it.body)
      },
    )
  }

  @Test
  fun `getSegmentUsers with a limit`() = runTest {
    client.runTest(
      call = {
        getSegmentUsers(
          segmentID = "segmentID1",
          fetchAllUserProfilesParams = LimitParam(
            limit = 10,
          ),
        )
      },
      intercept = {
        assertEquals("/1/segments/segmentID1/users".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"limit":10}""", it.body)
      },
    )
  }

  @Test
  fun `getSegmentUsers with a nextPageToken`() = runTest {
    client.runTest(
      call = {
        getSegmentUsers(
          segmentID = "segmentID1",
          fetchAllUserProfilesParams = NextPageTokenParam(
            nextPageToken = "nextPageTokenExample123",
          ),
        )
      },
      intercept = {
        assertEquals("/1/segments/segmentID1/users".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"nextPageToken":"nextPageTokenExample123"}""", it.body)
      },
    )
  }

  @Test
  fun `getSegmentUsers with a previousPageToken`() = runTest {
    client.runTest(
      call = {
        getSegmentUsers(
          segmentID = "segmentID1",
          fetchAllUserProfilesParams = PreviousPageTokenParam(
            previousPageToken = "previousPageTokenExample123",
          ),
        )
      },
      intercept = {
        assertEquals("/1/segments/segmentID1/users".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"previousPageToken":"previousPageTokenExample123"}""", it.body)
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

  // updateModelInstance

  @Test
  fun `update a model instance`() = runTest {
    client.runTest(
      call = {
        updateModelInstance(
          modelID = "model1",
          updateModelParams = UpdateModelParams(
            name = "Shopping stage for EU users",
            modelAttributes = listOf("brand", "color", "category_level0", "category_level1"),
            modelStatus = ModelStatus.values().first { it.value == "inactive" },
          ),
        )
      },
      intercept = {
        assertEquals("/1/predict/models/model1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"name":"Shopping stage for EU users","modelAttributes":["brand","color","category_level0","category_level1"],"modelStatus":"inactive"}""", it.body)
      },
    )
  }

  // updateSegment

  @Test
  fun `updateSegment with name`() = runTest {
    client.runTest(
      call = {
        updateSegment(
          segmentID = "segment1",
          updateSegmentParams = SegmentNameParam(
            name = "example segment name",
          ),
        )
      },
      intercept = {
        assertEquals("/1/segments/segment1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"name":"example segment name"}""", it.body)
      },
    )
  }

  @Test
  fun `updateSegment with conditions`() = runTest {
    client.runTest(
      call = {
        updateSegment(
          segmentID = "segment1",
          updateSegmentParams = SegmentConditionsParam(
            conditions = SegmentParentConditions(
              operator = SegmentConditionOperator.values().first { it.value == "AND" },
              operands = listOf(
                SegmentOperandAffinity(
                  name = "predictions.order_value",
                  filters = listOf(
                    SegmentAffinityFilter(
                      operator = SegmentFilterOperatorNumerical.values().first { it.value == "GT" },
                      value = SegmentAffinityFilterValue.Number(200.toNumberType()),
                    ),
                  ),
                ),
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/segments/segment1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"conditions":{"operator":"AND","operands":[{"name":"predictions.order_value","filters":[{"operator":"GT","value":200}]}]}}""", it.body)
      },
    )
  }

  @Test
  fun `updateSegment with name and conditions`() = runTest {
    client.runTest(
      call = {
        updateSegment(
          segmentID = "segment1",
          updateSegmentParams = AllUpdateSegmentParams(
            name = "example segment name",
            conditions = SegmentParentConditions(
              operator = SegmentConditionOperator.values().first { it.value == "AND" },
              operands = listOf(
                SegmentOperandAffinity(
                  name = "predictions.order_value",
                  filters = listOf(
                    SegmentAffinityFilter(
                      operator = SegmentFilterOperatorNumerical.values().first { it.value == "GT" },
                      value = SegmentAffinityFilterValue.Number(200.toNumberType()),
                    ),
                  ),
                ),
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/segments/segment1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"name":"example segment name","conditions":{"operator":"AND","operands":[{"name":"predictions.order_value","filters":[{"operator":"GT","value":200}]}]}}""", it.body)
      },
    )
  }

  @Test
  fun `updateSegment with filter probability`() = runTest {
    client.runTest(
      call = {
        updateSegment(
          segmentID = "segment1",
          updateSegmentParams = SegmentConditionsParam(
            conditions = SegmentParentConditions(
              operator = SegmentConditionOperator.values().first { it.value == "AND" },
              operands = listOf(
                SegmentOperandAffinity(
                  name = "predictions.affinities.color",
                  filters = listOf(
                    SegmentAffinityFilter(
                      operator = SegmentFilterOperatorNumerical.values().first { it.value == "EQ" },
                      value = SegmentAffinityFilterValue.String("red"),
                      probability = SegmentFilterProbability(
                        gte = 0.5,
                        lte = 1,
                      ),
                    ),
                  ),
                ),
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/segments/segment1".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"conditions":{"operator":"AND","operands":[{"name":"predictions.affinities.color","filters":[{"operator":"EQ","value":"red","probability":{"GTE":0.5,"LTE":1}}]}]}}""", it.body)
      },
    )
  }
}
