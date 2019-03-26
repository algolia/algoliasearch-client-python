⚠️ This is the beta for our v2 client!

Our [v1 client](https://github.com/algolia/algoliasearch-client-python/tree/1.x) is still the LTS in [PyPI](https://pypi.org/project/algoliasearch/). Meaning, `pip install algoliasearch` still gets you the v1.

Once v2 comes out of beta (soon!), we'll update PyPI.

---

## Algolia API Client Python

[Algolia Search](https://www.algolia.com) is a hosted search engine capable of delivering real-time results from the first keystroke.

This readme/code introduces the upcoming Algolia API Client Python v2, the next major release of our API Client. This release includes several new features along with the latest bug fixes and improvements:

- Supports Python: 2.7, 3.4, 3.5, 3.6, and 3.7.
- Works in synchronous and **asynchronous** environments.
- Tons of new methods: waitable response objects, `replace_all_objects`,`clear_objects`, and more!

**Development Status**: 4 - Beta.

**Changelog**: Coming soon.

You'd like to contribute? Before start, we want to let you know that your **feedback** is important to us! Please consider start using this `v2` today! Found a bug or see something that can improved? Report it here: [github.com/algolia/algoliasearch-client-python/issues](https://github.com/algolia/algoliasearch-client-python/issues).

First, install Algoliasearch - API Client Python v2:
```
pip install --pre algoliasearch
```

### Example with synchronous usage:

```py
import os

from algoliasearch.search_client import SearchClient

client = SearchClient.create(
    'ALGOLIA_APPLICATION_ID',
    'ALGOLIA_ADMIN_KEY'
)

index = client.init_index('articles')

index.save_objects([
    {'objectID': 1, 'firstname': 'Jimmie', 'lastname': 'Barninger'},
    {'objectID': 2, 'firstname': 'Warren', 'lastname': 'Speach'}
]).wait()

hits = index.search('Jimmie')

print(hits)
```

### Example with asynchronous usage:

First, require asynchronous libraries:

```
pip install 'asyncio>=3.4,<4.0' 'aiohttp>=2.0,<4.0' 'async_timeout>=2.0,<4.0'
```

Then, asynchronous methods are available using the `async` suffix:

| synchronous   | asynchronous          |
|-------------- |--------------------   |
| search        | search_async          |
| save_objects  | save_objects_async    |
| set_settings  | set_settings_async    |
| save_synonyms | save_synonyms_async   |
| ...           | ...                   |


```py
import asyncio

from algoliasearch.search_client import SearchClient
from algoliasearch.responses import MultipleResponse

app_id = 'ALGOLIA_APPLICATION_ID'
api_key = 'ALGOLIA_ADMIN_KEY'

async def main():
    async with SearchClient.create(app_id, api_key) as client:
        index = client.init_index('articles')

        results = await asyncio.gather(
            index.save_object_async({'objectID': 1, 'foo': 'bar'}),
            index.save_object_async({'objectID': 2, 'foo': 'foo'})
        )

        MultipleResponse(results).wait()

        print(await index.search_async(''))

asyncio.run(main())

```

### License

Algolia API Client Python is an open-sourced software licensed under the [MIT license](LICENSE).
