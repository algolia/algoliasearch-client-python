# Introducing Algolia's API Client Python v2

Version: **v2.0.0-alpha.1**

Final release: No date is set, but this should happen sometime in end-March/begin-April.

## Preface

Big news: Algolia's API Client Python v2 is coming! So, what changes can we look forward to for this API Client?

- Follows 100% of the **API Client v2 specs** (just like PHP v2, and c# v2): contains waitable response objects, up-to-date retry strategy, `replace_all_objects`,`clear_objects`, and more
- Supports Python: **2.7 🥳**, 3.4, 3.5, 3.6, and 3.7
- Strong test suite, 100% test coverage on `unittest` (tests === **30secs locally!** 🏎), `flake8` (linter), and `mypy` (static-analysis) to ensure the quality of the code.
- Supports synchronous and **asynchronous** environments. 👉🏻 **Yes, in the same client and with support Python 2. It's amazing!**. Asynchronous methods are available using the `async` suffix:

| synchronous   | asynchronous          |
|-------------- |--------------------   |
| search        | search_async          |
| save_objects  | save_objects_async    |
| ...           | ...                   |

## Contributing

Thank you for considering to contribute to Algolia's API Client Python v2. Here is the list of tasks that I would love to get your help:

1. Using Python v1 within Algolia for non-critical projects? Start using this v2 today! Found a bug? Report it here: [https://github.com/algolia/algoliasearch-client-python](https://github.com/algolia/algoliasearch-client-python).
2. Have experience in Python? Check if the code/structure *Pythonic*
3. Coming from Java, or another robust language? Take a moment to analyze the quality of the code
4. Are you a test addicted like me? Take a moment to analyze the quality of tests
5. Play with the client.

## Get started locally

> **Requires:**
- **[Homebrew](https://brew.sh)**

First, You may use [Homebrew](https://brew.sh) to install Python 3.7:
```bash
brew install python
```

Then, install `pip`:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py
```

Finally, install `algoliasearch` - API Client Python v2:
```
pip install https://github.com/algolia/algoliasearch-client-python/archive/develop.zip
```

### Synchronous example:

```py
import os

from algoliasearch.search_client import SearchClient
from algoliasearch.exceptions import AlgoliaException

client = SearchClient.create(
    os.environ.get('ALGOLIA_APPLICATION_ID_1'),
    os.environ.get('ALGOLIA_ADMIN_KEY_1')
)

index = client.init_index('articles')

index.save_objects([
    {'objectID': 1, 'firstname': 'Jimmie', 'lastname': 'Barninger'},
    {'objectID': 2, 'firstname': 'Warren', 'lastname': 'Speach'}
]).wait()

hits = index.search('Jimmie')

print(hits)
```

### Asynchronous example:

First, require asynchronous libraries:

```
pip install 'asyncio>=3.4,<4.0' 'aiohttp>=2.0,<4.0' 'async_timeout>=2.0,<4.0'
```


```py
import os

from algoliasearch.search_client import SearchClient
from algoliasearch.exceptions import AlgoliaException
from algoliasearch.responses import MultipleResponse

client = SearchClient.create(
    os.environ.get('ALGOLIA_APPLICATION_ID_1'),
    os.environ.get('ALGOLIA_ADMIN_KEY_1')
)

index = client.init_index('articles')

try:
    index.clear_objects().wait()
except AlgoliaException:  # Index not found
    pass

import asyncio

loop = asyncio.get_event_loop()

tasks = [
    index.save_object_async({'objectID': 1, 'foo': 'bar'}),
    index.save_object_async({'objectID': 2, 'foo': 'bar'}),
]

MultipleResponse(
    loop.run_until_complete(asyncio.gather(*tasks))
).wait()

result = loop.run_until_complete(index.search_async(''))

loop.close()

print(result)
```
