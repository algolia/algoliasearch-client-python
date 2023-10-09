import 'package:algolia_client_search/algolia_client_search.dart';
import 'package:algolia_test/algolia_test.dart';
import 'package:test/test.dart';

void main() {
  // addApiKey
  test(
    'addApiKey',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.addApiKey(
        apiKey: ApiKey(
          acl: [
            Acl.fromJson("search"),
            Acl.fromJson("addObject"),
          ],
          description: "my new api key",
          validity: 300,
          maxQueriesPerIPPerHour: 100,
          maxHitsPerQuery: 20,
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/keys');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"acl":["search","addObject"],"description":"my new api key","validity":300,"maxQueriesPerIPPerHour":100,"maxHitsPerQuery":20}""");
      },
    ),
  );

  // addOrUpdateObject
  test(
    'addOrUpdateObject',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.addOrUpdateObject(
        indexName: "indexName",
        objectID: "uniqueID",
        body: {
          'key': "value",
        },
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/uniqueID');
        expect(request.method, 'put');
        expectBody(request.body, """{"key":"value"}""");
      },
    ),
  );

  // appendSource
  test(
    'appendSource',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.appendSource(
        source: Source(
          source: "theSource",
          description: "theDescription",
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/security/sources/append');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"source":"theSource","description":"theDescription"}""");
      },
    ),
  );

  // assignUserId
  test(
    'assignUserId',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.assignUserId(
        xAlgoliaUserID: "userID",
        assignUserIdParams: AssignUserIdParams(
          cluster: "theCluster",
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/clusters/mapping');
        expect(request.method, 'post');
        expectHeaders(request.headers, """{"x-algolia-user-id":"userID"}""");
        expectBody(request.body, """{"cluster":"theCluster"}""");
      },
    ),
  );

  // batch
  test(
    'allows batch method with `addObject` action',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.batch(
        indexName: "theIndexName",
        batchWriteParams: BatchWriteParams(
          requests: [
            BatchRequest(
              action: Action.fromJson("addObject"),
              body: {
                'key': "value",
              },
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/batch');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"action":"addObject","body":{"key":"value"}}]}""");
      },
    ),
  );

  // batch
  test(
    'allows batch method with `clear` action',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.batch(
        indexName: "theIndexName",
        batchWriteParams: BatchWriteParams(
          requests: [
            BatchRequest(
              action: Action.fromJson("clear"),
              body: {
                'key': "value",
              },
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/batch');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"action":"clear","body":{"key":"value"}}]}""");
      },
    ),
  );

  // batch
  test(
    'allows batch method with `delete` action',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.batch(
        indexName: "theIndexName",
        batchWriteParams: BatchWriteParams(
          requests: [
            BatchRequest(
              action: Action.fromJson("delete"),
              body: {
                'key': "value",
              },
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/batch');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"action":"delete","body":{"key":"value"}}]}""");
      },
    ),
  );

  // batch
  test(
    'allows batch method with `deleteObject` action',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.batch(
        indexName: "theIndexName",
        batchWriteParams: BatchWriteParams(
          requests: [
            BatchRequest(
              action: Action.fromJson("deleteObject"),
              body: {
                'key': "value",
              },
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/batch');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"action":"deleteObject","body":{"key":"value"}}]}""");
      },
    ),
  );

  // batch
  test(
    'allows batch method with `partialUpdateObject` action',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.batch(
        indexName: "theIndexName",
        batchWriteParams: BatchWriteParams(
          requests: [
            BatchRequest(
              action: Action.fromJson("partialUpdateObject"),
              body: {
                'key': "value",
              },
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/batch');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"action":"partialUpdateObject","body":{"key":"value"}}]}""");
      },
    ),
  );

  // batch
  test(
    'allows batch method with `partialUpdateObjectNoCreate` action',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.batch(
        indexName: "theIndexName",
        batchWriteParams: BatchWriteParams(
          requests: [
            BatchRequest(
              action: Action.fromJson("partialUpdateObjectNoCreate"),
              body: {
                'key': "value",
              },
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/batch');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"action":"partialUpdateObjectNoCreate","body":{"key":"value"}}]}""");
      },
    ),
  );

  // batch
  test(
    'allows batch method with `updateObject` action',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.batch(
        indexName: "theIndexName",
        batchWriteParams: BatchWriteParams(
          requests: [
            BatchRequest(
              action: Action.fromJson("updateObject"),
              body: {
                'key': "value",
              },
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/batch');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"action":"updateObject","body":{"key":"value"}}]}""");
      },
    ),
  );

  // batchAssignUserIds
  test(
    'batchAssignUserIds',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.batchAssignUserIds(
        xAlgoliaUserID: "userID",
        batchAssignUserIdsParams: BatchAssignUserIdsParams(
          cluster: "theCluster",
          users: [
            "user1",
            "user2",
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/clusters/mapping/batch');
        expect(request.method, 'post');
        expectHeaders(request.headers, """{"x-algolia-user-id":"userID"}""");
        expectBody(request.body,
            """{"cluster":"theCluster","users":["user1","user2"]}""");
      },
    ),
  );

  // batchDictionaryEntries
  test(
    'get batchDictionaryEntries results with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.batchDictionaryEntries(
        dictionaryName: DictionaryType.fromJson("compounds"),
        batchDictionaryEntriesParams: BatchDictionaryEntriesParams(
          requests: [
            BatchDictionaryEntriesRequest(
              action: DictionaryAction.fromJson("addEntry"),
              body: DictionaryEntry(
                objectID: "1",
                language: "en",
              ),
            ),
            BatchDictionaryEntriesRequest(
              action: DictionaryAction.fromJson("deleteEntry"),
              body: DictionaryEntry(
                objectID: "2",
                language: "fr",
              ),
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/dictionaries/compounds/batch');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"action":"addEntry","body":{"objectID":"1","language":"en"}},{"action":"deleteEntry","body":{"objectID":"2","language":"fr"}}]}""");
      },
    ),
  );

  // batchDictionaryEntries
  test(
    'get batchDictionaryEntries results with all parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.batchDictionaryEntries(
        dictionaryName: DictionaryType.fromJson("compounds"),
        batchDictionaryEntriesParams: BatchDictionaryEntriesParams(
          clearExistingDictionaryEntries: false,
          requests: [
            BatchDictionaryEntriesRequest(
              action: DictionaryAction.fromJson("addEntry"),
              body: DictionaryEntry(
                objectID: "1",
                language: "en",
                word: "fancy",
                words: [
                  "believe",
                  "algolia",
                ],
                decomposition: [
                  "trust",
                  "algolia",
                ],
                state: DictionaryEntryState.fromJson("enabled"),
              ),
            ),
            BatchDictionaryEntriesRequest(
              action: DictionaryAction.fromJson("deleteEntry"),
              body: DictionaryEntry(
                objectID: "2",
                language: "fr",
                word: "humility",
                words: [
                  "candor",
                  "algolia",
                ],
                decomposition: [
                  "grit",
                  "algolia",
                ],
                state: DictionaryEntryState.fromJson("enabled"),
              ),
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/dictionaries/compounds/batch');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"clearExistingDictionaryEntries":false,"requests":[{"action":"addEntry","body":{"objectID":"1","language":"en","word":"fancy","words":["believe","algolia"],"decomposition":["trust","algolia"],"state":"enabled"}},{"action":"deleteEntry","body":{"objectID":"2","language":"fr","word":"humility","words":["candor","algolia"],"decomposition":["grit","algolia"],"state":"enabled"}}]}""");
      },
    ),
  );

  // batchDictionaryEntries
  test(
    'get batchDictionaryEntries results additional properties',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.batchDictionaryEntries(
        dictionaryName: DictionaryType.fromJson("compounds"),
        batchDictionaryEntriesParams: BatchDictionaryEntriesParams(
          requests: [
            BatchDictionaryEntriesRequest(
              action: DictionaryAction.fromJson("addEntry"),
              body: DictionaryEntry(
                objectID: "1",
                language: "en",
                additionalProperties: {'additional': 'try me'},
              ),
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/dictionaries/compounds/batch');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"action":"addEntry","body":{"objectID":"1","language":"en","additional":"try me"}}]}""");
      },
    ),
  );

  // browse
  test(
    'browse with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.browse(
        indexName: "indexName",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/browse');
        expect(request.method, 'post');
        expectBody(request.body, """{}""");
      },
    ),
  );

  // browse
  test(
    'browse with search parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.browse(
        indexName: "indexName",
        browseParams: BrowseParamsObject(
          query: "myQuery",
          facetFilters: [
            "tags:algolia",
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/browse');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"query":"myQuery","facetFilters":["tags:algolia"]}""");
      },
    ),
  );

  // browse
  test(
    'browse allow a cursor in parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.browse(
        indexName: "indexName",
        browseParams: BrowseParamsObject(
          cursor: "test",
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/browse');
        expect(request.method, 'post');
        expectBody(request.body, """{"cursor":"test"}""");
      },
    ),
  );

  // clearAllSynonyms
  test(
    'clearAllSynonyms',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.clearAllSynonyms(
        indexName: "indexName",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/synonyms/clear');
        expect(request.method, 'post');
        expect(request.body, {});
      },
    ),
  );

  // clearObjects
  test(
    'clearObjects',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.clearObjects(
        indexName: "theIndexName",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/clear');
        expect(request.method, 'post');
        expect(request.body, {});
      },
    ),
  );

  // clearRules
  test(
    'clearRules',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.clearRules(
        indexName: "indexName",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/rules/clear');
        expect(request.method, 'post');
        expect(request.body, {});
      },
    ),
  );

  // del
  test(
    'allow del method for a custom path with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.del(
        path: "/test/minimal",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/minimal');
        expect(request.method, 'delete');
        expect(request.body, null);
      },
    ),
  );

  // del
  test(
    'allow del method for a custom path with all parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.del(
        path: "/test/all",
        parameters: {
          'query': "parameters",
        },
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/all');
        expect(request.method, 'delete');
        expectParams(request.queryParameters, """{"query":"parameters"}""");
        expect(request.body, null);
      },
    ),
  );

  // deleteApiKey
  test(
    'deleteApiKey',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.deleteApiKey(
        key: "myTestApiKey",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/keys/myTestApiKey');
        expect(request.method, 'delete');
        expect(request.body, null);
      },
    ),
  );

  // deleteBy
  test(
    'deleteBy',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.deleteBy(
        indexName: "theIndexName",
        deleteByParams: DeleteByParams(
          filters: "brand:brandName",
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/deleteByQuery');
        expect(request.method, 'post');
        expectBody(request.body, """{"filters":"brand:brandName"}""");
      },
    ),
  );

  // deleteIndex
  test(
    'deleteIndex',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.deleteIndex(
        indexName: "theIndexName",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName');
        expect(request.method, 'delete');
        expect(request.body, null);
      },
    ),
  );

  // deleteObject
  test(
    'deleteObject',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.deleteObject(
        indexName: "theIndexName",
        objectID: "uniqueID",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/uniqueID');
        expect(request.method, 'delete');
        expect(request.body, null);
      },
    ),
  );

  // deleteRule
  test(
    'deleteRule',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.deleteRule(
        indexName: "indexName",
        objectID: "id1",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/rules/id1');
        expect(request.method, 'delete');
        expect(request.body, null);
      },
    ),
  );

  // deleteSource
  test(
    'deleteSource',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.deleteSource(
        source: "theSource",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/security/sources/theSource');
        expect(request.method, 'delete');
        expect(request.body, null);
      },
    ),
  );

  // deleteSynonym
  test(
    'deleteSynonym',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.deleteSynonym(
        indexName: "indexName",
        objectID: "id1",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/synonyms/id1');
        expect(request.method, 'delete');
        expect(request.body, null);
      },
    ),
  );

  // get
  test(
    'allow get method for a custom path with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.get(
        path: "/test/minimal",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/minimal');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // get
  test(
    'allow get method for a custom path with all parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.get(
        path: "/test/all",
        parameters: {
          'query': "parameters",
        },
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/all');
        expect(request.method, 'get');
        expectParams(request.queryParameters, """{"query":"parameters"}""");
        expect(request.body, null);
      },
    ),
  );

  // getApiKey
  test(
    'getApiKey',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.getApiKey(
        key: "myTestApiKey",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/keys/myTestApiKey');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // getDictionaryLanguages
  test(
    'get getDictionaryLanguages',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.getDictionaryLanguages(),
      intercept: (request) {
        expectPath(request.path, '/1/dictionaries/*/languages');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // getDictionarySettings
  test(
    'get getDictionarySettings results',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.getDictionarySettings(),
      intercept: (request) {
        expectPath(request.path, '/1/dictionaries/*/settings');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // getLogs
  test(
    'getLogs with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.getLogs(),
      intercept: (request) {
        expectPath(request.path, '/1/logs');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // getLogs
  test(
    'getLogs with parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.getLogs(
        offset: 5,
        length: 10,
        indexName: "theIndexName",
        type: LogType.fromJson("all"),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/logs');
        expect(request.method, 'get');
        expectParams(request.queryParameters,
            """{"offset":"5","length":"10","indexName":"theIndexName","type":"all"}""");
        expect(request.body, null);
      },
    ),
  );

  // getObject
  test(
    'getObject',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.getObject(
        indexName: "theIndexName",
        objectID: "uniqueID",
        attributesToRetrieve: [
          "attr1",
          "attr2",
        ],
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/uniqueID');
        expect(request.method, 'get');
        expectParams(request.queryParameters,
            """{"attributesToRetrieve":"attr1,attr2"}""");
        expect(request.body, null);
      },
    ),
  );

  // getObjects
  test(
    'getObjects',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.getObjects(
        getObjectsParams: GetObjectsParams(
          requests: [
            GetObjectsRequest(
              attributesToRetrieve: [
                "attr1",
                "attr2",
              ],
              objectID: "uniqueID",
              indexName: "theIndexName",
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/*/objects');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"attributesToRetrieve":["attr1","attr2"],"objectID":"uniqueID","indexName":"theIndexName"}]}""");
      },
    ),
  );

  // getRule
  test(
    'getRule',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.getRule(
        indexName: "indexName",
        objectID: "id1",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/rules/id1');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // getSettings
  test(
    'getSettings',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.getSettings(
        indexName: "theIndexName",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/settings');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // getSources
  test(
    'getSources',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.getSources(),
      intercept: (request) {
        expectPath(request.path, '/1/security/sources');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // getSynonym
  test(
    'getSynonym',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.getSynonym(
        indexName: "indexName",
        objectID: "id1",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/synonyms/id1');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // getTask
  test(
    'getTask',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.getTask(
        indexName: "theIndexName",
        taskID: 123,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/task/123');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // getTopUserIds
  test(
    'getTopUserIds',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.getTopUserIds(),
      intercept: (request) {
        expectPath(request.path, '/1/clusters/mapping/top');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // getUserId
  test(
    'getUserId',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.getUserId(
        userID: "uniqueID",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/clusters/mapping/uniqueID');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // hasPendingMappings
  test(
    'hasPendingMappings with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.hasPendingMappings(),
      intercept: (request) {
        expectPath(request.path, '/1/clusters/mapping/pending');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // hasPendingMappings
  test(
    'hasPendingMappings with parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.hasPendingMappings(
        getClusters: true,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/clusters/mapping/pending');
        expect(request.method, 'get');
        expectParams(request.queryParameters, """{"getClusters":"true"}""");
        expect(request.body, null);
      },
    ),
  );

  // listApiKeys
  test(
    'listApiKeys',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.listApiKeys(),
      intercept: (request) {
        expectPath(request.path, '/1/keys');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // listClusters
  test(
    'listClusters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.listClusters(),
      intercept: (request) {
        expectPath(request.path, '/1/clusters');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // listIndices
  test(
    'listIndices with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.listIndices(),
      intercept: (request) {
        expectPath(request.path, '/1/indexes');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // listIndices
  test(
    'listIndices with parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.listIndices(
        page: 8,
        hitsPerPage: 3,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes');
        expect(request.method, 'get');
        expectParams(
            request.queryParameters, """{"page":"8","hitsPerPage":"3"}""");
        expect(request.body, null);
      },
    ),
  );

  // listUserIds
  test(
    'listUserIds with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.listUserIds(),
      intercept: (request) {
        expectPath(request.path, '/1/clusters/mapping');
        expect(request.method, 'get');
        expect(request.body, null);
      },
    ),
  );

  // listUserIds
  test(
    'listUserIds with parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.listUserIds(
        page: 8,
        hitsPerPage: 100,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/clusters/mapping');
        expect(request.method, 'get');
        expectParams(
            request.queryParameters, """{"page":"8","hitsPerPage":"100"}""");
        expect(request.body, null);
      },
    ),
  );

  // multipleBatch
  test(
    'multipleBatch',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.multipleBatch(
        batchParams: BatchParams(
          requests: [
            MultipleBatchRequest(
              action: Action.fromJson("addObject"),
              body: {
                'key': "value",
              },
              indexName: "theIndexName",
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/*/batch');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"action":"addObject","body":{"key":"value"},"indexName":"theIndexName"}]}""");
      },
    ),
  );

  // operationIndex
  test(
    'operationIndex',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.operationIndex(
        indexName: "theIndexName",
        operationIndexParams: OperationIndexParams(
          operation: OperationType.fromJson("copy"),
          destination: "dest",
          scope: [
            ScopeType.fromJson("rules"),
            ScopeType.fromJson("settings"),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/operation');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"operation":"copy","destination":"dest","scope":["rules","settings"]}""");
      },
    ),
  );

  // partialUpdateObject
  test(
    'partialUpdateObject',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.partialUpdateObject(
        indexName: "theIndexName",
        objectID: "uniqueID",
        attributesToUpdate: {
          'id1': "test",
          'id2': BuiltInOperation(
            operation: BuiltInOperationType.fromJson("AddUnique"),
            value: "test2",
          ),
        },
        createIfNotExists: true,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/uniqueID/partial');
        expect(request.method, 'post');
        expectParams(
            request.queryParameters, """{"createIfNotExists":"true"}""");
        expectBody(request.body,
            """{"id1":"test","id2":{"_operation":"AddUnique","value":"test2"}}""");
      },
    ),
  );

  // post
  test(
    'allow post method for a custom path with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.post(
        path: "/test/minimal",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/minimal');
        expect(request.method, 'post');
        expectBody(request.body, """{}""");
      },
    ),
  );

  // post
  test(
    'allow post method for a custom path with all parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.post(
        path: "/test/all",
        parameters: {
          'query': "parameters",
        },
        body: {
          'body': "parameters",
        },
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/all');
        expect(request.method, 'post');
        expectParams(request.queryParameters, """{"query":"parameters"}""");
        expectBody(request.body, """{"body":"parameters"}""");
      },
    ),
  );

  // post
  test(
    'requestOptions can override default query parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.post(
        path: "/test/requestOptions",
        parameters: {
          'query': "parameters",
        },
        body: {
          'facet': "filters",
        },
        requestOptions: RequestOptions(
          urlParameters: {
            'query': "myQueryParameter",
          },
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/requestOptions');
        expect(request.method, 'post');
        expectParams(
            request.queryParameters, """{"query":"myQueryParameter"}""");
        expectBody(request.body, """{"facet":"filters"}""");
      },
    ),
  );

  // post
  test(
    'requestOptions merges query parameters with default ones',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.post(
        path: "/test/requestOptions",
        parameters: {
          'query': "parameters",
        },
        body: {
          'facet': "filters",
        },
        requestOptions: RequestOptions(
          urlParameters: {
            'query2': "myQueryParameter",
          },
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/requestOptions');
        expect(request.method, 'post');
        expectParams(request.queryParameters,
            """{"query":"parameters","query2":"myQueryParameter"}""");
        expectBody(request.body, """{"facet":"filters"}""");
      },
    ),
  );

  // post
  test(
    'requestOptions can override default headers',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.post(
        path: "/test/requestOptions",
        parameters: {
          'query': "parameters",
        },
        body: {
          'facet': "filters",
        },
        requestOptions: RequestOptions(
          headers: {
            'x-algolia-api-key': 'myApiKey',
          },
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/requestOptions');
        expect(request.method, 'post');
        expectHeaders(request.headers, """{"x-algolia-api-key":"myApiKey"}""");
        expectParams(request.queryParameters, """{"query":"parameters"}""");
        expectBody(request.body, """{"facet":"filters"}""");
      },
    ),
  );

  // post
  test(
    'requestOptions merges headers with default ones',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.post(
        path: "/test/requestOptions",
        parameters: {
          'query': "parameters",
        },
        body: {
          'facet': "filters",
        },
        requestOptions: RequestOptions(
          headers: {
            'x-algolia-api-key': 'myApiKey',
          },
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/requestOptions');
        expect(request.method, 'post');
        expectHeaders(request.headers, """{"x-algolia-api-key":"myApiKey"}""");
        expectParams(request.queryParameters, """{"query":"parameters"}""");
        expectBody(request.body, """{"facet":"filters"}""");
      },
    ),
  );

  // post
  test(
    'requestOptions queryParameters accepts booleans',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.post(
        path: "/test/requestOptions",
        parameters: {
          'query': "parameters",
        },
        body: {
          'facet': "filters",
        },
        requestOptions: RequestOptions(
          urlParameters: {
            'isItWorking': true,
          },
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/requestOptions');
        expect(request.method, 'post');
        expectParams(request.queryParameters,
            """{"query":"parameters","isItWorking":"true"}""");
        expectBody(request.body, """{"facet":"filters"}""");
      },
    ),
  );

  // post
  test(
    'requestOptions queryParameters accepts integers',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.post(
        path: "/test/requestOptions",
        parameters: {
          'query': "parameters",
        },
        body: {
          'facet': "filters",
        },
        requestOptions: RequestOptions(
          urlParameters: {
            'myParam': 2,
          },
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/requestOptions');
        expect(request.method, 'post');
        expectParams(request.queryParameters,
            """{"query":"parameters","myParam":"2"}""");
        expectBody(request.body, """{"facet":"filters"}""");
      },
    ),
  );

  // post
  test(
    'requestOptions queryParameters accepts list of string',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.post(
        path: "/test/requestOptions",
        parameters: {
          'query': "parameters",
        },
        body: {
          'facet': "filters",
        },
        requestOptions: RequestOptions(
          urlParameters: {
            'myParam': [
              "c",
              "d",
            ],
          },
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/requestOptions');
        expect(request.method, 'post');
        expectParams(request.queryParameters,
            """{"query":"parameters","myParam":"c,d"}""");
        expectBody(request.body, """{"facet":"filters"}""");
      },
    ),
  );

  // post
  test(
    'requestOptions queryParameters accepts list of booleans',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.post(
        path: "/test/requestOptions",
        parameters: {
          'query': "parameters",
        },
        body: {
          'facet': "filters",
        },
        requestOptions: RequestOptions(
          urlParameters: {
            'myParam': [
              true,
              true,
              false,
            ],
          },
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/requestOptions');
        expect(request.method, 'post');
        expectParams(request.queryParameters,
            """{"query":"parameters","myParam":"true,true,false"}""");
        expectBody(request.body, """{"facet":"filters"}""");
      },
    ),
  );

  // post
  test(
    'requestOptions queryParameters accepts list of integers',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.post(
        path: "/test/requestOptions",
        parameters: {
          'query': "parameters",
        },
        body: {
          'facet': "filters",
        },
        requestOptions: RequestOptions(
          urlParameters: {
            'myParam': [
              1,
              2,
            ],
          },
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/requestOptions');
        expect(request.method, 'post');
        expectParams(request.queryParameters,
            """{"query":"parameters","myParam":"1,2"}""");
        expectBody(request.body, """{"facet":"filters"}""");
      },
    ),
  );

  // put
  test(
    'allow put method for a custom path with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.put(
        path: "/test/minimal",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/minimal');
        expect(request.method, 'put');
        expectBody(request.body, """{}""");
      },
    ),
  );

  // put
  test(
    'allow put method for a custom path with all parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.put(
        path: "/test/all",
        parameters: {
          'query': "parameters",
        },
        body: {
          'body': "parameters",
        },
      ),
      intercept: (request) {
        expectPath(request.path, '/1/test/all');
        expect(request.method, 'put');
        expectParams(request.queryParameters, """{"query":"parameters"}""");
        expectBody(request.body, """{"body":"parameters"}""");
      },
    ),
  );

  // removeUserId
  test(
    'removeUserId',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.removeUserId(
        userID: "uniqueID",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/clusters/mapping/uniqueID');
        expect(request.method, 'delete');
        expect(request.body, null);
      },
    ),
  );

  // replaceSources
  test(
    'replaceSources',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.replaceSources(
        source: [
          Source(
            source: "theSource",
            description: "theDescription",
          ),
        ],
      ),
      intercept: (request) {
        expectPath(request.path, '/1/security/sources');
        expect(request.method, 'put');
        expectBody(request.body,
            """[{"source":"theSource","description":"theDescription"}]""");
      },
    ),
  );

  // restoreApiKey
  test(
    'restoreApiKey',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.restoreApiKey(
        key: "myApiKey",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/keys/myApiKey/restore');
        expect(request.method, 'post');
        expect(request.body, {});
      },
    ),
  );

  // saveObject
  test(
    'saveObject',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.saveObject(
        indexName: "theIndexName",
        body: {
          'objectID': "id",
          'test': "val",
        },
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName');
        expect(request.method, 'post');
        expectBody(request.body, """{"objectID":"id","test":"val"}""");
      },
    ),
  );

  // saveRule
  test(
    'saveRule with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.saveRule(
        indexName: "indexName",
        objectID: "id1",
        rule: Rule(
          objectID: "id1",
          conditions: [
            Condition(
              pattern: "apple",
              anchoring: Anchoring.fromJson("contains"),
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/rules/id1');
        expect(request.method, 'put');
        expectBody(request.body,
            """{"objectID":"id1","conditions":[{"pattern":"apple","anchoring":"contains"}]}""");
      },
    ),
  );

  // saveRule
  test(
    'saveRule with all parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.saveRule(
        indexName: "indexName",
        objectID: "id1",
        rule: Rule(
          objectID: "id1",
          conditions: [
            Condition(
              pattern: "apple",
              anchoring: Anchoring.fromJson("contains"),
              alternatives: false,
              context: "search",
            ),
          ],
          consequence: Consequence(
            params: ConsequenceParams(
              filters: "brand:apple",
              query: ConsequenceQueryObject(
                remove: [
                  "algolia",
                ],
                edits: [
                  Edit(
                    type: EditType.fromJson("remove"),
                    delete: "abc",
                    insert: "cde",
                  ),
                  Edit(
                    type: EditType.fromJson("replace"),
                    delete: "abc",
                    insert: "cde",
                  ),
                ],
              ),
            ),
            hide: [
              ConsequenceHide(
                objectID: "321",
              ),
            ],
            filterPromotes: false,
            userData: {
              'algolia': 'aloglia',
            },
            promote: [
              PromoteObjectID(
                objectID: "abc",
                position: 3,
              ),
              PromoteObjectIDs(
                objectIDs: [
                  "abc",
                  "def",
                ],
                position: 1,
              ),
            ],
          ),
          description: "test",
          enabled: true,
          validity: [
            TimeRange(
              from: 1656670273,
              until: 1656670277,
            ),
          ],
        ),
        forwardToReplicas: true,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/rules/id1');
        expect(request.method, 'put');
        expectParams(
            request.queryParameters, """{"forwardToReplicas":"true"}""");
        expectBody(request.body,
            """{"objectID":"id1","conditions":[{"pattern":"apple","anchoring":"contains","alternatives":false,"context":"search"}],"consequence":{"params":{"filters":"brand:apple","query":{"remove":["algolia"],"edits":[{"type":"remove","delete":"abc","insert":"cde"},{"type":"replace","delete":"abc","insert":"cde"}]}},"hide":[{"objectID":"321"}],"filterPromotes":false,"userData":{"algolia":"aloglia"},"promote":[{"objectID":"abc","position":3},{"objectIDs":["abc","def"],"position":1}]},"description":"test","enabled":true,"validity":[{"from":1656670273,"until":1656670277}]}""");
      },
    ),
  );

  // saveRules
  test(
    'saveRules with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.saveRules(
        indexName: "indexName",
        rules: [
          Rule(
            objectID: "a-rule-id",
            conditions: [
              Condition(
                pattern: "smartphone",
                anchoring: Anchoring.fromJson("contains"),
              ),
            ],
          ),
          Rule(
            objectID: "a-second-rule-id",
            conditions: [
              Condition(
                pattern: "apple",
                anchoring: Anchoring.fromJson("contains"),
              ),
            ],
          ),
        ],
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/rules/batch');
        expect(request.method, 'post');
        expectBody(request.body,
            """[{"objectID":"a-rule-id","conditions":[{"pattern":"smartphone","anchoring":"contains"}]},{"objectID":"a-second-rule-id","conditions":[{"pattern":"apple","anchoring":"contains"}]}]""");
      },
    ),
  );

  // saveRules
  test(
    'saveRules with all parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.saveRules(
        indexName: "indexName",
        rules: [
          Rule(
            objectID: "id1",
            conditions: [
              Condition(
                pattern: "apple",
                anchoring: Anchoring.fromJson("contains"),
                alternatives: false,
                context: "search",
              ),
            ],
            consequence: Consequence(
              params: ConsequenceParams(
                filters: "brand:apple",
                query: ConsequenceQueryObject(
                  remove: [
                    "algolia",
                  ],
                  edits: [
                    Edit(
                      type: EditType.fromJson("remove"),
                      delete: "abc",
                      insert: "cde",
                    ),
                    Edit(
                      type: EditType.fromJson("replace"),
                      delete: "abc",
                      insert: "cde",
                    ),
                  ],
                ),
              ),
              hide: [
                ConsequenceHide(
                  objectID: "321",
                ),
              ],
              filterPromotes: false,
              userData: {
                'algolia': 'aloglia',
              },
              promote: [
                PromoteObjectID(
                  objectID: "abc",
                  position: 3,
                ),
                PromoteObjectIDs(
                  objectIDs: [
                    "abc",
                    "def",
                  ],
                  position: 1,
                ),
              ],
            ),
            description: "test",
            enabled: true,
            validity: [
              TimeRange(
                from: 1656670273,
                until: 1656670277,
              ),
            ],
          ),
        ],
        forwardToReplicas: true,
        clearExistingRules: true,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/rules/batch');
        expect(request.method, 'post');
        expectParams(request.queryParameters,
            """{"forwardToReplicas":"true","clearExistingRules":"true"}""");
        expectBody(request.body,
            """[{"objectID":"id1","conditions":[{"pattern":"apple","anchoring":"contains","alternatives":false,"context":"search"}],"consequence":{"params":{"filters":"brand:apple","query":{"remove":["algolia"],"edits":[{"type":"remove","delete":"abc","insert":"cde"},{"type":"replace","delete":"abc","insert":"cde"}]}},"hide":[{"objectID":"321"}],"filterPromotes":false,"userData":{"algolia":"aloglia"},"promote":[{"objectID":"abc","position":3},{"objectIDs":["abc","def"],"position":1}]},"description":"test","enabled":true,"validity":[{"from":1656670273,"until":1656670277}]}]""");
      },
    ),
  );

  // saveSynonym
  test(
    'saveSynonym',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.saveSynonym(
        indexName: "indexName",
        objectID: "id1",
        synonymHit: SynonymHit(
          objectID: "id1",
          type: SynonymType.fromJson("synonym"),
          synonyms: [
            "car",
            "vehicule",
            "auto",
          ],
        ),
        forwardToReplicas: true,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/synonyms/id1');
        expect(request.method, 'put');
        expectParams(
            request.queryParameters, """{"forwardToReplicas":"true"}""");
        expectBody(request.body,
            """{"objectID":"id1","type":"synonym","synonyms":["car","vehicule","auto"]}""");
      },
    ),
  );

  // saveSynonyms
  test(
    'saveSynonyms',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.saveSynonyms(
        indexName: "indexName",
        synonymHit: [
          SynonymHit(
            objectID: "id1",
            type: SynonymType.fromJson("synonym"),
            synonyms: [
              "car",
              "vehicule",
              "auto",
            ],
          ),
          SynonymHit(
            objectID: "id2",
            type: SynonymType.fromJson("onewaysynonym"),
            input: "iphone",
            synonyms: [
              "ephone",
              "aphone",
              "yphone",
            ],
          ),
        ],
        forwardToReplicas: true,
        replaceExistingSynonyms: false,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/synonyms/batch');
        expect(request.method, 'post');
        expectParams(request.queryParameters,
            """{"forwardToReplicas":"true","replaceExistingSynonyms":"false"}""");
        expectBody(request.body,
            """[{"objectID":"id1","type":"synonym","synonyms":["car","vehicule","auto"]},{"objectID":"id2","type":"onewaysynonym","input":"iphone","synonyms":["ephone","aphone","yphone"]}]""");
      },
    ),
  );

  // search
  test(
    'search for a single hits request with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.search(
        searchMethodParams: SearchMethodParams(
          requests: [
            SearchForHits(
              indexName: "theIndexName",
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/*/queries');
        expect(request.method, 'post');
        expectBody(
            request.body, """{"requests":[{"indexName":"theIndexName"}]}""");
      },
    ),
  );

  // search
  test(
    'search for a single facet request with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.search(
        searchMethodParams: SearchMethodParams(
          requests: [
            SearchForFacets(
              indexName: "theIndexName",
              type: SearchTypeFacet.fromJson("facet"),
              facet: "theFacet",
            ),
          ],
          strategy: SearchStrategy.fromJson("stopIfEnoughMatches"),
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/*/queries');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"indexName":"theIndexName","type":"facet","facet":"theFacet"}],"strategy":"stopIfEnoughMatches"}""");
      },
    ),
  );

  // search
  test(
    'search for a single hits request with all parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.search(
        searchMethodParams: SearchMethodParams(
          requests: [
            SearchForHits(
              indexName: "theIndexName",
              query: "myQuery",
              hitsPerPage: 50,
              type: SearchTypeDefault.fromJson("default"),
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/*/queries');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"indexName":"theIndexName","query":"myQuery","hitsPerPage":50,"type":"default"}]}""");
      },
    ),
  );

  // search
  test(
    'search for a single facet request with all parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.search(
        searchMethodParams: SearchMethodParams(
          requests: [
            SearchForFacets(
              indexName: "theIndexName",
              type: SearchTypeFacet.fromJson("facet"),
              facet: "theFacet",
              facetQuery: "theFacetQuery",
              query: "theQuery",
              maxFacetHits: 50,
            ),
          ],
          strategy: SearchStrategy.fromJson("stopIfEnoughMatches"),
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/*/queries');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"indexName":"theIndexName","type":"facet","facet":"theFacet","facetQuery":"theFacetQuery","query":"theQuery","maxFacetHits":50}],"strategy":"stopIfEnoughMatches"}""");
      },
    ),
  );

  // search
  test(
    'search for multiple mixed requests in multiple indices with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.search(
        searchMethodParams: SearchMethodParams(
          requests: [
            SearchForHits(
              indexName: "theIndexName",
            ),
            SearchForFacets(
              indexName: "theIndexName2",
              type: SearchTypeFacet.fromJson("facet"),
              facet: "theFacet",
            ),
            SearchForHits(
              indexName: "theIndexName",
              type: SearchTypeDefault.fromJson("default"),
            ),
          ],
          strategy: SearchStrategy.fromJson("stopIfEnoughMatches"),
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/*/queries');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"indexName":"theIndexName"},{"indexName":"theIndexName2","type":"facet","facet":"theFacet"},{"indexName":"theIndexName","type":"default"}],"strategy":"stopIfEnoughMatches"}""");
      },
    ),
  );

  // search
  test(
    'search for multiple mixed requests in multiple indices with all parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.search(
        searchMethodParams: SearchMethodParams(
          requests: [
            SearchForFacets(
              indexName: "theIndexName",
              type: SearchTypeFacet.fromJson("facet"),
              facet: "theFacet",
              facetQuery: "theFacetQuery",
              query: "theQuery",
              maxFacetHits: 50,
            ),
            SearchForHits(
              indexName: "theIndexName",
              query: "myQuery",
              hitsPerPage: 50,
              type: SearchTypeDefault.fromJson("default"),
            ),
          ],
          strategy: SearchStrategy.fromJson("stopIfEnoughMatches"),
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/*/queries');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"indexName":"theIndexName","type":"facet","facet":"theFacet","facetQuery":"theFacetQuery","query":"theQuery","maxFacetHits":50},{"indexName":"theIndexName","query":"myQuery","hitsPerPage":50,"type":"default"}],"strategy":"stopIfEnoughMatches"}""");
      },
    ),
  );

  // search
  test(
    'search filters accept all of the possible shapes',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.search(
        searchMethodParams: SearchMethodParams(
          requests: [
            SearchForHits(
              indexName: "theIndexName",
              facetFilters: "mySearch:filters",
              reRankingApplyFilter: "mySearch:filters",
              tagFilters: "mySearch:filters",
              numericFilters: "mySearch:filters",
              optionalFilters: "mySearch:filters",
            ),
            SearchForHits(
              indexName: "theIndexName",
              facetFilters: [
                "mySearch:filters",
                [
                  "mySearch:filters",
                ],
              ],
              reRankingApplyFilter: [
                "mySearch:filters",
                [
                  "mySearch:filters",
                ],
              ],
              tagFilters: [
                "mySearch:filters",
                [
                  "mySearch:filters",
                ],
              ],
              numericFilters: [
                "mySearch:filters",
                [
                  "mySearch:filters",
                ],
              ],
              optionalFilters: [
                "mySearch:filters",
                [
                  "mySearch:filters",
                ],
              ],
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/*/queries');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"indexName":"theIndexName","facetFilters":"mySearch:filters","reRankingApplyFilter":"mySearch:filters","tagFilters":"mySearch:filters","numericFilters":"mySearch:filters","optionalFilters":"mySearch:filters"},{"indexName":"theIndexName","facetFilters":["mySearch:filters",["mySearch:filters"]],"reRankingApplyFilter":["mySearch:filters",["mySearch:filters"]],"tagFilters":["mySearch:filters",["mySearch:filters"]],"numericFilters":["mySearch:filters",["mySearch:filters"]],"optionalFilters":["mySearch:filters",["mySearch:filters"]]}]}""");
      },
    ),
  );

  // search
  test(
    'search with all search parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.search(
        searchMethodParams: SearchMethodParams(
          requests: [
            SearchForHits(
              advancedSyntax: true,
              advancedSyntaxFeatures: [
                AdvancedSyntaxFeatures.fromJson("exactPhrase"),
              ],
              allowTyposOnNumericTokens: true,
              alternativesAsExact: [
                AlternativesAsExact.fromJson("multiWordsSynonym"),
              ],
              analytics: true,
              analyticsTags: [
                "",
              ],
              aroundLatLng: "",
              aroundLatLngViaIP: true,
              aroundPrecision: 0,
              aroundRadius: AroundRadiusAll.fromJson("all"),
              attributeCriteriaComputedByMinProximity: true,
              attributesForFaceting: [
                "",
              ],
              attributesToHighlight: [
                "",
              ],
              attributesToRetrieve: [
                "",
              ],
              attributesToSnippet: [
                "",
              ],
              clickAnalytics: true,
              customRanking: [
                "",
              ],
              decompoundQuery: true,
              disableExactOnAttributes: [
                "",
              ],
              disableTypoToleranceOnAttributes: [
                "",
              ],
              distinct: 0,
              enableABTest: true,
              enablePersonalization: true,
              enableReRanking: true,
              enableRules: true,
              exactOnSingleWordQuery:
                  ExactOnSingleWordQuery.fromJson("attribute"),
              explain: [
                "foo",
                "bar",
              ],
              facetFilters: [
                "",
              ],
              facetingAfterDistinct: true,
              facets: [
                "",
              ],
              filters: "",
              getRankingInfo: true,
              highlightPostTag: "",
              highlightPreTag: "",
              hitsPerPage: 0,
              ignorePlurals: false,
              indexName: "theIndexName",
              insideBoundingBox: [
                [
                  47.3165,
                  4.9665,
                  47.3424,
                  5.0201,
                ],
                [
                  40.9234,
                  2.1185,
                  38.643,
                  1.9916,
                ],
              ],
              insidePolygon: [
                [
                  47.3165,
                  4.9665,
                  47.3424,
                  5.0201,
                  47.32,
                  4.9,
                ],
                [
                  40.9234,
                  2.1185,
                  38.643,
                  1.9916,
                  39.2587,
                  2.0104,
                ],
              ],
              keepDiacriticsOnCharacters: "",
              length: 0,
              maxValuesPerFacet: 0,
              minProximity: 0,
              minWordSizefor1Typo: 0,
              minWordSizefor2Typos: 0,
              minimumAroundRadius: 0,
              naturalLanguages: [
                "",
              ],
              numericFilters: [
                "",
              ],
              offset: 0,
              optionalFilters: [
                "",
              ],
              optionalWords: [
                "",
              ],
              page: 0,
              percentileComputation: true,
              personalizationImpact: 0,
              query: "",
              queryLanguages: [
                "",
              ],
              queryType: QueryType.fromJson("prefixAll"),
              ranking: [
                "",
              ],
              reRankingApplyFilter: [
                "",
              ],
              relevancyStrictness: 0,
              removeStopWords: true,
              removeWordsIfNoResults:
                  RemoveWordsIfNoResults.fromJson("allOptional"),
              renderingContent: RenderingContent(
                facetOrdering: FacetOrdering(
                  facets: Facets(
                    order: [
                      "a",
                      "b",
                    ],
                  ),
                  values: {
                    'a': Value(
                      order: [
                        "b",
                      ],
                      sortRemainingBy: SortRemainingBy.fromJson("count"),
                    ),
                  },
                ),
              ),
              replaceSynonymsInHighlight: true,
              responseFields: [
                "",
              ],
              restrictHighlightAndSnippetArrays: true,
              restrictSearchableAttributes: [
                "",
              ],
              ruleContexts: [
                "",
              ],
              similarQuery: "",
              snippetEllipsisText: "",
              sortFacetValuesBy: "",
              sumOrFiltersScores: true,
              synonyms: true,
              tagFilters: [
                "",
              ],
              type: SearchTypeDefault.fromJson("default"),
              typoTolerance: TypoToleranceEnum.fromJson("min"),
              userToken: "",
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/*/queries');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"requests":[{"advancedSyntax":true,"advancedSyntaxFeatures":["exactPhrase"],"allowTyposOnNumericTokens":true,"alternativesAsExact":["multiWordsSynonym"],"analytics":true,"analyticsTags":[""],"aroundLatLng":"","aroundLatLngViaIP":true,"aroundPrecision":0,"aroundRadius":"all","attributeCriteriaComputedByMinProximity":true,"attributesForFaceting":[""],"attributesToHighlight":[""],"attributesToRetrieve":[""],"attributesToSnippet":[""],"clickAnalytics":true,"customRanking":[""],"decompoundQuery":true,"disableExactOnAttributes":[""],"disableTypoToleranceOnAttributes":[""],"distinct":0,"enableABTest":true,"enablePersonalization":true,"enableReRanking":true,"enableRules":true,"exactOnSingleWordQuery":"attribute","explain":["foo","bar"],"facetFilters":[""],"facetingAfterDistinct":true,"facets":[""],"filters":"","getRankingInfo":true,"highlightPostTag":"","highlightPreTag":"","hitsPerPage":0,"ignorePlurals":false,"indexName":"theIndexName","insideBoundingBox":[[47.3165,4.9665,47.3424,5.0201],[40.9234,2.1185,38.643,1.9916]],"insidePolygon":[[47.3165,4.9665,47.3424,5.0201,47.32,4.9],[40.9234,2.1185,38.643,1.9916,39.2587,2.0104]],"keepDiacriticsOnCharacters":"","length":0,"maxValuesPerFacet":0,"minProximity":0,"minWordSizefor1Typo":0,"minWordSizefor2Typos":0,"minimumAroundRadius":0,"naturalLanguages":[""],"numericFilters":[""],"offset":0,"optionalFilters":[""],"optionalWords":[""],"page":0,"percentileComputation":true,"personalizationImpact":0,"query":"","queryLanguages":[""],"queryType":"prefixAll","ranking":[""],"reRankingApplyFilter":[""],"relevancyStrictness":0,"removeStopWords":true,"removeWordsIfNoResults":"allOptional","renderingContent":{"facetOrdering":{"facets":{"order":["a","b"]},"values":{"a":{"order":["b"],"sortRemainingBy":"count"}}}},"replaceSynonymsInHighlight":true,"responseFields":[""],"restrictHighlightAndSnippetArrays":true,"restrictSearchableAttributes":[""],"ruleContexts":[""],"similarQuery":"","snippetEllipsisText":"","sortFacetValuesBy":"","sumOrFiltersScores":true,"synonyms":true,"tagFilters":[""],"type":"default","typoTolerance":"min","userToken":""}]}""");
      },
    ),
  );

  // searchDictionaryEntries
  test(
    'get searchDictionaryEntries results with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.searchDictionaryEntries(
        dictionaryName: DictionaryType.fromJson("compounds"),
        searchDictionaryEntriesParams: SearchDictionaryEntriesParams(
          query: "foo",
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/dictionaries/compounds/search');
        expect(request.method, 'post');
        expectBody(request.body, """{"query":"foo"}""");
      },
    ),
  );

  // searchDictionaryEntries
  test(
    'get searchDictionaryEntries results with all parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.searchDictionaryEntries(
        dictionaryName: DictionaryType.fromJson("compounds"),
        searchDictionaryEntriesParams: SearchDictionaryEntriesParams(
          query: "foo",
          page: 4,
          hitsPerPage: 2,
          language: "fr",
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/dictionaries/compounds/search');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"query":"foo","page":4,"hitsPerPage":2,"language":"fr"}""");
      },
    ),
  );

  // searchForFacetValues
  test(
    'get searchForFacetValues results with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.searchForFacetValues(
        indexName: "indexName",
        facetName: "facetName",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/facets/facetName/query');
        expect(request.method, 'post');
        expectBody(request.body, """{}""");
      },
    ),
  );

  // searchForFacetValues
  test(
    'get searchForFacetValues results with all parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.searchForFacetValues(
        indexName: "indexName",
        facetName: "facetName",
        searchForFacetValuesRequest: SearchForFacetValuesRequest(
          params: "query=foo&facetFilters=['bar']",
          facetQuery: "foo",
          maxFacetHits: 42,
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/facets/facetName/query');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"params":"query=foo&facetFilters=['bar']","facetQuery":"foo","maxFacetHits":42}""");
      },
    ),
  );

  // searchRules
  test(
    'searchRules',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.searchRules(
        indexName: "indexName",
        searchRulesParams: SearchRulesParams(
          query: "something",
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/rules/search');
        expect(request.method, 'post');
        expectBody(request.body, """{"query":"something"}""");
      },
    ),
  );

  // searchSingleIndex
  test(
    'search with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.searchSingleIndex(
        indexName: "indexName",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/query');
        expect(request.method, 'post');
        expectBody(request.body, """{}""");
      },
    ),
  );

  // searchSingleIndex
  test(
    'search with searchParams',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.searchSingleIndex(
        indexName: "indexName",
        searchParams: SearchParamsObject(
          query: "myQuery",
          facetFilters: [
            "tags:algolia",
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/query');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"query":"myQuery","facetFilters":["tags:algolia"]}""");
      },
    ),
  );

  // searchSynonyms
  test(
    'searchSynonyms with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.searchSynonyms(
        indexName: "indexName",
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/synonyms/search');
        expect(request.method, 'post');
        expectBody(request.body, """{}""");
      },
    ),
  );

  // searchSynonyms
  test(
    'searchSynonyms with all parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.searchSynonyms(
        indexName: "indexName",
        type: SynonymType.fromJson("altcorrection1"),
        page: 10,
        hitsPerPage: 10,
        searchSynonymsParams: SearchSynonymsParams(
          query: "myQuery",
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/indexName/synonyms/search');
        expect(request.method, 'post');
        expectParams(request.queryParameters,
            """{"type":"altcorrection1","page":"10","hitsPerPage":"10"}""");
        expectBody(request.body, """{"query":"myQuery"}""");
      },
    ),
  );

  // searchUserIds
  test(
    'searchUserIds',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.searchUserIds(
        searchUserIdsParams: SearchUserIdsParams(
          query: "test",
          clusterName: "theClusterName",
          page: 5,
          hitsPerPage: 10,
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/clusters/mapping/search');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"query":"test","clusterName":"theClusterName","page":5,"hitsPerPage":10}""");
      },
    ),
  );

  // setDictionarySettings
  test(
    'get setDictionarySettings results with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.setDictionarySettings(
        dictionarySettingsParams: DictionarySettingsParams(
          disableStandardEntries: StandardEntries(
            plurals: {
              'fr': false,
              'en': false,
              'ru': true,
            },
          ),
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/dictionaries/*/settings');
        expect(request.method, 'put');
        expectBody(request.body,
            """{"disableStandardEntries":{"plurals":{"fr":false,"en":false,"ru":true}}}""");
      },
    ),
  );

  // setDictionarySettings
  test(
    'get setDictionarySettings results with all parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.setDictionarySettings(
        dictionarySettingsParams: DictionarySettingsParams(
          disableStandardEntries: StandardEntries(
            plurals: {
              'fr': false,
              'en': false,
              'ru': true,
            },
            stopwords: {
              'fr': false,
            },
            compounds: {
              'ru': true,
            },
          ),
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/dictionaries/*/settings');
        expect(request.method, 'put');
        expectBody(request.body,
            """{"disableStandardEntries":{"plurals":{"fr":false,"en":false,"ru":true},"stopwords":{"fr":false},"compounds":{"ru":true}}}""");
      },
    ),
  );

  // setSettings
  test(
    'setSettings with minimal parameters',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.setSettings(
        indexName: "theIndexName",
        indexSettings: IndexSettings(
          paginationLimitedTo: 10,
        ),
        forwardToReplicas: true,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/settings');
        expect(request.method, 'put');
        expectParams(
            request.queryParameters, """{"forwardToReplicas":"true"}""");
        expectBody(request.body, """{"paginationLimitedTo":10}""");
      },
    ),
  );

  // setSettings
  test(
    'setSettings allow boolean `typoTolerance`',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.setSettings(
        indexName: "theIndexName",
        indexSettings: IndexSettings(
          typoTolerance: true,
        ),
        forwardToReplicas: true,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/settings');
        expect(request.method, 'put');
        expectParams(
            request.queryParameters, """{"forwardToReplicas":"true"}""");
        expectBody(request.body, """{"typoTolerance":true}""");
      },
    ),
  );

  // setSettings
  test(
    'setSettings allow enum `typoTolerance`',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.setSettings(
        indexName: "theIndexName",
        indexSettings: IndexSettings(
          typoTolerance: TypoToleranceEnum.fromJson("min"),
        ),
        forwardToReplicas: true,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/settings');
        expect(request.method, 'put');
        expectParams(
            request.queryParameters, """{"forwardToReplicas":"true"}""");
        expectBody(request.body, """{"typoTolerance":"min"}""");
      },
    ),
  );

  // setSettings
  test(
    'setSettings allow boolean `ignorePlurals`',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.setSettings(
        indexName: "theIndexName",
        indexSettings: IndexSettings(
          ignorePlurals: true,
        ),
        forwardToReplicas: true,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/settings');
        expect(request.method, 'put');
        expectParams(
            request.queryParameters, """{"forwardToReplicas":"true"}""");
        expectBody(request.body, """{"ignorePlurals":true}""");
      },
    ),
  );

  // setSettings
  test(
    'setSettings allow list of string `ignorePlurals`',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.setSettings(
        indexName: "theIndexName",
        indexSettings: IndexSettings(
          ignorePlurals: [
            "algolia",
          ],
        ),
        forwardToReplicas: true,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/settings');
        expect(request.method, 'put');
        expectParams(
            request.queryParameters, """{"forwardToReplicas":"true"}""");
        expectBody(request.body, """{"ignorePlurals":["algolia"]}""");
      },
    ),
  );

  // setSettings
  test(
    'setSettings allow boolean `removeStopWords`',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.setSettings(
        indexName: "theIndexName",
        indexSettings: IndexSettings(
          removeStopWords: true,
        ),
        forwardToReplicas: true,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/settings');
        expect(request.method, 'put');
        expectParams(
            request.queryParameters, """{"forwardToReplicas":"true"}""");
        expectBody(request.body, """{"removeStopWords":true}""");
      },
    ),
  );

  // setSettings
  test(
    'setSettings allow list of string `removeStopWords`',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.setSettings(
        indexName: "theIndexName",
        indexSettings: IndexSettings(
          removeStopWords: [
            "algolia",
          ],
        ),
        forwardToReplicas: true,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/settings');
        expect(request.method, 'put');
        expectParams(
            request.queryParameters, """{"forwardToReplicas":"true"}""");
        expectBody(request.body, """{"removeStopWords":["algolia"]}""");
      },
    ),
  );

  // setSettings
  test(
    'setSettings allow boolean `distinct`',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.setSettings(
        indexName: "theIndexName",
        indexSettings: IndexSettings(
          distinct: true,
        ),
        forwardToReplicas: true,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/settings');
        expect(request.method, 'put');
        expectParams(
            request.queryParameters, """{"forwardToReplicas":"true"}""");
        expectBody(request.body, """{"distinct":true}""");
      },
    ),
  );

  // setSettings
  test(
    'setSettings allow integers for `distinct`',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.setSettings(
        indexName: "theIndexName",
        indexSettings: IndexSettings(
          distinct: 1,
        ),
        forwardToReplicas: true,
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/settings');
        expect(request.method, 'put');
        expectParams(
            request.queryParameters, """{"forwardToReplicas":"true"}""");
        expectBody(request.body, """{"distinct":1}""");
      },
    ),
  );

  // setSettings
  test(
    'setSettings allow all `indexSettings`',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.setSettings(
        indexName: "theIndexName",
        indexSettings: IndexSettings(
          advancedSyntax: true,
          advancedSyntaxFeatures: [
            AdvancedSyntaxFeatures.fromJson("exactPhrase"),
          ],
          allowCompressionOfIntegerArray: true,
          allowTyposOnNumericTokens: true,
          alternativesAsExact: [
            AlternativesAsExact.fromJson("singleWordSynonym"),
          ],
          attributeCriteriaComputedByMinProximity: true,
          attributeForDistinct: "test",
          attributesForFaceting: [
            "algolia",
          ],
          attributesToHighlight: [
            "algolia",
          ],
          attributesToRetrieve: [
            "algolia",
          ],
          attributesToSnippet: [
            "algolia",
          ],
          attributesToTransliterate: [
            "algolia",
          ],
          camelCaseAttributes: [
            "algolia",
          ],
          customNormalization: {
            'algolia': {
              'aloglia': "aglolia",
            },
          },
          customRanking: [
            "algolia",
          ],
          decompoundQuery: false,
          decompoundedAttributes: {
            'algolia': "aloglia",
          },
          disableExactOnAttributes: [
            "algolia",
          ],
          disablePrefixOnAttributes: [
            "algolia",
          ],
          disableTypoToleranceOnAttributes: [
            "algolia",
          ],
          disableTypoToleranceOnWords: [
            "algolia",
          ],
          distinct: 3,
          enablePersonalization: true,
          enableReRanking: false,
          enableRules: true,
          exactOnSingleWordQuery: ExactOnSingleWordQuery.fromJson("attribute"),
          highlightPreTag: "<span>",
          highlightPostTag: "</span>",
          hitsPerPage: 10,
          ignorePlurals: false,
          indexLanguages: [
            "algolia",
          ],
          keepDiacriticsOnCharacters: "abc",
          maxFacetHits: 20,
          maxValuesPerFacet: 30,
          minProximity: 6,
          minWordSizefor1Typo: 5,
          minWordSizefor2Typos: 11,
          mode: Mode.fromJson("neuralSearch"),
          numericAttributesForFiltering: [
            "algolia",
          ],
          optionalWords: [
            "myspace",
          ],
          paginationLimitedTo: 0,
          queryLanguages: [
            "algolia",
          ],
          queryType: QueryType.fromJson("prefixLast"),
          ranking: [
            "geo",
          ],
          reRankingApplyFilter: "mySearch:filters",
          relevancyStrictness: 10,
          removeStopWords: false,
          removeWordsIfNoResults: RemoveWordsIfNoResults.fromJson("lastWords"),
          renderingContent: RenderingContent(
            facetOrdering: FacetOrdering(
              facets: Facets(
                order: [
                  "a",
                  "b",
                ],
              ),
              values: {
                'a': Value(
                  order: [
                    "b",
                  ],
                  sortRemainingBy: SortRemainingBy.fromJson("count"),
                ),
              },
            ),
          ),
          replaceSynonymsInHighlight: true,
          replicas: [
            "",
          ],
          responseFields: [
            "algolia",
          ],
          restrictHighlightAndSnippetArrays: true,
          searchableAttributes: [
            "foo",
          ],
          semanticSearch: SemanticSearch(
            eventSources: [
              "foo",
            ],
          ),
          separatorsToIndex: "bar",
          snippetEllipsisText: "---",
          sortFacetValuesBy: "date",
          typoTolerance: false,
          unretrievableAttributes: [
            "foo",
          ],
          userData: {
            'user': 'data',
          },
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/indexes/theIndexName/settings');
        expect(request.method, 'put');
        expectBody(request.body,
            """{"advancedSyntax":true,"advancedSyntaxFeatures":["exactPhrase"],"allowCompressionOfIntegerArray":true,"allowTyposOnNumericTokens":true,"alternativesAsExact":["singleWordSynonym"],"attributeCriteriaComputedByMinProximity":true,"attributeForDistinct":"test","attributesForFaceting":["algolia"],"attributesToHighlight":["algolia"],"attributesToRetrieve":["algolia"],"attributesToSnippet":["algolia"],"attributesToTransliterate":["algolia"],"camelCaseAttributes":["algolia"],"customNormalization":{"algolia":{"aloglia":"aglolia"}},"customRanking":["algolia"],"decompoundQuery":false,"decompoundedAttributes":{"algolia":"aloglia"},"disableExactOnAttributes":["algolia"],"disablePrefixOnAttributes":["algolia"],"disableTypoToleranceOnAttributes":["algolia"],"disableTypoToleranceOnWords":["algolia"],"distinct":3,"enablePersonalization":true,"enableReRanking":false,"enableRules":true,"exactOnSingleWordQuery":"attribute","highlightPreTag":"<span>","highlightPostTag":"</span>","hitsPerPage":10,"ignorePlurals":false,"indexLanguages":["algolia"],"keepDiacriticsOnCharacters":"abc","maxFacetHits":20,"maxValuesPerFacet":30,"minProximity":6,"minWordSizefor1Typo":5,"minWordSizefor2Typos":11,"mode":"neuralSearch","numericAttributesForFiltering":["algolia"],"optionalWords":["myspace"],"paginationLimitedTo":0,"queryLanguages":["algolia"],"queryType":"prefixLast","ranking":["geo"],"reRankingApplyFilter":"mySearch:filters","relevancyStrictness":10,"removeStopWords":false,"removeWordsIfNoResults":"lastWords","renderingContent":{"facetOrdering":{"facets":{"order":["a","b"]},"values":{"a":{"order":["b"],"sortRemainingBy":"count"}}}},"replaceSynonymsInHighlight":true,"replicas":[""],"responseFields":["algolia"],"restrictHighlightAndSnippetArrays":true,"searchableAttributes":["foo"],"semanticSearch":{"eventSources":["foo"]},"separatorsToIndex":"bar","snippetEllipsisText":"---","sortFacetValuesBy":"date","typoTolerance":false,"unretrievableAttributes":["foo"],"userData":{"user":"data"}}""");
      },
    ),
  );

  // updateApiKey
  test(
    'updateApiKey',
    () => runTest(
      builder: (requester) => SearchClient(
        appId: 'appId',
        apiKey: 'apiKey',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.updateApiKey(
        key: "myApiKey",
        apiKey: ApiKey(
          acl: [
            Acl.fromJson("search"),
            Acl.fromJson("addObject"),
          ],
          validity: 300,
          maxQueriesPerIPPerHour: 100,
          maxHitsPerQuery: 20,
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/keys/myApiKey');
        expect(request.method, 'put');
        expectBody(request.body,
            """{"acl":["search","addObject"],"validity":300,"maxQueriesPerIPPerHour":100,"maxHitsPerQuery":20}""");
      },
    ),
  );
}
