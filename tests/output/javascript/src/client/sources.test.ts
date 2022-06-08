/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable require-await */
// @ts-nocheck Failing tests will have type errors, but we cannot suppress them even with @ts-expect-error because it doesn't work for a block of lines.
import type { SourcesClient } from '@experimental-api-clients-automation/client-sources';
import { sourcesClient } from '@experimental-api-clients-automation/client-sources';
import { echoRequester } from '@experimental-api-clients-automation/requester-node-http';

const appId = 'test-app-id';
const apiKey = 'test-api-key';

function createClient(): SourcesClient {
  return sourcesClient(appId, apiKey, 'us', { requester: echoRequester() });
}

describe('api', () => {
  test('calls api with correct host', async () => {
    const $client = createClient();

    const result = await $client.post({ path: '/test' });

    expect(result.host).toEqual('data.us.algolia.com');
  });
});

describe('commonApi', () => {
  test('calls api with correct user agent', async () => {
    const $client = createClient();

    const result = await $client.post({ path: '/test' });

    expect(decodeURI(result.algoliaAgent)).toMatch(
      /^Algolia for JavaScript \(\d+\.\d+\.\d+(-.*)?\)(; [a-zA-Z. ]+ (\(\d+\.\d+\.\d+(-.*)?\))?)*(; Sources (\(\d+\.\d+\.\d+(-.*)?\)))(; [a-zA-Z. ]+ (\(\d+\.\d+\.\d+(-.*)?\))?)*$/
    );
  });

  test('calls api with correct timeouts', async () => {
    const $client = createClient();

    const result = await $client.post({ path: '/test' });

    expect(result).toEqual(
      expect.objectContaining({ connectTimeout: 2000, responseTimeout: 30000 })
    );
  });
});

describe('parameters', () => {
  test('throws when region is not given', async () => {
    try {
      const $client = sourcesClient('my-app-id', 'my-api-key', '', {
        requester: echoRequester(),
      });

      throw new Error('test is expected to throw error');
    } catch (e) {
      expect(e.message).toMatch('`region` is missing.');
    }
  });

  test('throws when incorrect region is given', async () => {
    try {
      const $client = sourcesClient('my-app-id', 'my-api-key', 'not_a_region', {
        requester: echoRequester(),
      });

      throw new Error('test is expected to throw error');
    } catch (e) {
      expect(e.message).toMatch(
        '`region` must be one of the following: de, us'
      );
    }
  });

  test('does not throw when region is given', async () => {
    const $client = sourcesClient('my-app-id', 'my-api-key', 'us', {
      requester: echoRequester(),
    });
  });
});
