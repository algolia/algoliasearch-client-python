import 'package:algoliasearch/algoliasearch_lite.dart';
import 'package:algolia_test/algolia_test.dart';
import 'package:test/test.dart';

void main() {
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
                47.3165,
                4.9665,
              ],
              insidePolygon: [
                47.3165,
                4.9665,
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
            """{"requests":[{"advancedSyntax":true,"advancedSyntaxFeatures":["exactPhrase"],"allowTyposOnNumericTokens":true,"alternativesAsExact":["multiWordsSynonym"],"analytics":true,"analyticsTags":[""],"aroundLatLng":"","aroundLatLngViaIP":true,"aroundPrecision":0,"aroundRadius":"all","attributeCriteriaComputedByMinProximity":true,"attributesForFaceting":[""],"attributesToHighlight":[""],"attributesToRetrieve":[""],"attributesToSnippet":[""],"clickAnalytics":true,"customRanking":[""],"decompoundQuery":true,"disableExactOnAttributes":[""],"disableTypoToleranceOnAttributes":[""],"distinct":0,"enableABTest":true,"enablePersonalization":true,"enableReRanking":true,"enableRules":true,"exactOnSingleWordQuery":"attribute","explain":["foo","bar"],"facetFilters":[""],"facetingAfterDistinct":true,"facets":[""],"filters":"","getRankingInfo":true,"highlightPostTag":"","highlightPreTag":"","hitsPerPage":0,"ignorePlurals":false,"indexName":"theIndexName","insideBoundingBox":[47.3165,4.9665],"insidePolygon":[47.3165,4.9665],"keepDiacriticsOnCharacters":"","length":0,"maxValuesPerFacet":0,"minProximity":0,"minWordSizefor1Typo":0,"minWordSizefor2Typos":0,"minimumAroundRadius":0,"naturalLanguages":[""],"numericFilters":[""],"offset":0,"optionalFilters":[""],"optionalWords":[""],"page":0,"percentileComputation":true,"personalizationImpact":0,"query":"","queryLanguages":[""],"queryType":"prefixAll","ranking":[""],"reRankingApplyFilter":[""],"relevancyStrictness":0,"removeStopWords":true,"removeWordsIfNoResults":"allOptional","renderingContent":{"facetOrdering":{"facets":{"order":["a","b"]},"values":{"a":{"order":["b"],"sortRemainingBy":"count"}}}},"replaceSynonymsInHighlight":true,"responseFields":[""],"restrictHighlightAndSnippetArrays":true,"restrictSearchableAttributes":[""],"ruleContexts":[""],"similarQuery":"","snippetEllipsisText":"","sortFacetValuesBy":"","sumOrFiltersScores":true,"synonyms":true,"tagFilters":[""],"type":"default","typoTolerance":"min","userToken":""}]}""");
      },
    ),
  );
}
