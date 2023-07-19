import type { EchoResponse, RequestOptions } from '@algolia/client-common';
import { searchClient } from '@algolia/client-search';
import { echoRequester } from '@algolia/requester-node-http';

const appId = process.env.ALGOLIA_APPLICATION_ID || 'test_app_id';
const apiKey = process.env.ALGOLIA_SEARCH_KEY || 'test_api_key';

const client = searchClient(appId, apiKey, { requester: echoRequester() });

describe('addApiKey', () => {
  test('addApiKey', async () => {
    const req = (await client.addApiKey({
      acl: ['search', 'addObject'],
      description: 'my new api key',
      validity: 300,
      maxQueriesPerIPPerHour: 100,
      maxHitsPerQuery: 20,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/keys');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      acl: ['search', 'addObject'],
      description: 'my new api key',
      validity: 300,
      maxQueriesPerIPPerHour: 100,
      maxHitsPerQuery: 20,
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('addOrUpdateObject', () => {
  test('addOrUpdateObject', async () => {
    const req = (await client.addOrUpdateObject({
      indexName: 'indexName',
      objectID: 'uniqueID',
      body: { key: 'value' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/uniqueID');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({ key: 'value' });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('appendSource', () => {
  test('appendSource', async () => {
    const req = (await client.appendSource({
      source: 'theSource',
      description: 'theDescription',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/security/sources/append');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      source: 'theSource',
      description: 'theDescription',
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('assignUserId', () => {
  test('assignUserId', async () => {
    const req = (await client.assignUserId({
      xAlgoliaUserID: 'userID',
      assignUserIdParams: { cluster: 'theCluster' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/clusters/mapping');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ cluster: 'theCluster' });
    expect(req.searchParams).toStrictEqual(undefined);
    expect(req.headers).toEqual(
      expect.objectContaining({ 'x-algolia-user-id': 'userID' })
    );
  });
});

describe('batch', () => {
  test('allows batch method with `addObject` action', async () => {
    const req = (await client.batch({
      indexName: 'theIndexName',
      batchWriteParams: {
        requests: [{ action: 'addObject', body: { key: 'value' } }],
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/batch');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [{ action: 'addObject', body: { key: 'value' } }],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('allows batch method with `clear` action', async () => {
    const req = (await client.batch({
      indexName: 'theIndexName',
      batchWriteParams: {
        requests: [{ action: 'clear', body: { key: 'value' } }],
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/batch');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [{ action: 'clear', body: { key: 'value' } }],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('allows batch method with `delete` action', async () => {
    const req = (await client.batch({
      indexName: 'theIndexName',
      batchWriteParams: {
        requests: [{ action: 'delete', body: { key: 'value' } }],
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/batch');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [{ action: 'delete', body: { key: 'value' } }],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('allows batch method with `deleteObject` action', async () => {
    const req = (await client.batch({
      indexName: 'theIndexName',
      batchWriteParams: {
        requests: [{ action: 'deleteObject', body: { key: 'value' } }],
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/batch');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [{ action: 'deleteObject', body: { key: 'value' } }],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('allows batch method with `partialUpdateObject` action', async () => {
    const req = (await client.batch({
      indexName: 'theIndexName',
      batchWriteParams: {
        requests: [{ action: 'partialUpdateObject', body: { key: 'value' } }],
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/batch');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [{ action: 'partialUpdateObject', body: { key: 'value' } }],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('allows batch method with `partialUpdateObjectNoCreate` action', async () => {
    const req = (await client.batch({
      indexName: 'theIndexName',
      batchWriteParams: {
        requests: [
          { action: 'partialUpdateObjectNoCreate', body: { key: 'value' } },
        ],
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/batch');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [
        { action: 'partialUpdateObjectNoCreate', body: { key: 'value' } },
      ],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('allows batch method with `updateObject` action', async () => {
    const req = (await client.batch({
      indexName: 'theIndexName',
      batchWriteParams: {
        requests: [{ action: 'updateObject', body: { key: 'value' } }],
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/batch');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [{ action: 'updateObject', body: { key: 'value' } }],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('batchAssignUserIds', () => {
  test('batchAssignUserIds', async () => {
    const req = (await client.batchAssignUserIds({
      xAlgoliaUserID: 'userID',
      batchAssignUserIdsParams: {
        cluster: 'theCluster',
        users: ['user1', 'user2'],
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/clusters/mapping/batch');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      cluster: 'theCluster',
      users: ['user1', 'user2'],
    });
    expect(req.searchParams).toStrictEqual(undefined);
    expect(req.headers).toEqual(
      expect.objectContaining({ 'x-algolia-user-id': 'userID' })
    );
  });
});

describe('batchDictionaryEntries', () => {
  test('get batchDictionaryEntries results with minimal parameters', async () => {
    const req = (await client.batchDictionaryEntries({
      dictionaryName: 'compounds',
      batchDictionaryEntriesParams: {
        requests: [
          { action: 'addEntry', body: { objectID: '1', language: 'en' } },
          { action: 'deleteEntry', body: { objectID: '2', language: 'fr' } },
        ],
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/dictionaries/compounds/batch');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [
        { action: 'addEntry', body: { objectID: '1', language: 'en' } },
        { action: 'deleteEntry', body: { objectID: '2', language: 'fr' } },
      ],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('get batchDictionaryEntries results with all parameters', async () => {
    const req = (await client.batchDictionaryEntries({
      dictionaryName: 'compounds',
      batchDictionaryEntriesParams: {
        clearExistingDictionaryEntries: false,
        requests: [
          {
            action: 'addEntry',
            body: {
              objectID: '1',
              language: 'en',
              word: 'fancy',
              words: ['believe', 'algolia'],
              decomposition: ['trust', 'algolia'],
              state: 'enabled',
            },
          },
          {
            action: 'deleteEntry',
            body: {
              objectID: '2',
              language: 'fr',
              word: 'humility',
              words: ['candor', 'algolia'],
              decomposition: ['grit', 'algolia'],
              state: 'enabled',
            },
          },
        ],
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/dictionaries/compounds/batch');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      clearExistingDictionaryEntries: false,
      requests: [
        {
          action: 'addEntry',
          body: {
            objectID: '1',
            language: 'en',
            word: 'fancy',
            words: ['believe', 'algolia'],
            decomposition: ['trust', 'algolia'],
            state: 'enabled',
          },
        },
        {
          action: 'deleteEntry',
          body: {
            objectID: '2',
            language: 'fr',
            word: 'humility',
            words: ['candor', 'algolia'],
            decomposition: ['grit', 'algolia'],
            state: 'enabled',
          },
        },
      ],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('get batchDictionaryEntries results additional properties', async () => {
    const req = (await client.batchDictionaryEntries({
      dictionaryName: 'compounds',
      batchDictionaryEntriesParams: {
        requests: [
          {
            action: 'addEntry',
            body: { objectID: '1', language: 'en', additional: 'try me' },
          },
        ],
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/dictionaries/compounds/batch');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [
        {
          action: 'addEntry',
          body: { objectID: '1', language: 'en', additional: 'try me' },
        },
      ],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('browse', () => {
  test('browse with minimal parameters', async () => {
    const req = (await client.browse({
      indexName: 'indexName',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/browse');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({});
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('browse with search parameters', async () => {
    const req = (await client.browse({
      indexName: 'indexName',
      browseParams: { query: 'myQuery', facetFilters: ['tags:algolia'] },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/browse');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      query: 'myQuery',
      facetFilters: ['tags:algolia'],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('browse allow a cursor in parameters', async () => {
    const req = (await client.browse({
      indexName: 'indexName',
      browseParams: { cursor: 'test' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/browse');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ cursor: 'test' });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('clearAllSynonyms', () => {
  test('clearAllSynonyms', async () => {
    const req = (await client.clearAllSynonyms({
      indexName: 'indexName',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/synonyms/clear');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('clearObjects', () => {
  test('clearObjects', async () => {
    const req = (await client.clearObjects({
      indexName: 'theIndexName',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/clear');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('clearRules', () => {
  test('clearRules', async () => {
    const req = (await client.clearRules({
      indexName: 'indexName',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/rules/clear');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('del', () => {
  test('allow del method for a custom path with minimal parameters', async () => {
    const req = (await client.del({
      path: '/test/minimal',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/minimal');
    expect(req.method).toEqual('DELETE');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('allow del method for a custom path with all parameters', async () => {
    const req = (await client.del({
      path: '/test/all',
      parameters: { query: 'parameters' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/all');
    expect(req.method).toEqual('DELETE');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual({ query: 'parameters' });
  });
});

describe('deleteApiKey', () => {
  test('deleteApiKey', async () => {
    const req = (await client.deleteApiKey({
      key: 'myTestApiKey',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/keys/myTestApiKey');
    expect(req.method).toEqual('DELETE');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('deleteBy', () => {
  test('deleteBy', async () => {
    const req = (await client.deleteBy({
      indexName: 'theIndexName',
      deleteByParams: { filters: 'brand:brandName' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/deleteByQuery');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ filters: 'brand:brandName' });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('deleteIndex', () => {
  test('deleteIndex', async () => {
    const req = (await client.deleteIndex({
      indexName: 'theIndexName',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName');
    expect(req.method).toEqual('DELETE');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('deleteObject', () => {
  test('deleteObject', async () => {
    const req = (await client.deleteObject({
      indexName: 'theIndexName',
      objectID: 'uniqueID',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/uniqueID');
    expect(req.method).toEqual('DELETE');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('deleteRule', () => {
  test('deleteRule', async () => {
    const req = (await client.deleteRule({
      indexName: 'indexName',
      objectID: 'id1',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/rules/id1');
    expect(req.method).toEqual('DELETE');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('deleteSource', () => {
  test('deleteSource', async () => {
    const req = (await client.deleteSource({
      source: 'theSource',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/security/sources/theSource');
    expect(req.method).toEqual('DELETE');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('deleteSynonym', () => {
  test('deleteSynonym', async () => {
    const req = (await client.deleteSynonym({
      indexName: 'indexName',
      objectID: 'id1',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/synonyms/id1');
    expect(req.method).toEqual('DELETE');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('get', () => {
  test('allow get method for a custom path with minimal parameters', async () => {
    const req = (await client.get({
      path: '/test/minimal',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/minimal');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('allow get method for a custom path with all parameters', async () => {
    const req = (await client.get({
      path: '/test/all',
      parameters: { query: 'parameters' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/all');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual({ query: 'parameters' });
  });
});

describe('getApiKey', () => {
  test('getApiKey', async () => {
    const req = (await client.getApiKey({
      key: 'myTestApiKey',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/keys/myTestApiKey');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getDictionaryLanguages', () => {
  test('get getDictionaryLanguages', async () => {
    const req =
      (await client.getDictionaryLanguages()) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/dictionaries/*/languages');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getDictionarySettings', () => {
  test('get getDictionarySettings results', async () => {
    const req =
      (await client.getDictionarySettings()) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/dictionaries/*/settings');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getLogs', () => {
  test('getLogs with minimal parameters', async () => {
    const req = (await client.getLogs()) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/logs');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('getLogs with parameters', async () => {
    const req = (await client.getLogs({
      offset: 5,
      length: 10,
      indexName: 'theIndexName',
      type: 'all',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/logs');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual({
      offset: '5',
      length: '10',
      indexName: 'theIndexName',
      type: 'all',
    });
  });
});

describe('getObject', () => {
  test('getObject', async () => {
    const req = (await client.getObject({
      indexName: 'theIndexName',
      objectID: 'uniqueID',
      attributesToRetrieve: ['attr1', 'attr2'],
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/uniqueID');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual({
      attributesToRetrieve: 'attr1,attr2',
    });
  });
});

describe('getObjects', () => {
  test('getObjects', async () => {
    const req = (await client.getObjects({
      requests: [
        {
          attributesToRetrieve: ['attr1', 'attr2'],
          objectID: 'uniqueID',
          indexName: 'theIndexName',
        },
      ],
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/*/objects');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [
        {
          attributesToRetrieve: ['attr1', 'attr2'],
          objectID: 'uniqueID',
          indexName: 'theIndexName',
        },
      ],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getRule', () => {
  test('getRule', async () => {
    const req = (await client.getRule({
      indexName: 'indexName',
      objectID: 'id1',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/rules/id1');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getSettings', () => {
  test('getSettings', async () => {
    const req = (await client.getSettings({
      indexName: 'theIndexName',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/settings');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getSources', () => {
  test('getSources', async () => {
    const req = (await client.getSources()) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/security/sources');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getSynonym', () => {
  test('getSynonym', async () => {
    const req = (await client.getSynonym({
      indexName: 'indexName',
      objectID: 'id1',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/synonyms/id1');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getTask', () => {
  test('getTask', async () => {
    const req = (await client.getTask({
      indexName: 'theIndexName',
      taskID: 123,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/task/123');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getTopUserIds', () => {
  test('getTopUserIds', async () => {
    const req = (await client.getTopUserIds()) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/clusters/mapping/top');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getUserId', () => {
  test('getUserId', async () => {
    const req = (await client.getUserId({
      userID: 'uniqueID',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/clusters/mapping/uniqueID');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('hasPendingMappings', () => {
  test('hasPendingMappings with minimal parameters', async () => {
    const req = (await client.hasPendingMappings()) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/clusters/mapping/pending');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('hasPendingMappings with parameters', async () => {
    const req = (await client.hasPendingMappings({
      getClusters: true,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/clusters/mapping/pending');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual({ getClusters: 'true' });
  });
});

describe('listApiKeys', () => {
  test('listApiKeys', async () => {
    const req = (await client.listApiKeys()) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/keys');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('listClusters', () => {
  test('listClusters', async () => {
    const req = (await client.listClusters()) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/clusters');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('listIndices', () => {
  test('listIndices with minimal parameters', async () => {
    const req = (await client.listIndices()) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('listIndices with parameters', async () => {
    const req = (await client.listIndices({
      page: 8,
      hitsPerPage: 3,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual({ page: '8', hitsPerPage: '3' });
  });
});

describe('listUserIds', () => {
  test('listUserIds with minimal parameters', async () => {
    const req = (await client.listUserIds()) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/clusters/mapping');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('listUserIds with parameters', async () => {
    const req = (await client.listUserIds({
      page: 8,
      hitsPerPage: 100,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/clusters/mapping');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual({ page: '8', hitsPerPage: '100' });
  });
});

describe('multipleBatch', () => {
  test('multipleBatch', async () => {
    const req = (await client.multipleBatch({
      requests: [
        {
          action: 'addObject',
          body: { key: 'value' },
          indexName: 'theIndexName',
        },
      ],
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/*/batch');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [
        {
          action: 'addObject',
          body: { key: 'value' },
          indexName: 'theIndexName',
        },
      ],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('operationIndex', () => {
  test('operationIndex', async () => {
    const req = (await client.operationIndex({
      indexName: 'theIndexName',
      operationIndexParams: {
        operation: 'copy',
        destination: 'dest',
        scope: ['rules', 'settings'],
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/operation');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      operation: 'copy',
      destination: 'dest',
      scope: ['rules', 'settings'],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('partialUpdateObject', () => {
  test('partialUpdateObject', async () => {
    const req = (await client.partialUpdateObject({
      indexName: 'theIndexName',
      objectID: 'uniqueID',
      attributesToUpdate: {
        id1: 'test',
        id2: { _operation: 'AddUnique', value: 'test2' },
      },
      createIfNotExists: true,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/uniqueID/partial');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      id1: 'test',
      id2: { _operation: 'AddUnique', value: 'test2' },
    });
    expect(req.searchParams).toStrictEqual({ createIfNotExists: 'true' });
  });
});

describe('post', () => {
  test('allow post method for a custom path with minimal parameters', async () => {
    const req = (await client.post({
      path: '/test/minimal',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/minimal');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({});
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('allow post method for a custom path with all parameters', async () => {
    const req = (await client.post({
      path: '/test/all',
      parameters: { query: 'parameters' },
      body: { body: 'parameters' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/all');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ body: 'parameters' });
    expect(req.searchParams).toStrictEqual({ query: 'parameters' });
  });

  test('requestOptions can override default query parameters', async () => {
    const requestOptions: RequestOptions = {
      queryParameters: { query: 'myQueryParameter' },
    };

    const req = (await client.post(
      {
        path: '/test/requestOptions',
        parameters: { query: 'parameters' },
        body: { facet: 'filters' },
      },
      requestOptions
    )) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/requestOptions');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ facet: 'filters' });
    expect(req.searchParams).toStrictEqual({ query: 'myQueryParameter' });
  });

  test('requestOptions merges query parameters with default ones', async () => {
    const requestOptions: RequestOptions = {
      queryParameters: { query2: 'myQueryParameter' },
    };

    const req = (await client.post(
      {
        path: '/test/requestOptions',
        parameters: { query: 'parameters' },
        body: { facet: 'filters' },
      },
      requestOptions
    )) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/requestOptions');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ facet: 'filters' });
    expect(req.searchParams).toStrictEqual({
      query: 'parameters',
      query2: 'myQueryParameter',
    });
  });

  test('requestOptions can override default headers', async () => {
    const requestOptions: RequestOptions = {
      headers: { 'x-algolia-api-key': 'myApiKey' },
    };

    const req = (await client.post(
      {
        path: '/test/requestOptions',
        parameters: { query: 'parameters' },
        body: { facet: 'filters' },
      },
      requestOptions
    )) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/requestOptions');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ facet: 'filters' });
    expect(req.searchParams).toStrictEqual({ query: 'parameters' });
    expect(req.headers).toEqual(
      expect.objectContaining({ 'x-algolia-api-key': 'myApiKey' })
    );
  });

  test('requestOptions merges headers with default ones', async () => {
    const requestOptions: RequestOptions = {
      headers: { 'x-algolia-api-key': 'myApiKey' },
    };

    const req = (await client.post(
      {
        path: '/test/requestOptions',
        parameters: { query: 'parameters' },
        body: { facet: 'filters' },
      },
      requestOptions
    )) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/requestOptions');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ facet: 'filters' });
    expect(req.searchParams).toStrictEqual({ query: 'parameters' });
    expect(req.headers).toEqual(
      expect.objectContaining({ 'x-algolia-api-key': 'myApiKey' })
    );
  });

  test('requestOptions queryParameters accepts booleans', async () => {
    const requestOptions: RequestOptions = {
      queryParameters: { isItWorking: true },
    };

    const req = (await client.post(
      {
        path: '/test/requestOptions',
        parameters: { query: 'parameters' },
        body: { facet: 'filters' },
      },
      requestOptions
    )) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/requestOptions');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ facet: 'filters' });
    expect(req.searchParams).toStrictEqual({
      query: 'parameters',
      isItWorking: 'true',
    });
  });

  test('requestOptions queryParameters accepts integers', async () => {
    const requestOptions: RequestOptions = {
      queryParameters: { myParam: 2 },
    };

    const req = (await client.post(
      {
        path: '/test/requestOptions',
        parameters: { query: 'parameters' },
        body: { facet: 'filters' },
      },
      requestOptions
    )) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/requestOptions');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ facet: 'filters' });
    expect(req.searchParams).toStrictEqual({
      query: 'parameters',
      myParam: '2',
    });
  });

  test('requestOptions queryParameters accepts list of string', async () => {
    const requestOptions: RequestOptions = {
      queryParameters: { myParam: ['c', 'd'] },
    };

    const req = (await client.post(
      {
        path: '/test/requestOptions',
        parameters: { query: 'parameters' },
        body: { facet: 'filters' },
      },
      requestOptions
    )) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/requestOptions');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ facet: 'filters' });
    expect(req.searchParams).toStrictEqual({
      query: 'parameters',
      myParam: 'c,d',
    });
  });

  test('requestOptions queryParameters accepts list of booleans', async () => {
    const requestOptions: RequestOptions = {
      queryParameters: { myParam: [true, true, false] },
    };

    const req = (await client.post(
      {
        path: '/test/requestOptions',
        parameters: { query: 'parameters' },
        body: { facet: 'filters' },
      },
      requestOptions
    )) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/requestOptions');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ facet: 'filters' });
    expect(req.searchParams).toStrictEqual({
      query: 'parameters',
      myParam: 'true,true,false',
    });
  });

  test('requestOptions queryParameters accepts list of integers', async () => {
    const requestOptions: RequestOptions = {
      queryParameters: { myParam: [1, 2] },
    };

    const req = (await client.post(
      {
        path: '/test/requestOptions',
        parameters: { query: 'parameters' },
        body: { facet: 'filters' },
      },
      requestOptions
    )) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/requestOptions');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ facet: 'filters' });
    expect(req.searchParams).toStrictEqual({
      query: 'parameters',
      myParam: '1,2',
    });
  });
});

describe('put', () => {
  test('allow put method for a custom path with minimal parameters', async () => {
    const req = (await client.put({
      path: '/test/minimal',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/minimal');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({});
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('allow put method for a custom path with all parameters', async () => {
    const req = (await client.put({
      path: '/test/all',
      parameters: { query: 'parameters' },
      body: { body: 'parameters' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/test/all');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({ body: 'parameters' });
    expect(req.searchParams).toStrictEqual({ query: 'parameters' });
  });
});

describe('removeUserId', () => {
  test('removeUserId', async () => {
    const req = (await client.removeUserId({
      userID: 'uniqueID',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/clusters/mapping/uniqueID');
    expect(req.method).toEqual('DELETE');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('replaceSources', () => {
  test('replaceSources', async () => {
    const req = (await client.replaceSources({
      source: [{ source: 'theSource', description: 'theDescription' }],
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/security/sources');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual([
      { source: 'theSource', description: 'theDescription' },
    ]);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('restoreApiKey', () => {
  test('restoreApiKey', async () => {
    const req = (await client.restoreApiKey({
      key: 'myApiKey',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/keys/myApiKey/restore');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('saveObject', () => {
  test('saveObject', async () => {
    const req = (await client.saveObject({
      indexName: 'theIndexName',
      body: { objectID: 'id', test: 'val' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ objectID: 'id', test: 'val' });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('saveRule', () => {
  test('saveRule with minimal parameters', async () => {
    const req = (await client.saveRule({
      indexName: 'indexName',
      objectID: 'id1',
      rule: {
        objectID: 'id1',
        conditions: [{ pattern: 'apple', anchoring: 'contains' }],
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/rules/id1');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({
      objectID: 'id1',
      conditions: [{ pattern: 'apple', anchoring: 'contains' }],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('saveRule with all parameters', async () => {
    const req = (await client.saveRule({
      indexName: 'indexName',
      objectID: 'id1',
      rule: {
        objectID: 'id1',
        conditions: [
          {
            pattern: 'apple',
            anchoring: 'contains',
            alternatives: false,
            context: 'search',
          },
        ],
        consequence: {
          params: {
            filters: 'brand:apple',
            query: {
              remove: ['algolia'],
              edits: [
                { type: 'remove', delete: 'abc', insert: 'cde' },
                { type: 'replace', delete: 'abc', insert: 'cde' },
              ],
            },
          },
          hide: [{ objectID: '321' }],
          filterPromotes: false,
          userData: { algolia: 'aloglia' },
          promote: [
            { objectID: 'abc', position: 3 },
            { objectIDs: ['abc', 'def'], position: 1 },
          ],
        },
        description: 'test',
        enabled: true,
        validity: [{ from: 1656670273, until: 1656670277 }],
      },
      forwardToReplicas: true,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/rules/id1');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({
      objectID: 'id1',
      conditions: [
        {
          pattern: 'apple',
          anchoring: 'contains',
          alternatives: false,
          context: 'search',
        },
      ],
      consequence: {
        params: {
          filters: 'brand:apple',
          query: {
            remove: ['algolia'],
            edits: [
              { type: 'remove', delete: 'abc', insert: 'cde' },
              { type: 'replace', delete: 'abc', insert: 'cde' },
            ],
          },
        },
        hide: [{ objectID: '321' }],
        filterPromotes: false,
        userData: { algolia: 'aloglia' },
        promote: [
          { objectID: 'abc', position: 3 },
          { objectIDs: ['abc', 'def'], position: 1 },
        ],
      },
      description: 'test',
      enabled: true,
      validity: [{ from: 1656670273, until: 1656670277 }],
    });
    expect(req.searchParams).toStrictEqual({ forwardToReplicas: 'true' });
  });
});

describe('saveRules', () => {
  test('saveRules with minimal parameters', async () => {
    const req = (await client.saveRules({
      indexName: 'indexName',
      rules: [
        {
          objectID: 'a-rule-id',
          conditions: [{ pattern: 'smartphone', anchoring: 'contains' }],
        },
        {
          objectID: 'a-second-rule-id',
          conditions: [{ pattern: 'apple', anchoring: 'contains' }],
        },
      ],
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/rules/batch');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual([
      {
        objectID: 'a-rule-id',
        conditions: [{ pattern: 'smartphone', anchoring: 'contains' }],
      },
      {
        objectID: 'a-second-rule-id',
        conditions: [{ pattern: 'apple', anchoring: 'contains' }],
      },
    ]);
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('saveRules with all parameters', async () => {
    const req = (await client.saveRules({
      indexName: 'indexName',
      rules: [
        {
          objectID: 'id1',
          conditions: [
            {
              pattern: 'apple',
              anchoring: 'contains',
              alternatives: false,
              context: 'search',
            },
          ],
          consequence: {
            params: {
              filters: 'brand:apple',
              query: {
                remove: ['algolia'],
                edits: [
                  { type: 'remove', delete: 'abc', insert: 'cde' },
                  { type: 'replace', delete: 'abc', insert: 'cde' },
                ],
              },
            },
            hide: [{ objectID: '321' }],
            filterPromotes: false,
            userData: { algolia: 'aloglia' },
            promote: [
              { objectID: 'abc', position: 3 },
              { objectIDs: ['abc', 'def'], position: 1 },
            ],
          },
          description: 'test',
          enabled: true,
          validity: [{ from: 1656670273, until: 1656670277 }],
        },
      ],
      forwardToReplicas: true,
      clearExistingRules: true,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/rules/batch');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual([
      {
        objectID: 'id1',
        conditions: [
          {
            pattern: 'apple',
            anchoring: 'contains',
            alternatives: false,
            context: 'search',
          },
        ],
        consequence: {
          params: {
            filters: 'brand:apple',
            query: {
              remove: ['algolia'],
              edits: [
                { type: 'remove', delete: 'abc', insert: 'cde' },
                { type: 'replace', delete: 'abc', insert: 'cde' },
              ],
            },
          },
          hide: [{ objectID: '321' }],
          filterPromotes: false,
          userData: { algolia: 'aloglia' },
          promote: [
            { objectID: 'abc', position: 3 },
            { objectIDs: ['abc', 'def'], position: 1 },
          ],
        },
        description: 'test',
        enabled: true,
        validity: [{ from: 1656670273, until: 1656670277 }],
      },
    ]);
    expect(req.searchParams).toStrictEqual({
      forwardToReplicas: 'true',
      clearExistingRules: 'true',
    });
  });
});

describe('saveSynonym', () => {
  test('saveSynonym', async () => {
    const req = (await client.saveSynonym({
      indexName: 'indexName',
      objectID: 'id1',
      synonymHit: {
        objectID: 'id1',
        type: 'synonym',
        synonyms: ['car', 'vehicule', 'auto'],
      },
      forwardToReplicas: true,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/synonyms/id1');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({
      objectID: 'id1',
      type: 'synonym',
      synonyms: ['car', 'vehicule', 'auto'],
    });
    expect(req.searchParams).toStrictEqual({ forwardToReplicas: 'true' });
  });
});

describe('saveSynonyms', () => {
  test('saveSynonyms', async () => {
    const req = (await client.saveSynonyms({
      indexName: 'indexName',
      synonymHit: [
        {
          objectID: 'id1',
          type: 'synonym',
          synonyms: ['car', 'vehicule', 'auto'],
        },
        {
          objectID: 'id2',
          type: 'onewaysynonym',
          input: 'iphone',
          synonyms: ['ephone', 'aphone', 'yphone'],
        },
      ],
      forwardToReplicas: true,
      replaceExistingSynonyms: false,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/synonyms/batch');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual([
      {
        objectID: 'id1',
        type: 'synonym',
        synonyms: ['car', 'vehicule', 'auto'],
      },
      {
        objectID: 'id2',
        type: 'onewaysynonym',
        input: 'iphone',
        synonyms: ['ephone', 'aphone', 'yphone'],
      },
    ]);
    expect(req.searchParams).toStrictEqual({
      forwardToReplicas: 'true',
      replaceExistingSynonyms: 'false',
    });
  });
});

describe('search', () => {
  test('search for a single hits request with minimal parameters', async () => {
    const req = (await client.search({
      requests: [{ indexName: 'theIndexName' }],
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/*/queries');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ requests: [{ indexName: 'theIndexName' }] });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('search for a single facet request with minimal parameters', async () => {
    const req = (await client.search({
      requests: [
        { indexName: 'theIndexName', type: 'facet', facet: 'theFacet' },
      ],
      strategy: 'stopIfEnoughMatches',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/*/queries');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [
        { indexName: 'theIndexName', type: 'facet', facet: 'theFacet' },
      ],
      strategy: 'stopIfEnoughMatches',
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('search for a single hits request with all parameters', async () => {
    const req = (await client.search({
      requests: [
        {
          indexName: 'theIndexName',
          query: 'myQuery',
          hitsPerPage: 50,
          type: 'default',
        },
      ],
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/*/queries');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [
        {
          indexName: 'theIndexName',
          query: 'myQuery',
          hitsPerPage: 50,
          type: 'default',
        },
      ],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('search for a single facet request with all parameters', async () => {
    const req = (await client.search({
      requests: [
        {
          indexName: 'theIndexName',
          type: 'facet',
          facet: 'theFacet',
          facetQuery: 'theFacetQuery',
          query: 'theQuery',
          maxFacetHits: 50,
        },
      ],
      strategy: 'stopIfEnoughMatches',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/*/queries');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [
        {
          indexName: 'theIndexName',
          type: 'facet',
          facet: 'theFacet',
          facetQuery: 'theFacetQuery',
          query: 'theQuery',
          maxFacetHits: 50,
        },
      ],
      strategy: 'stopIfEnoughMatches',
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('search for multiple mixed requests in multiple indices with minimal parameters', async () => {
    const req = (await client.search({
      requests: [
        { indexName: 'theIndexName' },
        { indexName: 'theIndexName2', type: 'facet', facet: 'theFacet' },
        { indexName: 'theIndexName', type: 'default' },
      ],
      strategy: 'stopIfEnoughMatches',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/*/queries');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [
        { indexName: 'theIndexName' },
        { indexName: 'theIndexName2', type: 'facet', facet: 'theFacet' },
        { indexName: 'theIndexName', type: 'default' },
      ],
      strategy: 'stopIfEnoughMatches',
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('search for multiple mixed requests in multiple indices with all parameters', async () => {
    const req = (await client.search({
      requests: [
        {
          indexName: 'theIndexName',
          type: 'facet',
          facet: 'theFacet',
          facetQuery: 'theFacetQuery',
          query: 'theQuery',
          maxFacetHits: 50,
        },
        {
          indexName: 'theIndexName',
          query: 'myQuery',
          hitsPerPage: 50,
          type: 'default',
        },
      ],
      strategy: 'stopIfEnoughMatches',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/*/queries');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [
        {
          indexName: 'theIndexName',
          type: 'facet',
          facet: 'theFacet',
          facetQuery: 'theFacetQuery',
          query: 'theQuery',
          maxFacetHits: 50,
        },
        {
          indexName: 'theIndexName',
          query: 'myQuery',
          hitsPerPage: 50,
          type: 'default',
        },
      ],
      strategy: 'stopIfEnoughMatches',
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('search filters accept all of the possible shapes', async () => {
    const req = (await client.search({
      requests: [
        {
          indexName: 'theIndexName',
          facetFilters: 'mySearch:filters',
          reRankingApplyFilter: 'mySearch:filters',
          tagFilters: 'mySearch:filters',
          numericFilters: 'mySearch:filters',
          optionalFilters: 'mySearch:filters',
        },
        {
          indexName: 'theIndexName',
          facetFilters: ['mySearch:filters', ['mySearch:filters']],
          reRankingApplyFilter: ['mySearch:filters', ['mySearch:filters']],
          tagFilters: ['mySearch:filters', ['mySearch:filters']],
          numericFilters: ['mySearch:filters', ['mySearch:filters']],
          optionalFilters: ['mySearch:filters', ['mySearch:filters']],
        },
      ],
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/*/queries');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [
        {
          indexName: 'theIndexName',
          facetFilters: 'mySearch:filters',
          reRankingApplyFilter: 'mySearch:filters',
          tagFilters: 'mySearch:filters',
          numericFilters: 'mySearch:filters',
          optionalFilters: 'mySearch:filters',
        },
        {
          indexName: 'theIndexName',
          facetFilters: ['mySearch:filters', ['mySearch:filters']],
          reRankingApplyFilter: ['mySearch:filters', ['mySearch:filters']],
          tagFilters: ['mySearch:filters', ['mySearch:filters']],
          numericFilters: ['mySearch:filters', ['mySearch:filters']],
          optionalFilters: ['mySearch:filters', ['mySearch:filters']],
        },
      ],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('search with all search parameters', async () => {
    const req = (await client.search({
      requests: [
        {
          indexName: 'theIndexName',
          query: '',
          similarQuery: '',
          filters: '',
          facetFilters: [''],
          optionalFilters: [''],
          numericFilters: [''],
          tagFilters: [''],
          sumOrFiltersScores: true,
          facets: [''],
          maxValuesPerFacet: 0,
          facetingAfterDistinct: true,
          sortFacetValuesBy: '',
          page: 0,
          offset: 0,
          length: 0,
          aroundLatLng: '',
          aroundLatLngViaIP: true,
          aroundRadius: 'all',
          aroundPrecision: 0,
          minimumAroundRadius: 0,
          insideBoundingBox: [47.3165, 4.9665],
          insidePolygon: [47.3165, 4.9665],
          naturalLanguages: [''],
          ruleContexts: [''],
          personalizationImpact: 0,
          userToken: '',
          getRankingInfo: true,
          clickAnalytics: true,
          analytics: true,
          analyticsTags: [''],
          percentileComputation: true,
          enableABTest: true,
          enableReRanking: true,
          reRankingApplyFilter: [''],
          attributesForFaceting: [''],
          attributesToRetrieve: [''],
          restrictSearchableAttributes: [''],
          ranking: [''],
          customRanking: [''],
          relevancyStrictness: 0,
          attributesToHighlight: [''],
          attributesToSnippet: [''],
          highlightPreTag: '',
          highlightPostTag: '',
          snippetEllipsisText: '',
          restrictHighlightAndSnippetArrays: true,
          hitsPerPage: 0,
          minWordSizefor1Typo: 0,
          minWordSizefor2Typos: 0,
          typoTolerance: 'min',
          allowTyposOnNumericTokens: true,
          disableTypoToleranceOnAttributes: [''],
          ignorePlurals: false,
          removeStopWords: true,
          keepDiacriticsOnCharacters: '',
          queryLanguages: [''],
          decompoundQuery: true,
          enableRules: true,
          enablePersonalization: true,
          queryType: 'prefixAll',
          removeWordsIfNoResults: 'allOptional',
          advancedSyntax: true,
          optionalWords: [''],
          disableExactOnAttributes: [''],
          exactOnSingleWordQuery: 'attribute',
          alternativesAsExact: ['multiWordsSynonym'],
          advancedSyntaxFeatures: ['exactPhrase'],
          distinct: 0,
          synonyms: true,
          replaceSynonymsInHighlight: true,
          minProximity: 0,
          responseFields: [''],
          attributeCriteriaComputedByMinProximity: true,
          renderingContent: {
            facetOrdering: {
              facets: { order: ['a', 'b'] },
              values: { a: { order: ['b'], sortRemainingBy: 'count' } },
            },
          },
          type: 'default',
        },
      ],
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/*/queries');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      requests: [
        {
          indexName: 'theIndexName',
          query: '',
          similarQuery: '',
          filters: '',
          facetFilters: [''],
          optionalFilters: [''],
          numericFilters: [''],
          tagFilters: [''],
          sumOrFiltersScores: true,
          facets: [''],
          maxValuesPerFacet: 0,
          facetingAfterDistinct: true,
          sortFacetValuesBy: '',
          page: 0,
          offset: 0,
          length: 0,
          aroundLatLng: '',
          aroundLatLngViaIP: true,
          aroundRadius: 'all',
          aroundPrecision: 0,
          minimumAroundRadius: 0,
          insideBoundingBox: [47.3165, 4.9665],
          insidePolygon: [47.3165, 4.9665],
          naturalLanguages: [''],
          ruleContexts: [''],
          personalizationImpact: 0,
          userToken: '',
          getRankingInfo: true,
          clickAnalytics: true,
          analytics: true,
          analyticsTags: [''],
          percentileComputation: true,
          enableABTest: true,
          enableReRanking: true,
          reRankingApplyFilter: [''],
          attributesForFaceting: [''],
          attributesToRetrieve: [''],
          restrictSearchableAttributes: [''],
          ranking: [''],
          customRanking: [''],
          relevancyStrictness: 0,
          attributesToHighlight: [''],
          attributesToSnippet: [''],
          highlightPreTag: '',
          highlightPostTag: '',
          snippetEllipsisText: '',
          restrictHighlightAndSnippetArrays: true,
          hitsPerPage: 0,
          minWordSizefor1Typo: 0,
          minWordSizefor2Typos: 0,
          typoTolerance: 'min',
          allowTyposOnNumericTokens: true,
          disableTypoToleranceOnAttributes: [''],
          ignorePlurals: false,
          removeStopWords: true,
          keepDiacriticsOnCharacters: '',
          queryLanguages: [''],
          decompoundQuery: true,
          enableRules: true,
          enablePersonalization: true,
          queryType: 'prefixAll',
          removeWordsIfNoResults: 'allOptional',
          advancedSyntax: true,
          optionalWords: [''],
          disableExactOnAttributes: [''],
          exactOnSingleWordQuery: 'attribute',
          alternativesAsExact: ['multiWordsSynonym'],
          advancedSyntaxFeatures: ['exactPhrase'],
          distinct: 0,
          synonyms: true,
          replaceSynonymsInHighlight: true,
          minProximity: 0,
          responseFields: [''],
          attributeCriteriaComputedByMinProximity: true,
          renderingContent: {
            facetOrdering: {
              facets: { order: ['a', 'b'] },
              values: { a: { order: ['b'], sortRemainingBy: 'count' } },
            },
          },
          type: 'default',
        },
      ],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('searchDictionaryEntries', () => {
  test('get searchDictionaryEntries results with minimal parameters', async () => {
    const req = (await client.searchDictionaryEntries({
      dictionaryName: 'compounds',
      searchDictionaryEntriesParams: { query: 'foo' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/dictionaries/compounds/search');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ query: 'foo' });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('get searchDictionaryEntries results with all parameters', async () => {
    const req = (await client.searchDictionaryEntries({
      dictionaryName: 'compounds',
      searchDictionaryEntriesParams: {
        query: 'foo',
        page: 4,
        hitsPerPage: 2,
        language: 'fr',
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/dictionaries/compounds/search');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      query: 'foo',
      page: 4,
      hitsPerPage: 2,
      language: 'fr',
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('searchForFacetValues', () => {
  test('get searchForFacetValues results with minimal parameters', async () => {
    const req = (await client.searchForFacetValues({
      indexName: 'indexName',
      facetName: 'facetName',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/facets/facetName/query');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({});
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('get searchForFacetValues results with all parameters', async () => {
    const req = (await client.searchForFacetValues({
      indexName: 'indexName',
      facetName: 'facetName',
      searchForFacetValuesRequest: {
        params: "query=foo&facetFilters=['bar']",
        facetQuery: 'foo',
        maxFacetHits: 42,
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/facets/facetName/query');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      params: "query=foo&facetFilters=['bar']",
      facetQuery: 'foo',
      maxFacetHits: 42,
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('searchRules', () => {
  test('searchRules', async () => {
    const req = (await client.searchRules({
      indexName: 'indexName',
      searchRulesParams: { query: 'something' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/rules/search');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ query: 'something' });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('searchSingleIndex', () => {
  test('search with minimal parameters', async () => {
    const req = (await client.searchSingleIndex({
      indexName: 'indexName',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/query');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({});
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('search with searchParams', async () => {
    const req = (await client.searchSingleIndex({
      indexName: 'indexName',
      searchParams: { query: 'myQuery', facetFilters: ['tags:algolia'] },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/query');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      query: 'myQuery',
      facetFilters: ['tags:algolia'],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('searchSynonyms', () => {
  test('searchSynonyms with minimal parameters', async () => {
    const req = (await client.searchSynonyms({
      indexName: 'indexName',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/synonyms/search');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({});
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('searchSynonyms with all parameters', async () => {
    const req = (await client.searchSynonyms({
      indexName: 'indexName',
      type: 'altcorrection1',
      page: 10,
      hitsPerPage: 10,
      searchSynonymsParams: { query: 'myQuery' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/indexName/synonyms/search');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({ query: 'myQuery' });
    expect(req.searchParams).toStrictEqual({
      type: 'altcorrection1',
      page: '10',
      hitsPerPage: '10',
    });
  });
});

describe('searchUserIds', () => {
  test('searchUserIds', async () => {
    const req = (await client.searchUserIds({
      query: 'test',
      clusterName: 'theClusterName',
      page: 5,
      hitsPerPage: 10,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/clusters/mapping/search');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      query: 'test',
      clusterName: 'theClusterName',
      page: 5,
      hitsPerPage: 10,
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('setDictionarySettings', () => {
  test('get setDictionarySettings results with minimal parameters', async () => {
    const req = (await client.setDictionarySettings({
      disableStandardEntries: { plurals: { fr: false, en: false, ru: true } },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/dictionaries/*/settings');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({
      disableStandardEntries: { plurals: { fr: false, en: false, ru: true } },
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('get setDictionarySettings results with all parameters', async () => {
    const req = (await client.setDictionarySettings({
      disableStandardEntries: {
        plurals: { fr: false, en: false, ru: true },
        stopwords: { fr: false },
        compounds: { ru: true },
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/dictionaries/*/settings');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({
      disableStandardEntries: {
        plurals: { fr: false, en: false, ru: true },
        stopwords: { fr: false },
        compounds: { ru: true },
      },
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('setSettings', () => {
  test('setSettings with minimal parameters', async () => {
    const req = (await client.setSettings({
      indexName: 'theIndexName',
      indexSettings: { paginationLimitedTo: 10 },
      forwardToReplicas: true,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/settings');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({ paginationLimitedTo: 10 });
    expect(req.searchParams).toStrictEqual({ forwardToReplicas: 'true' });
  });

  test('setSettings allow boolean `typoTolerance`', async () => {
    const req = (await client.setSettings({
      indexName: 'theIndexName',
      indexSettings: { typoTolerance: true },
      forwardToReplicas: true,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/settings');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({ typoTolerance: true });
    expect(req.searchParams).toStrictEqual({ forwardToReplicas: 'true' });
  });

  test('setSettings allow enum `typoTolerance`', async () => {
    const req = (await client.setSettings({
      indexName: 'theIndexName',
      indexSettings: { typoTolerance: 'min' },
      forwardToReplicas: true,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/settings');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({ typoTolerance: 'min' });
    expect(req.searchParams).toStrictEqual({ forwardToReplicas: 'true' });
  });

  test('setSettings allow boolean `ignorePlurals`', async () => {
    const req = (await client.setSettings({
      indexName: 'theIndexName',
      indexSettings: { ignorePlurals: true },
      forwardToReplicas: true,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/settings');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({ ignorePlurals: true });
    expect(req.searchParams).toStrictEqual({ forwardToReplicas: 'true' });
  });

  test('setSettings allow list of string `ignorePlurals`', async () => {
    const req = (await client.setSettings({
      indexName: 'theIndexName',
      indexSettings: { ignorePlurals: ['algolia'] },
      forwardToReplicas: true,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/settings');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({ ignorePlurals: ['algolia'] });
    expect(req.searchParams).toStrictEqual({ forwardToReplicas: 'true' });
  });

  test('setSettings allow boolean `removeStopWords`', async () => {
    const req = (await client.setSettings({
      indexName: 'theIndexName',
      indexSettings: { removeStopWords: true },
      forwardToReplicas: true,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/settings');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({ removeStopWords: true });
    expect(req.searchParams).toStrictEqual({ forwardToReplicas: 'true' });
  });

  test('setSettings allow list of string `removeStopWords`', async () => {
    const req = (await client.setSettings({
      indexName: 'theIndexName',
      indexSettings: { removeStopWords: ['algolia'] },
      forwardToReplicas: true,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/settings');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({ removeStopWords: ['algolia'] });
    expect(req.searchParams).toStrictEqual({ forwardToReplicas: 'true' });
  });

  test('setSettings allow boolean `distinct`', async () => {
    const req = (await client.setSettings({
      indexName: 'theIndexName',
      indexSettings: { distinct: true },
      forwardToReplicas: true,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/settings');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({ distinct: true });
    expect(req.searchParams).toStrictEqual({ forwardToReplicas: 'true' });
  });

  test('setSettings allow integers for `distinct`', async () => {
    const req = (await client.setSettings({
      indexName: 'theIndexName',
      indexSettings: { distinct: 1 },
      forwardToReplicas: true,
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/settings');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({ distinct: 1 });
    expect(req.searchParams).toStrictEqual({ forwardToReplicas: 'true' });
  });

  test('setSettings allow all `indexSettings`', async () => {
    const req = (await client.setSettings({
      indexName: 'theIndexName',
      indexSettings: {
        replicas: [''],
        paginationLimitedTo: 0,
        disableTypoToleranceOnWords: ['algolia'],
        attributesToTransliterate: ['algolia'],
        camelCaseAttributes: ['algolia'],
        decompoundedAttributes: { algolia: 'aloglia' },
        indexLanguages: ['algolia'],
        disablePrefixOnAttributes: ['algolia'],
        allowCompressionOfIntegerArray: true,
        numericAttributesForFiltering: ['algolia'],
        separatorsToIndex: 'algolia',
        searchableAttributes: ['algolia'],
        userData: { user: 'data' },
        customNormalization: { algolia: { aloglia: 'aglolia' } },
        attributesForFaceting: ['algolia'],
        unretrievableAttributes: ['algolia'],
        attributesToRetrieve: ['algolia'],
        restrictSearchableAttributes: ['algolia'],
        ranking: ['geo'],
        customRanking: ['algolia'],
        relevancyStrictness: 10,
        attributesToHighlight: ['algolia'],
        attributesToSnippet: ['algolia'],
        highlightPreTag: '<span>',
        highlightPostTag: '</span>',
        snippetEllipsisText: '---',
        restrictHighlightAndSnippetArrays: true,
        hitsPerPage: 10,
        minWordSizefor1Typo: 5,
        minWordSizefor2Typos: 11,
        typoTolerance: false,
        allowTyposOnNumericTokens: true,
        disableTypoToleranceOnAttributes: ['algolia'],
        ignorePlurals: false,
        removeStopWords: false,
        keepDiacriticsOnCharacters: 'abc',
        queryLanguages: ['algolia'],
        decompoundQuery: false,
        enableRules: false,
        enablePersonalization: true,
        queryType: 'prefixLast',
        removeWordsIfNoResults: 'lastWords',
        advancedSyntax: true,
        optionalWords: ['algolia'],
        disableExactOnAttributes: ['algolia'],
        exactOnSingleWordQuery: 'attribute',
        alternativesAsExact: ['singleWordSynonym'],
        advancedSyntaxFeatures: ['exactPhrase'],
        distinct: 3,
        attributeForDistinct: 'test',
        synonyms: false,
        replaceSynonymsInHighlight: true,
        minProximity: 6,
        responseFields: ['algolia'],
        maxFacetHits: 50,
        attributeCriteriaComputedByMinProximity: true,
        renderingContent: {
          facetOrdering: {
            facets: { order: ['a', 'b'] },
            values: { a: { order: ['b'], sortRemainingBy: 'count' } },
          },
        },
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/indexes/theIndexName/settings');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({
      replicas: [''],
      paginationLimitedTo: 0,
      disableTypoToleranceOnWords: ['algolia'],
      attributesToTransliterate: ['algolia'],
      camelCaseAttributes: ['algolia'],
      decompoundedAttributes: { algolia: 'aloglia' },
      indexLanguages: ['algolia'],
      disablePrefixOnAttributes: ['algolia'],
      allowCompressionOfIntegerArray: true,
      numericAttributesForFiltering: ['algolia'],
      separatorsToIndex: 'algolia',
      searchableAttributes: ['algolia'],
      userData: { user: 'data' },
      customNormalization: { algolia: { aloglia: 'aglolia' } },
      attributesForFaceting: ['algolia'],
      unretrievableAttributes: ['algolia'],
      attributesToRetrieve: ['algolia'],
      restrictSearchableAttributes: ['algolia'],
      ranking: ['geo'],
      customRanking: ['algolia'],
      relevancyStrictness: 10,
      attributesToHighlight: ['algolia'],
      attributesToSnippet: ['algolia'],
      highlightPreTag: '<span>',
      highlightPostTag: '</span>',
      snippetEllipsisText: '---',
      restrictHighlightAndSnippetArrays: true,
      hitsPerPage: 10,
      minWordSizefor1Typo: 5,
      minWordSizefor2Typos: 11,
      typoTolerance: false,
      allowTyposOnNumericTokens: true,
      disableTypoToleranceOnAttributes: ['algolia'],
      ignorePlurals: false,
      removeStopWords: false,
      keepDiacriticsOnCharacters: 'abc',
      queryLanguages: ['algolia'],
      decompoundQuery: false,
      enableRules: false,
      enablePersonalization: true,
      queryType: 'prefixLast',
      removeWordsIfNoResults: 'lastWords',
      advancedSyntax: true,
      optionalWords: ['algolia'],
      disableExactOnAttributes: ['algolia'],
      exactOnSingleWordQuery: 'attribute',
      alternativesAsExact: ['singleWordSynonym'],
      advancedSyntaxFeatures: ['exactPhrase'],
      distinct: 3,
      attributeForDistinct: 'test',
      synonyms: false,
      replaceSynonymsInHighlight: true,
      minProximity: 6,
      responseFields: ['algolia'],
      maxFacetHits: 50,
      attributeCriteriaComputedByMinProximity: true,
      renderingContent: {
        facetOrdering: {
          facets: { order: ['a', 'b'] },
          values: { a: { order: ['b'], sortRemainingBy: 'count' } },
        },
      },
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('updateApiKey', () => {
  test('updateApiKey', async () => {
    const req = (await client.updateApiKey({
      key: 'myApiKey',
      apiKey: {
        acl: ['search', 'addObject'],
        validity: 300,
        maxQueriesPerIPPerHour: 100,
        maxHitsPerQuery: 20,
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/keys/myApiKey');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({
      acl: ['search', 'addObject'],
      validity: 300,
      maxQueriesPerIPPerHour: 100,
      maxHitsPerQuery: 20,
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});
