package com.algolia.client;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.algolia.EchoInterceptor;
import com.algolia.EchoResponse;
import com.algolia.api.InsightsClient;
import com.algolia.model.insights.*;
import com.algolia.utils.ClientOptions;
import com.algolia.utils.HttpRequester;
import java.util.*;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class InsightsClientClientTests {

  private HttpRequester requester;
  private EchoInterceptor echo;

  @BeforeAll
  void init() {
    requester = new HttpRequester();
    echo = new EchoInterceptor();
    requester.addInterceptor(echo.getEchoInterceptor());
  }

  InsightsClient createClient() {
    return new InsightsClient("appId", "apiKey", "us", new ClientOptions().setRequester(requester));
  }

  @Test
  @DisplayName("calls api with correct user agent")
  void commonApiTest0() {
    InsightsClient $client = createClient();

    String path0 = "/test";

    $client.post(path0);
    EchoResponse result = echo.getLastResponse();

    {
      String regexp =
        "^Algolia for Java \\(\\d+\\.\\d+\\.\\d+(-.*)?\\)(; [a-zA-Z. ]+" +
        " (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*(; Insights" +
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
    InsightsClient $client = createClient();

    String path0 = "/test";

    $client.get(path0);
    EchoResponse result = echo.getLastResponse();

    assertEquals(2000, result.connectTimeout);
    assertEquals(5000, result.responseTimeout);
  }

  @Test
  @DisplayName("calls api with default write timeouts")
  void commonApiTest2() {
    InsightsClient $client = createClient();

    String path0 = "/test";

    $client.post(path0);
    EchoResponse result = echo.getLastResponse();

    assertEquals(2000, result.connectTimeout);
    assertEquals(30000, result.responseTimeout);
  }

  @Test
  @DisplayName("fallbacks to the alias when region is not given")
  void parametersTest0() {
    InsightsClient $client = new InsightsClient("my-app-id", "my-api-key", new ClientOptions().setRequester(requester));

    InsightsEvents insightsEvents0 = new InsightsEvents();
    {
      List events1 = new ArrayList<>();
      {}
      insightsEvents0.setEvents(events1);
    }

    $client.pushEvents(insightsEvents0);
    EchoResponse result = echo.getLastResponse();

    assertEquals("insights.algolia.io", result.host);
  }

  @Test
  @DisplayName("uses the correct region")
  void parametersTest1() {
    InsightsClient $client = new InsightsClient("my-app-id", "my-api-key", "us", new ClientOptions().setRequester(requester));

    String path0 = "/test";

    $client.del(path0);
    EchoResponse result = echo.getLastResponse();

    assertEquals("insights.us.algolia.io", result.host);
  }

  @Test
  @DisplayName("throws when incorrect region is given")
  void parametersTest2() {
    {
      Exception exception = assertThrows(
        Exception.class,
        () -> {
          InsightsClient $client = new InsightsClient(
            "my-app-id",
            "my-api-key",
            "not_a_region",
            new ClientOptions().setRequester(requester)
          );
        }
      );
      assertEquals("`region` must be one of the following: de, us", exception.getMessage());
    }
  }
}
