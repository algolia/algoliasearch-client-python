import 'package:algolia_client_search/algolia_client_search.dart';
import 'package:algolia_test/algolia_test.dart';
import 'package:test/test.dart';
import 'package:test_api/hooks.dart';

void main() {
  test('calls api with correct read host', () {
    final client = SearchClient(
      appId: "test-app-id",
      apiKey: "test-api-key",
    );
    runTest(
      builder: (requester) => SearchClient(
        appId: client.appId,
        apiKey: client.apiKey,
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.get(
        path: "/test",
      ),
      intercept: (request) {
        expect(request.host.url, 'test-app-id-dsn.algolia.net');
      },
    );
  });
  test('calls api with correct write host', () {
    final client = SearchClient(
      appId: "test-app-id",
      apiKey: "test-api-key",
    );
    runTest(
      builder: (requester) => SearchClient(
        appId: client.appId,
        apiKey: client.apiKey,
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.post(
        path: "/test",
      ),
      intercept: (request) {
        expect(request.host.url, 'test-app-id.algolia.net');
      },
    );
  });

  test('calls api with correct user agent', () {
    final client = SearchClient(
      appId: 'appId',
      apiKey: 'apiKey',
    );
    runTest(
      builder: (requester) => SearchClient(
        appId: client.appId,
        apiKey: client.apiKey,
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.post(
        path: "/test",
      ),
      intercept: (request) {
        TestHandle.current.markSkipped('User agent added using an interceptor');
      },
    );
  });
  test('calls api with default read timeouts', () {
    final client = SearchClient(
      appId: 'appId',
      apiKey: 'apiKey',
    );
    runTest(
      builder: (requester) => SearchClient(
        appId: client.appId,
        apiKey: client.apiKey,
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.get(
        path: "/test",
      ),
      intercept: (request) {
        expect(5000, request.timeout.inMilliseconds);
      },
    );
  });
  test('calls api with default write timeouts', () {
    final client = SearchClient(
      appId: 'appId',
      apiKey: 'apiKey',
    );
    runTest(
      builder: (requester) => SearchClient(
        appId: client.appId,
        apiKey: client.apiKey,
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.post(
        path: "/test",
      ),
      intercept: (request) {
        expect(30000, request.timeout.inMilliseconds);
      },
    );
  });

  test('client throws with invalid parameters', () {
    expectError(
      '`appId` is missing.',
      () {
        final client = SearchClient(
          appId: "",
          apiKey: "",
        );
      },
    );
    expectError(
      '`appId` is missing.',
      () {
        final client = SearchClient(
          appId: "",
          apiKey: "my-api-key",
        );
      },
    );
    expectError(
      '`apiKey` is missing.',
      () {
        final client = SearchClient(
          appId: "my-app-id",
          apiKey: "",
        );
      },
    );
  });
  test('`addApiKey` throws with invalid parameters', () {
    final client = SearchClient(
      appId: 'appId',
      apiKey: 'apiKey',
    );
    expectError(
      'Parameter `apiKey` is required when calling `addApiKey`.',
      () {
        return client.addApiKey(
          apiKey: empty(),
        );
      },
    );
  });
  test('`addOrUpdateObject` throws with invalid parameters', () {
    final client = SearchClient(
      appId: 'appId',
      apiKey: 'apiKey',
    );
    expectError(
      'Parameter `indexName` is required when calling `addOrUpdateObject`.',
      () {
        return client.addOrUpdateObject(
          indexName: empty(),
          objectID: "my-object-id",
          body: {},
        );
      },
    );
    expectError(
      'Parameter `objectID` is required when calling `addOrUpdateObject`.',
      () {
        return client.addOrUpdateObject(
          indexName: "my-index-name",
          objectID: empty(),
          body: {},
        );
      },
    );
    expectError(
      'Parameter `body` is required when calling `addOrUpdateObject`.',
      () {
        return client.addOrUpdateObject(
          indexName: "my-index-name",
          objectID: "my-object-id",
          body: empty(),
        );
      },
    );
  });
}
