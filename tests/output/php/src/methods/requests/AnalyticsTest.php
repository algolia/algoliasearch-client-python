<?php

namespace Algolia\AlgoliaSearch\Test\Api;

use Algolia\AlgoliaSearch\Api\AnalyticsClient;
use Algolia\AlgoliaSearch\Configuration\AnalyticsConfig;
use Algolia\AlgoliaSearch\Http\HttpClientInterface;
use Algolia\AlgoliaSearch\Http\Psr7\Response;
use Algolia\AlgoliaSearch\RetryStrategy\ApiWrapper;
use Algolia\AlgoliaSearch\RetryStrategy\ClusterHosts;
use GuzzleHttp\Psr7\Query;
use PHPUnit\Framework\TestCase;
use Psr\Http\Message\RequestInterface;

/**
 * AnalyticsTest.
 *
 * @category Class
 *
 * @internal
 *
 * @coversNothing
 */
class AnalyticsTest extends TestCase implements HttpClientInterface
{
    /**
     * @var RequestInterface[]
     */
    private $recordedRequests = [];

    public function sendRequest(RequestInterface $request, $timeout, $connectTimeout)
    {
        $this->recordedRequests[] = $request;

        return new Response(200, [], '{}');
    }

    /**
     * Test case for Del
     * allow del method for a custom path with minimal parameters.
     */
    public function testDel0()
    {
        $client = $this->getClient();
        $client->del(
            '/test/minimal',
        );

        $this->assertRequests([
            [
                'path' => '/1/test/minimal',
                'method' => 'DELETE',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for Del
     * allow del method for a custom path with all parameters.
     */
    public function testDel1()
    {
        $client = $this->getClient();
        $client->del(
            '/test/all',
            ['query' => 'parameters',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/test/all',
                'method' => 'DELETE',
                'body' => null,
                'queryParameters' => json_decode('{"query":"parameters"}', true),
            ],
        ]);
    }

    /**
     * Test case for Get
     * allow get method for a custom path with minimal parameters.
     */
    public function testGet0()
    {
        $client = $this->getClient();
        $client->get(
            '/test/minimal',
        );

        $this->assertRequests([
            [
                'path' => '/1/test/minimal',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for Get
     * allow get method for a custom path with all parameters.
     */
    public function testGet1()
    {
        $client = $this->getClient();
        $client->get(
            '/test/all',
            ['query' => 'parameters',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/test/all',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"query":"parameters"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetAverageClickPosition
     * get getAverageClickPosition with minimal parameters.
     */
    public function testGetAverageClickPosition0()
    {
        $client = $this->getClient();
        $client->getAverageClickPosition(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/clicks/averageClickPosition',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetAverageClickPosition
     * get getAverageClickPosition with all parameters.
     */
    public function testGetAverageClickPosition1()
    {
        $client = $this->getClient();
        $client->getAverageClickPosition(
            'index',
            '1999-09-19',
            '2001-01-01',
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/clicks/averageClickPosition',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetClickPositions
     * get getClickPositions with minimal parameters.
     */
    public function testGetClickPositions0()
    {
        $client = $this->getClient();
        $client->getClickPositions(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/clicks/positions',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetClickPositions
     * get getClickPositions with all parameters.
     */
    public function testGetClickPositions1()
    {
        $client = $this->getClient();
        $client->getClickPositions(
            'index',
            '1999-09-19',
            '2001-01-01',
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/clicks/positions',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetClickThroughRate
     * get getClickThroughRate with minimal parameters.
     */
    public function testGetClickThroughRate0()
    {
        $client = $this->getClient();
        $client->getClickThroughRate(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/clicks/clickThroughRate',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetClickThroughRate
     * get getClickThroughRate with all parameters.
     */
    public function testGetClickThroughRate1()
    {
        $client = $this->getClient();
        $client->getClickThroughRate(
            'index',
            '1999-09-19',
            '2001-01-01',
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/clicks/clickThroughRate',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetConversationRate
     * get getConversationRate with minimal parameters.
     */
    public function testGetConversationRate0()
    {
        $client = $this->getClient();
        $client->getConversationRate(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/conversions/conversionRate',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetConversationRate
     * get getConversationRate with all parameters.
     */
    public function testGetConversationRate1()
    {
        $client = $this->getClient();
        $client->getConversationRate(
            'index',
            '1999-09-19',
            '2001-01-01',
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/conversions/conversionRate',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetNoClickRate
     * get getNoClickRate with minimal parameters.
     */
    public function testGetNoClickRate0()
    {
        $client = $this->getClient();
        $client->getNoClickRate(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/searches/noClickRate',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetNoClickRate
     * get getNoClickRate with all parameters.
     */
    public function testGetNoClickRate1()
    {
        $client = $this->getClient();
        $client->getNoClickRate(
            'index',
            '1999-09-19',
            '2001-01-01',
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/searches/noClickRate',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetNoResultsRate
     * get getNoResultsRate with minimal parameters.
     */
    public function testGetNoResultsRate0()
    {
        $client = $this->getClient();
        $client->getNoResultsRate(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/searches/noResultRate',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetNoResultsRate
     * get getNoResultsRate with all parameters.
     */
    public function testGetNoResultsRate1()
    {
        $client = $this->getClient();
        $client->getNoResultsRate(
            'index',
            '1999-09-19',
            '2001-01-01',
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/searches/noResultRate',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetSearchesCount
     * get getSearchesCount with minimal parameters.
     */
    public function testGetSearchesCount0()
    {
        $client = $this->getClient();
        $client->getSearchesCount(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/searches/count',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetSearchesCount
     * get getSearchesCount with all parameters.
     */
    public function testGetSearchesCount1()
    {
        $client = $this->getClient();
        $client->getSearchesCount(
            'index',
            '1999-09-19',
            '2001-01-01',
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/searches/count',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetSearchesNoClicks
     * get getSearchesNoClicks with minimal parameters.
     */
    public function testGetSearchesNoClicks0()
    {
        $client = $this->getClient();
        $client->getSearchesNoClicks(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/searches/noClicks',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetSearchesNoClicks
     * get getSearchesNoClicks with all parameters.
     */
    public function testGetSearchesNoClicks1()
    {
        $client = $this->getClient();
        $client->getSearchesNoClicks(
            'index',
            '1999-09-19',
            '2001-01-01',
            21,
            42,
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/searches/noClicks',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetSearchesNoResults
     * get getSearchesNoResults with minimal parameters.
     */
    public function testGetSearchesNoResults0()
    {
        $client = $this->getClient();
        $client->getSearchesNoResults(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/searches/noResults',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetSearchesNoResults
     * get getSearchesNoResults with all parameters.
     */
    public function testGetSearchesNoResults1()
    {
        $client = $this->getClient();
        $client->getSearchesNoResults(
            'index',
            '1999-09-19',
            '2001-01-01',
            21,
            42,
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/searches/noResults',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetStatus
     * get getStatus with minimal parameters.
     */
    public function testGetStatus0()
    {
        $client = $this->getClient();
        $client->getStatus(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/status',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetTopCountries
     * get getTopCountries with minimal parameters.
     */
    public function testGetTopCountries0()
    {
        $client = $this->getClient();
        $client->getTopCountries(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/countries',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetTopCountries
     * get getTopCountries with all parameters.
     */
    public function testGetTopCountries1()
    {
        $client = $this->getClient();
        $client->getTopCountries(
            'index',
            '1999-09-19',
            '2001-01-01',
            21,
            42,
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/countries',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetTopFilterAttributes
     * get getTopFilterAttributes with minimal parameters.
     */
    public function testGetTopFilterAttributes0()
    {
        $client = $this->getClient();
        $client->getTopFilterAttributes(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/filters',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetTopFilterAttributes
     * get getTopFilterAttributes with all parameters.
     */
    public function testGetTopFilterAttributes1()
    {
        $client = $this->getClient();
        $client->getTopFilterAttributes(
            'index',
            'mySearch',
            '1999-09-19',
            '2001-01-01',
            21,
            42,
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/filters',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetTopFilterForAttribute
     * get getTopFilterForAttribute with minimal parameters.
     */
    public function testGetTopFilterForAttribute0()
    {
        $client = $this->getClient();
        $client->getTopFilterForAttribute(
            'myAttribute',
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/filters/myAttribute',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetTopFilterForAttribute
     * get getTopFilterForAttribute with minimal parameters and multiple attributes.
     */
    public function testGetTopFilterForAttribute1()
    {
        $client = $this->getClient();
        $client->getTopFilterForAttribute(
            'myAttribute1,myAttribute2',
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/filters/myAttribute1%2CmyAttribute2',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetTopFilterForAttribute
     * get getTopFilterForAttribute with all parameters.
     */
    public function testGetTopFilterForAttribute2()
    {
        $client = $this->getClient();
        $client->getTopFilterForAttribute(
            'myAttribute',
            'index',
            'mySearch',
            '1999-09-19',
            '2001-01-01',
            21,
            42,
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/filters/myAttribute',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetTopFilterForAttribute
     * get getTopFilterForAttribute with all parameters and multiple attributes.
     */
    public function testGetTopFilterForAttribute3()
    {
        $client = $this->getClient();
        $client->getTopFilterForAttribute(
            'myAttribute1,myAttribute2',
            'index',
            'mySearch',
            '1999-09-19',
            '2001-01-01',
            21,
            42,
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/filters/myAttribute1%2CmyAttribute2',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetTopFiltersNoResults
     * get getTopFiltersNoResults with minimal parameters.
     */
    public function testGetTopFiltersNoResults0()
    {
        $client = $this->getClient();
        $client->getTopFiltersNoResults(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/filters/noResults',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetTopFiltersNoResults
     * get getTopFiltersNoResults with all parameters.
     */
    public function testGetTopFiltersNoResults1()
    {
        $client = $this->getClient();
        $client->getTopFiltersNoResults(
            'index',
            'mySearch',
            '1999-09-19',
            '2001-01-01',
            21,
            42,
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/filters/noResults',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","search":"mySearch","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetTopHits
     * get getTopHits with minimal parameters.
     */
    public function testGetTopHits0()
    {
        $client = $this->getClient();
        $client->getTopHits(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/hits',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetTopHits
     * get getTopHits with all parameters.
     */
    public function testGetTopHits1()
    {
        $client = $this->getClient();
        $client->getTopHits(
            'index',
            'mySearch',
            true,
            '1999-09-19',
            '2001-01-01',
            21,
            42,
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/hits',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","search":"mySearch","clickAnalytics":"true","startDate":"1999-09-19","endDate":"2001-01-01","limit":"21","offset":"42","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetTopSearches
     * get getTopSearches with minimal parameters.
     */
    public function testGetTopSearches0()
    {
        $client = $this->getClient();
        $client->getTopSearches(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/searches',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetTopSearches
     * get getTopSearches with all parameters.
     */
    public function testGetTopSearches1()
    {
        $client = $this->getClient();
        $client->getTopSearches(
            'index',
            true,
            '1999-09-19',
            '2001-01-01',
            'searchCount',
            'asc',
            21,
            42,
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/searches',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","clickAnalytics":"true","startDate":"1999-09-19","endDate":"2001-01-01","orderBy":"searchCount","direction":"asc","limit":"21","offset":"42","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetUsersCount
     * get getUsersCount with minimal parameters.
     */
    public function testGetUsersCount0()
    {
        $client = $this->getClient();
        $client->getUsersCount(
            'index',
        );

        $this->assertRequests([
            [
                'path' => '/2/users/count',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetUsersCount
     * get getUsersCount with all parameters.
     */
    public function testGetUsersCount1()
    {
        $client = $this->getClient();
        $client->getUsersCount(
            'index',
            '1999-09-19',
            '2001-01-01',
            'tag',
        );

        $this->assertRequests([
            [
                'path' => '/2/users/count',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"index":"index","startDate":"1999-09-19","endDate":"2001-01-01","tags":"tag"}', true),
            ],
        ]);
    }

    /**
     * Test case for Post
     * allow post method for a custom path with minimal parameters.
     */
    public function testPost0()
    {
        $client = $this->getClient();
        $client->post(
            '/test/minimal',
        );

        $this->assertRequests([
            [
                'path' => '/1/test/minimal',
                'method' => 'POST',
                'body' => json_decode('{}'),
            ],
        ]);
    }

    /**
     * Test case for Post
     * allow post method for a custom path with all parameters.
     */
    public function testPost1()
    {
        $client = $this->getClient();
        $client->post(
            '/test/all',
            ['query' => 'parameters',
            ],
            ['body' => 'parameters',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/test/all',
                'method' => 'POST',
                'body' => json_decode('{"body":"parameters"}'),
                'queryParameters' => json_decode('{"query":"parameters"}', true),
            ],
        ]);
    }

    /**
     * Test case for Post
     * requestOptions can override default query parameters.
     */
    public function testPost2()
    {
        $client = $this->getClient();
        $requestOptions = [
            'queryParameters' => [
                'query' => 'myQueryParameter',
            ],
            'headers' => [
            ],
        ];
        $client->post(
            '/test/requestOptions',
            ['query' => 'parameters',
            ],
            ['facet' => 'filters',
            ],
            $requestOptions
        );

        $this->assertRequests([
            [
                'path' => '/1/test/requestOptions',
                'method' => 'POST',
                'body' => json_decode('{"facet":"filters"}'),
                'queryParameters' => json_decode('{"query":"myQueryParameter"}', true),
            ],
        ]);
    }

    /**
     * Test case for Post
     * requestOptions merges query parameters with default ones.
     */
    public function testPost3()
    {
        $client = $this->getClient();
        $requestOptions = [
            'queryParameters' => [
                'query2' => 'myQueryParameter',
            ],
            'headers' => [
            ],
        ];
        $client->post(
            '/test/requestOptions',
            ['query' => 'parameters',
            ],
            ['facet' => 'filters',
            ],
            $requestOptions
        );

        $this->assertRequests([
            [
                'path' => '/1/test/requestOptions',
                'method' => 'POST',
                'body' => json_decode('{"facet":"filters"}'),
                'queryParameters' => json_decode('{"query":"parameters","query2":"myQueryParameter"}', true),
            ],
        ]);
    }

    /**
     * Test case for Post
     * requestOptions can override default headers.
     */
    public function testPost4()
    {
        $client = $this->getClient();
        $requestOptions = [
            'queryParameters' => [
            ],
            'headers' => [
                'x-algolia-api-key' => 'myApiKey',
            ],
        ];
        $client->post(
            '/test/requestOptions',
            ['query' => 'parameters',
            ],
            ['facet' => 'filters',
            ],
            $requestOptions
        );

        $this->assertRequests([
            [
                'path' => '/1/test/requestOptions',
                'method' => 'POST',
                'body' => json_decode('{"facet":"filters"}'),
                'queryParameters' => json_decode('{"query":"parameters"}', true),
                'headers' => json_decode('{"x-algolia-api-key":"myApiKey"}', true),
            ],
        ]);
    }

    /**
     * Test case for Post
     * requestOptions merges headers with default ones.
     */
    public function testPost5()
    {
        $client = $this->getClient();
        $requestOptions = [
            'queryParameters' => [
            ],
            'headers' => [
                'x-algolia-api-key' => 'myApiKey',
            ],
        ];
        $client->post(
            '/test/requestOptions',
            ['query' => 'parameters',
            ],
            ['facet' => 'filters',
            ],
            $requestOptions
        );

        $this->assertRequests([
            [
                'path' => '/1/test/requestOptions',
                'method' => 'POST',
                'body' => json_decode('{"facet":"filters"}'),
                'queryParameters' => json_decode('{"query":"parameters"}', true),
                'headers' => json_decode('{"x-algolia-api-key":"myApiKey"}', true),
            ],
        ]);
    }

    /**
     * Test case for Post
     * requestOptions queryParameters accepts booleans.
     */
    public function testPost6()
    {
        $client = $this->getClient();
        $requestOptions = [
            'queryParameters' => [
                'isItWorking' => true,
            ],
            'headers' => [
            ],
        ];
        $client->post(
            '/test/requestOptions',
            ['query' => 'parameters',
            ],
            ['facet' => 'filters',
            ],
            $requestOptions
        );

        $this->assertRequests([
            [
                'path' => '/1/test/requestOptions',
                'method' => 'POST',
                'body' => json_decode('{"facet":"filters"}'),
                'queryParameters' => json_decode('{"query":"parameters","isItWorking":"true"}', true),
            ],
        ]);
    }

    /**
     * Test case for Post
     * requestOptions queryParameters accepts integers.
     */
    public function testPost7()
    {
        $client = $this->getClient();
        $requestOptions = [
            'queryParameters' => [
                'myParam' => 2,
            ],
            'headers' => [
            ],
        ];
        $client->post(
            '/test/requestOptions',
            ['query' => 'parameters',
            ],
            ['facet' => 'filters',
            ],
            $requestOptions
        );

        $this->assertRequests([
            [
                'path' => '/1/test/requestOptions',
                'method' => 'POST',
                'body' => json_decode('{"facet":"filters"}'),
                'queryParameters' => json_decode('{"query":"parameters","myParam":"2"}', true),
            ],
        ]);
    }

    /**
     * Test case for Post
     * requestOptions queryParameters accepts list of string.
     */
    public function testPost8()
    {
        $client = $this->getClient();
        $requestOptions = [
            'queryParameters' => [
                'myParam' => ['c', 'd',
                ],
            ],
            'headers' => [
            ],
        ];
        $client->post(
            '/test/requestOptions',
            ['query' => 'parameters',
            ],
            ['facet' => 'filters',
            ],
            $requestOptions
        );

        $this->assertRequests([
            [
                'path' => '/1/test/requestOptions',
                'method' => 'POST',
                'body' => json_decode('{"facet":"filters"}'),
                'queryParameters' => json_decode('{"query":"parameters","myParam":"c,d"}', true),
            ],
        ]);
    }

    /**
     * Test case for Post
     * requestOptions queryParameters accepts list of booleans.
     */
    public function testPost9()
    {
        $client = $this->getClient();
        $requestOptions = [
            'queryParameters' => [
                'myParam' => [true, true, false,
                ],
            ],
            'headers' => [
            ],
        ];
        $client->post(
            '/test/requestOptions',
            ['query' => 'parameters',
            ],
            ['facet' => 'filters',
            ],
            $requestOptions
        );

        $this->assertRequests([
            [
                'path' => '/1/test/requestOptions',
                'method' => 'POST',
                'body' => json_decode('{"facet":"filters"}'),
                'queryParameters' => json_decode('{"query":"parameters","myParam":"true,true,false"}', true),
            ],
        ]);
    }

    /**
     * Test case for Post
     * requestOptions queryParameters accepts list of integers.
     */
    public function testPost10()
    {
        $client = $this->getClient();
        $requestOptions = [
            'queryParameters' => [
                'myParam' => [1, 2,
                ],
            ],
            'headers' => [
            ],
        ];
        $client->post(
            '/test/requestOptions',
            ['query' => 'parameters',
            ],
            ['facet' => 'filters',
            ],
            $requestOptions
        );

        $this->assertRequests([
            [
                'path' => '/1/test/requestOptions',
                'method' => 'POST',
                'body' => json_decode('{"facet":"filters"}'),
                'queryParameters' => json_decode('{"query":"parameters","myParam":"1,2"}', true),
            ],
        ]);
    }

    /**
     * Test case for Put
     * allow put method for a custom path with minimal parameters.
     */
    public function testPut0()
    {
        $client = $this->getClient();
        $client->put(
            '/test/minimal',
        );

        $this->assertRequests([
            [
                'path' => '/1/test/minimal',
                'method' => 'PUT',
                'body' => json_decode('{}'),
            ],
        ]);
    }

    /**
     * Test case for Put
     * allow put method for a custom path with all parameters.
     */
    public function testPut1()
    {
        $client = $this->getClient();
        $client->put(
            '/test/all',
            ['query' => 'parameters',
            ],
            ['body' => 'parameters',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/test/all',
                'method' => 'PUT',
                'body' => json_decode('{"body":"parameters"}'),
                'queryParameters' => json_decode('{"query":"parameters"}', true),
            ],
        ]);
    }

    protected function assertRequests(array $requests)
    {
        $this->assertGreaterThan(0, count($requests));
        $this->assertEquals(count($requests), count($this->recordedRequests));

        foreach ($requests as $i => $request) {
            $recordedRequest = $this->recordedRequests[$i];

            $this->assertEquals($request['method'], $recordedRequest->getMethod());

            $this->assertEquals($request['path'], $recordedRequest->getUri()->getPath());

            if (isset($request['body'])) {
                $this->assertEquals(
                    json_encode($request['body']),
                    $recordedRequest->getBody()->getContents()
                );
            }

            if (isset($request['queryParameters'])) {
                $this->assertEquals(
                    Query::build($request['queryParameters']),
                    $recordedRequest->getUri()->getQuery()
                );
            }

            if (isset($request['headers'])) {
                foreach ($request['headers'] as $key => $value) {
                    $this->assertArrayHasKey(
                        $key,
                        $recordedRequest->getHeaders()
                    );
                    $this->assertEquals(
                        $recordedRequest->getHeaderLine($key),
                        $value
                    );
                }
            }
        }
    }

    protected function getClient()
    {
        $api = new ApiWrapper($this, AnalyticsConfig::create(getenv('ALGOLIA_APP_ID'), getenv('ALGOLIA_API_KEY')), ClusterHosts::create('127.0.0.1'));
        $config = AnalyticsConfig::create('foo', 'bar');

        return new AnalyticsClient($api, $config);
    }
}
