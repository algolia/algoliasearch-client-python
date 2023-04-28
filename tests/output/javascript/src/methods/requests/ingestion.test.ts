import type { EchoResponse, RequestOptions } from '@algolia/client-common';
import { ingestionClient } from '@algolia/ingestion';
import { echoRequester } from '@algolia/requester-node-http';

const appId = process.env.ALGOLIA_APPLICATION_ID || 'test_app_id';
const apiKey = process.env.ALGOLIA_SEARCH_KEY || 'test_api_key';

const client = ingestionClient(appId, apiKey, 'us', {
  requester: echoRequester(),
});

describe('createAuthentication', () => {
  test('createAuthenticationOAuth', async () => {
    const req = (await client.createAuthentication({
      type: 'oauth',
      name: 'authName',
      input: {
        url: 'http://test.oauth',
        client_id: 'myID',
        client_secret: 'mySecret',
      },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/authentications');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      type: 'oauth',
      name: 'authName',
      input: {
        url: 'http://test.oauth',
        client_id: 'myID',
        client_secret: 'mySecret',
      },
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('createAuthenticationAlgolia', async () => {
    const req = (await client.createAuthentication({
      type: 'algolia',
      name: 'authName',
      input: { appID: 'myappID', apiKey: 'randomApiKey' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/authentications');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      type: 'algolia',
      name: 'authName',
      input: { appID: 'myappID', apiKey: 'randomApiKey' },
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('createDestination', () => {
  test('createDestination', async () => {
    const req = (await client.createDestination({
      type: 'search',
      name: 'destinationName',
      input: { indexPrefix: 'prefix_' },
      authenticationID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/destinations');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      type: 'search',
      name: 'destinationName',
      input: { indexPrefix: 'prefix_' },
      authenticationID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('createSource', () => {
  test('createSource', async () => {
    const req = (await client.createSource({
      type: 'commercetools',
      name: 'sourceName',
      input: {
        storeKeys: ['myStore'],
        locales: ['de'],
        url: 'http://commercetools.com',
        projectKey: 'keyID',
      },
      authenticationID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/sources');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      type: 'commercetools',
      name: 'sourceName',
      input: {
        storeKeys: ['myStore'],
        locales: ['de'],
        url: 'http://commercetools.com',
        projectKey: 'keyID',
      },
      authenticationID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('createTask', () => {
  test('createTaskOnDemand', async () => {
    const req = (await client.createTask({
      sourceID: 'search',
      destinationID: 'destinationName',
      trigger: { type: 'onDemand' },
      action: 'replace',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/tasks');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      sourceID: 'search',
      destinationID: 'destinationName',
      trigger: { type: 'onDemand' },
      action: 'replace',
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('createTaskSchedule', async () => {
    const req = (await client.createTask({
      sourceID: 'search',
      destinationID: 'destinationName',
      trigger: { type: 'schedule', cron: '* * * * *' },
      action: 'replace',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/tasks');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      sourceID: 'search',
      destinationID: 'destinationName',
      trigger: { type: 'schedule', cron: '* * * * *' },
      action: 'replace',
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });

  test('createTaskSubscription', async () => {
    const req = (await client.createTask({
      sourceID: 'search',
      destinationID: 'destinationName',
      trigger: { type: 'onDemand' },
      action: 'replace',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/tasks');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      sourceID: 'search',
      destinationID: 'destinationName',
      trigger: { type: 'onDemand' },
      action: 'replace',
    });
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

describe('deleteAuthentication', () => {
  test('deleteAuthentication', async () => {
    const req = (await client.deleteAuthentication({
      authenticationID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual(
      '/1/authentications/6c02aeb1-775e-418e-870b-1faccd4b2c0f'
    );
    expect(req.method).toEqual('DELETE');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('deleteDestination', () => {
  test('deleteDestination', async () => {
    const req = (await client.deleteDestination({
      destinationID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual(
      '/1/destinations/6c02aeb1-775e-418e-870b-1faccd4b2c0f'
    );
    expect(req.method).toEqual('DELETE');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('deleteSource', () => {
  test('deleteSource', async () => {
    const req = (await client.deleteSource({
      sourceID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/sources/6c02aeb1-775e-418e-870b-1faccd4b2c0f');
    expect(req.method).toEqual('DELETE');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('deleteTask', () => {
  test('deleteTask', async () => {
    const req = (await client.deleteTask({
      taskID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/tasks/6c02aeb1-775e-418e-870b-1faccd4b2c0f');
    expect(req.method).toEqual('DELETE');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('disableTask', () => {
  test('disableTask', async () => {
    const req = (await client.disableTask({
      taskID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual(
      '/1/tasks/6c02aeb1-775e-418e-870b-1faccd4b2c0f/disable'
    );
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('enableTask', () => {
  test('enableTask', async () => {
    const req = (await client.enableTask({
      taskID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual(
      '/1/tasks/6c02aeb1-775e-418e-870b-1faccd4b2c0f/enable'
    );
    expect(req.method).toEqual('PUT');
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

describe('getAuthentication', () => {
  test('getAuthentication', async () => {
    const req = (await client.getAuthentication({
      authenticationID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual(
      '/1/authentications/6c02aeb1-775e-418e-870b-1faccd4b2c0f'
    );
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getAuthentications', () => {
  test('getAuthentications', async () => {
    const req = (await client.getAuthentications()) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/authentications');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getDestination', () => {
  test('getDestination', async () => {
    const req = (await client.getDestination({
      destinationID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual(
      '/1/destinations/6c02aeb1-775e-418e-870b-1faccd4b2c0f'
    );
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getDestinations', () => {
  test('getDestinations', async () => {
    const req = (await client.getDestinations()) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/destinations');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getEvent', () => {
  test('getEvent', async () => {
    const req = (await client.getEvent({
      runID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
      eventID: '6c02aeb1-775e-418e-870b-1faccd4b2c0c',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual(
      '/1/runs/6c02aeb1-775e-418e-870b-1faccd4b2c0f/events/6c02aeb1-775e-418e-870b-1faccd4b2c0c'
    );
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getEvents', () => {
  test('getEvents', async () => {
    const req = (await client.getEvents({
      runID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual(
      '/1/runs/6c02aeb1-775e-418e-870b-1faccd4b2c0f/events'
    );
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getRun', () => {
  test('getRun', async () => {
    const req = (await client.getRun({
      runID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/runs/6c02aeb1-775e-418e-870b-1faccd4b2c0f');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getRuns', () => {
  test('getRuns', async () => {
    const req = (await client.getRuns()) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/runs');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getSource', () => {
  test('getSource', async () => {
    const req = (await client.getSource({
      sourceID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/sources/6c02aeb1-775e-418e-870b-1faccd4b2c0f');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getSources', () => {
  test('getSources', async () => {
    const req = (await client.getSources()) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/sources');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getTask', () => {
  test('getTask', async () => {
    const req = (await client.getTask({
      taskID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/tasks/6c02aeb1-775e-418e-870b-1faccd4b2c0f');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('getTasks', () => {
  test('getTasks', async () => {
    const req = (await client.getTasks()) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/tasks');
    expect(req.method).toEqual('GET');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
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

describe('runTask', () => {
  test('runTask', async () => {
    const req = (await client.runTask({
      taskID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
    })) as unknown as EchoResponse;

    expect(req.path).toEqual(
      '/1/tasks/6c02aeb1-775e-418e-870b-1faccd4b2c0f/run'
    );
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual(undefined);
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('searchAuthentications', () => {
  test('searchAuthentications', async () => {
    const req = (await client.searchAuthentications({
      authenticationIDs: [
        '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
        '947ac9c4-7e58-4c87-b1e7-14a68e99699a',
      ],
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/authentications/search');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      authenticationIDs: [
        '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
        '947ac9c4-7e58-4c87-b1e7-14a68e99699a',
      ],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('searchDestinations', () => {
  test('searchDestinations', async () => {
    const req = (await client.searchDestinations({
      destinationIDs: [
        '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
        '947ac9c4-7e58-4c87-b1e7-14a68e99699a',
      ],
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/destinations/search');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      destinationIDs: [
        '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
        '947ac9c4-7e58-4c87-b1e7-14a68e99699a',
      ],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('searchSources', () => {
  test('searchSources', async () => {
    const req = (await client.searchSources({
      sourceIDs: [
        '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
        '947ac9c4-7e58-4c87-b1e7-14a68e99699a',
      ],
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/sources/search');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      sourceIDs: [
        '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
        '947ac9c4-7e58-4c87-b1e7-14a68e99699a',
      ],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('searchTasks', () => {
  test('searchTasks', async () => {
    const req = (await client.searchTasks({
      taskIDs: [
        '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
        '947ac9c4-7e58-4c87-b1e7-14a68e99699a',
      ],
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/tasks/search');
    expect(req.method).toEqual('POST');
    expect(req.data).toEqual({
      taskIDs: [
        '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
        '947ac9c4-7e58-4c87-b1e7-14a68e99699a',
      ],
    });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('updateAuthentication', () => {
  test('updateAuthentication', async () => {
    const req = (await client.updateAuthentication({
      authenticationID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
      authenticationUpdate: { name: 'newName' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual(
      '/1/authentications/6c02aeb1-775e-418e-870b-1faccd4b2c0f'
    );
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({ name: 'newName' });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('updateDestination', () => {
  test('updateDestination', async () => {
    const req = (await client.updateDestination({
      destinationID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
      destinationUpdate: { name: 'newName' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual(
      '/1/destinations/6c02aeb1-775e-418e-870b-1faccd4b2c0f'
    );
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({ name: 'newName' });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('updateSource', () => {
  test('updateSource', async () => {
    const req = (await client.updateSource({
      sourceID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
      sourceUpdate: { name: 'newName' },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/sources/6c02aeb1-775e-418e-870b-1faccd4b2c0f');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({ name: 'newName' });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});

describe('updateTask', () => {
  test('updateTask', async () => {
    const req = (await client.updateTask({
      taskID: '6c02aeb1-775e-418e-870b-1faccd4b2c0f',
      taskUpdate: { enabled: false },
    })) as unknown as EchoResponse;

    expect(req.path).toEqual('/1/tasks/6c02aeb1-775e-418e-870b-1faccd4b2c0f');
    expect(req.method).toEqual('PUT');
    expect(req.data).toEqual({ enabled: false });
    expect(req.searchParams).toStrictEqual(undefined);
  });
});
