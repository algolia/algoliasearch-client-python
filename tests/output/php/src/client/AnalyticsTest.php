<?php

namespace Algolia\AlgoliaSearch\Test\Client;

use Algolia\AlgoliaSearch\Api\AnalyticsClient;
use Algolia\AlgoliaSearch\Configuration\AnalyticsConfig;
use Algolia\AlgoliaSearch\Http\HttpClientInterface;
use Algolia\AlgoliaSearch\Http\Psr7\Response;
use Algolia\AlgoliaSearch\RetryStrategy\ApiWrapper;
use Algolia\AlgoliaSearch\RetryStrategy\ClusterHosts;
use PHPUnit\Framework\TestCase;
use Psr\Http\Message\RequestInterface;

/**
 * Client tests for AnalyticsClient
 */
class AnalyticsTest extends TestCase implements HttpClientInterface
{
    public const APP_ID = 'test-app-id';
    public const API_KEY = 'test-api-key';

    /**
     * @var RequestInterface
     */
    private $recordedRequest;

    /**
     * @return AnalyticsClient
     */
    private function createClient($appId, $apiKey, $region = 'us')
    {
        $config = AnalyticsConfig::create(
            $appId,
            $apiKey,
            $region
        );
        $clusterHosts = AnalyticsClient::getClusterHosts($config);
        $api = new ApiWrapper($this, $config, $clusterHosts);

        return new AnalyticsClient($api, $config);
    }

    public function sendRequest(RequestInterface $request, $timeout, $connectTimeout)
    {
        $this->recordedRequest = [
            'request' => $request,
            'responseTimeout' => $timeout * 1000,
            'connectTimeout' => $connectTimeout * 1000,
        ];

        return new Response(200, [], '{}');
    }

    /**
    * Test case : calls api with correct user agent
    */
    public function test0commonApi()
    {
        $client = $this->createClient(self::APP_ID, self::API_KEY);
        $client->post(
            "/test",
        );

        $this->assertTrue(
            (bool) preg_match(
                '/^Algolia for PHP \\(\\d+\\.\\d+\\.\\d+(-.*)?\\)(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*(; Analytics (\\(\\d+\\.\\d+\\.\\d+(-.*)?\\)))(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*$/',
                $this->recordedRequest['request']->getHeader('User-Agent')[0]
            )
        );
    }

    /**
    * Test case : calls api with default read timeouts
    */
    public function test1commonApi()
    {
        $client = $this->createClient(self::APP_ID, self::API_KEY);
        $client->get(
            "/test",
        );

        $this->assertEquals(
            2000,
            $this->recordedRequest['connectTimeout']
        );

        $this->assertEquals(
            5000,
            $this->recordedRequest['responseTimeout']
        );
    }

    /**
    * Test case : calls api with default write timeouts
    */
    public function test2commonApi()
    {
        $client = $this->createClient(self::APP_ID, self::API_KEY);
        $client->post(
            "/test",
        );

        $this->assertEquals(
            2000,
            $this->recordedRequest['connectTimeout']
        );

        $this->assertEquals(
            30000,
            $this->recordedRequest['responseTimeout']
        );
    }

    /**
    * Test case : fallbacks to the alias when region is not given
    */
    public function test0parameters()
    {
        $client = $this->createClient(
            "my-app-id",
            "my-api-key",
            null
        );

        // Make sure everything went fine without errors
        $this->assertIsObject($client);
        $client->getAverageClickPosition(
            "my-index",
        );

        $this->assertEquals(
            'analytics.algolia.com',
            $this->recordedRequest['request']->getUri()->getHost()
        );
    }

    /**
    * Test case : uses the correct region
    */
    public function test1parameters()
    {
        $client = $this->createClient(
            "my-app-id",
            "my-api-key",
            "de"
        );

        // Make sure everything went fine without errors
        $this->assertIsObject($client);
        $client->post(
            "/test",
        );

        $this->assertEquals(
            'analytics.de.algolia.com',
            $this->recordedRequest['request']->getUri()->getHost()
        );
    }

    /**
    * Test case : throws when incorrect region is given
    */
    public function test2parameters()
    {
        try {
            $client = $this->createClient(
                "my-app-id",
                "my-api-key",
                "not_a_region"
            );

        } catch (\Exception $e) {
            $this->assertEquals($e->getMessage(), '`region` must be one of the following: de, us');
        }
    }

    /**
    * Test case : getAverageClickPosition throws without index
    */
    public function test3parameters()
    {
        $client = $this->createClient(self::APP_ID, self::API_KEY);
        try {
            $client->getClickPositions(
                null,
            );

        } catch (\Exception $e) {
            $this->assertEquals($e->getMessage(), 'Parameter `index` is required when calling `getClickPositions`.');
        }
    }

}
