import 'package:algolia_client_insights/algolia_client_insights.dart';
import 'package:algolia_test/algolia_test.dart';
import 'package:test/test.dart';

void main() {
  // del
  test(
    'allow del method for a custom path with minimal parameters',
    () => runTest(
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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

  // get
  test(
    'allow get method for a custom path with minimal parameters',
    () => runTest(
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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

  // post
  test(
    'allow post method for a custom path with minimal parameters',
    () => runTest(
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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

  // pushEvents
  test(
    'pushEvents',
    () => runTest(
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.pushEvents(
        insightsEvents: InsightsEvents(
          events: [
            ClickedObjectIDsAfterSearch(
              eventType: ClickEvent.fromJson("click"),
              eventName: "Product Clicked",
              index: "products",
              userToken: "user-123456",
              timestamp: 1641290601962,
              objectIDs: [
                "9780545139700",
                "9780439784542",
              ],
              queryID: "43b15df305339e827f0ac0bdc5ebcaa7",
              positions: [
                7,
                6,
              ],
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/events');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"events":[{"eventType":"click","eventName":"Product Clicked","index":"products","userToken":"user-123456","timestamp":1641290601962,"objectIDs":["9780545139700","9780439784542"],"queryID":"43b15df305339e827f0ac0bdc5ebcaa7","positions":[7,6]}]}""");
      },
    ),
  );

  // pushEvents
  test(
    'Many events type',
    () => runTest(
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.pushEvents(
        insightsEvents: InsightsEvents(
          events: [
            ConvertedObjectIDsAfterSearch(
              eventType: ConversionEvent.fromJson("conversion"),
              eventName: "Product Purchased",
              index: "products",
              userToken: "user-123456",
              timestamp: 1641290601962,
              objectIDs: [
                "9780545139700",
                "9780439784542",
              ],
              queryID: "43b15df305339e827f0ac0bdc5ebcaa7",
            ),
            ViewedObjectIDs(
              eventType: ViewEvent.fromJson("view"),
              eventName: "Product Detail Page Viewed",
              index: "products",
              userToken: "user-123456",
              timestamp: 1641290601962,
              objectIDs: [
                "9780545139700",
                "9780439784542",
              ],
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/events');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"events":[{"eventType":"conversion","eventName":"Product Purchased","index":"products","userToken":"user-123456","timestamp":1641290601962,"objectIDs":["9780545139700","9780439784542"],"queryID":"43b15df305339e827f0ac0bdc5ebcaa7"},{"eventType":"view","eventName":"Product Detail Page Viewed","index":"products","userToken":"user-123456","timestamp":1641290601962,"objectIDs":["9780545139700","9780439784542"]}]}""");
      },
    ),
  );

  // pushEvents
  test(
    'ConvertedObjectIDsAfterSearch',
    () => runTest(
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.pushEvents(
        insightsEvents: InsightsEvents(
          events: [
            ConvertedObjectIDsAfterSearch(
              eventType: ConversionEvent.fromJson("conversion"),
              eventName: "Product Purchased",
              index: "products",
              userToken: "user-123456",
              timestamp: 1641290601962,
              objectIDs: [
                "9780545139700",
                "9780439784542",
              ],
              queryID: "43b15df305339e827f0ac0bdc5ebcaa7",
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/events');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"events":[{"eventType":"conversion","eventName":"Product Purchased","index":"products","userToken":"user-123456","timestamp":1641290601962,"objectIDs":["9780545139700","9780439784542"],"queryID":"43b15df305339e827f0ac0bdc5ebcaa7"}]}""");
      },
    ),
  );

  // pushEvents
  test(
    'ViewedObjectIDs',
    () => runTest(
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
        options: ClientOptions(requester: requester),
      ),
      call: (client) => client.pushEvents(
        insightsEvents: InsightsEvents(
          events: [
            ViewedObjectIDs(
              eventType: ViewEvent.fromJson("view"),
              eventName: "Product Detail Page Viewed",
              index: "products",
              userToken: "user-123456",
              timestamp: 1641290601962,
              objectIDs: [
                "9780545139700",
                "9780439784542",
              ],
            ),
          ],
        ),
      ),
      intercept: (request) {
        expectPath(request.path, '/1/events');
        expect(request.method, 'post');
        expectBody(request.body,
            """{"events":[{"eventType":"view","eventName":"Product Detail Page Viewed","index":"products","userToken":"user-123456","timestamp":1641290601962,"objectIDs":["9780545139700","9780439784542"]}]}""");
      },
    ),
  );

  // put
  test(
    'allow put method for a custom path with minimal parameters',
    () => runTest(
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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
      builder: (requester) => InsightsClient(
        appId: 'appId',
        apiKey: 'apiKey',
        region: 'us',
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
}
