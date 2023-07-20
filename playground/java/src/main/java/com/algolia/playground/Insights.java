package com.algolia.playground;

import com.algolia.api.InsightsClient;
import com.algolia.exceptions.*;
import com.algolia.model.insights.*;
import io.github.cdimascio.dotenv.Dotenv;

public class Insights {

  public static void main(String[] args) {
    Dotenv dotenv = Dotenv.configure().directory("../").load();

    InsightsClient client = new InsightsClient(dotenv.get("ALGOLIA_APPLICATION_ID"), dotenv.get("ALGOLIA_SEARCH_KEY"));

    String indexName = dotenv.get("SEARCH_INDEX");
    InsightsEvents params = new InsightsEvents();
    EventsItems event = EventsItems.of(new ClickedObjectIDs()
      .setEventType(ClickEvent.CLICK)
      .setUserToken("user")
      .setIndex("test_what")
      .setEventName("test"));
    params.addEvents(event);

    try {
      EventsResponse result = client.pushEvents(params);
      System.out.println(result);
    } catch (AlgoliaApiException e) {
      // the API failed
      System.err.println("Exception when calling InsightsClient#pushEvents");
      System.err.println("Status code: " + e.getHttpErrorCode());
      System.err.println("Reason: " + e.getMessage());
      e.printStackTrace();
    } catch (AlgoliaRetryException e) {
      // the retry failed
      System.err.println("Exception in the retry strategy");
      e.printStackTrace();
    } catch (AlgoliaRuntimeException e) {
      // the serialization or something else failed
      e.printStackTrace();
    }
  }
}
