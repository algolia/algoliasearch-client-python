**Note:** The readme/code you are seeing it's part of upcoming release: Algolia API Client Python v2.

Algolia's Python client provides the perfect starting point to integrate
Algolia into your Python application. It is carefully crafted to simplify the usage
of Algolia within your Python Project.

## Preface

- Tons of new features: contains waitable response objects, up-to-date retry strategy, `replace_all_objects`,`clear_objects`, and more!

- Supports Python: **2.7 🥳**, 3.4, 3.5, 3.6, and 3.7.

- Strong test suite, 100% test coverage on `unittest` (tests === **30secs locally!** 🏎), `flake8` 
(linter), and `mypy` (static-analysis) to ensure the quality of the code.

- Supports synchronous and **asynchronous** environments. 👉🏻 **Yes, in the same client and with support Python 2. It's amazing!** Asynchronous methods are available using the `async` suffix:

| synchronous   | asynchronous          |
|-------------- |--------------------   |
| search        | search_async          |
| save_objects  | save_objects_async    |
| ...           | ...                   |

## Contributing

Thank you for considering to contribute to Algolia's API Client Python v2. Here is the list of tasks that I would love to get your help:

1. Using Python v1 within Algolia for non-critical projects? Start using this v2 today!
3. Analyze the code quality
4. Analyze the quality of tests
5. Create a [free account](https://www.algolia.com/users/sign_up/hacker) at Algolia, and play with this client.

## Get started locally

> **Requires:**
- **[Homebrew](https://brew.sh)**

First, use [Homebrew](https://brew.sh) to install Python 3.7:
```bash
# Install Python 3
brew install python3

# Create your Python project directory
mkdir my-new-project
cd my-new-project

# Create a Python Virtual Environment inside your directory
python3 -m venv venv

# Activate the Python Virtual Environment
source venv/bin/activate

# At any time, use the following command to deactivate it
deactivate
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
import asyncio
import os

from algoliasearch.search_client import SearchClient
from algoliasearch.exceptions import AlgoliaException
from algoliasearch.responses import MultipleResponse

app_id = os.environ.get('ALGOLIA_APPLICATION_ID_1')
api_key = os.environ.get('ALGOLIA_ADMIN_KEY_1')


async def main():
    async with SearchClient.create(app_id, api_key) as client:
        index = client.init_index('articles')

        try:
            (await index.clear_objects_async()).wait()
        except AlgoliaException:  # Index not found
            pass

        results = await asyncio.gather(
            index.save_object_async({'objectID': 1, 'foo': 'bar'}),
            index.save_object_async({'objectID': 2, 'foo': 'foo'})
        )

        MultipleResponse(results).wait()

        print(await index.search_async(''))

asyncio.run(main())
```
