package com.algolia.client;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.algolia.EchoInterceptor;
import com.algolia.EchoResponse;
import com.algolia.api.SearchClient;
import com.algolia.config.*;
import com.algolia.model.search.*;
import java.util.*;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class SearchClientClientTests {

  private EchoInterceptor echo = new EchoInterceptor();

  SearchClient createClient() {
    return new SearchClient("appId", "apiKey", buildClientOptions());
  }

  private ClientOptions buildClientOptions() {
    return ClientOptions.builder().setRequesterConfig(requester -> requester.addInterceptor(echo)).build();
  }

  @Test
  @DisplayName("calls api with correct read host")
  void apiTest0() {
    SearchClient client = new SearchClient("test-app-id", "test-api-key", buildClientOptions());

    String path0 = "/test";

    client.get(path0);
    EchoResponse result = echo.getLastResponse();

    assertEquals("test-app-id-dsn.algolia.net", result.host);
  }

  @Test
  @DisplayName("calls api with correct write host")
  void apiTest1() {
    SearchClient client = new SearchClient("test-app-id", "test-api-key", buildClientOptions());

    String path0 = "/test";

    client.post(path0);
    EchoResponse result = echo.getLastResponse();

    assertEquals("test-app-id.algolia.net", result.host);
  }

  @Test
  @DisplayName("calls api with correct user agent")
  void commonApiTest0() {
    SearchClient client = createClient();

    String path0 = "/test";

    client.post(path0);
    EchoResponse result = echo.getLastResponse();

    {
      String regexp =
        "^Algolia for Java \\(\\d+\\.\\d+\\.\\d+(-.*)?\\)(; [a-zA-Z. ]+" +
        " (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*(; Search" +
        " (\\(\\d+\\.\\d+\\.\\d+(-.*)?\\)))(; [a-zA-Z. ]+" +
        " (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*$";
      assertTrue(
        result.headers.get("user-agent").matches(regexp),
        "Expected " + result.headers.get("user-agent") + " to match the following regex: " + regexp
      );
    }
  }

  @Test
  @DisplayName("calls api with default read timeouts")
  void commonApiTest1() {
    SearchClient client = createClient();

    String path0 = "/test";

    client.get(path0);
    EchoResponse result = echo.getLastResponse();

    assertEquals(2000, result.connectTimeout);
    assertEquals(5000, result.responseTimeout);
  }

  @Test
  @DisplayName("calls api with default write timeouts")
  void commonApiTest2() {
    SearchClient client = createClient();

    String path0 = "/test";

    client.post(path0);
    EchoResponse result = echo.getLastResponse();

    assertEquals(2000, result.connectTimeout);
    assertEquals(30000, result.responseTimeout);
  }

  @Test
  @DisplayName("client throws with invalid parameters")
  void parametersTest0() {
    {
      Exception exception = assertThrows(
        Exception.class,
        () -> {
          SearchClient client = new SearchClient("", "", buildClientOptions());
        }
      );
      assertEquals("`appId` is missing.", exception.getMessage());
    }
    {
      Exception exception = assertThrows(
        Exception.class,
        () -> {
          SearchClient client = new SearchClient("", "my-api-key", buildClientOptions());
        }
      );
      assertEquals("`appId` is missing.", exception.getMessage());
    }
    {
      Exception exception = assertThrows(
        Exception.class,
        () -> {
          SearchClient client = new SearchClient("my-app-id", "", buildClientOptions());
        }
      );
      assertEquals("`apiKey` is missing.", exception.getMessage());
    }
  }

  @Test
  @DisplayName("`addApiKey` throws with invalid parameters")
  void parametersTest1() {
    SearchClient client = createClient();

    {
      Exception exception = assertThrows(
        Exception.class,
        () -> {
          ApiKey apiKey0 = null;

          client.addApiKey(apiKey0);
          EchoResponse result = echo.getLastResponse();
        }
      );
      assertEquals("Parameter `apiKey` is required when calling `addApiKey`.", exception.getMessage());
    }
  }

  @Test
  @DisplayName("`addOrUpdateObject` throws with invalid parameters")
  void parametersTest2() {
    SearchClient client = createClient();

    {
      Exception exception = assertThrows(
        Exception.class,
        () -> {
          String indexName0 = null;
          String objectID0 = "my-object-id";
          Map<String, Object> body0 = new HashMap<>();
          {}

          client.addOrUpdateObject(indexName0, objectID0, body0);
          EchoResponse result = echo.getLastResponse();
        }
      );
      assertEquals("Parameter `indexName` is required when calling `addOrUpdateObject`.", exception.getMessage());
    }
    {
      Exception exception = assertThrows(
        Exception.class,
        () -> {
          String indexName0 = "my-index-name";
          String objectID0 = null;
          Map<String, Object> body0 = new HashMap<>();
          {}

          client.addOrUpdateObject(indexName0, objectID0, body0);
          EchoResponse result = echo.getLastResponse();
        }
      );
      assertEquals("Parameter `objectID` is required when calling `addOrUpdateObject`.", exception.getMessage());
    }
    {
      Exception exception = assertThrows(
        Exception.class,
        () -> {
          String indexName0 = "my-index-name";
          String objectID0 = "my-object-id";
          Object body0 = null;

          client.addOrUpdateObject(indexName0, objectID0, body0);
          EchoResponse result = echo.getLastResponse();
        }
      );
      assertEquals("Parameter `body` is required when calling `addOrUpdateObject`.", exception.getMessage());
    }
  }
}
