package com.algolia.client;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.algolia.EchoInterceptor;
import com.algolia.EchoResponse;
import com.algolia.api.AbtestingClient;
import com.algolia.model.abtesting.*;
import com.algolia.utils.ClientOptions;
import com.algolia.utils.HttpRequester;
import java.util.*;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class AbtestingClientClientTests {

  private HttpRequester requester;
  private EchoInterceptor echo;

  @BeforeAll
  void init() {
    requester = new HttpRequester();
    echo = new EchoInterceptor();
    requester.addInterceptor(echo.getEchoInterceptor());
  }

  AbtestingClient createClient() {
    return new AbtestingClient("appId", "apiKey", "us", ClientOptions.build().setRequester(requester));
  }

  @Test
  @DisplayName("calls api with correct user agent")
  void commonApiTest0() {
    AbtestingClient $client = createClient();

    String path0 = "/test";

    $client.post(path0);
    EchoResponse result = echo.getLastResponse();

    {
      String regexp =
        "^Algolia for Java \\(\\d+\\.\\d+\\.\\d+(-.*)?\\)(; [a-zA-Z. ]+" +
        " (\\(\\d+\\.\\d+\\.\\d+(-.*)?\\))?)*(; Abtesting" +
        " (\\(\\d+\\.\\d+\\.\\d+(-.*)?\\)))(; [a-zA-Z. ]+" +
        " (\\(\\d+\\.\\d+\\.\\d+(-.*)?\\))?)*$";
      assertTrue(
        result.headers.get("user-agent").matches(regexp),
        "Expected " + result.headers.get("user-agent") + " to match the following regex: " + regexp
      );
    }
  }

  @Test
  @DisplayName("calls api with correct timeouts")
  void commonApiTest1() {
    AbtestingClient $client = createClient();

    String path0 = "/test";

    $client.post(path0);
    EchoResponse result = echo.getLastResponse();

    assertEquals(2000, result.connectTimeout);
    assertEquals(30000, result.responseTimeout);
  }

  @Test
  @DisplayName("fallbacks to the alias when region is not given")
  void parametersTest0() {
    AbtestingClient $client = new AbtestingClient("my-app-id", "my-api-key", ClientOptions.build().setRequester(requester));

    int id0 = 123;

    $client.getABTest(id0);
    EchoResponse result = echo.getLastResponse();

    assertEquals("analytics.algolia.com", result.host);
  }
}