package com.algolia.client

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

  @Test
  fun `calls api with correct user agent`() = runTest {
    val client = AnalyticsClient(appId = "appId", apiKey = "apiKey", region = "us")
    client.runTest(
      call = {
        post(
          path = "/test",
        )
      },
      intercept = {
        val regexp = "^Algolia for Kotlin \\(\\d+\\.\\d+\\.\\d+(-.*)?\\)(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*(; Analytics (\\(\\d+\\.\\d+\\.\\d+(-.*)?\\)))(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*$".toRegex()
        val header = it.url.parameters["X-Algolia-Agent"]?.decodeURLPart().orEmpty()
        assertTrue(actual = header.matches(regexp), message = "Expected $header to match the following regex: $regexp")
      },
    )
  }

  @Test
  fun `calls api with default read timeouts`() = runTest {
    val client = AnalyticsClient(appId = "appId", apiKey = "apiKey", region = "us")
    client.runTest(
      call = {
        get(
          path = "/test",
        )
      },
      intercept = {
        assertEquals(2000, it.connectTimeout)
        assertEquals(5000, it.socketTimeout)
      },
    )
  }

  @Test
  fun `calls api with default write timeouts`() = runTest {
    val client = AnalyticsClient(appId = "appId", apiKey = "apiKey", region = "us")
    client.runTest(
      call = {
        post(
          path = "/test",
        )
      },
      intercept = {
        assertEquals(2000, it.connectTimeout)
        assertEquals(30000, it.socketTimeout)
      },
    )
  }

  @Test
  fun `fallbacks to the alias when region is not given`() = runTest {
    val client = AnalyticsClient(appId = "my-app-id", apiKey = "my-api-key")
    client.runTest(
      call = {
        getAverageClickPosition(
          index = "my-index",
        )
      },
      intercept = {
        assertEquals("analytics.algolia.com", it.url.host)
      },
    )
  }

  @Test
  fun `uses the correct region`() = runTest {
    val client = AnalyticsClient(appId = "my-app-id", apiKey = "my-api-key", "de")
    client.runTest(
      call = {
        post(
          path = "/test",
        )
      },
      intercept = {
        assertEquals("analytics.de.algolia.com", it.url.host)
      },
    )
  }

  @Test
  fun `throws when incorrect region is given`() = runTest {
    assertFails {
      val client = AnalyticsClient(appId = "my-app-id", apiKey = "my-api-key", "not_a_region")
    }.let { error -> assertError(error, "`region` must be one of the following: de, us") }
  }

  @Test
  fun `getAverageClickPosition throws without index`() = runTest {
    val client = AnalyticsClient(appId = "appId", apiKey = "apiKey", region = "us")
    assertFails {
      client.getClickPositions(
        index = empty(),
      )
    }.let { error -> assertError(error, "Parameter `index` is required when calling `getClickPositions`.") }
  }
}
