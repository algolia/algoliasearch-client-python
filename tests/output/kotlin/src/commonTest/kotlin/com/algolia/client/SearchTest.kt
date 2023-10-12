package com.algolia.client

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

  @Test
  fun `calls api with correct read host`() = runTest {
    val client = SearchClient(appId = "test-app-id", apiKey = "test-api-key")
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
    val client = SearchClient(appId = "test-app-id", apiKey = "test-api-key")
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
    val client = SearchClient(appId = "appId", apiKey = "apiKey")
    client.runTest(
      call = {
        post(
          path = "/test",
        )
      },
      intercept = {
        val regexp = "^Algolia for Kotlin \\(\\d+\\.\\d+\\.\\d+(-.*)?\\)(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*(; Search (\\(\\d+\\.\\d+\\.\\d+(-.*)?\\)))(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*$".toRegex()
        val header = it.headers["User-Agent"].orEmpty()
        assertTrue(actual = header.matches(regexp), message = "Expected $header to match the following regex: $regexp")
      },
    )
  }

  @Test
  fun `calls api with default read timeouts`() = runTest {
    val client = SearchClient(appId = "appId", apiKey = "apiKey")
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
    val client = SearchClient(appId = "appId", apiKey = "apiKey")
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
  fun `client throws with invalid parameters`() = runTest {
    assertFails {
      val client = SearchClient(appId = "", apiKey = "")
    }.let { error -> assertError(error, "`appId` is missing.") }
    assertFails {
      val client = SearchClient(appId = "", apiKey = "my-api-key")
    }.let { error -> assertError(error, "`appId` is missing.") }
    assertFails {
      val client = SearchClient(appId = "my-app-id", apiKey = "")
    }.let { error -> assertError(error, "`apiKey` is missing.") }
  }

  @Test
  fun `'addApiKey' throws with invalid parameters`() = runTest {
    val client = SearchClient(appId = "appId", apiKey = "apiKey")
    assertFails {
      client.addApiKey(
        apiKey = empty(),
      )
    }.let { error -> assertError(error, "Parameter `apiKey` is required when calling `addApiKey`.") }
  }

  @Test
  fun `'addOrUpdateObject' throws with invalid parameters`() = runTest {
    val client = SearchClient(appId = "appId", apiKey = "apiKey")
    assertFails {
      client.addOrUpdateObject(
        indexName = empty(),
        objectID = "my-object-id",
        body = buildJsonObject {
        },
      )
    }.let { error -> assertError(error, "Parameter `indexName` is required when calling `addOrUpdateObject`.") }
    assertFails {
      client.addOrUpdateObject(
        indexName = "my-index-name",
        objectID = empty(),
        body = buildJsonObject {
        },
      )
    }.let { error -> assertError(error, "Parameter `objectID` is required when calling `addOrUpdateObject`.") }
    assertFails {
      client.addOrUpdateObject(
        indexName = "my-index-name",
        objectID = "my-object-id",
        body = empty(),
      )
    }.let { error -> assertError(error, "Parameter `body` is required when calling `addOrUpdateObject`.") }
  }
}
