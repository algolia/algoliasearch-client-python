import 'package:algolia_client_recommend/algolia_client_recommend.dart';
import 'package:algolia_test/algolia_test.dart';
import 'package:test/test.dart';
import 'package:test_api/hooks.dart';

void main() {
  test('calls api with correct read host', () {
    final client = RecommendClient(
      appId: "test-app-id",
      apiKey: "test-api-key",
    );
    runTest(
      builder: (requester) => RecommendClient(
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
    final client = RecommendClient(
      appId: "test-app-id",
      apiKey: "test-api-key",
    );
    runTest(
      builder: (requester) => RecommendClient(
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
    final client = RecommendClient(
      appId: 'appId',
      apiKey: 'apiKey',
    );
    runTest(
      builder: (requester) => RecommendClient(
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
    final client = RecommendClient(
      appId: 'appId',
      apiKey: 'apiKey',
    );
    runTest(
      builder: (requester) => RecommendClient(
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
    final client = RecommendClient(
      appId: 'appId',
      apiKey: 'apiKey',
    );
    runTest(
      builder: (requester) => RecommendClient(
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
}
