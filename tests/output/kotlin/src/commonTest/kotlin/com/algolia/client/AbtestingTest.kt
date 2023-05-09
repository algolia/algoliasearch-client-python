package com.algolia.client

import com.algolia.client.api.AbtestingClient
import com.algolia.client.configuration.*
import com.algolia.client.model.abtesting.*
import com.algolia.client.transport.*
import com.algolia.extension.*
import com.algolia.utils.*
import io.ktor.http.*
import kotlinx.coroutines.test.*
import kotlinx.serialization.json.*
import kotlin.test.*

class AbtestingTest {

  @Test
  fun `calls api with correct user agent`() = runTest {
    val client = AbtestingClient(appId = "appId", apiKey = "apiKey", region = "us")
    client.runTest(
      call = {
        post(
          path = "/test",
        )
      },
      intercept = {
        val regexp = "^Algolia for Kotlin \\(\\d+\\.\\d+\\.\\d+(-.*)?\\)(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*(; Abtesting (\\(\\d+\\.\\d+\\.\\d+(-.*)?\\)))(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*$".toRegex()
        val header = it.url.parameters["X-Algolia-Agent"]?.decodeURLPart().orEmpty()
        assertTrue(actual = header.matches(regexp), message = "Expected $header to match the following regex: $regexp")
      },
    )
  }

  @Test
  fun `calls api with default read timeouts`() = runTest {
    val client = AbtestingClient(appId = "appId", apiKey = "apiKey", region = "us")
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
    val client = AbtestingClient(appId = "appId", apiKey = "apiKey", region = "us")
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
    val client = AbtestingClient(appId = "my-app-id", apiKey = "my-api-key")
    client.runTest(
      call = {
        getABTest(
          id = 123,
        )
      },
      intercept = {
        assertEquals("analytics.algolia.com", it.url.host)
      },
    )
  }

  @Test
  fun `uses the correct region`() = runTest {
    val client = AbtestingClient(appId = "my-app-id", apiKey = "my-api-key", "us")
    client.runTest(
      call = {
        getABTest(
          id = 123,
        )
      },
      intercept = {
        assertEquals("analytics.us.algolia.com", it.url.host)
      },
    )
  }

  @Test
  fun `throws when incorrect region is given`() = runTest {
    assertFails {
      val client = AbtestingClient(appId = "my-app-id", apiKey = "my-api-key", "not_a_region")
    }.let { error -> assertError(error, "`region` must be one of the following: de, us") }
  }
}
