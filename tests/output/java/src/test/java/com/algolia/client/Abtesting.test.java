package com.algolia.client;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.algolia.EchoInterceptor;
import com.algolia.EchoResponse;
import com.algolia.api.AbtestingClient;
import com.algolia.config.*;
import com.algolia.model.abtesting.*;
import java.util.*;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class AbtestingClientClientTests {

  private EchoInterceptor echo = new EchoInterceptor();

  AbtestingClient createClient() {
    return new AbtestingClient("appId", "apiKey", "us", buildClientOptions());
  }

  private ClientOptions buildClientOptions() {
    return ClientOptions.builder().setRequesterConfig(requester -> requester.addInterceptor(echo)).build();
  }

  @Test
  @DisplayName("calls api with correct user agent")
  void commonApiTest0() {
    AbtestingClient client = createClient();

    String path0 = "/test";

    client.post(path0);
    EchoResponse result = echo.getLastResponse();

    {
      String regexp =
        "^Algolia for Java \\(\\d+\\.\\d+\\.\\d+(-.*)?\\)(; [a-zA-Z. ]+" +
        " (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*(; Abtesting" +
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
    AbtestingClient client = createClient();

    String path0 = "/test";

    client.get(path0);
    EchoResponse result = echo.getLastResponse();

    assertEquals(2000, result.connectTimeout);
    assertEquals(5000, result.responseTimeout);
  }

  @Test
  @DisplayName("calls api with default write timeouts")
  void commonApiTest2() {
    AbtestingClient client = createClient();

    String path0 = "/test";

    client.post(path0);
    EchoResponse result = echo.getLastResponse();

    assertEquals(2000, result.connectTimeout);
    assertEquals(30000, result.responseTimeout);
  }

  @Test
  @DisplayName("fallbacks to the alias when region is not given")
  void parametersTest0() {
    AbtestingClient client = new AbtestingClient("my-app-id", "my-api-key", buildClientOptions());

    int id0 = 123;

    client.getABTest(id0);
    EchoResponse result = echo.getLastResponse();

    assertEquals("analytics.algolia.com", result.host);
  }

  @Test
  @DisplayName("uses the correct region")
  void parametersTest1() {
    AbtestingClient client = new AbtestingClient("my-app-id", "my-api-key", "us", buildClientOptions());

    int id0 = 123;

    client.getABTest(id0);
    EchoResponse result = echo.getLastResponse();

    assertEquals("analytics.us.algolia.com", result.host);
  }

  @Test
  @DisplayName("throws when incorrect region is given")
  void parametersTest2() {
    {
      Exception exception = assertThrows(
        Exception.class,
        () -> {
          AbtestingClient client = new AbtestingClient("my-app-id", "my-api-key", "not_a_region", buildClientOptions());
        }
      );
      assertEquals("`region` must be one of the following: de, us", exception.getMessage());
    }
  }
}
