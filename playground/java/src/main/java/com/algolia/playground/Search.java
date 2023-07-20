package com.algolia.playground;

import com.algolia.api.SearchClient;
import com.algolia.exceptions.*;
import com.algolia.model.search.*;
import com.algolia.utils.*;
import io.github.cdimascio.dotenv.Dotenv;
import java.util.*;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

class Actor extends Hit {

  public String name;

  public Actor() {}

  public Actor(String name) {
    this.name = name;
  }
}

public class Search {

  public static void main(String[] args) {
    Dotenv dotenv = Dotenv.configure().directory("../").load();

    SearchClient client = new SearchClient(
      dotenv.get("ALGOLIA_APPLICATION_ID"),
      dotenv.get("ALGOLIA_ADMIN_KEY"),
      new ClientOptions()
        .addAlgoliaAgentSegment("test", "8.0.0")
        .addAlgoliaAgentSegment("JVM", "11.0.14")
        .addAlgoliaAgentSegment("no version")
    );

    client.setLogLevel(LogLevel.NONE);

    String indexName = dotenv.get("SEARCH_INDEX");
    String query = dotenv.get("SEARCH_QUERY");

    try {
      List<Actor> records = Arrays.asList(new Actor("Tom Cruise"), new Actor("Scarlett Johansson"));

      List<BatchRequest> batch = new ArrayList<>();

      for (Actor record : records) {
        batch.add(new BatchRequest().setAction(Action.ADD_OBJECT).setBody(record));
      }

      BatchResponse response = client.batch(indexName, new BatchWriteParams().setRequests(batch));

      client.waitForTask(indexName, response.getTaskID());

      client.setLogLevel(LogLevel.BASIC);

      SearchMethodParams searchMethodParams = new SearchMethodParams();
      List<SearchQuery> requests = new ArrayList<>();
      requests.add(SearchQuery.of(new SearchForHits().setIndexName(indexName).setQuery(query).addAttributesToSnippet("title").addAttributesToSnippet("alternative_titles")));
      searchMethodParams.setRequests(requests);

      CompletableFuture<SearchResponses<Actor>> result = client.searchAsync(searchMethodParams, Actor.class);

      SearchResponses<Actor> sr = result.get();
      Actor a = sr.getResults().get(0).getHits().get(0);
      System.out.println(a.name);
      
    } catch (InterruptedException e) {
      System.err.println("InterrupedException" + e.getMessage());
      e.printStackTrace();
    } catch (ExecutionException e) {
      System.err.println("ExecutionException" + e.getMessage());
      e.printStackTrace();
    } catch (AlgoliaApiException e) {
      // the API failed
      System.err.println("Exception when calling SearchClient#search");
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
