package com.algolia.methods.requests;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.fail;

import com.algolia.EchoInterceptor;
import com.algolia.EchoResponse;
import com.algolia.api.SearchClient;
import com.algolia.model.search.*;
import com.algolia.utils.ClientOptions;
import com.algolia.utils.HttpRequester;
import com.algolia.utils.JSONBuilder;
import com.algolia.utils.RequestOptions;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.*;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.skyscreamer.jsonassert.JSONAssert;
import org.skyscreamer.jsonassert.JSONCompareMode;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class SearchClientRequestsTests {

  private SearchClient client;
  private EchoInterceptor echo;
  private ObjectMapper json;

  @BeforeAll
  void init() {
    json = new JSONBuilder().failOnUnknown(true).build();
    HttpRequester requester = new HttpRequester();
    echo = new EchoInterceptor();
    requester.addInterceptor(echo.getEchoInterceptor());
    client = new SearchClient("appId", "apiKey", new ClientOptions().setRequester(requester));
  }

  @Test
  @DisplayName("addApiKey")
  void addApiKeyTest0() {
    ApiKey apiKey0 = new ApiKey();
    {
      List<Acl> acl1 = new ArrayList<>();
      {
        Acl acl_02 = Acl.fromValue("search");
        acl1.add(acl_02);
        Acl acl_12 = Acl.fromValue("addObject");
        acl1.add(acl_12);
      }
      apiKey0.setAcl(acl1);
      String description1 = "my new api key";
      apiKey0.setDescription(description1);
      int validity1 = 300;
      apiKey0.setValidity(validity1);
      int maxQueriesPerIPPerHour1 = 100;
      apiKey0.setMaxQueriesPerIPPerHour(maxQueriesPerIPPerHour1);
      int maxHitsPerQuery1 = 20;
      apiKey0.setMaxHitsPerQuery(maxHitsPerQuery1);
    }

    assertDoesNotThrow(() -> {
      client.addApiKey(apiKey0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/keys");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"acl\":[\"search\",\"addObject\"],\"description\":\"my new api" +
        " key\",\"validity\":300,\"maxQueriesPerIPPerHour\":100,\"maxHitsPerQuery\":20}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("addOrUpdateObject")
  void addOrUpdateObjectTest0() {
    String indexName0 = "indexName";
    String objectID0 = "uniqueID";
    Map<String, String> body0 = new HashMap<>();
    {
      String key1 = "value";
      body0.put("key", key1);
    }

    assertDoesNotThrow(() -> {
      client.addOrUpdateObject(indexName0, objectID0, body0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/uniqueID");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"key\":\"value\"}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("appendSource")
  void appendSourceTest0() {
    Source source0 = new Source();
    {
      String source1 = "theSource";
      source0.setSource(source1);
      String description1 = "theDescription";
      source0.setDescription(description1);
    }

    assertDoesNotThrow(() -> {
      client.appendSource(source0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/security/sources/append");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"source\":\"theSource\",\"description\":\"theDescription\"}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("assignUserId")
  void assignUserIdTest0() {
    String xAlgoliaUserID0 = "userID";
    AssignUserIdParams assignUserIdParams0 = new AssignUserIdParams();
    {
      String cluster1 = "theCluster";
      assignUserIdParams0.setCluster(cluster1);
    }

    assertDoesNotThrow(() -> {
      client.assignUserId(xAlgoliaUserID0, assignUserIdParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/clusters/mapping");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"cluster\":\"theCluster\"}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedHeaders = json.readValue(
        "{\"x-algolia-user-id\":\"userID\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, String> actualHeaders = req.headers;

      for (Map.Entry<String, String> p : expectedHeaders.entrySet()) {
        assertEquals(actualHeaders.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse headers json");
    }
  }

  @Test
  @DisplayName("allows batch method with `addObject` action")
  void batchTest0() {
    String indexName0 = "theIndexName";
    BatchWriteParams batchWriteParams0 = new BatchWriteParams();
    {
      List<BatchRequest> requests1 = new ArrayList<>();
      {
        BatchRequest requests_02 = new BatchRequest();
        {
          Action action3 = Action.fromValue("addObject");
          requests_02.setAction(action3);
          Map<String, String> body3 = new HashMap<>();
          {
            String key4 = "value";
            body3.put("key", key4);
          }
          requests_02.setBody(body3);
        }
        requests1.add(requests_02);
      }
      batchWriteParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.batch(indexName0, batchWriteParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/batch");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"requests\":[{\"action\":\"addObject\",\"body\":{\"key\":\"value\"}}]}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("allows batch method with `clear` action")
  void batchTest1() {
    String indexName0 = "theIndexName";
    BatchWriteParams batchWriteParams0 = new BatchWriteParams();
    {
      List<BatchRequest> requests1 = new ArrayList<>();
      {
        BatchRequest requests_02 = new BatchRequest();
        {
          Action action3 = Action.fromValue("clear");
          requests_02.setAction(action3);
          Map<String, String> body3 = new HashMap<>();
          {
            String key4 = "value";
            body3.put("key", key4);
          }
          requests_02.setBody(body3);
        }
        requests1.add(requests_02);
      }
      batchWriteParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.batch(indexName0, batchWriteParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/batch");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"requests\":[{\"action\":\"clear\",\"body\":{\"key\":\"value\"}}]}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("allows batch method with `delete` action")
  void batchTest2() {
    String indexName0 = "theIndexName";
    BatchWriteParams batchWriteParams0 = new BatchWriteParams();
    {
      List<BatchRequest> requests1 = new ArrayList<>();
      {
        BatchRequest requests_02 = new BatchRequest();
        {
          Action action3 = Action.fromValue("delete");
          requests_02.setAction(action3);
          Map<String, String> body3 = new HashMap<>();
          {
            String key4 = "value";
            body3.put("key", key4);
          }
          requests_02.setBody(body3);
        }
        requests1.add(requests_02);
      }
      batchWriteParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.batch(indexName0, batchWriteParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/batch");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"requests\":[{\"action\":\"delete\",\"body\":{\"key\":\"value\"}}]}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("allows batch method with `deleteObject` action")
  void batchTest3() {
    String indexName0 = "theIndexName";
    BatchWriteParams batchWriteParams0 = new BatchWriteParams();
    {
      List<BatchRequest> requests1 = new ArrayList<>();
      {
        BatchRequest requests_02 = new BatchRequest();
        {
          Action action3 = Action.fromValue("deleteObject");
          requests_02.setAction(action3);
          Map<String, String> body3 = new HashMap<>();
          {
            String key4 = "value";
            body3.put("key", key4);
          }
          requests_02.setBody(body3);
        }
        requests1.add(requests_02);
      }
      batchWriteParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.batch(indexName0, batchWriteParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/batch");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"requests\":[{\"action\":\"deleteObject\",\"body\":{\"key\":\"value\"}}]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("allows batch method with `partialUpdateObject` action")
  void batchTest4() {
    String indexName0 = "theIndexName";
    BatchWriteParams batchWriteParams0 = new BatchWriteParams();
    {
      List<BatchRequest> requests1 = new ArrayList<>();
      {
        BatchRequest requests_02 = new BatchRequest();
        {
          Action action3 = Action.fromValue("partialUpdateObject");
          requests_02.setAction(action3);
          Map<String, String> body3 = new HashMap<>();
          {
            String key4 = "value";
            body3.put("key", key4);
          }
          requests_02.setBody(body3);
        }
        requests1.add(requests_02);
      }
      batchWriteParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.batch(indexName0, batchWriteParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/batch");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"requests\":[{\"action\":\"partialUpdateObject\",\"body\":{\"key\":\"value\"}}]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("allows batch method with `partialUpdateObjectNoCreate` action")
  void batchTest5() {
    String indexName0 = "theIndexName";
    BatchWriteParams batchWriteParams0 = new BatchWriteParams();
    {
      List<BatchRequest> requests1 = new ArrayList<>();
      {
        BatchRequest requests_02 = new BatchRequest();
        {
          Action action3 = Action.fromValue("partialUpdateObjectNoCreate");
          requests_02.setAction(action3);
          Map<String, String> body3 = new HashMap<>();
          {
            String key4 = "value";
            body3.put("key", key4);
          }
          requests_02.setBody(body3);
        }
        requests1.add(requests_02);
      }
      batchWriteParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.batch(indexName0, batchWriteParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/batch");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"requests\":[{\"action\":\"partialUpdateObjectNoCreate\",\"body\":{\"key\":\"value\"}}]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("allows batch method with `updateObject` action")
  void batchTest6() {
    String indexName0 = "theIndexName";
    BatchWriteParams batchWriteParams0 = new BatchWriteParams();
    {
      List<BatchRequest> requests1 = new ArrayList<>();
      {
        BatchRequest requests_02 = new BatchRequest();
        {
          Action action3 = Action.fromValue("updateObject");
          requests_02.setAction(action3);
          Map<String, String> body3 = new HashMap<>();
          {
            String key4 = "value";
            body3.put("key", key4);
          }
          requests_02.setBody(body3);
        }
        requests1.add(requests_02);
      }
      batchWriteParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.batch(indexName0, batchWriteParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/batch");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"requests\":[{\"action\":\"updateObject\",\"body\":{\"key\":\"value\"}}]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("batchAssignUserIds")
  void batchAssignUserIdsTest0() {
    String xAlgoliaUserID0 = "userID";
    BatchAssignUserIdsParams batchAssignUserIdsParams0 = new BatchAssignUserIdsParams();
    {
      String cluster1 = "theCluster";
      batchAssignUserIdsParams0.setCluster(cluster1);
      List<String> users1 = new ArrayList<>();
      {
        String users_02 = "user1";
        users1.add(users_02);
        String users_12 = "user2";
        users1.add(users_12);
      }
      batchAssignUserIdsParams0.setUsers(users1);
    }

    assertDoesNotThrow(() -> {
      client.batchAssignUserIds(xAlgoliaUserID0, batchAssignUserIdsParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/clusters/mapping/batch");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"cluster\":\"theCluster\",\"users\":[\"user1\",\"user2\"]}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedHeaders = json.readValue(
        "{\"x-algolia-user-id\":\"userID\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, String> actualHeaders = req.headers;

      for (Map.Entry<String, String> p : expectedHeaders.entrySet()) {
        assertEquals(actualHeaders.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse headers json");
    }
  }

  @Test
  @DisplayName("get batchDictionaryEntries results with minimal parameters")
  void batchDictionaryEntriesTest0() {
    DictionaryType dictionaryName0 = DictionaryType.fromValue("compounds");
    BatchDictionaryEntriesParams batchDictionaryEntriesParams0 = new BatchDictionaryEntriesParams();
    {
      List<BatchDictionaryEntriesRequest> requests1 = new ArrayList<>();
      {
        BatchDictionaryEntriesRequest requests_02 = new BatchDictionaryEntriesRequest();
        {
          DictionaryAction action3 = DictionaryAction.fromValue("addEntry");
          requests_02.setAction(action3);
          DictionaryEntry body3 = new DictionaryEntry();
          {
            String objectID4 = "1";
            body3.setObjectID(objectID4);
            String language4 = "en";
            body3.setLanguage(language4);
          }
          requests_02.setBody(body3);
        }
        requests1.add(requests_02);
        BatchDictionaryEntriesRequest requests_12 = new BatchDictionaryEntriesRequest();
        {
          DictionaryAction action3 = DictionaryAction.fromValue("deleteEntry");
          requests_12.setAction(action3);
          DictionaryEntry body3 = new DictionaryEntry();
          {
            String objectID4 = "2";
            body3.setObjectID(objectID4);
            String language4 = "fr";
            body3.setLanguage(language4);
          }
          requests_12.setBody(body3);
        }
        requests1.add(requests_12);
      }
      batchDictionaryEntriesParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.batchDictionaryEntries(dictionaryName0, batchDictionaryEntriesParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/dictionaries/compounds/batch");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"requests\":[{\"action\":\"addEntry\",\"body\":{\"objectID\":\"1\",\"language\":\"en\"}},{\"action\":\"deleteEntry\",\"body\":{\"objectID\":\"2\",\"language\":\"fr\"}}]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("get batchDictionaryEntries results with all parameters")
  void batchDictionaryEntriesTest1() {
    DictionaryType dictionaryName0 = DictionaryType.fromValue("compounds");
    BatchDictionaryEntriesParams batchDictionaryEntriesParams0 = new BatchDictionaryEntriesParams();
    {
      boolean clearExistingDictionaryEntries1 = false;
      batchDictionaryEntriesParams0.setClearExistingDictionaryEntries(clearExistingDictionaryEntries1);
      List<BatchDictionaryEntriesRequest> requests1 = new ArrayList<>();
      {
        BatchDictionaryEntriesRequest requests_02 = new BatchDictionaryEntriesRequest();
        {
          DictionaryAction action3 = DictionaryAction.fromValue("addEntry");
          requests_02.setAction(action3);
          DictionaryEntry body3 = new DictionaryEntry();
          {
            String objectID4 = "1";
            body3.setObjectID(objectID4);
            String language4 = "en";
            body3.setLanguage(language4);
            String word4 = "fancy";
            body3.setWord(word4);
            List<String> words4 = new ArrayList<>();
            {
              String words_05 = "believe";
              words4.add(words_05);
              String words_15 = "algolia";
              words4.add(words_15);
            }
            body3.setWords(words4);
            List<String> decomposition4 = new ArrayList<>();
            {
              String decomposition_05 = "trust";
              decomposition4.add(decomposition_05);
              String decomposition_15 = "algolia";
              decomposition4.add(decomposition_15);
            }
            body3.setDecomposition(decomposition4);
            DictionaryEntryState state4 = DictionaryEntryState.fromValue("enabled");
            body3.setState(state4);
          }
          requests_02.setBody(body3);
        }
        requests1.add(requests_02);
        BatchDictionaryEntriesRequest requests_12 = new BatchDictionaryEntriesRequest();
        {
          DictionaryAction action3 = DictionaryAction.fromValue("deleteEntry");
          requests_12.setAction(action3);
          DictionaryEntry body3 = new DictionaryEntry();
          {
            String objectID4 = "2";
            body3.setObjectID(objectID4);
            String language4 = "fr";
            body3.setLanguage(language4);
            String word4 = "humility";
            body3.setWord(word4);
            List<String> words4 = new ArrayList<>();
            {
              String words_05 = "candor";
              words4.add(words_05);
              String words_15 = "algolia";
              words4.add(words_15);
            }
            body3.setWords(words4);
            List<String> decomposition4 = new ArrayList<>();
            {
              String decomposition_05 = "grit";
              decomposition4.add(decomposition_05);
              String decomposition_15 = "algolia";
              decomposition4.add(decomposition_15);
            }
            body3.setDecomposition(decomposition4);
            DictionaryEntryState state4 = DictionaryEntryState.fromValue("enabled");
            body3.setState(state4);
          }
          requests_12.setBody(body3);
        }
        requests1.add(requests_12);
      }
      batchDictionaryEntriesParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.batchDictionaryEntries(dictionaryName0, batchDictionaryEntriesParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/dictionaries/compounds/batch");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"clearExistingDictionaryEntries\":false,\"requests\":[{\"action\":\"addEntry\",\"body\":{\"objectID\":\"1\",\"language\":\"en\",\"word\":\"fancy\",\"words\":[\"believe\",\"algolia\"],\"decomposition\":[\"trust\",\"algolia\"],\"state\":\"enabled\"}},{\"action\":\"deleteEntry\",\"body\":{\"objectID\":\"2\",\"language\":\"fr\",\"word\":\"humility\",\"words\":[\"candor\",\"algolia\"],\"decomposition\":[\"grit\",\"algolia\"],\"state\":\"enabled\"}}]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("get batchDictionaryEntries results additional properties")
  void batchDictionaryEntriesTest2() {
    DictionaryType dictionaryName0 = DictionaryType.fromValue("compounds");
    BatchDictionaryEntriesParams batchDictionaryEntriesParams0 = new BatchDictionaryEntriesParams();
    {
      List<BatchDictionaryEntriesRequest> requests1 = new ArrayList<>();
      {
        BatchDictionaryEntriesRequest requests_02 = new BatchDictionaryEntriesRequest();
        {
          DictionaryAction action3 = DictionaryAction.fromValue("addEntry");
          requests_02.setAction(action3);
          DictionaryEntry body3 = new DictionaryEntry();
          {
            String objectID4 = "1";
            body3.setObjectID(objectID4);
            String language4 = "en";
            body3.setLanguage(language4);
            String additional4 = "try me";
            body3.setAdditionalProperty("additional", additional4);
          }
          requests_02.setBody(body3);
        }
        requests1.add(requests_02);
      }
      batchDictionaryEntriesParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.batchDictionaryEntries(dictionaryName0, batchDictionaryEntriesParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/dictionaries/compounds/batch");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"requests\":[{\"action\":\"addEntry\",\"body\":{\"objectID\":\"1\",\"language\":\"en\",\"additional\":\"try" + " me\"}}]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("browse with minimal parameters")
  void browseTest0() {
    String indexName0 = "indexName";

    assertDoesNotThrow(() -> {
      client.browse(indexName0, Object.class);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/browse");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("browse with search parameters")
  void browseTest1() {
    String indexName0 = "indexName";
    BrowseParamsObject browseParams0 = new BrowseParamsObject();
    {
      String query1 = "myQuery";
      browseParams0.setQuery(query1);
      List<MixedSearchFilters> facetFilters1 = new ArrayList<>();
      {
        String facetFilters_02 = "tags:algolia";
        facetFilters1.add(MixedSearchFilters.of(facetFilters_02));
      }
      browseParams0.setFacetFilters(FacetFilters.of(facetFilters1));
    }

    assertDoesNotThrow(() -> {
      client.browse(indexName0, BrowseParams.of(browseParams0), Object.class);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/browse");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"query\":\"myQuery\",\"facetFilters\":[\"tags:algolia\"]}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("browse allow a cursor in parameters")
  void browseTest2() {
    String indexName0 = "indexName";
    BrowseParamsObject browseParams0 = new BrowseParamsObject();
    {
      String cursor1 = "test";
      browseParams0.setCursor(cursor1);
    }

    assertDoesNotThrow(() -> {
      client.browse(indexName0, BrowseParams.of(browseParams0), Object.class);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/browse");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"cursor\":\"test\"}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("clearAllSynonyms")
  void clearAllSynonymsTest0() {
    String indexName0 = "indexName";

    assertDoesNotThrow(() -> {
      client.clearAllSynonyms(indexName0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/synonyms/clear");
    assertEquals(req.method, "POST");
    assertEquals(req.body, "");
  }

  @Test
  @DisplayName("clearObjects")
  void clearObjectsTest0() {
    String indexName0 = "theIndexName";

    assertDoesNotThrow(() -> {
      client.clearObjects(indexName0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/clear");
    assertEquals(req.method, "POST");
    assertEquals(req.body, "");
  }

  @Test
  @DisplayName("clearRules")
  void clearRulesTest0() {
    String indexName0 = "indexName";

    assertDoesNotThrow(() -> {
      client.clearRules(indexName0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/rules/clear");
    assertEquals(req.method, "POST");
    assertEquals(req.body, "");
  }

  @Test
  @DisplayName("allow del method for a custom path with minimal parameters")
  void delTest0() {
    String path0 = "/test/minimal";

    assertDoesNotThrow(() -> {
      client.del(path0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/minimal");
    assertEquals(req.method, "DELETE");
    assertNull(req.body);
  }

  @Test
  @DisplayName("allow del method for a custom path with all parameters")
  void delTest1() {
    String path0 = "/test/all";
    Map<String, Object> parameters0 = new HashMap<>();
    {
      String query1 = "parameters";
      parameters0.put("query", query1);
    }

    assertDoesNotThrow(() -> {
      client.del(path0, parameters0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/all");
    assertEquals(req.method, "DELETE");
    assertNull(req.body);

    try {
      Map<String, String> expectedQuery = json.readValue("{\"query\":\"parameters\"}", new TypeReference<HashMap<String, String>>() {});
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("deleteApiKey")
  void deleteApiKeyTest0() {
    String key0 = "myTestApiKey";

    assertDoesNotThrow(() -> {
      client.deleteApiKey(key0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/keys/myTestApiKey");
    assertEquals(req.method, "DELETE");
    assertNull(req.body);
  }

  @Test
  @DisplayName("deleteBy")
  void deleteByTest0() {
    String indexName0 = "theIndexName";
    DeleteByParams deleteByParams0 = new DeleteByParams();
    {
      String filters1 = "brand:brandName";
      deleteByParams0.setFilters(filters1);
    }

    assertDoesNotThrow(() -> {
      client.deleteBy(indexName0, deleteByParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/deleteByQuery");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"filters\":\"brand:brandName\"}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("deleteIndex")
  void deleteIndexTest0() {
    String indexName0 = "theIndexName";

    assertDoesNotThrow(() -> {
      client.deleteIndex(indexName0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName");
    assertEquals(req.method, "DELETE");
    assertNull(req.body);
  }

  @Test
  @DisplayName("deleteObject")
  void deleteObjectTest0() {
    String indexName0 = "theIndexName";
    String objectID0 = "uniqueID";

    assertDoesNotThrow(() -> {
      client.deleteObject(indexName0, objectID0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/uniqueID");
    assertEquals(req.method, "DELETE");
    assertNull(req.body);
  }

  @Test
  @DisplayName("deleteRule")
  void deleteRuleTest0() {
    String indexName0 = "indexName";
    String objectID0 = "id1";

    assertDoesNotThrow(() -> {
      client.deleteRule(indexName0, objectID0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/rules/id1");
    assertEquals(req.method, "DELETE");
    assertNull(req.body);
  }

  @Test
  @DisplayName("deleteSource")
  void deleteSourceTest0() {
    String source0 = "theSource";

    assertDoesNotThrow(() -> {
      client.deleteSource(source0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/security/sources/theSource");
    assertEquals(req.method, "DELETE");
    assertNull(req.body);
  }

  @Test
  @DisplayName("deleteSynonym")
  void deleteSynonymTest0() {
    String indexName0 = "indexName";
    String objectID0 = "id1";

    assertDoesNotThrow(() -> {
      client.deleteSynonym(indexName0, objectID0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/synonyms/id1");
    assertEquals(req.method, "DELETE");
    assertNull(req.body);
  }

  @Test
  @DisplayName("allow get method for a custom path with minimal parameters")
  void getTest0() {
    String path0 = "/test/minimal";

    assertDoesNotThrow(() -> {
      client.get(path0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/minimal");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("allow get method for a custom path with all parameters")
  void getTest1() {
    String path0 = "/test/all";
    Map<String, Object> parameters0 = new HashMap<>();
    {
      String query1 = "parameters";
      parameters0.put("query", query1);
    }

    assertDoesNotThrow(() -> {
      client.get(path0, parameters0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/all");
    assertEquals(req.method, "GET");
    assertNull(req.body);

    try {
      Map<String, String> expectedQuery = json.readValue("{\"query\":\"parameters\"}", new TypeReference<HashMap<String, String>>() {});
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("getApiKey")
  void getApiKeyTest0() {
    String key0 = "myTestApiKey";

    assertDoesNotThrow(() -> {
      client.getApiKey(key0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/keys/myTestApiKey");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("get getDictionaryLanguages")
  void getDictionaryLanguagesTest0() {
    assertDoesNotThrow(() -> {
      client.getDictionaryLanguages();
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/dictionaries/*/languages");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("get getDictionarySettings results")
  void getDictionarySettingsTest0() {
    assertDoesNotThrow(() -> {
      client.getDictionarySettings();
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/dictionaries/*/settings");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("getLogs with minimal parameters")
  void getLogsTest0() {
    assertDoesNotThrow(() -> {
      client.getLogs();
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/logs");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("getLogs with parameters")
  void getLogsTest1() {
    int offset0 = 5;
    int length0 = 10;
    String indexName0 = "theIndexName";
    LogType type0 = LogType.fromValue("all");

    assertDoesNotThrow(() -> {
      client.getLogs(offset0, length0, indexName0, type0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/logs");
    assertEquals(req.method, "GET");
    assertNull(req.body);

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"offset\":\"5\",\"length\":\"10\",\"indexName\":\"theIndexName\",\"type\":\"all\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("getObject")
  void getObjectTest0() {
    String indexName0 = "theIndexName";
    String objectID0 = "uniqueID";
    List<String> attributesToRetrieve0 = new ArrayList<>();
    {
      String attributesToRetrieve_01 = "attr1";
      attributesToRetrieve0.add(attributesToRetrieve_01);
      String attributesToRetrieve_11 = "attr2";
      attributesToRetrieve0.add(attributesToRetrieve_11);
    }

    assertDoesNotThrow(() -> {
      client.getObject(indexName0, objectID0, attributesToRetrieve0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/uniqueID");
    assertEquals(req.method, "GET");
    assertNull(req.body);

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"attributesToRetrieve\":\"attr1,attr2\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("getObjects")
  void getObjectsTest0() {
    GetObjectsParams getObjectsParams0 = new GetObjectsParams();
    {
      List<GetObjectsRequest> requests1 = new ArrayList<>();
      {
        GetObjectsRequest requests_02 = new GetObjectsRequest();
        {
          List<String> attributesToRetrieve3 = new ArrayList<>();
          {
            String attributesToRetrieve_04 = "attr1";
            attributesToRetrieve3.add(attributesToRetrieve_04);
            String attributesToRetrieve_14 = "attr2";
            attributesToRetrieve3.add(attributesToRetrieve_14);
          }
          requests_02.setAttributesToRetrieve(attributesToRetrieve3);
          String objectID3 = "uniqueID";
          requests_02.setObjectID(objectID3);
          String indexName3 = "theIndexName";
          requests_02.setIndexName(indexName3);
        }
        requests1.add(requests_02);
      }
      getObjectsParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.getObjects(getObjectsParams0, Object.class);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/*/objects");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"requests\":[{\"attributesToRetrieve\":[\"attr1\",\"attr2\"],\"objectID\":\"uniqueID\",\"indexName\":\"theIndexName\"}]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("getRule")
  void getRuleTest0() {
    String indexName0 = "indexName";
    String objectID0 = "id1";

    assertDoesNotThrow(() -> {
      client.getRule(indexName0, objectID0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/rules/id1");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("getSettings")
  void getSettingsTest0() {
    String indexName0 = "theIndexName";

    assertDoesNotThrow(() -> {
      client.getSettings(indexName0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/settings");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("getSources")
  void getSourcesTest0() {
    assertDoesNotThrow(() -> {
      client.getSources();
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/security/sources");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("getSynonym")
  void getSynonymTest0() {
    String indexName0 = "indexName";
    String objectID0 = "id1";

    assertDoesNotThrow(() -> {
      client.getSynonym(indexName0, objectID0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/synonyms/id1");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("getTask")
  void getTaskTest0() {
    String indexName0 = "theIndexName";
    long taskID0 = 123L;

    assertDoesNotThrow(() -> {
      client.getTask(indexName0, taskID0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/task/123");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("getTopUserIds")
  void getTopUserIdsTest0() {
    assertDoesNotThrow(() -> {
      client.getTopUserIds();
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/clusters/mapping/top");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("getUserId")
  void getUserIdTest0() {
    String userID0 = "uniqueID";

    assertDoesNotThrow(() -> {
      client.getUserId(userID0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/clusters/mapping/uniqueID");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("hasPendingMappings with minimal parameters")
  void hasPendingMappingsTest0() {
    assertDoesNotThrow(() -> {
      client.hasPendingMappings();
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/clusters/mapping/pending");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("hasPendingMappings with parameters")
  void hasPendingMappingsTest1() {
    boolean getClusters0 = true;

    assertDoesNotThrow(() -> {
      client.hasPendingMappings(getClusters0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/clusters/mapping/pending");
    assertEquals(req.method, "GET");
    assertNull(req.body);

    try {
      Map<String, String> expectedQuery = json.readValue("{\"getClusters\":\"true\"}", new TypeReference<HashMap<String, String>>() {});
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("listApiKeys")
  void listApiKeysTest0() {
    assertDoesNotThrow(() -> {
      client.listApiKeys();
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/keys");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("listClusters")
  void listClustersTest0() {
    assertDoesNotThrow(() -> {
      client.listClusters();
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/clusters");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("listIndices with minimal parameters")
  void listIndicesTest0() {
    assertDoesNotThrow(() -> {
      client.listIndices();
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("listIndices with parameters")
  void listIndicesTest1() {
    int page0 = 8;
    int hitsPerPage0 = 3;

    assertDoesNotThrow(() -> {
      client.listIndices(page0, hitsPerPage0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes");
    assertEquals(req.method, "GET");
    assertNull(req.body);

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"page\":\"8\",\"hitsPerPage\":\"3\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("listUserIds with minimal parameters")
  void listUserIdsTest0() {
    assertDoesNotThrow(() -> {
      client.listUserIds();
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/clusters/mapping");
    assertEquals(req.method, "GET");
    assertNull(req.body);
  }

  @Test
  @DisplayName("listUserIds with parameters")
  void listUserIdsTest1() {
    int page0 = 8;
    int hitsPerPage0 = 100;

    assertDoesNotThrow(() -> {
      client.listUserIds(page0, hitsPerPage0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/clusters/mapping");
    assertEquals(req.method, "GET");
    assertNull(req.body);

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"page\":\"8\",\"hitsPerPage\":\"100\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("multipleBatch")
  void multipleBatchTest0() {
    BatchParams batchParams0 = new BatchParams();
    {
      List<MultipleBatchRequest> requests1 = new ArrayList<>();
      {
        MultipleBatchRequest requests_02 = new MultipleBatchRequest();
        {
          Action action3 = Action.fromValue("addObject");
          requests_02.setAction(action3);
          Map<String, String> body3 = new HashMap<>();
          {
            String key4 = "value";
            body3.put("key", key4);
          }
          requests_02.setBody(body3);
          String indexName3 = "theIndexName";
          requests_02.setIndexName(indexName3);
        }
        requests1.add(requests_02);
      }
      batchParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.multipleBatch(batchParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/*/batch");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"requests\":[{\"action\":\"addObject\",\"body\":{\"key\":\"value\"},\"indexName\":\"theIndexName\"}]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("operationIndex")
  void operationIndexTest0() {
    String indexName0 = "theIndexName";
    OperationIndexParams operationIndexParams0 = new OperationIndexParams();
    {
      OperationType operation1 = OperationType.fromValue("copy");
      operationIndexParams0.setOperation(operation1);
      String destination1 = "dest";
      operationIndexParams0.setDestination(destination1);
      List<ScopeType> scope1 = new ArrayList<>();
      {
        ScopeType scope_02 = ScopeType.fromValue("rules");
        scope1.add(scope_02);
        ScopeType scope_12 = ScopeType.fromValue("settings");
        scope1.add(scope_12);
      }
      operationIndexParams0.setScope(scope1);
    }

    assertDoesNotThrow(() -> {
      client.operationIndex(indexName0, operationIndexParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/operation");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"operation\":\"copy\",\"destination\":\"dest\",\"scope\":[\"rules\",\"settings\"]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("partialUpdateObject")
  void partialUpdateObjectTest0() {
    String indexName0 = "theIndexName";
    String objectID0 = "uniqueID";
    Map<String, AttributeToUpdate> attributesToUpdate0 = new HashMap<>();
    {
      String id11 = "test";
      attributesToUpdate0.put("id1", AttributeToUpdate.of(id11));
      BuiltInOperation id21 = new BuiltInOperation();
      {
        BuiltInOperationType operation2 = BuiltInOperationType.fromValue("AddUnique");
        id21.setOperation(operation2);
        String value2 = "test2";
        id21.setValue(value2);
      }
      attributesToUpdate0.put("id2", AttributeToUpdate.of(id21));
    }
    boolean createIfNotExists0 = true;

    assertDoesNotThrow(() -> {
      client.partialUpdateObject(indexName0, objectID0, attributesToUpdate0, createIfNotExists0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/uniqueID/partial");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"id1\":\"test\",\"id2\":{\"_operation\":\"AddUnique\",\"value\":\"test2\"}}",
        req.body,
        JSONCompareMode.STRICT
      );
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"createIfNotExists\":\"true\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("allow post method for a custom path with minimal parameters")
  void postTest0() {
    String path0 = "/test/minimal";

    assertDoesNotThrow(() -> {
      client.post(path0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/minimal");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("allow post method for a custom path with all parameters")
  void postTest1() {
    String path0 = "/test/all";
    Map<String, Object> parameters0 = new HashMap<>();
    {
      String query1 = "parameters";
      parameters0.put("query", query1);
    }
    Map<String, String> body0 = new HashMap<>();
    {
      String body1 = "parameters";
      body0.put("body", body1);
    }

    assertDoesNotThrow(() -> {
      client.post(path0, parameters0, body0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/all");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"body\":\"parameters\"}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue("{\"query\":\"parameters\"}", new TypeReference<HashMap<String, String>>() {});
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("requestOptions can override default query parameters")
  void postTest2() {
    String path0 = "/test/requestOptions";
    Map<String, Object> parameters0 = new HashMap<>();
    {
      String query1 = "parameters";
      parameters0.put("query", query1);
    }
    Map<String, String> body0 = new HashMap<>();
    {
      String facet1 = "filters";
      body0.put("facet", facet1);
    }

    RequestOptions requestOptions = new RequestOptions();
    requestOptions.addExtraQueryParameters("query", "myQueryParameter");

    assertDoesNotThrow(() -> {
      client.post(path0, parameters0, body0, requestOptions);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/requestOptions");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"facet\":\"filters\"}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"query\":\"myQueryParameter\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("requestOptions merges query parameters with default ones")
  void postTest3() {
    String path0 = "/test/requestOptions";
    Map<String, Object> parameters0 = new HashMap<>();
    {
      String query1 = "parameters";
      parameters0.put("query", query1);
    }
    Map<String, String> body0 = new HashMap<>();
    {
      String facet1 = "filters";
      body0.put("facet", facet1);
    }

    RequestOptions requestOptions = new RequestOptions();
    requestOptions.addExtraQueryParameters("query2", "myQueryParameter");

    assertDoesNotThrow(() -> {
      client.post(path0, parameters0, body0, requestOptions);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/requestOptions");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"facet\":\"filters\"}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"query\":\"parameters\",\"query2\":\"myQueryParameter\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("requestOptions can override default headers")
  void postTest4() {
    String path0 = "/test/requestOptions";
    Map<String, Object> parameters0 = new HashMap<>();
    {
      String query1 = "parameters";
      parameters0.put("query", query1);
    }
    Map<String, String> body0 = new HashMap<>();
    {
      String facet1 = "filters";
      body0.put("facet", facet1);
    }

    RequestOptions requestOptions = new RequestOptions();
    requestOptions.addExtraHeader("x-algolia-api-key", "myApiKey");

    assertDoesNotThrow(() -> {
      client.post(path0, parameters0, body0, requestOptions);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/requestOptions");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"facet\":\"filters\"}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue("{\"query\":\"parameters\"}", new TypeReference<HashMap<String, String>>() {});
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }

    try {
      Map<String, String> expectedHeaders = json.readValue(
        "{\"x-algolia-api-key\":\"myApiKey\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, String> actualHeaders = req.headers;

      for (Map.Entry<String, String> p : expectedHeaders.entrySet()) {
        assertEquals(actualHeaders.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse headers json");
    }
  }

  @Test
  @DisplayName("requestOptions merges headers with default ones")
  void postTest5() {
    String path0 = "/test/requestOptions";
    Map<String, Object> parameters0 = new HashMap<>();
    {
      String query1 = "parameters";
      parameters0.put("query", query1);
    }
    Map<String, String> body0 = new HashMap<>();
    {
      String facet1 = "filters";
      body0.put("facet", facet1);
    }

    RequestOptions requestOptions = new RequestOptions();
    requestOptions.addExtraHeader("x-algolia-api-key", "myApiKey");

    assertDoesNotThrow(() -> {
      client.post(path0, parameters0, body0, requestOptions);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/requestOptions");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"facet\":\"filters\"}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue("{\"query\":\"parameters\"}", new TypeReference<HashMap<String, String>>() {});
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }

    try {
      Map<String, String> expectedHeaders = json.readValue(
        "{\"x-algolia-api-key\":\"myApiKey\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, String> actualHeaders = req.headers;

      for (Map.Entry<String, String> p : expectedHeaders.entrySet()) {
        assertEquals(actualHeaders.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse headers json");
    }
  }

  @Test
  @DisplayName("requestOptions queryParameters accepts booleans")
  void postTest6() {
    String path0 = "/test/requestOptions";
    Map<String, Object> parameters0 = new HashMap<>();
    {
      String query1 = "parameters";
      parameters0.put("query", query1);
    }
    Map<String, String> body0 = new HashMap<>();
    {
      String facet1 = "filters";
      body0.put("facet", facet1);
    }

    RequestOptions requestOptions = new RequestOptions();
    requestOptions.addExtraQueryParameters("isItWorking", true);

    assertDoesNotThrow(() -> {
      client.post(path0, parameters0, body0, requestOptions);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/requestOptions");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"facet\":\"filters\"}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"query\":\"parameters\",\"isItWorking\":\"true\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("requestOptions queryParameters accepts integers")
  void postTest7() {
    String path0 = "/test/requestOptions";
    Map<String, Object> parameters0 = new HashMap<>();
    {
      String query1 = "parameters";
      parameters0.put("query", query1);
    }
    Map<String, String> body0 = new HashMap<>();
    {
      String facet1 = "filters";
      body0.put("facet", facet1);
    }

    RequestOptions requestOptions = new RequestOptions();
    requestOptions.addExtraQueryParameters("myParam", 2);

    assertDoesNotThrow(() -> {
      client.post(path0, parameters0, body0, requestOptions);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/requestOptions");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"facet\":\"filters\"}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"query\":\"parameters\",\"myParam\":\"2\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("requestOptions queryParameters accepts list of string")
  void postTest8() {
    String path0 = "/test/requestOptions";
    Map<String, Object> parameters0 = new HashMap<>();
    {
      String query1 = "parameters";
      parameters0.put("query", query1);
    }
    Map<String, String> body0 = new HashMap<>();
    {
      String facet1 = "filters";
      body0.put("facet", facet1);
    }

    RequestOptions requestOptions = new RequestOptions();
    requestOptions.addExtraQueryParameters("myParam", Arrays.asList("c", "d"));

    assertDoesNotThrow(() -> {
      client.post(path0, parameters0, body0, requestOptions);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/requestOptions");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"facet\":\"filters\"}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"query\":\"parameters\",\"myParam\":\"c,d\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("requestOptions queryParameters accepts list of booleans")
  void postTest9() {
    String path0 = "/test/requestOptions";
    Map<String, Object> parameters0 = new HashMap<>();
    {
      String query1 = "parameters";
      parameters0.put("query", query1);
    }
    Map<String, String> body0 = new HashMap<>();
    {
      String facet1 = "filters";
      body0.put("facet", facet1);
    }

    RequestOptions requestOptions = new RequestOptions();
    requestOptions.addExtraQueryParameters("myParam", Arrays.asList(true, true, false));

    assertDoesNotThrow(() -> {
      client.post(path0, parameters0, body0, requestOptions);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/requestOptions");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"facet\":\"filters\"}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"query\":\"parameters\",\"myParam\":\"true,true,false\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("requestOptions queryParameters accepts list of integers")
  void postTest10() {
    String path0 = "/test/requestOptions";
    Map<String, Object> parameters0 = new HashMap<>();
    {
      String query1 = "parameters";
      parameters0.put("query", query1);
    }
    Map<String, String> body0 = new HashMap<>();
    {
      String facet1 = "filters";
      body0.put("facet", facet1);
    }

    RequestOptions requestOptions = new RequestOptions();
    requestOptions.addExtraQueryParameters("myParam", Arrays.asList(1, 2));

    assertDoesNotThrow(() -> {
      client.post(path0, parameters0, body0, requestOptions);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/requestOptions");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"facet\":\"filters\"}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"query\":\"parameters\",\"myParam\":\"1,2\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("allow put method for a custom path with minimal parameters")
  void putTest0() {
    String path0 = "/test/minimal";

    assertDoesNotThrow(() -> {
      client.put(path0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/minimal");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("allow put method for a custom path with all parameters")
  void putTest1() {
    String path0 = "/test/all";
    Map<String, Object> parameters0 = new HashMap<>();
    {
      String query1 = "parameters";
      parameters0.put("query", query1);
    }
    Map<String, String> body0 = new HashMap<>();
    {
      String body1 = "parameters";
      body0.put("body", body1);
    }

    assertDoesNotThrow(() -> {
      client.put(path0, parameters0, body0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/test/all");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"body\":\"parameters\"}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue("{\"query\":\"parameters\"}", new TypeReference<HashMap<String, String>>() {});
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("removeUserId")
  void removeUserIdTest0() {
    String userID0 = "uniqueID";

    assertDoesNotThrow(() -> {
      client.removeUserId(userID0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/clusters/mapping/uniqueID");
    assertEquals(req.method, "DELETE");
    assertNull(req.body);
  }

  @Test
  @DisplayName("replaceSources")
  void replaceSourcesTest0() {
    List<Source> source0 = new ArrayList<>();
    {
      Source source_01 = new Source();
      {
        String source2 = "theSource";
        source_01.setSource(source2);
        String description2 = "theDescription";
        source_01.setDescription(description2);
      }
      source0.add(source_01);
    }

    assertDoesNotThrow(() -> {
      client.replaceSources(source0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/security/sources");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("[{\"source\":\"theSource\",\"description\":\"theDescription\"}]", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("restoreApiKey")
  void restoreApiKeyTest0() {
    String key0 = "myApiKey";

    assertDoesNotThrow(() -> {
      client.restoreApiKey(key0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/keys/myApiKey/restore");
    assertEquals(req.method, "POST");
    assertEquals(req.body, "");
  }

  @Test
  @DisplayName("saveObject")
  void saveObjectTest0() {
    String indexName0 = "theIndexName";
    Map<String, String> body0 = new HashMap<>();
    {
      String objectID1 = "id";
      body0.put("objectID", objectID1);
      String test1 = "val";
      body0.put("test", test1);
    }

    assertDoesNotThrow(() -> {
      client.saveObject(indexName0, body0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"objectID\":\"id\",\"test\":\"val\"}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("saveRule with minimal parameters")
  void saveRuleTest0() {
    String indexName0 = "indexName";
    String objectID0 = "id1";
    Rule rule0 = new Rule();
    {
      String objectID1 = "id1";
      rule0.setObjectID(objectID1);
      List<Condition> conditions1 = new ArrayList<>();
      {
        Condition conditions_02 = new Condition();
        {
          String pattern3 = "apple";
          conditions_02.setPattern(pattern3);
          Anchoring anchoring3 = Anchoring.fromValue("contains");
          conditions_02.setAnchoring(anchoring3);
        }
        conditions1.add(conditions_02);
      }
      rule0.setConditions(conditions1);
    }

    assertDoesNotThrow(() -> {
      client.saveRule(indexName0, objectID0, rule0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/rules/id1");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"objectID\":\"id1\",\"conditions\":[{\"pattern\":\"apple\",\"anchoring\":\"contains\"}]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("saveRule with all parameters")
  void saveRuleTest1() {
    String indexName0 = "indexName";
    String objectID0 = "id1";
    Rule rule0 = new Rule();
    {
      String objectID1 = "id1";
      rule0.setObjectID(objectID1);
      List<Condition> conditions1 = new ArrayList<>();
      {
        Condition conditions_02 = new Condition();
        {
          String pattern3 = "apple";
          conditions_02.setPattern(pattern3);
          Anchoring anchoring3 = Anchoring.fromValue("contains");
          conditions_02.setAnchoring(anchoring3);
          boolean alternatives3 = false;
          conditions_02.setAlternatives(alternatives3);
          String context3 = "search";
          conditions_02.setContext(context3);
        }
        conditions1.add(conditions_02);
      }
      rule0.setConditions(conditions1);
      Consequence consequence1 = new Consequence();
      {
        ConsequenceParams params2 = new ConsequenceParams();
        {
          String filters3 = "brand:apple";
          params2.setFilters(filters3);
          ConsequenceQueryObject query3 = new ConsequenceQueryObject();
          {
            List<String> remove4 = new ArrayList<>();
            {
              String remove_05 = "algolia";
              remove4.add(remove_05);
            }
            query3.setRemove(remove4);
            List<Edit> edits4 = new ArrayList<>();
            {
              Edit edits_05 = new Edit();
              {
                EditType type6 = EditType.fromValue("remove");
                edits_05.setType(type6);
                String delete6 = "abc";
                edits_05.setDelete(delete6);
                String insert6 = "cde";
                edits_05.setInsert(insert6);
              }
              edits4.add(edits_05);
              Edit edits_15 = new Edit();
              {
                EditType type6 = EditType.fromValue("replace");
                edits_15.setType(type6);
                String delete6 = "abc";
                edits_15.setDelete(delete6);
                String insert6 = "cde";
                edits_15.setInsert(insert6);
              }
              edits4.add(edits_15);
            }
            query3.setEdits(edits4);
          }
          params2.setQuery(ConsequenceQuery.of(query3));
        }
        consequence1.setParams(params2);
        List<ConsequenceHide> hide2 = new ArrayList<>();
        {
          ConsequenceHide hide_03 = new ConsequenceHide();
          {
            String objectID4 = "321";
            hide_03.setObjectID(objectID4);
          }
          hide2.add(hide_03);
        }
        consequence1.setHide(hide2);
        boolean filterPromotes2 = false;
        consequence1.setFilterPromotes(filterPromotes2);
        Map<String, String> userData2 = new HashMap<>();
        {
          String algolia3 = "aloglia";
          userData2.put("algolia", algolia3);
        }
        consequence1.setUserData(userData2);
        List<Promote> promote2 = new ArrayList<>();
        {
          PromoteObjectID promote_03 = new PromoteObjectID();
          {
            String objectID4 = "abc";
            promote_03.setObjectID(objectID4);
            int position4 = 3;
            promote_03.setPosition(position4);
          }
          promote2.add(Promote.of(promote_03));
          PromoteObjectIDs promote_13 = new PromoteObjectIDs();
          {
            List<String> objectIDs4 = new ArrayList<>();
            {
              String objectIDs_05 = "abc";
              objectIDs4.add(objectIDs_05);
              String objectIDs_15 = "def";
              objectIDs4.add(objectIDs_15);
            }
            promote_13.setObjectIDs(objectIDs4);
            int position4 = 1;
            promote_13.setPosition(position4);
          }
          promote2.add(Promote.of(promote_13));
        }
        consequence1.setPromote(promote2);
      }
      rule0.setConsequence(consequence1);
      String description1 = "test";
      rule0.setDescription(description1);
      boolean enabled1 = true;
      rule0.setEnabled(enabled1);
      List<TimeRange> validity1 = new ArrayList<>();
      {
        TimeRange validity_02 = new TimeRange();
        {
          int from3 = 1656670273;
          validity_02.setFrom(from3);
          int until3 = 1656670277;
          validity_02.setUntil(until3);
        }
        validity1.add(validity_02);
      }
      rule0.setValidity(validity1);
    }
    boolean forwardToReplicas0 = true;

    assertDoesNotThrow(() -> {
      client.saveRule(indexName0, objectID0, rule0, forwardToReplicas0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/rules/id1");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"objectID\":\"id1\",\"conditions\":[{\"pattern\":\"apple\",\"anchoring\":\"contains\",\"alternatives\":false,\"context\":\"search\"}],\"consequence\":{\"params\":{\"filters\":\"brand:apple\",\"query\":{\"remove\":[\"algolia\"],\"edits\":[{\"type\":\"remove\",\"delete\":\"abc\",\"insert\":\"cde\"},{\"type\":\"replace\",\"delete\":\"abc\",\"insert\":\"cde\"}]}},\"hide\":[{\"objectID\":\"321\"}],\"filterPromotes\":false,\"userData\":{\"algolia\":\"aloglia\"},\"promote\":[{\"objectID\":\"abc\",\"position\":3},{\"objectIDs\":[\"abc\",\"def\"],\"position\":1}]},\"description\":\"test\",\"enabled\":true,\"validity\":[{\"from\":1656670273,\"until\":1656670277}]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"forwardToReplicas\":\"true\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("saveRules with minimal parameters")
  void saveRulesTest0() {
    String indexName0 = "indexName";
    List<Rule> rules0 = new ArrayList<>();
    {
      Rule rules_01 = new Rule();
      {
        String objectID2 = "a-rule-id";
        rules_01.setObjectID(objectID2);
        List<Condition> conditions2 = new ArrayList<>();
        {
          Condition conditions_03 = new Condition();
          {
            String pattern4 = "smartphone";
            conditions_03.setPattern(pattern4);
            Anchoring anchoring4 = Anchoring.fromValue("contains");
            conditions_03.setAnchoring(anchoring4);
          }
          conditions2.add(conditions_03);
        }
        rules_01.setConditions(conditions2);
      }
      rules0.add(rules_01);
      Rule rules_11 = new Rule();
      {
        String objectID2 = "a-second-rule-id";
        rules_11.setObjectID(objectID2);
        List<Condition> conditions2 = new ArrayList<>();
        {
          Condition conditions_03 = new Condition();
          {
            String pattern4 = "apple";
            conditions_03.setPattern(pattern4);
            Anchoring anchoring4 = Anchoring.fromValue("contains");
            conditions_03.setAnchoring(anchoring4);
          }
          conditions2.add(conditions_03);
        }
        rules_11.setConditions(conditions2);
      }
      rules0.add(rules_11);
    }

    assertDoesNotThrow(() -> {
      client.saveRules(indexName0, rules0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/rules/batch");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "[{\"objectID\":\"a-rule-id\",\"conditions\":[{\"pattern\":\"smartphone\",\"anchoring\":\"contains\"}]},{\"objectID\":\"a-second-rule-id\",\"conditions\":[{\"pattern\":\"apple\",\"anchoring\":\"contains\"}]}]",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("saveRules with all parameters")
  void saveRulesTest1() {
    String indexName0 = "indexName";
    List<Rule> rules0 = new ArrayList<>();
    {
      Rule rules_01 = new Rule();
      {
        String objectID2 = "id1";
        rules_01.setObjectID(objectID2);
        List<Condition> conditions2 = new ArrayList<>();
        {
          Condition conditions_03 = new Condition();
          {
            String pattern4 = "apple";
            conditions_03.setPattern(pattern4);
            Anchoring anchoring4 = Anchoring.fromValue("contains");
            conditions_03.setAnchoring(anchoring4);
            boolean alternatives4 = false;
            conditions_03.setAlternatives(alternatives4);
            String context4 = "search";
            conditions_03.setContext(context4);
          }
          conditions2.add(conditions_03);
        }
        rules_01.setConditions(conditions2);
        Consequence consequence2 = new Consequence();
        {
          ConsequenceParams params3 = new ConsequenceParams();
          {
            String filters4 = "brand:apple";
            params3.setFilters(filters4);
            ConsequenceQueryObject query4 = new ConsequenceQueryObject();
            {
              List<String> remove5 = new ArrayList<>();
              {
                String remove_06 = "algolia";
                remove5.add(remove_06);
              }
              query4.setRemove(remove5);
              List<Edit> edits5 = new ArrayList<>();
              {
                Edit edits_06 = new Edit();
                {
                  EditType type7 = EditType.fromValue("remove");
                  edits_06.setType(type7);
                  String delete7 = "abc";
                  edits_06.setDelete(delete7);
                  String insert7 = "cde";
                  edits_06.setInsert(insert7);
                }
                edits5.add(edits_06);
                Edit edits_16 = new Edit();
                {
                  EditType type7 = EditType.fromValue("replace");
                  edits_16.setType(type7);
                  String delete7 = "abc";
                  edits_16.setDelete(delete7);
                  String insert7 = "cde";
                  edits_16.setInsert(insert7);
                }
                edits5.add(edits_16);
              }
              query4.setEdits(edits5);
            }
            params3.setQuery(ConsequenceQuery.of(query4));
          }
          consequence2.setParams(params3);
          List<ConsequenceHide> hide3 = new ArrayList<>();
          {
            ConsequenceHide hide_04 = new ConsequenceHide();
            {
              String objectID5 = "321";
              hide_04.setObjectID(objectID5);
            }
            hide3.add(hide_04);
          }
          consequence2.setHide(hide3);
          boolean filterPromotes3 = false;
          consequence2.setFilterPromotes(filterPromotes3);
          Map<String, String> userData3 = new HashMap<>();
          {
            String algolia4 = "aloglia";
            userData3.put("algolia", algolia4);
          }
          consequence2.setUserData(userData3);
          List<Promote> promote3 = new ArrayList<>();
          {
            PromoteObjectID promote_04 = new PromoteObjectID();
            {
              String objectID5 = "abc";
              promote_04.setObjectID(objectID5);
              int position5 = 3;
              promote_04.setPosition(position5);
            }
            promote3.add(Promote.of(promote_04));
            PromoteObjectIDs promote_14 = new PromoteObjectIDs();
            {
              List<String> objectIDs5 = new ArrayList<>();
              {
                String objectIDs_06 = "abc";
                objectIDs5.add(objectIDs_06);
                String objectIDs_16 = "def";
                objectIDs5.add(objectIDs_16);
              }
              promote_14.setObjectIDs(objectIDs5);
              int position5 = 1;
              promote_14.setPosition(position5);
            }
            promote3.add(Promote.of(promote_14));
          }
          consequence2.setPromote(promote3);
        }
        rules_01.setConsequence(consequence2);
        String description2 = "test";
        rules_01.setDescription(description2);
        boolean enabled2 = true;
        rules_01.setEnabled(enabled2);
        List<TimeRange> validity2 = new ArrayList<>();
        {
          TimeRange validity_03 = new TimeRange();
          {
            int from4 = 1656670273;
            validity_03.setFrom(from4);
            int until4 = 1656670277;
            validity_03.setUntil(until4);
          }
          validity2.add(validity_03);
        }
        rules_01.setValidity(validity2);
      }
      rules0.add(rules_01);
    }
    boolean forwardToReplicas0 = true;
    boolean clearExistingRules0 = true;

    assertDoesNotThrow(() -> {
      client.saveRules(indexName0, rules0, forwardToReplicas0, clearExistingRules0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/rules/batch");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "[{\"objectID\":\"id1\",\"conditions\":[{\"pattern\":\"apple\",\"anchoring\":\"contains\",\"alternatives\":false,\"context\":\"search\"}],\"consequence\":{\"params\":{\"filters\":\"brand:apple\",\"query\":{\"remove\":[\"algolia\"],\"edits\":[{\"type\":\"remove\",\"delete\":\"abc\",\"insert\":\"cde\"},{\"type\":\"replace\",\"delete\":\"abc\",\"insert\":\"cde\"}]}},\"hide\":[{\"objectID\":\"321\"}],\"filterPromotes\":false,\"userData\":{\"algolia\":\"aloglia\"},\"promote\":[{\"objectID\":\"abc\",\"position\":3},{\"objectIDs\":[\"abc\",\"def\"],\"position\":1}]},\"description\":\"test\",\"enabled\":true,\"validity\":[{\"from\":1656670273,\"until\":1656670277}]}]",
        req.body,
        JSONCompareMode.STRICT
      );
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"forwardToReplicas\":\"true\",\"clearExistingRules\":\"true\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("saveSynonym")
  void saveSynonymTest0() {
    String indexName0 = "indexName";
    String objectID0 = "id1";
    SynonymHit synonymHit0 = new SynonymHit();
    {
      String objectID1 = "id1";
      synonymHit0.setObjectID(objectID1);
      SynonymType type1 = SynonymType.fromValue("synonym");
      synonymHit0.setType(type1);
      List<String> synonyms1 = new ArrayList<>();
      {
        String synonyms_02 = "car";
        synonyms1.add(synonyms_02);
        String synonyms_12 = "vehicule";
        synonyms1.add(synonyms_12);
        String synonyms_22 = "auto";
        synonyms1.add(synonyms_22);
      }
      synonymHit0.setSynonyms(synonyms1);
    }
    boolean forwardToReplicas0 = true;

    assertDoesNotThrow(() -> {
      client.saveSynonym(indexName0, objectID0, synonymHit0, forwardToReplicas0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/synonyms/id1");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"objectID\":\"id1\",\"type\":\"synonym\",\"synonyms\":[\"car\",\"vehicule\",\"auto\"]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"forwardToReplicas\":\"true\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("saveSynonyms")
  void saveSynonymsTest0() {
    String indexName0 = "indexName";
    List<SynonymHit> synonymHit0 = new ArrayList<>();
    {
      SynonymHit synonymHit_01 = new SynonymHit();
      {
        String objectID2 = "id1";
        synonymHit_01.setObjectID(objectID2);
        SynonymType type2 = SynonymType.fromValue("synonym");
        synonymHit_01.setType(type2);
        List<String> synonyms2 = new ArrayList<>();
        {
          String synonyms_03 = "car";
          synonyms2.add(synonyms_03);
          String synonyms_13 = "vehicule";
          synonyms2.add(synonyms_13);
          String synonyms_23 = "auto";
          synonyms2.add(synonyms_23);
        }
        synonymHit_01.setSynonyms(synonyms2);
      }
      synonymHit0.add(synonymHit_01);
      SynonymHit synonymHit_11 = new SynonymHit();
      {
        String objectID2 = "id2";
        synonymHit_11.setObjectID(objectID2);
        SynonymType type2 = SynonymType.fromValue("onewaysynonym");
        synonymHit_11.setType(type2);
        String input2 = "iphone";
        synonymHit_11.setInput(input2);
        List<String> synonyms2 = new ArrayList<>();
        {
          String synonyms_03 = "ephone";
          synonyms2.add(synonyms_03);
          String synonyms_13 = "aphone";
          synonyms2.add(synonyms_13);
          String synonyms_23 = "yphone";
          synonyms2.add(synonyms_23);
        }
        synonymHit_11.setSynonyms(synonyms2);
      }
      synonymHit0.add(synonymHit_11);
    }
    boolean forwardToReplicas0 = true;
    boolean replaceExistingSynonyms0 = false;

    assertDoesNotThrow(() -> {
      client.saveSynonyms(indexName0, synonymHit0, forwardToReplicas0, replaceExistingSynonyms0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/synonyms/batch");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "[{\"objectID\":\"id1\",\"type\":\"synonym\",\"synonyms\":[\"car\",\"vehicule\",\"auto\"]},{\"objectID\":\"id2\",\"type\":\"onewaysynonym\",\"input\":\"iphone\",\"synonyms\":[\"ephone\",\"aphone\",\"yphone\"]}]",
        req.body,
        JSONCompareMode.STRICT
      );
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"forwardToReplicas\":\"true\",\"replaceExistingSynonyms\":\"false\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("search for a single hits request with minimal parameters")
  void searchTest0() {
    SearchMethodParams searchMethodParams0 = new SearchMethodParams();
    {
      List<SearchQuery> requests1 = new ArrayList<>();
      {
        SearchForHits requests_02 = new SearchForHits();
        {
          String indexName3 = "theIndexName";
          requests_02.setIndexName(indexName3);
        }
        requests1.add(SearchQuery.of(requests_02));
      }
      searchMethodParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.search(searchMethodParams0, Object.class);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/*/queries");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"requests\":[{\"indexName\":\"theIndexName\"}]}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("search for a single facet request with minimal parameters")
  void searchTest1() {
    SearchMethodParams searchMethodParams0 = new SearchMethodParams();
    {
      List<SearchQuery> requests1 = new ArrayList<>();
      {
        SearchForFacets requests_02 = new SearchForFacets();
        {
          String indexName3 = "theIndexName";
          requests_02.setIndexName(indexName3);
          SearchTypeFacet type3 = SearchTypeFacet.fromValue("facet");
          requests_02.setType(type3);
          String facet3 = "theFacet";
          requests_02.setFacet(facet3);
        }
        requests1.add(SearchQuery.of(requests_02));
      }
      searchMethodParams0.setRequests(requests1);
      SearchStrategy strategy1 = SearchStrategy.fromValue("stopIfEnoughMatches");
      searchMethodParams0.setStrategy(strategy1);
    }

    assertDoesNotThrow(() -> {
      client.search(searchMethodParams0, Object.class);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/*/queries");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"requests\":[{\"indexName\":\"theIndexName\",\"type\":\"facet\",\"facet\":\"theFacet\"}],\"strategy\":\"stopIfEnoughMatches\"}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("search for a single hits request with all parameters")
  void searchTest2() {
    SearchMethodParams searchMethodParams0 = new SearchMethodParams();
    {
      List<SearchQuery> requests1 = new ArrayList<>();
      {
        SearchForHits requests_02 = new SearchForHits();
        {
          String indexName3 = "theIndexName";
          requests_02.setIndexName(indexName3);
          String query3 = "myQuery";
          requests_02.setQuery(query3);
          int hitsPerPage3 = 50;
          requests_02.setHitsPerPage(hitsPerPage3);
          SearchTypeDefault type3 = SearchTypeDefault.fromValue("default");
          requests_02.setType(type3);
        }
        requests1.add(SearchQuery.of(requests_02));
      }
      searchMethodParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.search(searchMethodParams0, Object.class);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/*/queries");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"requests\":[{\"indexName\":\"theIndexName\",\"query\":\"myQuery\",\"hitsPerPage\":50,\"type\":\"default\"}]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("search for a single facet request with all parameters")
  void searchTest3() {
    SearchMethodParams searchMethodParams0 = new SearchMethodParams();
    {
      List<SearchQuery> requests1 = new ArrayList<>();
      {
        SearchForFacets requests_02 = new SearchForFacets();
        {
          String indexName3 = "theIndexName";
          requests_02.setIndexName(indexName3);
          SearchTypeFacet type3 = SearchTypeFacet.fromValue("facet");
          requests_02.setType(type3);
          String facet3 = "theFacet";
          requests_02.setFacet(facet3);
          String facetQuery3 = "theFacetQuery";
          requests_02.setFacetQuery(facetQuery3);
          String query3 = "theQuery";
          requests_02.setQuery(query3);
          int maxFacetHits3 = 50;
          requests_02.setMaxFacetHits(maxFacetHits3);
        }
        requests1.add(SearchQuery.of(requests_02));
      }
      searchMethodParams0.setRequests(requests1);
      SearchStrategy strategy1 = SearchStrategy.fromValue("stopIfEnoughMatches");
      searchMethodParams0.setStrategy(strategy1);
    }

    assertDoesNotThrow(() -> {
      client.search(searchMethodParams0, Object.class);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/*/queries");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"requests\":[{\"indexName\":\"theIndexName\",\"type\":\"facet\",\"facet\":\"theFacet\",\"facetQuery\":\"theFacetQuery\",\"query\":\"theQuery\",\"maxFacetHits\":50}],\"strategy\":\"stopIfEnoughMatches\"}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("search for multiple mixed requests in multiple indices with minimal parameters")
  void searchTest4() {
    SearchMethodParams searchMethodParams0 = new SearchMethodParams();
    {
      List<SearchQuery> requests1 = new ArrayList<>();
      {
        SearchForHits requests_02 = new SearchForHits();
        {
          String indexName3 = "theIndexName";
          requests_02.setIndexName(indexName3);
        }
        requests1.add(SearchQuery.of(requests_02));
        SearchForFacets requests_12 = new SearchForFacets();
        {
          String indexName3 = "theIndexName2";
          requests_12.setIndexName(indexName3);
          SearchTypeFacet type3 = SearchTypeFacet.fromValue("facet");
          requests_12.setType(type3);
          String facet3 = "theFacet";
          requests_12.setFacet(facet3);
        }
        requests1.add(SearchQuery.of(requests_12));
        SearchForHits requests_22 = new SearchForHits();
        {
          String indexName3 = "theIndexName";
          requests_22.setIndexName(indexName3);
          SearchTypeDefault type3 = SearchTypeDefault.fromValue("default");
          requests_22.setType(type3);
        }
        requests1.add(SearchQuery.of(requests_22));
      }
      searchMethodParams0.setRequests(requests1);
      SearchStrategy strategy1 = SearchStrategy.fromValue("stopIfEnoughMatches");
      searchMethodParams0.setStrategy(strategy1);
    }

    assertDoesNotThrow(() -> {
      client.search(searchMethodParams0, Object.class);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/*/queries");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"requests\":[{\"indexName\":\"theIndexName\"},{\"indexName\":\"theIndexName2\",\"type\":\"facet\",\"facet\":\"theFacet\"},{\"indexName\":\"theIndexName\",\"type\":\"default\"}],\"strategy\":\"stopIfEnoughMatches\"}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("search for multiple mixed requests in multiple indices with all parameters")
  void searchTest5() {
    SearchMethodParams searchMethodParams0 = new SearchMethodParams();
    {
      List<SearchQuery> requests1 = new ArrayList<>();
      {
        SearchForFacets requests_02 = new SearchForFacets();
        {
          String indexName3 = "theIndexName";
          requests_02.setIndexName(indexName3);
          SearchTypeFacet type3 = SearchTypeFacet.fromValue("facet");
          requests_02.setType(type3);
          String facet3 = "theFacet";
          requests_02.setFacet(facet3);
          String facetQuery3 = "theFacetQuery";
          requests_02.setFacetQuery(facetQuery3);
          String query3 = "theQuery";
          requests_02.setQuery(query3);
          int maxFacetHits3 = 50;
          requests_02.setMaxFacetHits(maxFacetHits3);
        }
        requests1.add(SearchQuery.of(requests_02));
        SearchForHits requests_12 = new SearchForHits();
        {
          String indexName3 = "theIndexName";
          requests_12.setIndexName(indexName3);
          String query3 = "myQuery";
          requests_12.setQuery(query3);
          int hitsPerPage3 = 50;
          requests_12.setHitsPerPage(hitsPerPage3);
          SearchTypeDefault type3 = SearchTypeDefault.fromValue("default");
          requests_12.setType(type3);
        }
        requests1.add(SearchQuery.of(requests_12));
      }
      searchMethodParams0.setRequests(requests1);
      SearchStrategy strategy1 = SearchStrategy.fromValue("stopIfEnoughMatches");
      searchMethodParams0.setStrategy(strategy1);
    }

    assertDoesNotThrow(() -> {
      client.search(searchMethodParams0, Object.class);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/*/queries");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"requests\":[{\"indexName\":\"theIndexName\",\"type\":\"facet\",\"facet\":\"theFacet\",\"facetQuery\":\"theFacetQuery\",\"query\":\"theQuery\",\"maxFacetHits\":50},{\"indexName\":\"theIndexName\",\"query\":\"myQuery\",\"hitsPerPage\":50,\"type\":\"default\"}],\"strategy\":\"stopIfEnoughMatches\"}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("search filters accept all of the possible shapes")
  void searchTest6() {
    SearchMethodParams searchMethodParams0 = new SearchMethodParams();
    {
      List<SearchQuery> requests1 = new ArrayList<>();
      {
        SearchForHits requests_02 = new SearchForHits();
        {
          String indexName3 = "theIndexName";
          requests_02.setIndexName(indexName3);
          String facetFilters3 = "mySearch:filters";
          requests_02.setFacetFilters(FacetFilters.of(facetFilters3));
          String reRankingApplyFilter3 = "mySearch:filters";
          requests_02.setReRankingApplyFilter(ReRankingApplyFilter.of(reRankingApplyFilter3));
          String tagFilters3 = "mySearch:filters";
          requests_02.setTagFilters(TagFilters.of(tagFilters3));
          String numericFilters3 = "mySearch:filters";
          requests_02.setNumericFilters(NumericFilters.of(numericFilters3));
          String optionalFilters3 = "mySearch:filters";
          requests_02.setOptionalFilters(OptionalFilters.of(optionalFilters3));
        }
        requests1.add(SearchQuery.of(requests_02));
        SearchForHits requests_12 = new SearchForHits();
        {
          String indexName3 = "theIndexName";
          requests_12.setIndexName(indexName3);
          List<MixedSearchFilters> facetFilters3 = new ArrayList<>();
          {
            String facetFilters_04 = "mySearch:filters";
            facetFilters3.add(MixedSearchFilters.of(facetFilters_04));
            List<String> facetFilters_14 = new ArrayList<>();
            {
              String facetFilters_1_05 = "mySearch:filters";
              facetFilters_14.add(facetFilters_1_05);
            }
            facetFilters3.add(MixedSearchFilters.of(facetFilters_14));
          }
          requests_12.setFacetFilters(FacetFilters.of(facetFilters3));
          List<MixedSearchFilters> reRankingApplyFilter3 = new ArrayList<>();
          {
            String reRankingApplyFilter_04 = "mySearch:filters";
            reRankingApplyFilter3.add(MixedSearchFilters.of(reRankingApplyFilter_04));
            List<String> reRankingApplyFilter_14 = new ArrayList<>();
            {
              String reRankingApplyFilter_1_05 = "mySearch:filters";
              reRankingApplyFilter_14.add(reRankingApplyFilter_1_05);
            }
            reRankingApplyFilter3.add(MixedSearchFilters.of(reRankingApplyFilter_14));
          }
          requests_12.setReRankingApplyFilter(ReRankingApplyFilter.of(reRankingApplyFilter3));
          List<MixedSearchFilters> tagFilters3 = new ArrayList<>();
          {
            String tagFilters_04 = "mySearch:filters";
            tagFilters3.add(MixedSearchFilters.of(tagFilters_04));
            List<String> tagFilters_14 = new ArrayList<>();
            {
              String tagFilters_1_05 = "mySearch:filters";
              tagFilters_14.add(tagFilters_1_05);
            }
            tagFilters3.add(MixedSearchFilters.of(tagFilters_14));
          }
          requests_12.setTagFilters(TagFilters.of(tagFilters3));
          List<MixedSearchFilters> numericFilters3 = new ArrayList<>();
          {
            String numericFilters_04 = "mySearch:filters";
            numericFilters3.add(MixedSearchFilters.of(numericFilters_04));
            List<String> numericFilters_14 = new ArrayList<>();
            {
              String numericFilters_1_05 = "mySearch:filters";
              numericFilters_14.add(numericFilters_1_05);
            }
            numericFilters3.add(MixedSearchFilters.of(numericFilters_14));
          }
          requests_12.setNumericFilters(NumericFilters.of(numericFilters3));
          List<MixedSearchFilters> optionalFilters3 = new ArrayList<>();
          {
            String optionalFilters_04 = "mySearch:filters";
            optionalFilters3.add(MixedSearchFilters.of(optionalFilters_04));
            List<String> optionalFilters_14 = new ArrayList<>();
            {
              String optionalFilters_1_05 = "mySearch:filters";
              optionalFilters_14.add(optionalFilters_1_05);
            }
            optionalFilters3.add(MixedSearchFilters.of(optionalFilters_14));
          }
          requests_12.setOptionalFilters(OptionalFilters.of(optionalFilters3));
        }
        requests1.add(SearchQuery.of(requests_12));
      }
      searchMethodParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.search(searchMethodParams0, Object.class);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/*/queries");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"requests\":[{\"indexName\":\"theIndexName\",\"facetFilters\":\"mySearch:filters\",\"reRankingApplyFilter\":\"mySearch:filters\",\"tagFilters\":\"mySearch:filters\",\"numericFilters\":\"mySearch:filters\",\"optionalFilters\":\"mySearch:filters\"},{\"indexName\":\"theIndexName\",\"facetFilters\":[\"mySearch:filters\",[\"mySearch:filters\"]],\"reRankingApplyFilter\":[\"mySearch:filters\",[\"mySearch:filters\"]],\"tagFilters\":[\"mySearch:filters\",[\"mySearch:filters\"]],\"numericFilters\":[\"mySearch:filters\",[\"mySearch:filters\"]],\"optionalFilters\":[\"mySearch:filters\",[\"mySearch:filters\"]]}]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("search with all search parameters")
  void searchTest7() {
    SearchMethodParams searchMethodParams0 = new SearchMethodParams();
    {
      List<SearchQuery> requests1 = new ArrayList<>();
      {
        SearchForHits requests_02 = new SearchForHits();
        {
          boolean advancedSyntax3 = true;
          requests_02.setAdvancedSyntax(advancedSyntax3);
          List<AdvancedSyntaxFeatures> advancedSyntaxFeatures3 = new ArrayList<>();
          {
            AdvancedSyntaxFeatures advancedSyntaxFeatures_04 = AdvancedSyntaxFeatures.fromValue("exactPhrase");
            advancedSyntaxFeatures3.add(advancedSyntaxFeatures_04);
          }
          requests_02.setAdvancedSyntaxFeatures(advancedSyntaxFeatures3);
          boolean allowTyposOnNumericTokens3 = true;
          requests_02.setAllowTyposOnNumericTokens(allowTyposOnNumericTokens3);
          List<AlternativesAsExact> alternativesAsExact3 = new ArrayList<>();
          {
            AlternativesAsExact alternativesAsExact_04 = AlternativesAsExact.fromValue("multiWordsSynonym");
            alternativesAsExact3.add(alternativesAsExact_04);
          }
          requests_02.setAlternativesAsExact(alternativesAsExact3);
          boolean analytics3 = true;
          requests_02.setAnalytics(analytics3);
          List<String> analyticsTags3 = new ArrayList<>();
          {
            String analyticsTags_04 = "";
            analyticsTags3.add(analyticsTags_04);
          }
          requests_02.setAnalyticsTags(analyticsTags3);
          String aroundLatLng3 = "";
          requests_02.setAroundLatLng(aroundLatLng3);
          boolean aroundLatLngViaIP3 = true;
          requests_02.setAroundLatLngViaIP(aroundLatLngViaIP3);
          int aroundPrecision3 = 0;
          requests_02.setAroundPrecision(AroundPrecision.of(aroundPrecision3));
          AroundRadiusAll aroundRadius3 = AroundRadiusAll.fromValue("all");
          requests_02.setAroundRadius(AroundRadius.of(aroundRadius3));
          boolean attributeCriteriaComputedByMinProximity3 = true;
          requests_02.setAttributeCriteriaComputedByMinProximity(attributeCriteriaComputedByMinProximity3);
          List<String> attributesForFaceting3 = new ArrayList<>();
          {
            String attributesForFaceting_04 = "";
            attributesForFaceting3.add(attributesForFaceting_04);
          }
          requests_02.setAttributesForFaceting(attributesForFaceting3);
          List<String> attributesToHighlight3 = new ArrayList<>();
          {
            String attributesToHighlight_04 = "";
            attributesToHighlight3.add(attributesToHighlight_04);
          }
          requests_02.setAttributesToHighlight(attributesToHighlight3);
          List<String> attributesToRetrieve3 = new ArrayList<>();
          {
            String attributesToRetrieve_04 = "";
            attributesToRetrieve3.add(attributesToRetrieve_04);
          }
          requests_02.setAttributesToRetrieve(attributesToRetrieve3);
          List<String> attributesToSnippet3 = new ArrayList<>();
          {
            String attributesToSnippet_04 = "";
            attributesToSnippet3.add(attributesToSnippet_04);
          }
          requests_02.setAttributesToSnippet(attributesToSnippet3);
          boolean clickAnalytics3 = true;
          requests_02.setClickAnalytics(clickAnalytics3);
          List<String> customRanking3 = new ArrayList<>();
          {
            String customRanking_04 = "";
            customRanking3.add(customRanking_04);
          }
          requests_02.setCustomRanking(customRanking3);
          boolean decompoundQuery3 = true;
          requests_02.setDecompoundQuery(decompoundQuery3);
          List<String> disableExactOnAttributes3 = new ArrayList<>();
          {
            String disableExactOnAttributes_04 = "";
            disableExactOnAttributes3.add(disableExactOnAttributes_04);
          }
          requests_02.setDisableExactOnAttributes(disableExactOnAttributes3);
          List<String> disableTypoToleranceOnAttributes3 = new ArrayList<>();
          {
            String disableTypoToleranceOnAttributes_04 = "";
            disableTypoToleranceOnAttributes3.add(disableTypoToleranceOnAttributes_04);
          }
          requests_02.setDisableTypoToleranceOnAttributes(disableTypoToleranceOnAttributes3);
          int distinct3 = 0;
          requests_02.setDistinct(Distinct.of(distinct3));
          boolean enableABTest3 = true;
          requests_02.setEnableABTest(enableABTest3);
          boolean enablePersonalization3 = true;
          requests_02.setEnablePersonalization(enablePersonalization3);
          boolean enableReRanking3 = true;
          requests_02.setEnableReRanking(enableReRanking3);
          boolean enableRules3 = true;
          requests_02.setEnableRules(enableRules3);
          ExactOnSingleWordQuery exactOnSingleWordQuery3 = ExactOnSingleWordQuery.fromValue("attribute");
          requests_02.setExactOnSingleWordQuery(exactOnSingleWordQuery3);
          List<String> explain3 = new ArrayList<>();
          {
            String explain_04 = "foo";
            explain3.add(explain_04);
            String explain_14 = "bar";
            explain3.add(explain_14);
          }
          requests_02.setExplain(explain3);
          List<MixedSearchFilters> facetFilters3 = new ArrayList<>();
          {
            String facetFilters_04 = "";
            facetFilters3.add(MixedSearchFilters.of(facetFilters_04));
          }
          requests_02.setFacetFilters(FacetFilters.of(facetFilters3));
          boolean facetingAfterDistinct3 = true;
          requests_02.setFacetingAfterDistinct(facetingAfterDistinct3);
          List<String> facets3 = new ArrayList<>();
          {
            String facets_04 = "";
            facets3.add(facets_04);
          }
          requests_02.setFacets(facets3);
          String filters3 = "";
          requests_02.setFilters(filters3);
          boolean getRankingInfo3 = true;
          requests_02.setGetRankingInfo(getRankingInfo3);
          String highlightPostTag3 = "";
          requests_02.setHighlightPostTag(highlightPostTag3);
          String highlightPreTag3 = "";
          requests_02.setHighlightPreTag(highlightPreTag3);
          int hitsPerPage3 = 0;
          requests_02.setHitsPerPage(hitsPerPage3);
          boolean ignorePlurals3 = false;
          requests_02.setIgnorePlurals(IgnorePlurals.of(ignorePlurals3));
          String indexName3 = "theIndexName";
          requests_02.setIndexName(indexName3);
          List<Double> insideBoundingBox3 = new ArrayList<>();
          {
            double insideBoundingBox_04 = 47.3165;
            insideBoundingBox3.add(insideBoundingBox_04);
            double insideBoundingBox_14 = 4.9665;
            insideBoundingBox3.add(insideBoundingBox_14);
          }
          requests_02.setInsideBoundingBox(insideBoundingBox3);
          List<Double> insidePolygon3 = new ArrayList<>();
          {
            double insidePolygon_04 = 47.3165;
            insidePolygon3.add(insidePolygon_04);
            double insidePolygon_14 = 4.9665;
            insidePolygon3.add(insidePolygon_14);
          }
          requests_02.setInsidePolygon(insidePolygon3);
          String keepDiacriticsOnCharacters3 = "";
          requests_02.setKeepDiacriticsOnCharacters(keepDiacriticsOnCharacters3);
          int length3 = 0;
          requests_02.setLength(length3);
          int maxValuesPerFacet3 = 0;
          requests_02.setMaxValuesPerFacet(maxValuesPerFacet3);
          int minProximity3 = 0;
          requests_02.setMinProximity(minProximity3);
          int minWordSizefor1Typo3 = 0;
          requests_02.setMinWordSizefor1Typo(minWordSizefor1Typo3);
          int minWordSizefor2Typos3 = 0;
          requests_02.setMinWordSizefor2Typos(minWordSizefor2Typos3);
          int minimumAroundRadius3 = 0;
          requests_02.setMinimumAroundRadius(minimumAroundRadius3);
          List<String> naturalLanguages3 = new ArrayList<>();
          {
            String naturalLanguages_04 = "";
            naturalLanguages3.add(naturalLanguages_04);
          }
          requests_02.setNaturalLanguages(naturalLanguages3);
          List<MixedSearchFilters> numericFilters3 = new ArrayList<>();
          {
            String numericFilters_04 = "";
            numericFilters3.add(MixedSearchFilters.of(numericFilters_04));
          }
          requests_02.setNumericFilters(NumericFilters.of(numericFilters3));
          int offset3 = 0;
          requests_02.setOffset(offset3);
          List<MixedSearchFilters> optionalFilters3 = new ArrayList<>();
          {
            String optionalFilters_04 = "";
            optionalFilters3.add(MixedSearchFilters.of(optionalFilters_04));
          }
          requests_02.setOptionalFilters(OptionalFilters.of(optionalFilters3));
          List<String> optionalWords3 = new ArrayList<>();
          {
            String optionalWords_04 = "";
            optionalWords3.add(optionalWords_04);
          }
          requests_02.setOptionalWords(optionalWords3);
          int page3 = 0;
          requests_02.setPage(page3);
          boolean percentileComputation3 = true;
          requests_02.setPercentileComputation(percentileComputation3);
          int personalizationImpact3 = 0;
          requests_02.setPersonalizationImpact(personalizationImpact3);
          String query3 = "";
          requests_02.setQuery(query3);
          List<String> queryLanguages3 = new ArrayList<>();
          {
            String queryLanguages_04 = "";
            queryLanguages3.add(queryLanguages_04);
          }
          requests_02.setQueryLanguages(queryLanguages3);
          QueryType queryType3 = QueryType.fromValue("prefixAll");
          requests_02.setQueryType(queryType3);
          List<String> ranking3 = new ArrayList<>();
          {
            String ranking_04 = "";
            ranking3.add(ranking_04);
          }
          requests_02.setRanking(ranking3);
          List<MixedSearchFilters> reRankingApplyFilter3 = new ArrayList<>();
          {
            String reRankingApplyFilter_04 = "";
            reRankingApplyFilter3.add(MixedSearchFilters.of(reRankingApplyFilter_04));
          }
          requests_02.setReRankingApplyFilter(ReRankingApplyFilter.of(reRankingApplyFilter3));
          int relevancyStrictness3 = 0;
          requests_02.setRelevancyStrictness(relevancyStrictness3);
          boolean removeStopWords3 = true;
          requests_02.setRemoveStopWords(RemoveStopWords.of(removeStopWords3));
          RemoveWordsIfNoResults removeWordsIfNoResults3 = RemoveWordsIfNoResults.fromValue("allOptional");
          requests_02.setRemoveWordsIfNoResults(removeWordsIfNoResults3);
          RenderingContent renderingContent3 = new RenderingContent();
          {
            FacetOrdering facetOrdering4 = new FacetOrdering();
            {
              Facets facets5 = new Facets();
              {
                List<String> order6 = new ArrayList<>();
                {
                  String order_07 = "a";
                  order6.add(order_07);
                  String order_17 = "b";
                  order6.add(order_17);
                }
                facets5.setOrder(order6);
              }
              facetOrdering4.setFacets(facets5);
              Map<String, Value> values5 = new HashMap<>();
              {
                Value a6 = new Value();
                {
                  List<String> order7 = new ArrayList<>();
                  {
                    String order_08 = "b";
                    order7.add(order_08);
                  }
                  a6.setOrder(order7);
                  SortRemainingBy sortRemainingBy7 = SortRemainingBy.fromValue("count");
                  a6.setSortRemainingBy(sortRemainingBy7);
                }
                values5.put("a", a6);
              }
              facetOrdering4.setValues(values5);
            }
            renderingContent3.setFacetOrdering(facetOrdering4);
          }
          requests_02.setRenderingContent(renderingContent3);
          boolean replaceSynonymsInHighlight3 = true;
          requests_02.setReplaceSynonymsInHighlight(replaceSynonymsInHighlight3);
          List<String> responseFields3 = new ArrayList<>();
          {
            String responseFields_04 = "";
            responseFields3.add(responseFields_04);
          }
          requests_02.setResponseFields(responseFields3);
          boolean restrictHighlightAndSnippetArrays3 = true;
          requests_02.setRestrictHighlightAndSnippetArrays(restrictHighlightAndSnippetArrays3);
          List<String> restrictSearchableAttributes3 = new ArrayList<>();
          {
            String restrictSearchableAttributes_04 = "";
            restrictSearchableAttributes3.add(restrictSearchableAttributes_04);
          }
          requests_02.setRestrictSearchableAttributes(restrictSearchableAttributes3);
          List<String> ruleContexts3 = new ArrayList<>();
          {
            String ruleContexts_04 = "";
            ruleContexts3.add(ruleContexts_04);
          }
          requests_02.setRuleContexts(ruleContexts3);
          String similarQuery3 = "";
          requests_02.setSimilarQuery(similarQuery3);
          String snippetEllipsisText3 = "";
          requests_02.setSnippetEllipsisText(snippetEllipsisText3);
          String sortFacetValuesBy3 = "";
          requests_02.setSortFacetValuesBy(sortFacetValuesBy3);
          boolean sumOrFiltersScores3 = true;
          requests_02.setSumOrFiltersScores(sumOrFiltersScores3);
          boolean synonyms3 = true;
          requests_02.setSynonyms(synonyms3);
          List<MixedSearchFilters> tagFilters3 = new ArrayList<>();
          {
            String tagFilters_04 = "";
            tagFilters3.add(MixedSearchFilters.of(tagFilters_04));
          }
          requests_02.setTagFilters(TagFilters.of(tagFilters3));
          SearchTypeDefault type3 = SearchTypeDefault.fromValue("default");
          requests_02.setType(type3);
          TypoToleranceEnum typoTolerance3 = TypoToleranceEnum.fromValue("min");
          requests_02.setTypoTolerance(TypoTolerance.of(typoTolerance3));
          String userToken3 = "";
          requests_02.setUserToken(userToken3);
        }
        requests1.add(SearchQuery.of(requests_02));
      }
      searchMethodParams0.setRequests(requests1);
    }

    assertDoesNotThrow(() -> {
      client.search(searchMethodParams0, Object.class);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/*/queries");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"requests\":[{\"advancedSyntax\":true,\"advancedSyntaxFeatures\":[\"exactPhrase\"],\"allowTyposOnNumericTokens\":true,\"alternativesAsExact\":[\"multiWordsSynonym\"],\"analytics\":true,\"analyticsTags\":[\"\"],\"aroundLatLng\":\"\",\"aroundLatLngViaIP\":true,\"aroundPrecision\":0,\"aroundRadius\":\"all\",\"attributeCriteriaComputedByMinProximity\":true,\"attributesForFaceting\":[\"\"],\"attributesToHighlight\":[\"\"],\"attributesToRetrieve\":[\"\"],\"attributesToSnippet\":[\"\"],\"clickAnalytics\":true,\"customRanking\":[\"\"],\"decompoundQuery\":true,\"disableExactOnAttributes\":[\"\"],\"disableTypoToleranceOnAttributes\":[\"\"],\"distinct\":0,\"enableABTest\":true,\"enablePersonalization\":true,\"enableReRanking\":true,\"enableRules\":true,\"exactOnSingleWordQuery\":\"attribute\",\"explain\":[\"foo\",\"bar\"],\"facetFilters\":[\"\"],\"facetingAfterDistinct\":true,\"facets\":[\"\"],\"filters\":\"\",\"getRankingInfo\":true,\"highlightPostTag\":\"\",\"highlightPreTag\":\"\",\"hitsPerPage\":0,\"ignorePlurals\":false,\"indexName\":\"theIndexName\",\"insideBoundingBox\":[47.3165,4.9665],\"insidePolygon\":[47.3165,4.9665],\"keepDiacriticsOnCharacters\":\"\",\"length\":0,\"maxValuesPerFacet\":0,\"minProximity\":0,\"minWordSizefor1Typo\":0,\"minWordSizefor2Typos\":0,\"minimumAroundRadius\":0,\"naturalLanguages\":[\"\"],\"numericFilters\":[\"\"],\"offset\":0,\"optionalFilters\":[\"\"],\"optionalWords\":[\"\"],\"page\":0,\"percentileComputation\":true,\"personalizationImpact\":0,\"query\":\"\",\"queryLanguages\":[\"\"],\"queryType\":\"prefixAll\",\"ranking\":[\"\"],\"reRankingApplyFilter\":[\"\"],\"relevancyStrictness\":0,\"removeStopWords\":true,\"removeWordsIfNoResults\":\"allOptional\",\"renderingContent\":{\"facetOrdering\":{\"facets\":{\"order\":[\"a\",\"b\"]},\"values\":{\"a\":{\"order\":[\"b\"],\"sortRemainingBy\":\"count\"}}}},\"replaceSynonymsInHighlight\":true,\"responseFields\":[\"\"],\"restrictHighlightAndSnippetArrays\":true,\"restrictSearchableAttributes\":[\"\"],\"ruleContexts\":[\"\"],\"similarQuery\":\"\",\"snippetEllipsisText\":\"\",\"sortFacetValuesBy\":\"\",\"sumOrFiltersScores\":true,\"synonyms\":true,\"tagFilters\":[\"\"],\"type\":\"default\",\"typoTolerance\":\"min\",\"userToken\":\"\"}]}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("get searchDictionaryEntries results with minimal parameters")
  void searchDictionaryEntriesTest0() {
    DictionaryType dictionaryName0 = DictionaryType.fromValue("compounds");
    SearchDictionaryEntriesParams searchDictionaryEntriesParams0 = new SearchDictionaryEntriesParams();
    {
      String query1 = "foo";
      searchDictionaryEntriesParams0.setQuery(query1);
    }

    assertDoesNotThrow(() -> {
      client.searchDictionaryEntries(dictionaryName0, searchDictionaryEntriesParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/dictionaries/compounds/search");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"query\":\"foo\"}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("get searchDictionaryEntries results with all parameters")
  void searchDictionaryEntriesTest1() {
    DictionaryType dictionaryName0 = DictionaryType.fromValue("compounds");
    SearchDictionaryEntriesParams searchDictionaryEntriesParams0 = new SearchDictionaryEntriesParams();
    {
      String query1 = "foo";
      searchDictionaryEntriesParams0.setQuery(query1);
      int page1 = 4;
      searchDictionaryEntriesParams0.setPage(page1);
      int hitsPerPage1 = 2;
      searchDictionaryEntriesParams0.setHitsPerPage(hitsPerPage1);
      String language1 = "fr";
      searchDictionaryEntriesParams0.setLanguage(language1);
    }

    assertDoesNotThrow(() -> {
      client.searchDictionaryEntries(dictionaryName0, searchDictionaryEntriesParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/dictionaries/compounds/search");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"query\":\"foo\",\"page\":4,\"hitsPerPage\":2,\"language\":\"fr\"}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("get searchForFacetValues results with minimal parameters")
  void searchForFacetValuesTest0() {
    String indexName0 = "indexName";
    String facetName0 = "facetName";

    assertDoesNotThrow(() -> {
      client.searchForFacetValues(indexName0, facetName0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/facets/facetName/query");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("get searchForFacetValues results with all parameters")
  void searchForFacetValuesTest1() {
    String indexName0 = "indexName";
    String facetName0 = "facetName";
    SearchForFacetValuesRequest searchForFacetValuesRequest0 = new SearchForFacetValuesRequest();
    {
      String params1 = "query=foo&facetFilters=['bar']";
      searchForFacetValuesRequest0.setParams(params1);
      String facetQuery1 = "foo";
      searchForFacetValuesRequest0.setFacetQuery(facetQuery1);
      int maxFacetHits1 = 42;
      searchForFacetValuesRequest0.setMaxFacetHits(maxFacetHits1);
    }

    assertDoesNotThrow(() -> {
      client.searchForFacetValues(indexName0, facetName0, searchForFacetValuesRequest0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/facets/facetName/query");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"params\":\"query=foo&facetFilters=['bar']\",\"facetQuery\":\"foo\",\"maxFacetHits\":42}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("searchRules")
  void searchRulesTest0() {
    String indexName0 = "indexName";
    SearchRulesParams searchRulesParams0 = new SearchRulesParams();
    {
      String query1 = "something";
      searchRulesParams0.setQuery(query1);
    }

    assertDoesNotThrow(() -> {
      client.searchRules(indexName0, searchRulesParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/rules/search");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"query\":\"something\"}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("search with minimal parameters")
  void searchSingleIndexTest0() {
    String indexName0 = "indexName";

    assertDoesNotThrow(() -> {
      client.searchSingleIndex(indexName0, Object.class);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/query");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("search with searchParams")
  void searchSingleIndexTest1() {
    String indexName0 = "indexName";
    SearchParamsObject searchParams0 = new SearchParamsObject();
    {
      String query1 = "myQuery";
      searchParams0.setQuery(query1);
      List<MixedSearchFilters> facetFilters1 = new ArrayList<>();
      {
        String facetFilters_02 = "tags:algolia";
        facetFilters1.add(MixedSearchFilters.of(facetFilters_02));
      }
      searchParams0.setFacetFilters(FacetFilters.of(facetFilters1));
    }

    assertDoesNotThrow(() -> {
      client.searchSingleIndex(indexName0, SearchParams.of(searchParams0), Object.class);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/query");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"query\":\"myQuery\",\"facetFilters\":[\"tags:algolia\"]}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("searchSynonyms with minimal parameters")
  void searchSynonymsTest0() {
    String indexName0 = "indexName";

    assertDoesNotThrow(() -> {
      client.searchSynonyms(indexName0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/synonyms/search");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{}", req.body, JSONCompareMode.STRICT);
    });
  }

  @Test
  @DisplayName("searchSynonyms with all parameters")
  void searchSynonymsTest1() {
    String indexName0 = "indexName";
    SynonymType type0 = SynonymType.fromValue("altcorrection1");
    int page0 = 10;
    int hitsPerPage0 = 10;
    SearchSynonymsParams searchSynonymsParams0 = new SearchSynonymsParams();
    {
      String query1 = "myQuery";
      searchSynonymsParams0.setQuery(query1);
    }

    assertDoesNotThrow(() -> {
      client.searchSynonyms(indexName0, type0, page0, hitsPerPage0, searchSynonymsParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/indexName/synonyms/search");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"query\":\"myQuery\"}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"type\":\"altcorrection1\",\"page\":\"10\",\"hitsPerPage\":\"10\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("searchUserIds")
  void searchUserIdsTest0() {
    SearchUserIdsParams searchUserIdsParams0 = new SearchUserIdsParams();
    {
      String query1 = "test";
      searchUserIdsParams0.setQuery(query1);
      String clusterName1 = "theClusterName";
      searchUserIdsParams0.setClusterName(clusterName1);
      int page1 = 5;
      searchUserIdsParams0.setPage(page1);
      int hitsPerPage1 = 10;
      searchUserIdsParams0.setHitsPerPage(hitsPerPage1);
    }

    assertDoesNotThrow(() -> {
      client.searchUserIds(searchUserIdsParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/clusters/mapping/search");
    assertEquals(req.method, "POST");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"query\":\"test\",\"clusterName\":\"theClusterName\",\"page\":5,\"hitsPerPage\":10}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("get setDictionarySettings results with minimal parameters")
  void setDictionarySettingsTest0() {
    DictionarySettingsParams dictionarySettingsParams0 = new DictionarySettingsParams();
    {
      StandardEntries disableStandardEntries1 = new StandardEntries();
      {
        Map<String, Boolean> plurals2 = new HashMap<>();
        {
          boolean fr3 = false;
          plurals2.put("fr", fr3);
          boolean en3 = false;
          plurals2.put("en", en3);
          boolean ru3 = true;
          plurals2.put("ru", ru3);
        }
        disableStandardEntries1.setPlurals(plurals2);
      }
      dictionarySettingsParams0.setDisableStandardEntries(disableStandardEntries1);
    }

    assertDoesNotThrow(() -> {
      client.setDictionarySettings(dictionarySettingsParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/dictionaries/*/settings");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"disableStandardEntries\":{\"plurals\":{\"fr\":false,\"en\":false,\"ru\":true}}}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("get setDictionarySettings results with all parameters")
  void setDictionarySettingsTest1() {
    DictionarySettingsParams dictionarySettingsParams0 = new DictionarySettingsParams();
    {
      StandardEntries disableStandardEntries1 = new StandardEntries();
      {
        Map<String, Boolean> plurals2 = new HashMap<>();
        {
          boolean fr3 = false;
          plurals2.put("fr", fr3);
          boolean en3 = false;
          plurals2.put("en", en3);
          boolean ru3 = true;
          plurals2.put("ru", ru3);
        }
        disableStandardEntries1.setPlurals(plurals2);
        Map<String, Boolean> stopwords2 = new HashMap<>();
        {
          boolean fr3 = false;
          stopwords2.put("fr", fr3);
        }
        disableStandardEntries1.setStopwords(stopwords2);
        Map<String, Boolean> compounds2 = new HashMap<>();
        {
          boolean ru3 = true;
          compounds2.put("ru", ru3);
        }
        disableStandardEntries1.setCompounds(compounds2);
      }
      dictionarySettingsParams0.setDisableStandardEntries(disableStandardEntries1);
    }

    assertDoesNotThrow(() -> {
      client.setDictionarySettings(dictionarySettingsParams0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/dictionaries/*/settings");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"disableStandardEntries\":{\"plurals\":{\"fr\":false,\"en\":false,\"ru\":true},\"stopwords\":{\"fr\":false},\"compounds\":{\"ru\":true}}}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("setSettings with minimal parameters")
  void setSettingsTest0() {
    String indexName0 = "theIndexName";
    IndexSettings indexSettings0 = new IndexSettings();
    {
      int paginationLimitedTo1 = 10;
      indexSettings0.setPaginationLimitedTo(paginationLimitedTo1);
    }
    boolean forwardToReplicas0 = true;

    assertDoesNotThrow(() -> {
      client.setSettings(indexName0, indexSettings0, forwardToReplicas0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/settings");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"paginationLimitedTo\":10}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"forwardToReplicas\":\"true\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("setSettings allow boolean `typoTolerance`")
  void setSettingsTest1() {
    String indexName0 = "theIndexName";
    IndexSettings indexSettings0 = new IndexSettings();
    {
      boolean typoTolerance1 = true;
      indexSettings0.setTypoTolerance(TypoTolerance.of(typoTolerance1));
    }
    boolean forwardToReplicas0 = true;

    assertDoesNotThrow(() -> {
      client.setSettings(indexName0, indexSettings0, forwardToReplicas0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/settings");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"typoTolerance\":true}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"forwardToReplicas\":\"true\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("setSettings allow enum `typoTolerance`")
  void setSettingsTest2() {
    String indexName0 = "theIndexName";
    IndexSettings indexSettings0 = new IndexSettings();
    {
      TypoToleranceEnum typoTolerance1 = TypoToleranceEnum.fromValue("min");
      indexSettings0.setTypoTolerance(TypoTolerance.of(typoTolerance1));
    }
    boolean forwardToReplicas0 = true;

    assertDoesNotThrow(() -> {
      client.setSettings(indexName0, indexSettings0, forwardToReplicas0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/settings");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"typoTolerance\":\"min\"}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"forwardToReplicas\":\"true\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("setSettings allow boolean `ignorePlurals`")
  void setSettingsTest3() {
    String indexName0 = "theIndexName";
    IndexSettings indexSettings0 = new IndexSettings();
    {
      boolean ignorePlurals1 = true;
      indexSettings0.setIgnorePlurals(IgnorePlurals.of(ignorePlurals1));
    }
    boolean forwardToReplicas0 = true;

    assertDoesNotThrow(() -> {
      client.setSettings(indexName0, indexSettings0, forwardToReplicas0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/settings");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"ignorePlurals\":true}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"forwardToReplicas\":\"true\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("setSettings allow list of string `ignorePlurals`")
  void setSettingsTest4() {
    String indexName0 = "theIndexName";
    IndexSettings indexSettings0 = new IndexSettings();
    {
      List<String> ignorePlurals1 = new ArrayList<>();
      {
        String ignorePlurals_02 = "algolia";
        ignorePlurals1.add(ignorePlurals_02);
      }
      indexSettings0.setIgnorePlurals(IgnorePlurals.of(ignorePlurals1));
    }
    boolean forwardToReplicas0 = true;

    assertDoesNotThrow(() -> {
      client.setSettings(indexName0, indexSettings0, forwardToReplicas0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/settings");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"ignorePlurals\":[\"algolia\"]}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"forwardToReplicas\":\"true\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("setSettings allow boolean `removeStopWords`")
  void setSettingsTest5() {
    String indexName0 = "theIndexName";
    IndexSettings indexSettings0 = new IndexSettings();
    {
      boolean removeStopWords1 = true;
      indexSettings0.setRemoveStopWords(RemoveStopWords.of(removeStopWords1));
    }
    boolean forwardToReplicas0 = true;

    assertDoesNotThrow(() -> {
      client.setSettings(indexName0, indexSettings0, forwardToReplicas0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/settings");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"removeStopWords\":true}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"forwardToReplicas\":\"true\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("setSettings allow list of string `removeStopWords`")
  void setSettingsTest6() {
    String indexName0 = "theIndexName";
    IndexSettings indexSettings0 = new IndexSettings();
    {
      List<String> removeStopWords1 = new ArrayList<>();
      {
        String removeStopWords_02 = "algolia";
        removeStopWords1.add(removeStopWords_02);
      }
      indexSettings0.setRemoveStopWords(RemoveStopWords.of(removeStopWords1));
    }
    boolean forwardToReplicas0 = true;

    assertDoesNotThrow(() -> {
      client.setSettings(indexName0, indexSettings0, forwardToReplicas0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/settings");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"removeStopWords\":[\"algolia\"]}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"forwardToReplicas\":\"true\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("setSettings allow boolean `distinct`")
  void setSettingsTest7() {
    String indexName0 = "theIndexName";
    IndexSettings indexSettings0 = new IndexSettings();
    {
      boolean distinct1 = true;
      indexSettings0.setDistinct(Distinct.of(distinct1));
    }
    boolean forwardToReplicas0 = true;

    assertDoesNotThrow(() -> {
      client.setSettings(indexName0, indexSettings0, forwardToReplicas0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/settings");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"distinct\":true}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"forwardToReplicas\":\"true\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("setSettings allow integers for `distinct`")
  void setSettingsTest8() {
    String indexName0 = "theIndexName";
    IndexSettings indexSettings0 = new IndexSettings();
    {
      int distinct1 = 1;
      indexSettings0.setDistinct(Distinct.of(distinct1));
    }
    boolean forwardToReplicas0 = true;

    assertDoesNotThrow(() -> {
      client.setSettings(indexName0, indexSettings0, forwardToReplicas0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/settings");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals("{\"distinct\":1}", req.body, JSONCompareMode.STRICT);
    });

    try {
      Map<String, String> expectedQuery = json.readValue(
        "{\"forwardToReplicas\":\"true\"}",
        new TypeReference<HashMap<String, String>>() {}
      );
      Map<String, Object> actualQuery = req.queryParameters;

      assertEquals(expectedQuery.size(), actualQuery.size());
      for (Map.Entry<String, Object> p : actualQuery.entrySet()) {
        assertEquals(expectedQuery.get(p.getKey()), p.getValue());
      }
    } catch (JsonProcessingException e) {
      fail("failed to parse queryParameters json");
    }
  }

  @Test
  @DisplayName("setSettings allow all `indexSettings`")
  void setSettingsTest9() {
    String indexName0 = "theIndexName";
    IndexSettings indexSettings0 = new IndexSettings();
    {
      boolean advancedSyntax1 = true;
      indexSettings0.setAdvancedSyntax(advancedSyntax1);
      List<AdvancedSyntaxFeatures> advancedSyntaxFeatures1 = new ArrayList<>();
      {
        AdvancedSyntaxFeatures advancedSyntaxFeatures_02 = AdvancedSyntaxFeatures.fromValue("exactPhrase");
        advancedSyntaxFeatures1.add(advancedSyntaxFeatures_02);
      }
      indexSettings0.setAdvancedSyntaxFeatures(advancedSyntaxFeatures1);
      boolean allowCompressionOfIntegerArray1 = true;
      indexSettings0.setAllowCompressionOfIntegerArray(allowCompressionOfIntegerArray1);
      boolean allowTyposOnNumericTokens1 = true;
      indexSettings0.setAllowTyposOnNumericTokens(allowTyposOnNumericTokens1);
      List<AlternativesAsExact> alternativesAsExact1 = new ArrayList<>();
      {
        AlternativesAsExact alternativesAsExact_02 = AlternativesAsExact.fromValue("singleWordSynonym");
        alternativesAsExact1.add(alternativesAsExact_02);
      }
      indexSettings0.setAlternativesAsExact(alternativesAsExact1);
      boolean attributeCriteriaComputedByMinProximity1 = true;
      indexSettings0.setAttributeCriteriaComputedByMinProximity(attributeCriteriaComputedByMinProximity1);
      String attributeForDistinct1 = "test";
      indexSettings0.setAttributeForDistinct(attributeForDistinct1);
      List<String> attributesForFaceting1 = new ArrayList<>();
      {
        String attributesForFaceting_02 = "algolia";
        attributesForFaceting1.add(attributesForFaceting_02);
      }
      indexSettings0.setAttributesForFaceting(attributesForFaceting1);
      List<String> attributesToHighlight1 = new ArrayList<>();
      {
        String attributesToHighlight_02 = "algolia";
        attributesToHighlight1.add(attributesToHighlight_02);
      }
      indexSettings0.setAttributesToHighlight(attributesToHighlight1);
      List<String> attributesToRetrieve1 = new ArrayList<>();
      {
        String attributesToRetrieve_02 = "algolia";
        attributesToRetrieve1.add(attributesToRetrieve_02);
      }
      indexSettings0.setAttributesToRetrieve(attributesToRetrieve1);
      List<String> attributesToSnippet1 = new ArrayList<>();
      {
        String attributesToSnippet_02 = "algolia";
        attributesToSnippet1.add(attributesToSnippet_02);
      }
      indexSettings0.setAttributesToSnippet(attributesToSnippet1);
      List<String> attributesToTransliterate1 = new ArrayList<>();
      {
        String attributesToTransliterate_02 = "algolia";
        attributesToTransliterate1.add(attributesToTransliterate_02);
      }
      indexSettings0.setAttributesToTransliterate(attributesToTransliterate1);
      List<String> camelCaseAttributes1 = new ArrayList<>();
      {
        String camelCaseAttributes_02 = "algolia";
        camelCaseAttributes1.add(camelCaseAttributes_02);
      }
      indexSettings0.setCamelCaseAttributes(camelCaseAttributes1);
      Map<String, Map<String, String>> customNormalization1 = new HashMap<>();
      {
        Map<String, String> algolia2 = new HashMap<>();
        {
          String aloglia3 = "aglolia";
          algolia2.put("aloglia", aloglia3);
        }
        customNormalization1.put("algolia", algolia2);
      }
      indexSettings0.setCustomNormalization(customNormalization1);
      List<String> customRanking1 = new ArrayList<>();
      {
        String customRanking_02 = "algolia";
        customRanking1.add(customRanking_02);
      }
      indexSettings0.setCustomRanking(customRanking1);
      boolean decompoundQuery1 = false;
      indexSettings0.setDecompoundQuery(decompoundQuery1);
      Map<String, String> decompoundedAttributes1 = new HashMap<>();
      {
        String algolia2 = "aloglia";
        decompoundedAttributes1.put("algolia", algolia2);
      }
      indexSettings0.setDecompoundedAttributes(decompoundedAttributes1);
      List<String> disableExactOnAttributes1 = new ArrayList<>();
      {
        String disableExactOnAttributes_02 = "algolia";
        disableExactOnAttributes1.add(disableExactOnAttributes_02);
      }
      indexSettings0.setDisableExactOnAttributes(disableExactOnAttributes1);
      List<String> disablePrefixOnAttributes1 = new ArrayList<>();
      {
        String disablePrefixOnAttributes_02 = "algolia";
        disablePrefixOnAttributes1.add(disablePrefixOnAttributes_02);
      }
      indexSettings0.setDisablePrefixOnAttributes(disablePrefixOnAttributes1);
      List<String> disableTypoToleranceOnAttributes1 = new ArrayList<>();
      {
        String disableTypoToleranceOnAttributes_02 = "algolia";
        disableTypoToleranceOnAttributes1.add(disableTypoToleranceOnAttributes_02);
      }
      indexSettings0.setDisableTypoToleranceOnAttributes(disableTypoToleranceOnAttributes1);
      List<String> disableTypoToleranceOnWords1 = new ArrayList<>();
      {
        String disableTypoToleranceOnWords_02 = "algolia";
        disableTypoToleranceOnWords1.add(disableTypoToleranceOnWords_02);
      }
      indexSettings0.setDisableTypoToleranceOnWords(disableTypoToleranceOnWords1);
      int distinct1 = 3;
      indexSettings0.setDistinct(Distinct.of(distinct1));
      boolean enablePersonalization1 = true;
      indexSettings0.setEnablePersonalization(enablePersonalization1);
      boolean enableReRanking1 = false;
      indexSettings0.setEnableReRanking(enableReRanking1);
      boolean enableRules1 = true;
      indexSettings0.setEnableRules(enableRules1);
      ExactOnSingleWordQuery exactOnSingleWordQuery1 = ExactOnSingleWordQuery.fromValue("attribute");
      indexSettings0.setExactOnSingleWordQuery(exactOnSingleWordQuery1);
      String highlightPreTag1 = "<span>";
      indexSettings0.setHighlightPreTag(highlightPreTag1);
      String highlightPostTag1 = "</span>";
      indexSettings0.setHighlightPostTag(highlightPostTag1);
      int hitsPerPage1 = 10;
      indexSettings0.setHitsPerPage(hitsPerPage1);
      boolean ignorePlurals1 = false;
      indexSettings0.setIgnorePlurals(IgnorePlurals.of(ignorePlurals1));
      List<String> indexLanguages1 = new ArrayList<>();
      {
        String indexLanguages_02 = "algolia";
        indexLanguages1.add(indexLanguages_02);
      }
      indexSettings0.setIndexLanguages(indexLanguages1);
      String keepDiacriticsOnCharacters1 = "abc";
      indexSettings0.setKeepDiacriticsOnCharacters(keepDiacriticsOnCharacters1);
      int maxFacetHits1 = 20;
      indexSettings0.setMaxFacetHits(maxFacetHits1);
      int maxValuesPerFacet1 = 30;
      indexSettings0.setMaxValuesPerFacet(maxValuesPerFacet1);
      int minProximity1 = 6;
      indexSettings0.setMinProximity(minProximity1);
      int minWordSizefor1Typo1 = 5;
      indexSettings0.setMinWordSizefor1Typo(minWordSizefor1Typo1);
      int minWordSizefor2Typos1 = 11;
      indexSettings0.setMinWordSizefor2Typos(minWordSizefor2Typos1);
      Mode mode1 = Mode.fromValue("neuralSearch");
      indexSettings0.setMode(mode1);
      List<String> numericAttributesForFiltering1 = new ArrayList<>();
      {
        String numericAttributesForFiltering_02 = "algolia";
        numericAttributesForFiltering1.add(numericAttributesForFiltering_02);
      }
      indexSettings0.setNumericAttributesForFiltering(numericAttributesForFiltering1);
      List<String> optionalWords1 = new ArrayList<>();
      {
        String optionalWords_02 = "myspace";
        optionalWords1.add(optionalWords_02);
      }
      indexSettings0.setOptionalWords(optionalWords1);
      int paginationLimitedTo1 = 0;
      indexSettings0.setPaginationLimitedTo(paginationLimitedTo1);
      List<String> queryLanguages1 = new ArrayList<>();
      {
        String queryLanguages_02 = "algolia";
        queryLanguages1.add(queryLanguages_02);
      }
      indexSettings0.setQueryLanguages(queryLanguages1);
      QueryType queryType1 = QueryType.fromValue("prefixLast");
      indexSettings0.setQueryType(queryType1);
      List<String> ranking1 = new ArrayList<>();
      {
        String ranking_02 = "geo";
        ranking1.add(ranking_02);
      }
      indexSettings0.setRanking(ranking1);
      String reRankingApplyFilter1 = "mySearch:filters";
      indexSettings0.setReRankingApplyFilter(ReRankingApplyFilter.of(reRankingApplyFilter1));
      int relevancyStrictness1 = 10;
      indexSettings0.setRelevancyStrictness(relevancyStrictness1);
      boolean removeStopWords1 = false;
      indexSettings0.setRemoveStopWords(RemoveStopWords.of(removeStopWords1));
      RemoveWordsIfNoResults removeWordsIfNoResults1 = RemoveWordsIfNoResults.fromValue("lastWords");
      indexSettings0.setRemoveWordsIfNoResults(removeWordsIfNoResults1);
      RenderingContent renderingContent1 = new RenderingContent();
      {
        FacetOrdering facetOrdering2 = new FacetOrdering();
        {
          Facets facets3 = new Facets();
          {
            List<String> order4 = new ArrayList<>();
            {
              String order_05 = "a";
              order4.add(order_05);
              String order_15 = "b";
              order4.add(order_15);
            }
            facets3.setOrder(order4);
          }
          facetOrdering2.setFacets(facets3);
          Map<String, Value> values3 = new HashMap<>();
          {
            Value a4 = new Value();
            {
              List<String> order5 = new ArrayList<>();
              {
                String order_06 = "b";
                order5.add(order_06);
              }
              a4.setOrder(order5);
              SortRemainingBy sortRemainingBy5 = SortRemainingBy.fromValue("count");
              a4.setSortRemainingBy(sortRemainingBy5);
            }
            values3.put("a", a4);
          }
          facetOrdering2.setValues(values3);
        }
        renderingContent1.setFacetOrdering(facetOrdering2);
      }
      indexSettings0.setRenderingContent(renderingContent1);
      boolean replaceSynonymsInHighlight1 = true;
      indexSettings0.setReplaceSynonymsInHighlight(replaceSynonymsInHighlight1);
      List<String> replicas1 = new ArrayList<>();
      {
        String replicas_02 = "";
        replicas1.add(replicas_02);
      }
      indexSettings0.setReplicas(replicas1);
      List<String> responseFields1 = new ArrayList<>();
      {
        String responseFields_02 = "algolia";
        responseFields1.add(responseFields_02);
      }
      indexSettings0.setResponseFields(responseFields1);
      boolean restrictHighlightAndSnippetArrays1 = true;
      indexSettings0.setRestrictHighlightAndSnippetArrays(restrictHighlightAndSnippetArrays1);
      List<String> searchableAttributes1 = new ArrayList<>();
      {
        String searchableAttributes_02 = "foo";
        searchableAttributes1.add(searchableAttributes_02);
      }
      indexSettings0.setSearchableAttributes(searchableAttributes1);
      SemanticSearch semanticSearch1 = new SemanticSearch();
      {
        List<String> eventSources2 = new ArrayList<>();
        {
          String eventSources_03 = "foo";
          eventSources2.add(eventSources_03);
        }
        semanticSearch1.setEventSources(eventSources2);
      }
      indexSettings0.setSemanticSearch(semanticSearch1);
      String separatorsToIndex1 = "bar";
      indexSettings0.setSeparatorsToIndex(separatorsToIndex1);
      String snippetEllipsisText1 = "---";
      indexSettings0.setSnippetEllipsisText(snippetEllipsisText1);
      String sortFacetValuesBy1 = "date";
      indexSettings0.setSortFacetValuesBy(sortFacetValuesBy1);
      boolean typoTolerance1 = false;
      indexSettings0.setTypoTolerance(TypoTolerance.of(typoTolerance1));
      List<String> unretrievableAttributes1 = new ArrayList<>();
      {
        String unretrievableAttributes_02 = "foo";
        unretrievableAttributes1.add(unretrievableAttributes_02);
      }
      indexSettings0.setUnretrievableAttributes(unretrievableAttributes1);
      Map<String, String> userData1 = new HashMap<>();
      {
        String user2 = "data";
        userData1.put("user", user2);
      }
      indexSettings0.setUserData(userData1);
    }

    assertDoesNotThrow(() -> {
      client.setSettings(indexName0, indexSettings0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/indexes/theIndexName/settings");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"advancedSyntax\":true,\"advancedSyntaxFeatures\":[\"exactPhrase\"],\"allowCompressionOfIntegerArray\":true,\"allowTyposOnNumericTokens\":true,\"alternativesAsExact\":[\"singleWordSynonym\"],\"attributeCriteriaComputedByMinProximity\":true,\"attributeForDistinct\":\"test\",\"attributesForFaceting\":[\"algolia\"],\"attributesToHighlight\":[\"algolia\"],\"attributesToRetrieve\":[\"algolia\"],\"attributesToSnippet\":[\"algolia\"],\"attributesToTransliterate\":[\"algolia\"],\"camelCaseAttributes\":[\"algolia\"],\"customNormalization\":{\"algolia\":{\"aloglia\":\"aglolia\"}},\"customRanking\":[\"algolia\"],\"decompoundQuery\":false,\"decompoundedAttributes\":{\"algolia\":\"aloglia\"},\"disableExactOnAttributes\":[\"algolia\"],\"disablePrefixOnAttributes\":[\"algolia\"],\"disableTypoToleranceOnAttributes\":[\"algolia\"],\"disableTypoToleranceOnWords\":[\"algolia\"],\"distinct\":3,\"enablePersonalization\":true,\"enableReRanking\":false,\"enableRules\":true,\"exactOnSingleWordQuery\":\"attribute\",\"highlightPreTag\":\"<span>\",\"highlightPostTag\":\"</span>\",\"hitsPerPage\":10,\"ignorePlurals\":false,\"indexLanguages\":[\"algolia\"],\"keepDiacriticsOnCharacters\":\"abc\",\"maxFacetHits\":20,\"maxValuesPerFacet\":30,\"minProximity\":6,\"minWordSizefor1Typo\":5,\"minWordSizefor2Typos\":11,\"mode\":\"neuralSearch\",\"numericAttributesForFiltering\":[\"algolia\"],\"optionalWords\":[\"myspace\"],\"paginationLimitedTo\":0,\"queryLanguages\":[\"algolia\"],\"queryType\":\"prefixLast\",\"ranking\":[\"geo\"],\"reRankingApplyFilter\":\"mySearch:filters\",\"relevancyStrictness\":10,\"removeStopWords\":false,\"removeWordsIfNoResults\":\"lastWords\",\"renderingContent\":{\"facetOrdering\":{\"facets\":{\"order\":[\"a\",\"b\"]},\"values\":{\"a\":{\"order\":[\"b\"],\"sortRemainingBy\":\"count\"}}}},\"replaceSynonymsInHighlight\":true,\"replicas\":[\"\"],\"responseFields\":[\"algolia\"],\"restrictHighlightAndSnippetArrays\":true,\"searchableAttributes\":[\"foo\"],\"semanticSearch\":{\"eventSources\":[\"foo\"]},\"separatorsToIndex\":\"bar\",\"snippetEllipsisText\":\"---\",\"sortFacetValuesBy\":\"date\",\"typoTolerance\":false,\"unretrievableAttributes\":[\"foo\"],\"userData\":{\"user\":\"data\"}}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }

  @Test
  @DisplayName("updateApiKey")
  void updateApiKeyTest0() {
    String key0 = "myApiKey";
    ApiKey apiKey0 = new ApiKey();
    {
      List<Acl> acl1 = new ArrayList<>();
      {
        Acl acl_02 = Acl.fromValue("search");
        acl1.add(acl_02);
        Acl acl_12 = Acl.fromValue("addObject");
        acl1.add(acl_12);
      }
      apiKey0.setAcl(acl1);
      int validity1 = 300;
      apiKey0.setValidity(validity1);
      int maxQueriesPerIPPerHour1 = 100;
      apiKey0.setMaxQueriesPerIPPerHour(maxQueriesPerIPPerHour1);
      int maxHitsPerQuery1 = 20;
      apiKey0.setMaxHitsPerQuery(maxHitsPerQuery1);
    }

    assertDoesNotThrow(() -> {
      client.updateApiKey(key0, apiKey0);
    });
    EchoResponse req = echo.getLastResponse();

    assertEquals(req.path, "/1/keys/myApiKey");
    assertEquals(req.method, "PUT");
    assertDoesNotThrow(() -> {
      JSONAssert.assertEquals(
        "{\"acl\":[\"search\",\"addObject\"],\"validity\":300,\"maxQueriesPerIPPerHour\":100,\"maxHitsPerQuery\":20}",
        req.body,
        JSONCompareMode.STRICT
      );
    });
  }
}
