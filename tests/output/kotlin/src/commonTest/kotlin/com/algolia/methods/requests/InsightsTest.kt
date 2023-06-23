package com.algolia.methods.requests

import com.algolia.client.api.InsightsClient
import com.algolia.client.configuration.*
import com.algolia.client.model.insights.*
import com.algolia.client.transport.*
import com.algolia.extension.*
import com.algolia.utils.*
import io.ktor.http.*
import kotlinx.coroutines.test.*
import kotlinx.serialization.json.*
import kotlin.test.*

class InsightsTest {

  val client = InsightsClient(
    appId = "appId",
    apiKey = "apiKey",
    region = "us",
  )

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

  // pushEvents

  @Test
  fun `pushEvents`() = runTest {
    client.runTest(
      call = {
        pushEvents(
          insightsEvents = InsightsEvents(
            events = listOf(
              ClickedObjectIDsAfterSearch(
                eventType = ClickEvent.values().first { it.value == "click" },
                eventName = "Product Clicked",
                index = "products",
                userToken = "user-123456",
                timestamp = 1641290601962L,
                objectIDs = listOf("9780545139700", "9780439784542"),
                queryID = "43b15df305339e827f0ac0bdc5ebcaa7",
                positions = listOf(7, 6),
              ),
            ),
          ),
        )
      },
      intercept = {
        assertEquals("/1/events".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("POST"), it.method)
        assertJsonBody("""{"events":[{"eventType":"click","eventName":"Product Clicked","index":"products","userToken":"user-123456","timestamp":1641290601962,"objectIDs":["9780545139700","9780439784542"],"queryID":"43b15df305339e827f0ac0bdc5ebcaa7","positions":[7,6]}]}""", it.body)
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
}
