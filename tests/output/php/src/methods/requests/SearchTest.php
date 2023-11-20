<?php

namespace Algolia\AlgoliaSearch\Test\Api;

use Algolia\AlgoliaSearch\Api\SearchClient;
use Algolia\AlgoliaSearch\Configuration\SearchConfig;
use Algolia\AlgoliaSearch\Http\HttpClientInterface;
use Algolia\AlgoliaSearch\Http\Psr7\Response;
use Algolia\AlgoliaSearch\RetryStrategy\ApiWrapper;
use Algolia\AlgoliaSearch\RetryStrategy\ClusterHosts;
use GuzzleHttp\Psr7\Query;
use PHPUnit\Framework\TestCase;
use Psr\Http\Message\RequestInterface;

/**
 * SearchTest.
 *
 * @category Class
 *
 * @internal
 *
 * @coversNothing
 */
class SearchTest extends TestCase implements HttpClientInterface
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
     * Test case for AddApiKey
     * addApiKey.
     */
    public function testAddApiKey0()
    {
        $client = $this->getClient();
        $client->addApiKey(
            ['acl' => [
                'search',

                'addObject',
            ],
                'description' => 'my new api key',
                'validity' => 300,
                'maxQueriesPerIPPerHour' => 100,
                'maxHitsPerQuery' => 20,
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/keys',
                'method' => 'POST',
                'body' => json_decode('{"acl":["search","addObject"],"description":"my new api key","validity":300,"maxQueriesPerIPPerHour":100,"maxHitsPerQuery":20}'),
            ],
        ]);
    }

    /**
     * Test case for AddOrUpdateObject
     * addOrUpdateObject.
     */
    public function testAddOrUpdateObject0()
    {
        $client = $this->getClient();
        $client->addOrUpdateObject(
            'indexName',
            'uniqueID',
            ['key' => 'value',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/uniqueID',
                'method' => 'PUT',
                'body' => json_decode('{"key":"value"}'),
            ],
        ]);
    }

    /**
     * Test case for AppendSource
     * appendSource.
     */
    public function testAppendSource0()
    {
        $client = $this->getClient();
        $client->appendSource(
            ['source' => 'theSource',
                'description' => 'theDescription',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/security/sources/append',
                'method' => 'POST',
                'body' => json_decode('{"source":"theSource","description":"theDescription"}'),
            ],
        ]);
    }

    /**
     * Test case for AssignUserId
     * assignUserId.
     */
    public function testAssignUserId0()
    {
        $client = $this->getClient();
        $client->assignUserId(
            'userID',
            ['cluster' => 'theCluster',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/clusters/mapping',
                'method' => 'POST',
                'body' => json_decode('{"cluster":"theCluster"}'),
                'headers' => json_decode('{"x-algolia-user-id":"userID"}', true),
            ],
        ]);
    }

    /**
     * Test case for Batch
     * allows batch method with `addObject` action.
     */
    public function testBatch0()
    {
        $client = $this->getClient();
        $client->batch(
            'theIndexName',
            ['requests' => [
                ['action' => 'addObject',
                    'body' => ['key' => 'value',
                    ],
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/batch',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"action":"addObject","body":{"key":"value"}}]}'),
            ],
        ]);
    }

    /**
     * Test case for Batch
     * allows batch method with `clear` action.
     */
    public function testBatch1()
    {
        $client = $this->getClient();
        $client->batch(
            'theIndexName',
            ['requests' => [
                ['action' => 'clear',
                    'body' => ['key' => 'value',
                    ],
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/batch',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"action":"clear","body":{"key":"value"}}]}'),
            ],
        ]);
    }

    /**
     * Test case for Batch
     * allows batch method with `delete` action.
     */
    public function testBatch2()
    {
        $client = $this->getClient();
        $client->batch(
            'theIndexName',
            ['requests' => [
                ['action' => 'delete',
                    'body' => ['key' => 'value',
                    ],
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/batch',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"action":"delete","body":{"key":"value"}}]}'),
            ],
        ]);
    }

    /**
     * Test case for Batch
     * allows batch method with `deleteObject` action.
     */
    public function testBatch3()
    {
        $client = $this->getClient();
        $client->batch(
            'theIndexName',
            ['requests' => [
                ['action' => 'deleteObject',
                    'body' => ['key' => 'value',
                    ],
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/batch',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"action":"deleteObject","body":{"key":"value"}}]}'),
            ],
        ]);
    }

    /**
     * Test case for Batch
     * allows batch method with `partialUpdateObject` action.
     */
    public function testBatch4()
    {
        $client = $this->getClient();
        $client->batch(
            'theIndexName',
            ['requests' => [
                ['action' => 'partialUpdateObject',
                    'body' => ['key' => 'value',
                    ],
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/batch',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"action":"partialUpdateObject","body":{"key":"value"}}]}'),
            ],
        ]);
    }

    /**
     * Test case for Batch
     * allows batch method with `partialUpdateObjectNoCreate` action.
     */
    public function testBatch5()
    {
        $client = $this->getClient();
        $client->batch(
            'theIndexName',
            ['requests' => [
                ['action' => 'partialUpdateObjectNoCreate',
                    'body' => ['key' => 'value',
                    ],
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/batch',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"action":"partialUpdateObjectNoCreate","body":{"key":"value"}}]}'),
            ],
        ]);
    }

    /**
     * Test case for Batch
     * allows batch method with `updateObject` action.
     */
    public function testBatch6()
    {
        $client = $this->getClient();
        $client->batch(
            'theIndexName',
            ['requests' => [
                ['action' => 'updateObject',
                    'body' => ['key' => 'value',
                    ],
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/batch',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"action":"updateObject","body":{"key":"value"}}]}'),
            ],
        ]);
    }

    /**
     * Test case for BatchAssignUserIds
     * batchAssignUserIds.
     */
    public function testBatchAssignUserIds0()
    {
        $client = $this->getClient();
        $client->batchAssignUserIds(
            'userID',
            ['cluster' => 'theCluster',
                'users' => [
                    'user1',

                    'user2',
                ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/clusters/mapping/batch',
                'method' => 'POST',
                'body' => json_decode('{"cluster":"theCluster","users":["user1","user2"]}'),
                'headers' => json_decode('{"x-algolia-user-id":"userID"}', true),
            ],
        ]);
    }

    /**
     * Test case for BatchDictionaryEntries
     * get batchDictionaryEntries results with minimal parameters.
     */
    public function testBatchDictionaryEntries0()
    {
        $client = $this->getClient();
        $client->batchDictionaryEntries(
            'compounds',
            ['requests' => [
                ['action' => 'addEntry',
                    'body' => ['objectID' => '1',
                        'language' => 'en',
                    ],
                ],

                ['action' => 'deleteEntry',
                    'body' => ['objectID' => '2',
                        'language' => 'fr',
                    ],
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/dictionaries/compounds/batch',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"action":"addEntry","body":{"objectID":"1","language":"en"}},{"action":"deleteEntry","body":{"objectID":"2","language":"fr"}}]}'),
            ],
        ]);
    }

    /**
     * Test case for BatchDictionaryEntries
     * get batchDictionaryEntries results with all parameters.
     */
    public function testBatchDictionaryEntries1()
    {
        $client = $this->getClient();
        $client->batchDictionaryEntries(
            'compounds',
            ['clearExistingDictionaryEntries' => false,
                'requests' => [
                    ['action' => 'addEntry',
                        'body' => ['objectID' => '1',
                            'language' => 'en',
                            'word' => 'fancy',
                            'words' => [
                                'believe',

                                'algolia',
                            ],
                            'decomposition' => [
                                'trust',

                                'algolia',
                            ],
                            'state' => 'enabled',
                        ],
                    ],

                    ['action' => 'deleteEntry',
                        'body' => ['objectID' => '2',
                            'language' => 'fr',
                            'word' => 'humility',
                            'words' => [
                                'candor',

                                'algolia',
                            ],
                            'decomposition' => [
                                'grit',

                                'algolia',
                            ],
                            'state' => 'enabled',
                        ],
                    ],
                ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/dictionaries/compounds/batch',
                'method' => 'POST',
                'body' => json_decode('{"clearExistingDictionaryEntries":false,"requests":[{"action":"addEntry","body":{"objectID":"1","language":"en","word":"fancy","words":["believe","algolia"],"decomposition":["trust","algolia"],"state":"enabled"}},{"action":"deleteEntry","body":{"objectID":"2","language":"fr","word":"humility","words":["candor","algolia"],"decomposition":["grit","algolia"],"state":"enabled"}}]}'),
            ],
        ]);
    }

    /**
     * Test case for BatchDictionaryEntries
     * get batchDictionaryEntries results additional properties.
     */
    public function testBatchDictionaryEntries2()
    {
        $client = $this->getClient();
        $client->batchDictionaryEntries(
            'compounds',
            ['requests' => [
                ['action' => 'addEntry',
                    'body' => ['objectID' => '1',
                        'language' => 'en',
                        'additional' => 'try me',
                    ],
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/dictionaries/compounds/batch',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"action":"addEntry","body":{"objectID":"1","language":"en","additional":"try me"}}]}'),
            ],
        ]);
    }

    /**
     * Test case for Browse
     * browse with minimal parameters.
     */
    public function testBrowse0()
    {
        $client = $this->getClient();
        $client->browse(
            'indexName',
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/browse',
                'method' => 'POST',
                'body' => json_decode('{}'),
            ],
        ]);
    }

    /**
     * Test case for Browse
     * browse with search parameters.
     */
    public function testBrowse1()
    {
        $client = $this->getClient();
        $client->browse(
            'indexName',
            ['query' => 'myQuery',
                'facetFilters' => [
                    'tags:algolia',
                ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/browse',
                'method' => 'POST',
                'body' => json_decode('{"query":"myQuery","facetFilters":["tags:algolia"]}'),
            ],
        ]);
    }

    /**
     * Test case for Browse
     * browse allow a cursor in parameters.
     */
    public function testBrowse2()
    {
        $client = $this->getClient();
        $client->browse(
            'indexName',
            ['cursor' => 'test',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/browse',
                'method' => 'POST',
                'body' => json_decode('{"cursor":"test"}'),
            ],
        ]);
    }

    /**
     * Test case for ClearAllSynonyms
     * clearAllSynonyms.
     */
    public function testClearAllSynonyms0()
    {
        $client = $this->getClient();
        $client->clearAllSynonyms(
            'indexName',
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/synonyms/clear',
                'method' => 'POST',
                'body' => json_decode(''),
            ],
        ]);
    }

    /**
     * Test case for ClearObjects
     * clearObjects.
     */
    public function testClearObjects0()
    {
        $client = $this->getClient();
        $client->clearObjects(
            'theIndexName',
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/clear',
                'method' => 'POST',
                'body' => json_decode(''),
            ],
        ]);
    }

    /**
     * Test case for ClearRules
     * clearRules.
     */
    public function testClearRules0()
    {
        $client = $this->getClient();
        $client->clearRules(
            'indexName',
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/rules/clear',
                'method' => 'POST',
                'body' => json_decode(''),
            ],
        ]);
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
     * Test case for DeleteApiKey
     * deleteApiKey.
     */
    public function testDeleteApiKey0()
    {
        $client = $this->getClient();
        $client->deleteApiKey(
            'myTestApiKey',
        );

        $this->assertRequests([
            [
                'path' => '/1/keys/myTestApiKey',
                'method' => 'DELETE',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for DeleteBy
     * deleteBy.
     */
    public function testDeleteBy0()
    {
        $client = $this->getClient();
        $client->deleteBy(
            'theIndexName',
            ['filters' => 'brand:brandName',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/deleteByQuery',
                'method' => 'POST',
                'body' => json_decode('{"filters":"brand:brandName"}'),
            ],
        ]);
    }

    /**
     * Test case for DeleteIndex
     * deleteIndex.
     */
    public function testDeleteIndex0()
    {
        $client = $this->getClient();
        $client->deleteIndex(
            'theIndexName',
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName',
                'method' => 'DELETE',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for DeleteObject
     * deleteObject.
     */
    public function testDeleteObject0()
    {
        $client = $this->getClient();
        $client->deleteObject(
            'theIndexName',
            'uniqueID',
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/uniqueID',
                'method' => 'DELETE',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for DeleteRule
     * deleteRule.
     */
    public function testDeleteRule0()
    {
        $client = $this->getClient();
        $client->deleteRule(
            'indexName',
            'id1',
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/rules/id1',
                'method' => 'DELETE',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for DeleteSource
     * deleteSource.
     */
    public function testDeleteSource0()
    {
        $client = $this->getClient();
        $client->deleteSource(
            'theSource',
        );

        $this->assertRequests([
            [
                'path' => '/1/security/sources/theSource',
                'method' => 'DELETE',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for DeleteSynonym
     * deleteSynonym.
     */
    public function testDeleteSynonym0()
    {
        $client = $this->getClient();
        $client->deleteSynonym(
            'indexName',
            'id1',
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/synonyms/id1',
                'method' => 'DELETE',
                'body' => null,
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
     * Test case for GetApiKey
     * getApiKey.
     */
    public function testGetApiKey0()
    {
        $client = $this->getClient();
        $client->getApiKey(
            'myTestApiKey',
        );

        $this->assertRequests([
            [
                'path' => '/1/keys/myTestApiKey',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for GetDictionaryLanguages
     * get getDictionaryLanguages.
     */
    public function testGetDictionaryLanguages0()
    {
        $client = $this->getClient();
        $client->getDictionaryLanguages();

        $this->assertRequests([
            [
                'path' => '/1/dictionaries/*/languages',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for GetDictionarySettings
     * get getDictionarySettings results.
     */
    public function testGetDictionarySettings0()
    {
        $client = $this->getClient();
        $client->getDictionarySettings();

        $this->assertRequests([
            [
                'path' => '/1/dictionaries/*/settings',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for GetLogs
     * getLogs with minimal parameters.
     */
    public function testGetLogs0()
    {
        $client = $this->getClient();
        $client->getLogs();

        $this->assertRequests([
            [
                'path' => '/1/logs',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for GetLogs
     * getLogs with parameters.
     */
    public function testGetLogs1()
    {
        $client = $this->getClient();
        $client->getLogs(
            5,
            10,
            'theIndexName',
            'all',
        );

        $this->assertRequests([
            [
                'path' => '/1/logs',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"offset":"5","length":"10","indexName":"theIndexName","type":"all"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetObject
     * getObject.
     */
    public function testGetObject0()
    {
        $client = $this->getClient();
        $client->getObject(
            'theIndexName',
            'uniqueID',
            [
                'attr1',

                'attr2',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/uniqueID',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"attributesToRetrieve":"attr1,attr2"}', true),
            ],
        ]);
    }

    /**
     * Test case for GetObjects
     * getObjects.
     */
    public function testGetObjects0()
    {
        $client = $this->getClient();
        $client->getObjects(
            ['requests' => [
                ['attributesToRetrieve' => [
                    'attr1',

                    'attr2',
                ],
                    'objectID' => 'uniqueID',
                    'indexName' => 'theIndexName',
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/*/objects',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"attributesToRetrieve":["attr1","attr2"],"objectID":"uniqueID","indexName":"theIndexName"}]}'),
            ],
        ]);
    }

    /**
     * Test case for GetRule
     * getRule.
     */
    public function testGetRule0()
    {
        $client = $this->getClient();
        $client->getRule(
            'indexName',
            'id1',
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/rules/id1',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for GetSettings
     * getSettings.
     */
    public function testGetSettings0()
    {
        $client = $this->getClient();
        $client->getSettings(
            'theIndexName',
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/settings',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for GetSources
     * getSources.
     */
    public function testGetSources0()
    {
        $client = $this->getClient();
        $client->getSources();

        $this->assertRequests([
            [
                'path' => '/1/security/sources',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for GetSynonym
     * getSynonym.
     */
    public function testGetSynonym0()
    {
        $client = $this->getClient();
        $client->getSynonym(
            'indexName',
            'id1',
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/synonyms/id1',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for GetTask
     * getTask.
     */
    public function testGetTask0()
    {
        $client = $this->getClient();
        $client->getTask(
            'theIndexName',
            123,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/task/123',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for GetTopUserIds
     * getTopUserIds.
     */
    public function testGetTopUserIds0()
    {
        $client = $this->getClient();
        $client->getTopUserIds();

        $this->assertRequests([
            [
                'path' => '/1/clusters/mapping/top',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for GetUserId
     * getUserId.
     */
    public function testGetUserId0()
    {
        $client = $this->getClient();
        $client->getUserId(
            'uniqueID',
        );

        $this->assertRequests([
            [
                'path' => '/1/clusters/mapping/uniqueID',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for HasPendingMappings
     * hasPendingMappings with minimal parameters.
     */
    public function testHasPendingMappings0()
    {
        $client = $this->getClient();
        $client->hasPendingMappings();

        $this->assertRequests([
            [
                'path' => '/1/clusters/mapping/pending',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for HasPendingMappings
     * hasPendingMappings with parameters.
     */
    public function testHasPendingMappings1()
    {
        $client = $this->getClient();
        $client->hasPendingMappings(
            true,
        );

        $this->assertRequests([
            [
                'path' => '/1/clusters/mapping/pending',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"getClusters":"true"}', true),
            ],
        ]);
    }

    /**
     * Test case for ListApiKeys
     * listApiKeys.
     */
    public function testListApiKeys0()
    {
        $client = $this->getClient();
        $client->listApiKeys();

        $this->assertRequests([
            [
                'path' => '/1/keys',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for ListClusters
     * listClusters.
     */
    public function testListClusters0()
    {
        $client = $this->getClient();
        $client->listClusters();

        $this->assertRequests([
            [
                'path' => '/1/clusters',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for ListIndices
     * listIndices with minimal parameters.
     */
    public function testListIndices0()
    {
        $client = $this->getClient();
        $client->listIndices();

        $this->assertRequests([
            [
                'path' => '/1/indexes',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for ListIndices
     * listIndices with parameters.
     */
    public function testListIndices1()
    {
        $client = $this->getClient();
        $client->listIndices(
            8,
            3,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"page":"8","hitsPerPage":"3"}', true),
            ],
        ]);
    }

    /**
     * Test case for ListUserIds
     * listUserIds with minimal parameters.
     */
    public function testListUserIds0()
    {
        $client = $this->getClient();
        $client->listUserIds();

        $this->assertRequests([
            [
                'path' => '/1/clusters/mapping',
                'method' => 'GET',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for ListUserIds
     * listUserIds with parameters.
     */
    public function testListUserIds1()
    {
        $client = $this->getClient();
        $client->listUserIds(
            8,
            100,
        );

        $this->assertRequests([
            [
                'path' => '/1/clusters/mapping',
                'method' => 'GET',
                'body' => null,
                'queryParameters' => json_decode('{"page":"8","hitsPerPage":"100"}', true),
            ],
        ]);
    }

    /**
     * Test case for MultipleBatch
     * multipleBatch.
     */
    public function testMultipleBatch0()
    {
        $client = $this->getClient();
        $client->multipleBatch(
            ['requests' => [
                ['action' => 'addObject',
                    'body' => ['key' => 'value',
                    ],
                    'indexName' => 'theIndexName',
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/*/batch',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"action":"addObject","body":{"key":"value"},"indexName":"theIndexName"}]}'),
            ],
        ]);
    }

    /**
     * Test case for OperationIndex
     * operationIndex.
     */
    public function testOperationIndex0()
    {
        $client = $this->getClient();
        $client->operationIndex(
            'theIndexName',
            ['operation' => 'copy',
                'destination' => 'dest',
                'scope' => [
                    'rules',

                    'settings',
                ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/operation',
                'method' => 'POST',
                'body' => json_decode('{"operation":"copy","destination":"dest","scope":["rules","settings"]}'),
            ],
        ]);
    }

    /**
     * Test case for PartialUpdateObject
     * partialUpdateObject.
     */
    public function testPartialUpdateObject0()
    {
        $client = $this->getClient();
        $client->partialUpdateObject(
            'theIndexName',
            'uniqueID',
            ['id1' => 'test',
                'id2' => ['_operation' => 'AddUnique',
                    'value' => 'test2',
                ],
            ],
            true,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/uniqueID/partial',
                'method' => 'POST',
                'body' => json_decode('{"id1":"test","id2":{"_operation":"AddUnique","value":"test2"}}'),
                'queryParameters' => json_decode('{"createIfNotExists":"true"}', true),
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

    /**
     * Test case for RemoveUserId
     * removeUserId.
     */
    public function testRemoveUserId0()
    {
        $client = $this->getClient();
        $client->removeUserId(
            'uniqueID',
        );

        $this->assertRequests([
            [
                'path' => '/1/clusters/mapping/uniqueID',
                'method' => 'DELETE',
                'body' => null,
            ],
        ]);
    }

    /**
     * Test case for ReplaceSources
     * replaceSources.
     */
    public function testReplaceSources0()
    {
        $client = $this->getClient();
        $client->replaceSources(
            [
                ['source' => 'theSource',
                    'description' => 'theDescription',
                ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/security/sources',
                'method' => 'PUT',
                'body' => json_decode('[{"source":"theSource","description":"theDescription"}]'),
            ],
        ]);
    }

    /**
     * Test case for RestoreApiKey
     * restoreApiKey.
     */
    public function testRestoreApiKey0()
    {
        $client = $this->getClient();
        $client->restoreApiKey(
            'myApiKey',
        );

        $this->assertRequests([
            [
                'path' => '/1/keys/myApiKey/restore',
                'method' => 'POST',
                'body' => json_decode(''),
            ],
        ]);
    }

    /**
     * Test case for SaveObject
     * saveObject.
     */
    public function testSaveObject0()
    {
        $client = $this->getClient();
        $client->saveObject(
            'theIndexName',
            ['objectID' => 'id',
                'test' => 'val',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName',
                'method' => 'POST',
                'body' => json_decode('{"objectID":"id","test":"val"}'),
            ],
        ]);
    }

    /**
     * Test case for SaveRule
     * saveRule with minimal parameters.
     */
    public function testSaveRule0()
    {
        $client = $this->getClient();
        $client->saveRule(
            'indexName',
            'id1',
            ['objectID' => 'id1',
                'conditions' => [
                    ['pattern' => 'apple',
                        'anchoring' => 'contains',
                    ],
                ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/rules/id1',
                'method' => 'PUT',
                'body' => json_decode('{"objectID":"id1","conditions":[{"pattern":"apple","anchoring":"contains"}]}'),
            ],
        ]);
    }

    /**
     * Test case for SaveRule
     * saveRule with all parameters.
     */
    public function testSaveRule1()
    {
        $client = $this->getClient();
        $client->saveRule(
            'indexName',
            'id1',
            ['objectID' => 'id1',
                'conditions' => [
                    ['pattern' => 'apple',
                        'anchoring' => 'contains',
                        'alternatives' => false,
                        'context' => 'search',
                    ],
                ],
                'consequence' => ['params' => ['filters' => 'brand:apple',
                    'query' => ['remove' => [
                        'algolia',
                    ],
                        'edits' => [
                            ['type' => 'remove',
                                'delete' => 'abc',
                                'insert' => 'cde',
                            ],

                            ['type' => 'replace',
                                'delete' => 'abc',
                                'insert' => 'cde',
                            ],
                        ],
                    ],
                ],
                    'hide' => [
                        ['objectID' => '321',
                        ],
                    ],
                    'filterPromotes' => false,
                    'userData' => ['algolia' => 'aloglia'],
                    'promote' => [
                        ['objectID' => 'abc',
                            'position' => 3,
                        ],

                        ['objectIDs' => [
                            'abc',

                            'def',
                        ],
                            'position' => 1,
                        ],
                    ],
                ],
                'description' => 'test',
                'enabled' => true,
                'validity' => [
                    ['from' => 1656670273,
                        'until' => 1656670277,
                    ],
                ],
            ],
            true,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/rules/id1',
                'method' => 'PUT',
                'body' => json_decode('{"objectID":"id1","conditions":[{"pattern":"apple","anchoring":"contains","alternatives":false,"context":"search"}],"consequence":{"params":{"filters":"brand:apple","query":{"remove":["algolia"],"edits":[{"type":"remove","delete":"abc","insert":"cde"},{"type":"replace","delete":"abc","insert":"cde"}]}},"hide":[{"objectID":"321"}],"filterPromotes":false,"userData":{"algolia":"aloglia"},"promote":[{"objectID":"abc","position":3},{"objectIDs":["abc","def"],"position":1}]},"description":"test","enabled":true,"validity":[{"from":1656670273,"until":1656670277}]}'),
                'queryParameters' => json_decode('{"forwardToReplicas":"true"}', true),
            ],
        ]);
    }

    /**
     * Test case for SaveRules
     * saveRules with minimal parameters.
     */
    public function testSaveRules0()
    {
        $client = $this->getClient();
        $client->saveRules(
            'indexName',
            [
                ['objectID' => 'a-rule-id',
                    'conditions' => [
                        ['pattern' => 'smartphone',
                            'anchoring' => 'contains',
                        ],
                    ],
                ],

                ['objectID' => 'a-second-rule-id',
                    'conditions' => [
                        ['pattern' => 'apple',
                            'anchoring' => 'contains',
                        ],
                    ],
                ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/rules/batch',
                'method' => 'POST',
                'body' => json_decode('[{"objectID":"a-rule-id","conditions":[{"pattern":"smartphone","anchoring":"contains"}]},{"objectID":"a-second-rule-id","conditions":[{"pattern":"apple","anchoring":"contains"}]}]'),
            ],
        ]);
    }

    /**
     * Test case for SaveRules
     * saveRules with all parameters.
     */
    public function testSaveRules1()
    {
        $client = $this->getClient();
        $client->saveRules(
            'indexName',
            [
                ['objectID' => 'id1',
                    'conditions' => [
                        ['pattern' => 'apple',
                            'anchoring' => 'contains',
                            'alternatives' => false,
                            'context' => 'search',
                        ],
                    ],
                    'consequence' => ['params' => ['filters' => 'brand:apple',
                        'query' => ['remove' => [
                            'algolia',
                        ],
                            'edits' => [
                                ['type' => 'remove',
                                    'delete' => 'abc',
                                    'insert' => 'cde',
                                ],

                                ['type' => 'replace',
                                    'delete' => 'abc',
                                    'insert' => 'cde',
                                ],
                            ],
                        ],
                    ],
                        'hide' => [
                            ['objectID' => '321',
                            ],
                        ],
                        'filterPromotes' => false,
                        'userData' => ['algolia' => 'aloglia'],
                        'promote' => [
                            ['objectID' => 'abc',
                                'position' => 3,
                            ],

                            ['objectIDs' => [
                                'abc',

                                'def',
                            ],
                                'position' => 1,
                            ],
                        ],
                    ],
                    'description' => 'test',
                    'enabled' => true,
                    'validity' => [
                        ['from' => 1656670273,
                            'until' => 1656670277,
                        ],
                    ],
                ],
            ],
            true,
            true,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/rules/batch',
                'method' => 'POST',
                'body' => json_decode('[{"objectID":"id1","conditions":[{"pattern":"apple","anchoring":"contains","alternatives":false,"context":"search"}],"consequence":{"params":{"filters":"brand:apple","query":{"remove":["algolia"],"edits":[{"type":"remove","delete":"abc","insert":"cde"},{"type":"replace","delete":"abc","insert":"cde"}]}},"hide":[{"objectID":"321"}],"filterPromotes":false,"userData":{"algolia":"aloglia"},"promote":[{"objectID":"abc","position":3},{"objectIDs":["abc","def"],"position":1}]},"description":"test","enabled":true,"validity":[{"from":1656670273,"until":1656670277}]}]'),
                'queryParameters' => json_decode('{"forwardToReplicas":"true","clearExistingRules":"true"}', true),
            ],
        ]);
    }

    /**
     * Test case for SaveSynonym
     * saveSynonym.
     */
    public function testSaveSynonym0()
    {
        $client = $this->getClient();
        $client->saveSynonym(
            'indexName',
            'id1',
            ['objectID' => 'id1',
                'type' => 'synonym',
                'synonyms' => [
                    'car',

                    'vehicule',

                    'auto',
                ],
            ],
            true,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/synonyms/id1',
                'method' => 'PUT',
                'body' => json_decode('{"objectID":"id1","type":"synonym","synonyms":["car","vehicule","auto"]}'),
                'queryParameters' => json_decode('{"forwardToReplicas":"true"}', true),
            ],
        ]);
    }

    /**
     * Test case for SaveSynonyms
     * saveSynonyms.
     */
    public function testSaveSynonyms0()
    {
        $client = $this->getClient();
        $client->saveSynonyms(
            'indexName',
            [
                ['objectID' => 'id1',
                    'type' => 'synonym',
                    'synonyms' => [
                        'car',

                        'vehicule',

                        'auto',
                    ],
                ],

                ['objectID' => 'id2',
                    'type' => 'onewaysynonym',
                    'input' => 'iphone',
                    'synonyms' => [
                        'ephone',

                        'aphone',

                        'yphone',
                    ],
                ],
            ],
            true,
            false,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/synonyms/batch',
                'method' => 'POST',
                'body' => json_decode('[{"objectID":"id1","type":"synonym","synonyms":["car","vehicule","auto"]},{"objectID":"id2","type":"onewaysynonym","input":"iphone","synonyms":["ephone","aphone","yphone"]}]'),
                'queryParameters' => json_decode('{"forwardToReplicas":"true","replaceExistingSynonyms":"false"}', true),
            ],
        ]);
    }

    /**
     * Test case for Search
     * search for a single hits request with minimal parameters.
     */
    public function testSearch0()
    {
        $client = $this->getClient();
        $client->search(
            ['requests' => [
                ['indexName' => 'theIndexName',
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/*/queries',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"indexName":"theIndexName"}]}'),
            ],
        ]);
    }

    /**
     * Test case for Search
     * search for a single facet request with minimal parameters.
     */
    public function testSearch1()
    {
        $client = $this->getClient();
        $client->search(
            ['requests' => [
                ['indexName' => 'theIndexName',
                    'type' => 'facet',
                    'facet' => 'theFacet',
                ],
            ],
                'strategy' => 'stopIfEnoughMatches',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/*/queries',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"indexName":"theIndexName","type":"facet","facet":"theFacet"}],"strategy":"stopIfEnoughMatches"}'),
            ],
        ]);
    }

    /**
     * Test case for Search
     * search for a single hits request with all parameters.
     */
    public function testSearch2()
    {
        $client = $this->getClient();
        $client->search(
            ['requests' => [
                ['indexName' => 'theIndexName',
                    'query' => 'myQuery',
                    'hitsPerPage' => 50,
                    'type' => 'default',
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/*/queries',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"indexName":"theIndexName","query":"myQuery","hitsPerPage":50,"type":"default"}]}'),
            ],
        ]);
    }

    /**
     * Test case for Search
     * search for a single facet request with all parameters.
     */
    public function testSearch3()
    {
        $client = $this->getClient();
        $client->search(
            ['requests' => [
                ['indexName' => 'theIndexName',
                    'type' => 'facet',
                    'facet' => 'theFacet',
                    'facetQuery' => 'theFacetQuery',
                    'query' => 'theQuery',
                    'maxFacetHits' => 50,
                ],
            ],
                'strategy' => 'stopIfEnoughMatches',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/*/queries',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"indexName":"theIndexName","type":"facet","facet":"theFacet","facetQuery":"theFacetQuery","query":"theQuery","maxFacetHits":50}],"strategy":"stopIfEnoughMatches"}'),
            ],
        ]);
    }

    /**
     * Test case for Search
     * search for multiple mixed requests in multiple indices with minimal parameters.
     */
    public function testSearch4()
    {
        $client = $this->getClient();
        $client->search(
            ['requests' => [
                ['indexName' => 'theIndexName',
                ],

                ['indexName' => 'theIndexName2',
                    'type' => 'facet',
                    'facet' => 'theFacet',
                ],

                ['indexName' => 'theIndexName',
                    'type' => 'default',
                ],
            ],
                'strategy' => 'stopIfEnoughMatches',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/*/queries',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"indexName":"theIndexName"},{"indexName":"theIndexName2","type":"facet","facet":"theFacet"},{"indexName":"theIndexName","type":"default"}],"strategy":"stopIfEnoughMatches"}'),
            ],
        ]);
    }

    /**
     * Test case for Search
     * search for multiple mixed requests in multiple indices with all parameters.
     */
    public function testSearch5()
    {
        $client = $this->getClient();
        $client->search(
            ['requests' => [
                ['indexName' => 'theIndexName',
                    'type' => 'facet',
                    'facet' => 'theFacet',
                    'facetQuery' => 'theFacetQuery',
                    'query' => 'theQuery',
                    'maxFacetHits' => 50,
                ],

                ['indexName' => 'theIndexName',
                    'query' => 'myQuery',
                    'hitsPerPage' => 50,
                    'type' => 'default',
                ],
            ],
                'strategy' => 'stopIfEnoughMatches',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/*/queries',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"indexName":"theIndexName","type":"facet","facet":"theFacet","facetQuery":"theFacetQuery","query":"theQuery","maxFacetHits":50},{"indexName":"theIndexName","query":"myQuery","hitsPerPage":50,"type":"default"}],"strategy":"stopIfEnoughMatches"}'),
            ],
        ]);
    }

    /**
     * Test case for Search
     * search filters accept all of the possible shapes.
     */
    public function testSearch6()
    {
        $client = $this->getClient();
        $client->search(
            ['requests' => [
                ['indexName' => 'theIndexName',
                    'facetFilters' => 'mySearch:filters',
                    'reRankingApplyFilter' => 'mySearch:filters',
                    'tagFilters' => 'mySearch:filters',
                    'numericFilters' => 'mySearch:filters',
                    'optionalFilters' => 'mySearch:filters',
                ],

                ['indexName' => 'theIndexName',
                    'facetFilters' => [
                        'mySearch:filters',

                        [
                            'mySearch:filters',
                        ],
                    ],
                    'reRankingApplyFilter' => [
                        'mySearch:filters',

                        [
                            'mySearch:filters',
                        ],
                    ],
                    'tagFilters' => [
                        'mySearch:filters',

                        [
                            'mySearch:filters',
                        ],
                    ],
                    'numericFilters' => [
                        'mySearch:filters',

                        [
                            'mySearch:filters',
                        ],
                    ],
                    'optionalFilters' => [
                        'mySearch:filters',

                        [
                            'mySearch:filters',
                        ],
                    ],
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/*/queries',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"indexName":"theIndexName","facetFilters":"mySearch:filters","reRankingApplyFilter":"mySearch:filters","tagFilters":"mySearch:filters","numericFilters":"mySearch:filters","optionalFilters":"mySearch:filters"},{"indexName":"theIndexName","facetFilters":["mySearch:filters",["mySearch:filters"]],"reRankingApplyFilter":["mySearch:filters",["mySearch:filters"]],"tagFilters":["mySearch:filters",["mySearch:filters"]],"numericFilters":["mySearch:filters",["mySearch:filters"]],"optionalFilters":["mySearch:filters",["mySearch:filters"]]}]}'),
            ],
        ]);
    }

    /**
     * Test case for Search
     * search with all search parameters.
     */
    public function testSearch7()
    {
        $client = $this->getClient();
        $client->search(
            ['requests' => [
                ['advancedSyntax' => true,
                    'advancedSyntaxFeatures' => [
                        'exactPhrase',
                    ],
                    'allowTyposOnNumericTokens' => true,
                    'alternativesAsExact' => [
                        'multiWordsSynonym',
                    ],
                    'analytics' => true,
                    'analyticsTags' => [
                        '',
                    ],
                    'aroundLatLng' => '',
                    'aroundLatLngViaIP' => true,
                    'aroundPrecision' => 0,
                    'aroundRadius' => 'all',
                    'attributeCriteriaComputedByMinProximity' => true,
                    'attributesForFaceting' => [
                        '',
                    ],
                    'attributesToHighlight' => [
                        '',
                    ],
                    'attributesToRetrieve' => [
                        '',
                    ],
                    'attributesToSnippet' => [
                        '',
                    ],
                    'clickAnalytics' => true,
                    'customRanking' => [
                        '',
                    ],
                    'decompoundQuery' => true,
                    'disableExactOnAttributes' => [
                        '',
                    ],
                    'disableTypoToleranceOnAttributes' => [
                        '',
                    ],
                    'distinct' => 0,
                    'enableABTest' => true,
                    'enablePersonalization' => true,
                    'enableReRanking' => true,
                    'enableRules' => true,
                    'exactOnSingleWordQuery' => 'attribute',
                    'explain' => [
                        'foo',

                        'bar',
                    ],
                    'facetFilters' => [
                        '',
                    ],
                    'facetingAfterDistinct' => true,
                    'facets' => [
                        '',
                    ],
                    'filters' => '',
                    'getRankingInfo' => true,
                    'highlightPostTag' => '',
                    'highlightPreTag' => '',
                    'hitsPerPage' => 0,
                    'ignorePlurals' => false,
                    'indexName' => 'theIndexName',
                    'insideBoundingBox' => [
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
                    'insidePolygon' => [
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
                    'keepDiacriticsOnCharacters' => '',
                    'length' => 0,
                    'maxValuesPerFacet' => 0,
                    'minProximity' => 0,
                    'minWordSizefor1Typo' => 0,
                    'minWordSizefor2Typos' => 0,
                    'minimumAroundRadius' => 0,
                    'naturalLanguages' => [
                        '',
                    ],
                    'numericFilters' => [
                        '',
                    ],
                    'offset' => 0,
                    'optionalFilters' => [
                        '',
                    ],
                    'optionalWords' => [
                        '',
                    ],
                    'page' => 0,
                    'percentileComputation' => true,
                    'personalizationImpact' => 0,
                    'query' => '',
                    'queryLanguages' => [
                        '',
                    ],
                    'queryType' => 'prefixAll',
                    'ranking' => [
                        '',
                    ],
                    'reRankingApplyFilter' => [
                        '',
                    ],
                    'relevancyStrictness' => 0,
                    'removeStopWords' => true,
                    'removeWordsIfNoResults' => 'allOptional',
                    'renderingContent' => ['facetOrdering' => ['facets' => ['order' => [
                        'a',

                        'b',
                    ],
                    ],
                        'values' => ['a' => ['order' => [
                            'b',
                        ],
                            'sortRemainingBy' => 'count',
                        ],
                        ],
                    ],
                    ],
                    'replaceSynonymsInHighlight' => true,
                    'responseFields' => [
                        '',
                    ],
                    'restrictHighlightAndSnippetArrays' => true,
                    'restrictSearchableAttributes' => [
                        '',
                    ],
                    'ruleContexts' => [
                        '',
                    ],
                    'similarQuery' => '',
                    'snippetEllipsisText' => '',
                    'sortFacetValuesBy' => '',
                    'sumOrFiltersScores' => true,
                    'synonyms' => true,
                    'tagFilters' => [
                        '',
                    ],
                    'type' => 'default',
                    'typoTolerance' => 'min',
                    'userToken' => '',
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/*/queries',
                'method' => 'POST',
                'body' => json_decode('{"requests":[{"advancedSyntax":true,"advancedSyntaxFeatures":["exactPhrase"],"allowTyposOnNumericTokens":true,"alternativesAsExact":["multiWordsSynonym"],"analytics":true,"analyticsTags":[""],"aroundLatLng":"","aroundLatLngViaIP":true,"aroundPrecision":0,"aroundRadius":"all","attributeCriteriaComputedByMinProximity":true,"attributesForFaceting":[""],"attributesToHighlight":[""],"attributesToRetrieve":[""],"attributesToSnippet":[""],"clickAnalytics":true,"customRanking":[""],"decompoundQuery":true,"disableExactOnAttributes":[""],"disableTypoToleranceOnAttributes":[""],"distinct":0,"enableABTest":true,"enablePersonalization":true,"enableReRanking":true,"enableRules":true,"exactOnSingleWordQuery":"attribute","explain":["foo","bar"],"facetFilters":[""],"facetingAfterDistinct":true,"facets":[""],"filters":"","getRankingInfo":true,"highlightPostTag":"","highlightPreTag":"","hitsPerPage":0,"ignorePlurals":false,"indexName":"theIndexName","insideBoundingBox":[[47.3165,4.9665,47.3424,5.0201],[40.9234,2.1185,38.643,1.9916]],"insidePolygon":[[47.3165,4.9665,47.3424,5.0201,47.32,4.9],[40.9234,2.1185,38.643,1.9916,39.2587,2.0104]],"keepDiacriticsOnCharacters":"","length":0,"maxValuesPerFacet":0,"minProximity":0,"minWordSizefor1Typo":0,"minWordSizefor2Typos":0,"minimumAroundRadius":0,"naturalLanguages":[""],"numericFilters":[""],"offset":0,"optionalFilters":[""],"optionalWords":[""],"page":0,"percentileComputation":true,"personalizationImpact":0,"query":"","queryLanguages":[""],"queryType":"prefixAll","ranking":[""],"reRankingApplyFilter":[""],"relevancyStrictness":0,"removeStopWords":true,"removeWordsIfNoResults":"allOptional","renderingContent":{"facetOrdering":{"facets":{"order":["a","b"]},"values":{"a":{"order":["b"],"sortRemainingBy":"count"}}}},"replaceSynonymsInHighlight":true,"responseFields":[""],"restrictHighlightAndSnippetArrays":true,"restrictSearchableAttributes":[""],"ruleContexts":[""],"similarQuery":"","snippetEllipsisText":"","sortFacetValuesBy":"","sumOrFiltersScores":true,"synonyms":true,"tagFilters":[""],"type":"default","typoTolerance":"min","userToken":""}]}'),
            ],
        ]);
    }

    /**
     * Test case for SearchDictionaryEntries
     * get searchDictionaryEntries results with minimal parameters.
     */
    public function testSearchDictionaryEntries0()
    {
        $client = $this->getClient();
        $client->searchDictionaryEntries(
            'compounds',
            ['query' => 'foo',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/dictionaries/compounds/search',
                'method' => 'POST',
                'body' => json_decode('{"query":"foo"}'),
            ],
        ]);
    }

    /**
     * Test case for SearchDictionaryEntries
     * get searchDictionaryEntries results with all parameters.
     */
    public function testSearchDictionaryEntries1()
    {
        $client = $this->getClient();
        $client->searchDictionaryEntries(
            'compounds',
            ['query' => 'foo',
                'page' => 4,
                'hitsPerPage' => 2,
                'language' => 'fr',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/dictionaries/compounds/search',
                'method' => 'POST',
                'body' => json_decode('{"query":"foo","page":4,"hitsPerPage":2,"language":"fr"}'),
            ],
        ]);
    }

    /**
     * Test case for SearchForFacetValues
     * get searchForFacetValues results with minimal parameters.
     */
    public function testSearchForFacetValues0()
    {
        $client = $this->getClient();
        $client->searchForFacetValues(
            'indexName',
            'facetName',
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/facets/facetName/query',
                'method' => 'POST',
                'body' => json_decode('{}'),
            ],
        ]);
    }

    /**
     * Test case for SearchForFacetValues
     * get searchForFacetValues results with all parameters.
     */
    public function testSearchForFacetValues1()
    {
        $client = $this->getClient();
        $client->searchForFacetValues(
            'indexName',
            'facetName',
            ['params' => "query=foo&facetFilters=['bar']",
                'facetQuery' => 'foo',
                'maxFacetHits' => 42,
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/facets/facetName/query',
                'method' => 'POST',
                'body' => json_decode("{\"params\":\"query=foo&facetFilters=['bar']\",\"facetQuery\":\"foo\",\"maxFacetHits\":42}"),
            ],
        ]);
    }

    /**
     * Test case for SearchRules
     * searchRules.
     */
    public function testSearchRules0()
    {
        $client = $this->getClient();
        $client->searchRules(
            'indexName',
            ['query' => 'something',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/rules/search',
                'method' => 'POST',
                'body' => json_decode('{"query":"something"}'),
            ],
        ]);
    }

    /**
     * Test case for SearchSingleIndex
     * search with minimal parameters.
     */
    public function testSearchSingleIndex0()
    {
        $client = $this->getClient();
        $client->searchSingleIndex(
            'indexName',
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/query',
                'method' => 'POST',
                'body' => json_decode('{}'),
            ],
        ]);
    }

    /**
     * Test case for SearchSingleIndex
     * search with searchParams.
     */
    public function testSearchSingleIndex1()
    {
        $client = $this->getClient();
        $client->searchSingleIndex(
            'indexName',
            ['query' => 'myQuery',
                'facetFilters' => [
                    'tags:algolia',
                ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/query',
                'method' => 'POST',
                'body' => json_decode('{"query":"myQuery","facetFilters":["tags:algolia"]}'),
            ],
        ]);
    }

    /**
     * Test case for SearchSynonyms
     * searchSynonyms with minimal parameters.
     */
    public function testSearchSynonyms0()
    {
        $client = $this->getClient();
        $client->searchSynonyms(
            'indexName',
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/synonyms/search',
                'method' => 'POST',
                'body' => json_decode('{}'),
            ],
        ]);
    }

    /**
     * Test case for SearchSynonyms
     * searchSynonyms with all parameters.
     */
    public function testSearchSynonyms1()
    {
        $client = $this->getClient();
        $client->searchSynonyms(
            'indexName',
            'altcorrection1',
            10,
            10,
            ['query' => 'myQuery',
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/indexName/synonyms/search',
                'method' => 'POST',
                'body' => json_decode('{"query":"myQuery"}'),
                'queryParameters' => json_decode('{"type":"altcorrection1","page":"10","hitsPerPage":"10"}', true),
            ],
        ]);
    }

    /**
     * Test case for SearchUserIds
     * searchUserIds.
     */
    public function testSearchUserIds0()
    {
        $client = $this->getClient();
        $client->searchUserIds(
            ['query' => 'test',
                'clusterName' => 'theClusterName',
                'page' => 5,
                'hitsPerPage' => 10,
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/clusters/mapping/search',
                'method' => 'POST',
                'body' => json_decode('{"query":"test","clusterName":"theClusterName","page":5,"hitsPerPage":10}'),
            ],
        ]);
    }

    /**
     * Test case for SetDictionarySettings
     * get setDictionarySettings results with minimal parameters.
     */
    public function testSetDictionarySettings0()
    {
        $client = $this->getClient();
        $client->setDictionarySettings(
            ['disableStandardEntries' => ['plurals' => ['fr' => false,
                'en' => false,
                'ru' => true,
            ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/dictionaries/*/settings',
                'method' => 'PUT',
                'body' => json_decode('{"disableStandardEntries":{"plurals":{"fr":false,"en":false,"ru":true}}}'),
            ],
        ]);
    }

    /**
     * Test case for SetDictionarySettings
     * get setDictionarySettings results with all parameters.
     */
    public function testSetDictionarySettings1()
    {
        $client = $this->getClient();
        $client->setDictionarySettings(
            ['disableStandardEntries' => ['plurals' => ['fr' => false,
                'en' => false,
                'ru' => true,
            ],
                'stopwords' => ['fr' => false,
                ],
                'compounds' => ['ru' => true,
                ],
            ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/dictionaries/*/settings',
                'method' => 'PUT',
                'body' => json_decode('{"disableStandardEntries":{"plurals":{"fr":false,"en":false,"ru":true},"stopwords":{"fr":false},"compounds":{"ru":true}}}'),
            ],
        ]);
    }

    /**
     * Test case for SetSettings
     * setSettings with minimal parameters.
     */
    public function testSetSettings0()
    {
        $client = $this->getClient();
        $client->setSettings(
            'theIndexName',
            ['paginationLimitedTo' => 10,
            ],
            true,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/settings',
                'method' => 'PUT',
                'body' => json_decode('{"paginationLimitedTo":10}'),
                'queryParameters' => json_decode('{"forwardToReplicas":"true"}', true),
            ],
        ]);
    }

    /**
     * Test case for SetSettings
     * setSettings allow boolean `typoTolerance`.
     */
    public function testSetSettings1()
    {
        $client = $this->getClient();
        $client->setSettings(
            'theIndexName',
            ['typoTolerance' => true,
            ],
            true,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/settings',
                'method' => 'PUT',
                'body' => json_decode('{"typoTolerance":true}'),
                'queryParameters' => json_decode('{"forwardToReplicas":"true"}', true),
            ],
        ]);
    }

    /**
     * Test case for SetSettings
     * setSettings allow enum `typoTolerance`.
     */
    public function testSetSettings2()
    {
        $client = $this->getClient();
        $client->setSettings(
            'theIndexName',
            ['typoTolerance' => 'min',
            ],
            true,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/settings',
                'method' => 'PUT',
                'body' => json_decode('{"typoTolerance":"min"}'),
                'queryParameters' => json_decode('{"forwardToReplicas":"true"}', true),
            ],
        ]);
    }

    /**
     * Test case for SetSettings
     * setSettings allow boolean `ignorePlurals`.
     */
    public function testSetSettings3()
    {
        $client = $this->getClient();
        $client->setSettings(
            'theIndexName',
            ['ignorePlurals' => true,
            ],
            true,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/settings',
                'method' => 'PUT',
                'body' => json_decode('{"ignorePlurals":true}'),
                'queryParameters' => json_decode('{"forwardToReplicas":"true"}', true),
            ],
        ]);
    }

    /**
     * Test case for SetSettings
     * setSettings allow list of string `ignorePlurals`.
     */
    public function testSetSettings4()
    {
        $client = $this->getClient();
        $client->setSettings(
            'theIndexName',
            ['ignorePlurals' => [
                'algolia',
            ],
            ],
            true,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/settings',
                'method' => 'PUT',
                'body' => json_decode('{"ignorePlurals":["algolia"]}'),
                'queryParameters' => json_decode('{"forwardToReplicas":"true"}', true),
            ],
        ]);
    }

    /**
     * Test case for SetSettings
     * setSettings allow boolean `removeStopWords`.
     */
    public function testSetSettings5()
    {
        $client = $this->getClient();
        $client->setSettings(
            'theIndexName',
            ['removeStopWords' => true,
            ],
            true,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/settings',
                'method' => 'PUT',
                'body' => json_decode('{"removeStopWords":true}'),
                'queryParameters' => json_decode('{"forwardToReplicas":"true"}', true),
            ],
        ]);
    }

    /**
     * Test case for SetSettings
     * setSettings allow list of string `removeStopWords`.
     */
    public function testSetSettings6()
    {
        $client = $this->getClient();
        $client->setSettings(
            'theIndexName',
            ['removeStopWords' => [
                'algolia',
            ],
            ],
            true,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/settings',
                'method' => 'PUT',
                'body' => json_decode('{"removeStopWords":["algolia"]}'),
                'queryParameters' => json_decode('{"forwardToReplicas":"true"}', true),
            ],
        ]);
    }

    /**
     * Test case for SetSettings
     * setSettings allow boolean `distinct`.
     */
    public function testSetSettings7()
    {
        $client = $this->getClient();
        $client->setSettings(
            'theIndexName',
            ['distinct' => true,
            ],
            true,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/settings',
                'method' => 'PUT',
                'body' => json_decode('{"distinct":true}'),
                'queryParameters' => json_decode('{"forwardToReplicas":"true"}', true),
            ],
        ]);
    }

    /**
     * Test case for SetSettings
     * setSettings allow integers for `distinct`.
     */
    public function testSetSettings8()
    {
        $client = $this->getClient();
        $client->setSettings(
            'theIndexName',
            ['distinct' => 1,
            ],
            true,
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/settings',
                'method' => 'PUT',
                'body' => json_decode('{"distinct":1}'),
                'queryParameters' => json_decode('{"forwardToReplicas":"true"}', true),
            ],
        ]);
    }

    /**
     * Test case for SetSettings
     * setSettings allow all `indexSettings`.
     */
    public function testSetSettings9()
    {
        $client = $this->getClient();
        $client->setSettings(
            'theIndexName',
            ['advancedSyntax' => true,
                'advancedSyntaxFeatures' => [
                    'exactPhrase',
                ],
                'allowCompressionOfIntegerArray' => true,
                'allowTyposOnNumericTokens' => true,
                'alternativesAsExact' => [
                    'singleWordSynonym',
                ],
                'attributeCriteriaComputedByMinProximity' => true,
                'attributeForDistinct' => 'test',
                'attributesForFaceting' => [
                    'algolia',
                ],
                'attributesToHighlight' => [
                    'algolia',
                ],
                'attributesToRetrieve' => [
                    'algolia',
                ],
                'attributesToSnippet' => [
                    'algolia',
                ],
                'attributesToTransliterate' => [
                    'algolia',
                ],
                'camelCaseAttributes' => [
                    'algolia',
                ],
                'customNormalization' => ['algolia' => ['aloglia' => 'aglolia',
                ],
                ],
                'customRanking' => [
                    'algolia',
                ],
                'decompoundQuery' => false,
                'decompoundedAttributes' => ['algolia' => 'aloglia',
                ],
                'disableExactOnAttributes' => [
                    'algolia',
                ],
                'disablePrefixOnAttributes' => [
                    'algolia',
                ],
                'disableTypoToleranceOnAttributes' => [
                    'algolia',
                ],
                'disableTypoToleranceOnWords' => [
                    'algolia',
                ],
                'distinct' => 3,
                'enablePersonalization' => true,
                'enableReRanking' => false,
                'enableRules' => true,
                'exactOnSingleWordQuery' => 'attribute',
                'highlightPreTag' => '<span>',
                'highlightPostTag' => '</span>',
                'hitsPerPage' => 10,
                'ignorePlurals' => false,
                'indexLanguages' => [
                    'algolia',
                ],
                'keepDiacriticsOnCharacters' => 'abc',
                'maxFacetHits' => 20,
                'maxValuesPerFacet' => 30,
                'minProximity' => 6,
                'minWordSizefor1Typo' => 5,
                'minWordSizefor2Typos' => 11,
                'mode' => 'neuralSearch',
                'numericAttributesForFiltering' => [
                    'algolia',
                ],
                'optionalWords' => [
                    'myspace',
                ],
                'paginationLimitedTo' => 0,
                'queryLanguages' => [
                    'algolia',
                ],
                'queryType' => 'prefixLast',
                'ranking' => [
                    'geo',
                ],
                'reRankingApplyFilter' => 'mySearch:filters',
                'relevancyStrictness' => 10,
                'removeStopWords' => false,
                'removeWordsIfNoResults' => 'lastWords',
                'renderingContent' => ['facetOrdering' => ['facets' => ['order' => [
                    'a',

                    'b',
                ],
                ],
                    'values' => ['a' => ['order' => [
                        'b',
                    ],
                        'sortRemainingBy' => 'count',
                    ],
                    ],
                ],
                ],
                'replaceSynonymsInHighlight' => true,
                'replicas' => [
                    '',
                ],
                'responseFields' => [
                    'algolia',
                ],
                'restrictHighlightAndSnippetArrays' => true,
                'searchableAttributes' => [
                    'foo',
                ],
                'semanticSearch' => ['eventSources' => [
                    'foo',
                ],
                ],
                'separatorsToIndex' => 'bar',
                'snippetEllipsisText' => '---',
                'sortFacetValuesBy' => 'date',
                'typoTolerance' => false,
                'unretrievableAttributes' => [
                    'foo',
                ],
                'userData' => ['user' => 'data',
                ],
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/indexes/theIndexName/settings',
                'method' => 'PUT',
                'body' => json_decode('{"advancedSyntax":true,"advancedSyntaxFeatures":["exactPhrase"],"allowCompressionOfIntegerArray":true,"allowTyposOnNumericTokens":true,"alternativesAsExact":["singleWordSynonym"],"attributeCriteriaComputedByMinProximity":true,"attributeForDistinct":"test","attributesForFaceting":["algolia"],"attributesToHighlight":["algolia"],"attributesToRetrieve":["algolia"],"attributesToSnippet":["algolia"],"attributesToTransliterate":["algolia"],"camelCaseAttributes":["algolia"],"customNormalization":{"algolia":{"aloglia":"aglolia"}},"customRanking":["algolia"],"decompoundQuery":false,"decompoundedAttributes":{"algolia":"aloglia"},"disableExactOnAttributes":["algolia"],"disablePrefixOnAttributes":["algolia"],"disableTypoToleranceOnAttributes":["algolia"],"disableTypoToleranceOnWords":["algolia"],"distinct":3,"enablePersonalization":true,"enableReRanking":false,"enableRules":true,"exactOnSingleWordQuery":"attribute","highlightPreTag":"<span>","highlightPostTag":"</span>","hitsPerPage":10,"ignorePlurals":false,"indexLanguages":["algolia"],"keepDiacriticsOnCharacters":"abc","maxFacetHits":20,"maxValuesPerFacet":30,"minProximity":6,"minWordSizefor1Typo":5,"minWordSizefor2Typos":11,"mode":"neuralSearch","numericAttributesForFiltering":["algolia"],"optionalWords":["myspace"],"paginationLimitedTo":0,"queryLanguages":["algolia"],"queryType":"prefixLast","ranking":["geo"],"reRankingApplyFilter":"mySearch:filters","relevancyStrictness":10,"removeStopWords":false,"removeWordsIfNoResults":"lastWords","renderingContent":{"facetOrdering":{"facets":{"order":["a","b"]},"values":{"a":{"order":["b"],"sortRemainingBy":"count"}}}},"replaceSynonymsInHighlight":true,"replicas":[""],"responseFields":["algolia"],"restrictHighlightAndSnippetArrays":true,"searchableAttributes":["foo"],"semanticSearch":{"eventSources":["foo"]},"separatorsToIndex":"bar","snippetEllipsisText":"---","sortFacetValuesBy":"date","typoTolerance":false,"unretrievableAttributes":["foo"],"userData":{"user":"data"}}'),
            ],
        ]);
    }

    /**
     * Test case for UpdateApiKey
     * updateApiKey.
     */
    public function testUpdateApiKey0()
    {
        $client = $this->getClient();
        $client->updateApiKey(
            'myApiKey',
            ['acl' => [
                'search',

                'addObject',
            ],
                'validity' => 300,
                'maxQueriesPerIPPerHour' => 100,
                'maxHitsPerQuery' => 20,
            ],
        );

        $this->assertRequests([
            [
                'path' => '/1/keys/myApiKey',
                'method' => 'PUT',
                'body' => json_decode('{"acl":["search","addObject"],"validity":300,"maxQueriesPerIPPerHour":100,"maxHitsPerQuery":20}'),
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
        $api = new ApiWrapper($this, SearchConfig::create(getenv('ALGOLIA_APP_ID'), getenv('ALGOLIA_API_KEY')), ClusterHosts::create('127.0.0.1'));
        $config = SearchConfig::create('foo', 'bar');

        return new SearchClient($api, $config);
    }
}
