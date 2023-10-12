package com.algolia.client

import com.algolia.client.api.IngestionClient
import com.algolia.client.configuration.*
import com.algolia.client.model.ingestion.*
import com.algolia.client.transport.*
import com.algolia.utils.*
import io.ktor.http.*
import kotlinx.coroutines.test.*
import kotlinx.serialization.json.*
import kotlin.test.*

class IngestionTest {

  @Test
  fun `calls api with correct user agent`() = runTest {
    val client = IngestionClient(appId = "appId", apiKey = "apiKey", region = "us")
    client.runTest(
      call = {
        post(
          path = "/test",
        )
      },
      intercept = {
        val regexp = "^Algolia for Kotlin \\(\\d+\\.\\d+\\.\\d+(-.*)?\\)(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*(; Ingestion (\\(\\d+\\.\\d+\\.\\d+(-.*)?\\)))(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*$".toRegex()
        val header = it.headers["User-Agent"].orEmpty()
        assertTrue(actual = header.matches(regexp), message = "Expected $header to match the following regex: $regexp")
      },
    )
  }

  @Test
  fun `calls api with default read timeouts`() = runTest {
    val client = IngestionClient(appId = "appId", apiKey = "apiKey", region = "us")
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
    val client = IngestionClient(appId = "appId", apiKey = "apiKey", region = "us")
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
  fun `uses the correct region`() = runTest {
    val client = IngestionClient(appId = "my-app-id", apiKey = "my-api-key", "us")
    client.runTest(
      call = {
        getSource(
          sourceID = "6c02aeb1-775e-418e-870b-1faccd4b2c0f",
        )
      },
      intercept = {
        assertEquals("data.us.algolia.com", it.url.host)
      },
    )
  }

  @Test
  fun `throws when incorrect region is given`() = runTest {
    assertFails {
      val client = IngestionClient(appId = "my-app-id", apiKey = "my-api-key", "not_a_region")
    }.let { error -> assertError(error, "`region` is required and must be one of the following: eu, us") }
  }
}
