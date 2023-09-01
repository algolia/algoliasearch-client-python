<?php

namespace Algolia\AlgoliaSearch\Test\Client;

use Algolia\AlgoliaSearch\Api\PersonalizationClient;
use Algolia\AlgoliaSearch\Configuration\PersonalizationConfig;
use Algolia\AlgoliaSearch\Http\HttpClientInterface;
use Algolia\AlgoliaSearch\Http\Psr7\Response;
use Algolia\AlgoliaSearch\RetryStrategy\ApiWrapper;
use PHPUnit\Framework\TestCase;
use Psr\Http\Message\RequestInterface;

/**
 * Client tests for PersonalizationClient.
 *
 * @internal
 *
 * @coversNothing
 */
class PersonalizationTest extends TestCase implements HttpClientInterface
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
                '/^Algolia for PHP \\(\\d+\\.\\d+\\.\\d+(-.*)?\\)(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*(; Personalization (\\(\\d+\\.\\d+\\.\\d+(-.*)?\\)))(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*$/',
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
     * Test case : throws when region is not given.
     */
    public function test0parameters()
    {
        try {
            $client = $this->createClient(
                'my-app-id',
                'my-api-key',
                ''
            );
        } catch (\Exception $e) {
            $this->assertEquals($e->getMessage(), '`region` is required and must be one of the following: eu, us');
        }
    }

    /**
     * Test case : throws when incorrect region is given.
     */
    public function test1parameters()
    {
        try {
            $client = $this->createClient(
                'my-app-id',
                'my-api-key',
                'not_a_region'
            );
        } catch (\Exception $e) {
            $this->assertEquals($e->getMessage(), '`region` is required and must be one of the following: eu, us');
        }
    }

    /**
     * Test case : does not throw when region is given.
     */
    public function test2parameters()
    {
        $client = $this->createClient(
            'my-app-id',
            'my-api-key',
            'us'
        );

        // Make sure everything went fine without errors
        $this->assertIsObject($client);
    }

    /**
     * @param mixed $appId
     * @param mixed $apiKey
     * @param mixed $region
     *
     * @return PersonalizationClient
     */
    private function createClient($appId, $apiKey, $region = 'us')
    {
        $config = PersonalizationConfig::create(
            $appId,
            $apiKey,
            $region
        );
        $clusterHosts = PersonalizationClient::getClusterHosts($config);
        $api = new ApiWrapper($this, $config, $clusterHosts);

        return new PersonalizationClient($api, $config);
    }
}
