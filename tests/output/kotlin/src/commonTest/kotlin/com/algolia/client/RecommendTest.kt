package com.algolia.client

import com.algolia.client.api.RecommendClient
import com.algolia.client.configuration.*
import com.algolia.client.model.recommend.*
import com.algolia.client.transport.*
import com.algolia.utils.*
import io.ktor.http.*
import kotlinx.coroutines.test.*
import kotlinx.serialization.json.*
import kotlin.test.*

class RecommendTest {

  @Test
  fun `calls api with correct read host`() = runTest {
    val client = RecommendClient(appId = "test-app-id", apiKey = "test-api-key")
    client.runTest(
      call = {
        get(
          path = "/test",
        )
      },
      intercept = {
        assertEquals("test-app-id-dsn.algolia.net", it.url.host)
      },
    )
  }

  @Test
  fun `calls api with correct write host`() = runTest {
    val client = RecommendClient(appId = "test-app-id", apiKey = "test-api-key")
    client.runTest(
      call = {
        post(
          path = "/test",
        )
      },
      intercept = {
        assertEquals("test-app-id.algolia.net", it.url.host)
      },
    )
  }

  @Test
  fun `calls api with correct user agent`() = runTest {
    val client = RecommendClient(appId = "appId", apiKey = "apiKey")
    client.runTest(
      call = {
        post(
          path = "/test",
        )
      },
      intercept = {
        val regexp = "^Algolia for Kotlin \\(\\d+\\.\\d+\\.\\d+(-.*)?\\)(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*(; Recommend (\\(\\d+\\.\\d+\\.\\d+(-.*)?\\)))(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*$".toRegex()
        val header = it.headers["User-Agent"].orEmpty()
        assertTrue(actual = header.matches(regexp), message = "Expected $header to match the following regex: $regexp")
      },
    )
  }

  @Test
  fun `calls api with default read timeouts`() = runTest {
    val client = RecommendClient(appId = "appId", apiKey = "apiKey")
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
    val client = RecommendClient(appId = "appId", apiKey = "apiKey")
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
}
