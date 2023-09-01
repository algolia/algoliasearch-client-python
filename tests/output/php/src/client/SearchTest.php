<?php

namespace Algolia\AlgoliaSearch\Test\Client;

use Algolia\AlgoliaSearch\Api\SearchClient;
use Algolia\AlgoliaSearch\Configuration\SearchConfig;
use Algolia\AlgoliaSearch\Http\HttpClientInterface;
use Algolia\AlgoliaSearch\Http\Psr7\Response;
use Algolia\AlgoliaSearch\RetryStrategy\ApiWrapper;
use Algolia\AlgoliaSearch\RetryStrategy\ClusterHosts;
use PHPUnit\Framework\TestCase;
use Psr\Http\Message\RequestInterface;

/**
 * Client tests for SearchClient.
 *
 * @internal
 *
 * @coversNothing
 */
class SearchTest extends TestCase implements HttpClientInterface
{
    public const APP_ID = 'test-app-id';
    public const API_KEY = 'test-api-key';

    /**
     * @var RequestInterface
     */
    private $recordedRequest;

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
     * Test case : calls api with correct read host.
     */
    public function test0api()
    {
        $client = $this->createClient(
            'test-app-id',
            'test-api-key',
            null
        );

        // Make sure everything went fine without errors
        $this->assertIsObject($client);
        $client->get(
            '/test',
        );

        $this->assertEquals(
            'test-app-id-dsn.algolia.net',
            $this->recordedRequest['request']->getUri()->getHost()
        );
    }

    /**
     * Test case : calls api with correct write host.
     */
    public function test1api()
    {
        $client = $this->createClient(
            'test-app-id',
            'test-api-key',
            null
        );

        // Make sure everything went fine without errors
        $this->assertIsObject($client);
        $client->post(
            '/test',
        );

        $this->assertEquals(
            'test-app-id.algolia.net',
            $this->recordedRequest['request']->getUri()->getHost()
        );
    }

    /**
     * Test case : calls api with correct user agent.
     */
    public function test0commonApi()
    {
        $client = $this->createClient(self::APP_ID, self::API_KEY);
        $client->post(
            '/test',
        );

        $this->assertTrue(
            (bool) preg_match(
                '/^Algolia for PHP \\(\\d+\\.\\d+\\.\\d+(-.*)?\\)(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*(; Search (\\(\\d+\\.\\d+\\.\\d+(-.*)?\\)))(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*$/',
                $this->recordedRequest['request']->getHeader('User-Agent')[0]
            )
        );
    }

    /**
     * Test case : calls api with default read timeouts.
     */
    public function test1commonApi()
    {
        $client = $this->createClient(self::APP_ID, self::API_KEY);
        $client->get(
            '/test',
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
     * Test case : calls api with default write timeouts.
     */
    public function test2commonApi()
    {
        $client = $this->createClient(self::APP_ID, self::API_KEY);
        $client->post(
            '/test',
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
     * Test case : client throws with invalid parameters.
     */
    public function test0parameters()
    {
        try {
            $client = $this->createClient(
                null,
                null,
                null
            );
        } catch (\Exception $e) {
            $this->assertEquals($e->getMessage(), '`appId` is missing.');
        }

        try {
            $client = $this->createClient(
                null,
                'my-api-key',
                null
            );
        } catch (\Exception $e) {
            $this->assertEquals($e->getMessage(), '`appId` is missing.');
        }

        try {
            $client = $this->createClient(
                'my-app-id',
                null,
                null
            );
        } catch (\Exception $e) {
            $this->assertEquals($e->getMessage(), '`apiKey` is missing.');
        }
    }

    /**
     * Test case : `addApiKey` throws with invalid parameters.
     */
    public function test1parameters()
    {
        $client = $this->createClient(self::APP_ID, self::API_KEY);

        try {
            $client->addApiKey(
                null,
            );
        } catch (\Exception $e) {
            $this->assertEquals($e->getMessage(), 'Parameter `apiKey` is required when calling `addApiKey`.');
        }
    }

    /**
     * Test case : `addOrUpdateObject` throws with invalid parameters.
     */
    public function test2parameters()
    {
        $client = $this->createClient(self::APP_ID, self::API_KEY);

        try {
            $client->addOrUpdateObject(
                null,
                'my-object-id',
                [],
            );
        } catch (\Exception $e) {
            $this->assertEquals($e->getMessage(), 'Parameter `indexName` is required when calling `addOrUpdateObject`.');
        }

        try {
            $client->addOrUpdateObject(
                'my-index-name',
                null,
                [],
            );
        } catch (\Exception $e) {
            $this->assertEquals($e->getMessage(), 'Parameter `objectID` is required when calling `addOrUpdateObject`.');
        }

        try {
            $client->addOrUpdateObject(
                'my-index-name',
                'my-object-id',
                null,
            );
        } catch (\Exception $e) {
            $this->assertEquals($e->getMessage(), 'Parameter `body` is required when calling `addOrUpdateObject`.');
        }
    }

    /**
     * @param mixed $appId
     * @param mixed $apiKey
     * @param mixed $region
     *
     * @return SearchClient
     */
    private function createClient($appId, $apiKey, $region = '')
    {
        $config = SearchConfig::create($appId, $apiKey);
        $clusterHosts = ClusterHosts::createFromAppId($appId);
        $api = new ApiWrapper($this, $config, $clusterHosts);

        return new SearchClient($api, $config);
    }
}
