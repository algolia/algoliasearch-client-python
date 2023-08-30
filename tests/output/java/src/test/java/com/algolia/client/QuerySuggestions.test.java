package com.algolia.client;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.algolia.EchoInterceptor;
import com.algolia.EchoResponse;
import com.algolia.api.QuerySuggestionsClient;
import com.algolia.config.*;
import com.algolia.model.querysuggestions.*;
import java.util.*;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class QuerySuggestionsClientClientTests {

  private EchoInterceptor echo = new EchoInterceptor();

  QuerySuggestionsClient createClient() {
    return new QuerySuggestionsClient("appId", "apiKey", "us", buildClientOptions());
  }

  private ClientOptions buildClientOptions() {
    return ClientOptions.builder().setRequesterConfig(requester -> requester.addInterceptor(echo)).build();
  }

  @Test
  @DisplayName("calls api with correct user agent")
  void commonApiTest0() {
    QuerySuggestionsClient client = createClient();

    String path0 = "/test";

    client.post(path0);
    EchoResponse result = echo.getLastResponse();

    {
      String regexp =
        "^Algolia for Java \\(\\d+\\.\\d+\\.\\d+(-.*)?\\)(; [a-zA-Z. ]+" +
        " (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*(; QuerySuggestions" +
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
    QuerySuggestionsClient client = createClient();

    String path0 = "/test";

    client.get(path0);
    EchoResponse result = echo.getLastResponse();

    assertEquals(2000, result.connectTimeout);
    assertEquals(5000, result.responseTimeout);
  }

  @Test
  @DisplayName("calls api with default write timeouts")
  void commonApiTest2() {
    QuerySuggestionsClient client = createClient();

    String path0 = "/test";

    client.post(path0);
    EchoResponse result = echo.getLastResponse();

    assertEquals(2000, result.connectTimeout);
    assertEquals(30000, result.responseTimeout);
  }

  @Test
  @DisplayName("throws when region is not given")
  void parametersTest0() {
    {
      Exception exception = assertThrows(
        Exception.class,
        () -> {
          QuerySuggestionsClient client = new QuerySuggestionsClient("my-app-id", "my-api-key", "", buildClientOptions());
        }
      );
      assertEquals("`region` is required and must be one of the following: eu, us", exception.getMessage());
    }
  }

  @Test
  @DisplayName("throws when incorrect region is given")
  void parametersTest1() {
    {
      Exception exception = assertThrows(
        Exception.class,
        () -> {
          QuerySuggestionsClient client = new QuerySuggestionsClient("my-app-id", "my-api-key", "not_a_region", buildClientOptions());
        }
      );
      assertEquals("`region` is required and must be one of the following: eu, us", exception.getMessage());
    }
  }

  @Test
  @DisplayName("does not throw when region is given")
  void parametersTest2() {
    QuerySuggestionsClient client = new QuerySuggestionsClient("my-app-id", "my-api-key", "us", buildClientOptions());
  }
}
