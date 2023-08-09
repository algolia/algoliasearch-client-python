import 'package:algolia_client_insights/algolia_client_insights.dart';
import 'package:algolia_test/algolia_test.dart';
import 'package:test/test.dart';
import 'package:test_api/hooks.dart';

void main() {
  test('calls api with correct user agent', () {
    final client = InsightsClient(
      appId: 'appId',
      apiKey: 'apiKey',
      region: 'us',
    );
    runTest(
      builder: (requester) => InsightsClient(
        appId: client.appId,
        apiKey: client.apiKey,
        region: client.region,
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
    final client = InsightsClient(
      appId: 'appId',
      apiKey: 'apiKey',
      region: 'us',
    );
    runTest(
      builder: (requester) => InsightsClient(
        appId: client.appId,
        apiKey: client.apiKey,
        region: client.region,
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
    final client = InsightsClient(
      appId: 'appId',
      apiKey: 'apiKey',
      region: 'us',
    );
    runTest(
      builder: (requester) => InsightsClient(
        appId: client.appId,
        apiKey: client.apiKey,
        region: client.region,
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

  test('fallbacks to the alias when region is not given', () {
    final client = InsightsClient(
      appId: "my-app-id",
      apiKey: "my-api-key",
    );
    runTest(
      builder: (requester) => InsightsClient(
        appId: client.appId,
        apiKey: client.apiKey,
        region: client.region,
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.pushEvents(
        insightsEvents: InsightsEvents(
          events: [],
        ),
      ),
      intercept: (request) {
        expect(request.host.url, 'insights.algolia.io');
      },
    );
  });
  test('uses the correct region', () {
    final client = InsightsClient(
      appId: "my-app-id",
      apiKey: "my-api-key",
      region: 'us',
    );
    runTest(
      builder: (requester) => InsightsClient(
        appId: client.appId,
        apiKey: client.apiKey,
        region: client.region,
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.del(
        path: "/test",
      ),
      intercept: (request) {
        expect(request.host.url, 'insights.us.algolia.io');
      },
    );
  });
  test('throws when incorrect region is given', () {
    expectError(
      '`region` must be one of the following: de, us',
      () {
        final client = InsightsClient(
          appId: "my-app-id",
          apiKey: "my-api-key",
          region: 'not_a_region',
        );
      },
    );
  });
}
