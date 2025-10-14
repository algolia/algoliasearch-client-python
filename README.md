<p align="center">
  <a href="https://www.algolia.com">
    <img alt="Algolia for Python" src="https://raw.githubusercontent.com/algolia/algoliasearch-client-common/master/banners/python.png" >
  </a>

  <h4 align="center">The perfect starting point to integrate <a href="https://algolia.com" target="_blank">Algolia</a> within your Python project</h4>

  <p align="center">
    <a href="https://pypi.org/project/algoliasearch"><img src="https://img.shields.io/pypi/v/algoliasearch.svg" alt="PyPI"></img></a>
    <a href="https://pypi.org/project/algoliasearch"><img src="https://img.shields.io/badge/python-3.8|3.9|3.10|3.11|3.12-blue" alt="Python versions"></img></a>
    <a href="https://pypi.org/project/algoliasearch"><img src="https://img.shields.io/pypi/l/ansicolortags.svg" alt="License"></a>
  </p>
</p>

<p align="center">
  <a href="https://www.algolia.com/doc/libraries/python/" target="_blank">Documentation</a>  •
  <a href="https://github.com/algolia/algoliasearch-django" target="_blank">Django</a>  •
  <a href="https://discourse.algolia.com" target="_blank">Community Forum</a>  •
  <a href="http://stackoverflow.com/questions/tagged/algolia" target="_blank">Stack Overflow</a>  •
  <a href="https://github.com/algolia/algoliasearch-client-python/issues" target="_blank">Report a bug</a>  •
  <a href="https://alg.li/support" target="_blank">Support</a>
</p>

## ✨ Features

- Thin & minimal low-level HTTP client to interact with Algolia's API
- Supports Python from `3.8`

## 💡 Getting Started

First, install Algolia Python API Client via the [pip](https://pip.pypa.io/en/stable/installing) package manager:

```bash
pip install --upgrade 'algoliasearch>=4.0,<5.0'
```

You can now import the Algolia API client in your project and play with it.

```py
from algoliasearch.search.client import SearchClient

_client = SearchClient("YOUR_APP_ID", "YOUR_API_KEY")

# Add a new record to your Algolia index
response = await _client.save_object(
    index_name="<YOUR_INDEX_NAME>",
    body={
        "objectID": "id",
        "test": "val",
    },
)

# use the class directly
print(response)

# print the JSON response
print(response.to_json())

# Poll the task status to know when it has been indexed
await client.wait_for_task(index_name="<YOUR_INDEX_NAME>", task_id=response.task_id)

# Fetch search results, with typo tolerance
response = await _client.search(
    search_method_params={
        "requests": [
            {
                "indexName": "<YOUR_INDEX_NAME>",
                "query": "<YOUR_QUERY>",
                "hitsPerPage": 50,
            },
        ],
    },
)

# use the class directly
print(response)

# print the JSON response
print(response.to_json())
```

For full documentation, visit the **[Algolia Python API Client](https://www.algolia.com/doc/libraries/python/)**.

## ❓ Troubleshooting

Encountering an issue? Before reaching out to support, we recommend heading to our [FAQ](https://support.algolia.com/hc/sections/15061037630609-API-Client-FAQs) where you will find answers for the most common issues and gotchas with the client. You can also open [a GitHub issue](https://github.com/algolia/api-clients-automation/issues/new?assignees=&labels=&projects=&template=Bug_report.md)

## Contributing

This repository hosts the code of the generated Algolia API client for Python, if you'd like to contribute, head over to the [main repository](https://github.com/algolia/api-clients-automation). You can also find contributing guides on [our documentation website](https://api-clients-automation.netlify.app/docs/introduction).

## 📄 License

The Algolia Python API Client is an open-sourced software licensed under the [MIT license](LICENSE).
