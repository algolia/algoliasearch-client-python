package com.algolia.methods.requests

import com.algolia.client.api.AnalyticsClient
import com.algolia.client.configuration.*
import com.algolia.client.model.analytics.*
import com.algolia.client.transport.*
import com.algolia.extension.*
import com.algolia.utils.*
import io.ktor.http.*
import kotlinx.coroutines.test.*
import kotlinx.serialization.json.*
import kotlin.test.*

class AnalyticsTest {

  val client = AnalyticsClient(
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

  // getAverageClickPosition

  @Test
  fun `get getAverageClickPosition with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getAverageClickPosition(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/clicks/averageClickPosition".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getAverageClickPosition with all parameters`() = runTest {
    client.runTest(
      call = {
        getAverageClickPosition(
          index = "index",
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/clicks/averageClickPosition".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getClickPositions

  @Test
  fun `get getClickPositions with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getClickPositions(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/clicks/positions".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getClickPositions with all parameters`() = runTest {
    client.runTest(
      call = {
        getClickPositions(
          index = "index",
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/clicks/positions".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getClickThroughRate

  @Test
  fun `get getClickThroughRate with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getClickThroughRate(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/clicks/clickThroughRate".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getClickThroughRate with all parameters`() = runTest {
    client.runTest(
      call = {
        getClickThroughRate(
          index = "index",
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/clicks/clickThroughRate".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getConversationRate

  @Test
  fun `get getConversationRate with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getConversationRate(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/conversions/conversionRate".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getConversationRate with all parameters`() = runTest {
    client.runTest(
      call = {
        getConversationRate(
          index = "index",
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/conversions/conversionRate".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getNoClickRate

  @Test
  fun `get getNoClickRate with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getNoClickRate(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/searches/noClickRate".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getNoClickRate with all parameters`() = runTest {
    client.runTest(
      call = {
        getNoClickRate(
          index = "index",
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/searches/noClickRate".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getNoResultsRate

  @Test
  fun `get getNoResultsRate with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getNoResultsRate(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/searches/noResultRate".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getNoResultsRate with all parameters`() = runTest {
    client.runTest(
      call = {
        getNoResultsRate(
          index = "index",
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/searches/noResultRate".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getSearchesCount

  @Test
  fun `get getSearchesCount with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getSearchesCount(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/searches/count".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getSearchesCount with all parameters`() = runTest {
    client.runTest(
      call = {
        getSearchesCount(
          index = "index",
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/searches/count".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getSearchesNoClicks

  @Test
  fun `get getSearchesNoClicks with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getSearchesNoClicks(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/searches/noClicks".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getSearchesNoClicks with all parameters`() = runTest {
    client.runTest(
      call = {
        getSearchesNoClicks(
          index = "index",
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          limit = 21,
          offset = 42,
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/searches/noClicks".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getSearchesNoResults

  @Test
  fun `get getSearchesNoResults with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getSearchesNoResults(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/searches/noResults".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getSearchesNoResults with all parameters`() = runTest {
    client.runTest(
      call = {
        getSearchesNoResults(
          index = "index",
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          limit = 21,
          offset = 42,
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/searches/noResults".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getStatus

  @Test
  fun `get getStatus with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getStatus(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/status".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getTopCountries

  @Test
  fun `get getTopCountries with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getTopCountries(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/countries".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getTopCountries with all parameters`() = runTest {
    client.runTest(
      call = {
        getTopCountries(
          index = "index",
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          limit = 21,
          offset = 42,
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/countries".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getTopFilterAttributes

  @Test
  fun `get getTopFilterAttributes with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getTopFilterAttributes(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/filters".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getTopFilterAttributes with all parameters`() = runTest {
    client.runTest(
      call = {
        getTopFilterAttributes(
          index = "index",
          search = "mySearch",
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          limit = 21,
          offset = 42,
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/filters".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getTopFilterForAttribute

  @Test
  fun `get getTopFilterForAttribute with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getTopFilterForAttribute(
          attribute = "myAttribute",
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/filters/myAttribute".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getTopFilterForAttribute with minimal parameters and multiple attributes`() = runTest {
    client.runTest(
      call = {
        getTopFilterForAttribute(
          attribute = "myAttribute1,myAttribute2",
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/filters/myAttribute1%2CmyAttribute2".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getTopFilterForAttribute with all parameters`() = runTest {
    client.runTest(
      call = {
        getTopFilterForAttribute(
          attribute = "myAttribute",
          index = "index",
          search = "mySearch",
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          limit = 21,
          offset = 42,
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/filters/myAttribute".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getTopFilterForAttribute with all parameters and multiple attributes`() = runTest {
    client.runTest(
      call = {
        getTopFilterForAttribute(
          attribute = "myAttribute1,myAttribute2",
          index = "index",
          search = "mySearch",
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          limit = 21,
          offset = 42,
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/filters/myAttribute1%2CmyAttribute2".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getTopFiltersNoResults

  @Test
  fun `get getTopFiltersNoResults with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getTopFiltersNoResults(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/filters/noResults".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getTopFiltersNoResults with all parameters`() = runTest {
    client.runTest(
      call = {
        getTopFiltersNoResults(
          index = "index",
          search = "mySearch",
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          limit = 21,
          offset = 42,
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/filters/noResults".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getTopHits

  @Test
  fun `get getTopHits with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getTopHits(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/hits".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getTopHits with all parameters`() = runTest {
    client.runTest(
      call = {
        getTopHits(
          index = "index",
          search = "mySearch",
          clickAnalytics = true,
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          limit = 21,
          offset = 42,
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/hits".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","search":"mySearch","clickAnalytics":"true","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getTopSearches

  @Test
  fun `get getTopSearches with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getTopSearches(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/searches".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getTopSearches with all parameters`() = runTest {
    client.runTest(
      call = {
        getTopSearches(
          index = "index",
          clickAnalytics = true,
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          orderBy = OrderBy.values().first { it.value == "searchCount" },
          direction = Direction.values().first { it.value == "asc" },
          limit = 21,
          offset = 42,
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/searches".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","clickAnalytics":"true","startDate":"1999-09-19","endDate":"2001-01-01","orderBy":"searchCount","direction":"asc","limit":"21","offset":"42","tags":"tag"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  // getUsersCount

  @Test
  fun `get getUsersCount with minimal parameters`() = runTest {
    client.runTest(
      call = {
        getUsersCount(
          index = "index",
        )
      },
      intercept = {
        assertEquals("/2/users/count".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index"}""", it.url.parameters)
        assertNoBody(it.body)
      },
    )
  }

  @Test
  fun `get getUsersCount with all parameters`() = runTest {
    client.runTest(
      call = {
        getUsersCount(
          index = "index",
          startDate = "1999-09-19",
          endDate = "2001-01-01",
          tags = "tag",
        )
      },
      intercept = {
        assertEquals("/2/users/count".toPathSegments(), it.url.pathSegments)
        assertEquals(HttpMethod.parse("GET"), it.method)
        assertContainsAll("""{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}""", it.url.parameters)
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
