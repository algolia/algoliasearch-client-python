package com.algolia.client

import com.algolia.client.api.InsightsClient
import com.algolia.client.configuration.*
import com.algolia.client.model.insights.*
import com.algolia.client.transport.*
import com.algolia.utils.*
import io.ktor.http.*
import kotlinx.coroutines.test.*
import kotlinx.serialization.json.*
import kotlin.test.*

class InsightsTest {

  @Test
  fun `calls api with correct user agent`() = runTest {
    val client = InsightsClient(appId = "appId", apiKey = "apiKey", region = "us")
    client.runTest(
      call = {
        post(
          path = "/test",
        )
      },
      intercept = {
        val regexp = "^Algolia for Kotlin \\(\\d+\\.\\d+\\.\\d+(-.*)?\\)(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*(; Insights (\\(\\d+\\.\\d+\\.\\d+(-.*)?\\)))(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*$".toRegex()
        val header = it.url.parameters["X-Algolia-Agent"]?.decodeURLPart().orEmpty()
        assertTrue(actual = header.matches(regexp), message = "Expected $header to match the following regex: $regexp")
      },
    )
  }

  @Test
  fun `calls api with default read timeouts`() = runTest {
    val client = InsightsClient(appId = "appId", apiKey = "apiKey", region = "us")
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
    val client = InsightsClient(appId = "appId", apiKey = "apiKey", region = "us")
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
    val client = InsightsClient(appId = "my-app-id", apiKey = "my-api-key")
    client.runTest(
      call = {
        pushEvents(
          insightsEvents = InsightsEvents(
            events = listOf(),
          ),
        )
      },
      intercept = {
        assertEquals("insights.algolia.io", it.url.host)
      },
    )
  }

  @Test
  fun `uses the correct region`() = runTest {
    val client = InsightsClient(appId = "my-app-id", apiKey = "my-api-key", "us")
    client.runTest(
      call = {
        del(
          path = "/test",
        )
      },
      intercept = {
        assertEquals("insights.us.algolia.io", it.url.host)
      },
    )
  }

  @Test
  fun `throws when incorrect region is given`() = runTest {
    assertFails {
      val client = InsightsClient(appId = "my-app-id", apiKey = "my-api-key", "not_a_region")
    }.let { error -> assertError(error, "`region` must be one of the following: de, us") }
  }
}
