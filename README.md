<p align="center">
  <a href="https://www.algolia.com">
    <img alt="Algolia for Python" src="https://raw.githubusercontent.com/algolia/algoliasearch-client-common/master/banners/python.png" >
  </a>

  <h4 align="center">The perfect starting point to integrate <a href="https://algolia.com" target="_blank">Algolia</a> within your Python project</h4>

  <p align="center">
    <a href="https://pypi.org/project/algoliasearch"><img src="https://img.shields.io/pypi/v/algoliasearch.svg" alt="PyPI"></img></a>
    <a href="https://pypi.org/project/algoliasearch"><img src="https://img.shields.io/pypi/pyversions/ansicolortags.svg" alt="Python versions"></img></a>
    <a href="https://pypi.org/project/algoliasearch"><img src="https://img.shields.io/pypi/l/ansicolortags.svg" alt="License"></a>
  </p>
</p>

<p align="center">
  <a href="https://www.algolia.com/doc/api-client/getting-started/install/python/" target="_blank">Documentation</a>  •
  <a href="https://github.com/algolia/algoliasearch-django" target="_blank">Django</a>  •
  <a href="https://discourse.algolia.com" target="_blank">Community Forum</a>  •
  <a href="http://stackoverflow.com/questions/tagged/algolia" target="_blank">Stack Overflow</a>  •
  <a href="https://github.com/algolia/algoliasearch-client-python/issues" target="_blank">Report a bug</a>  •
  <a href="https://www.algolia.com/doc/api-client/troubleshooting/faq/python/" target="_blank">FAQ</a>  •
  <a href="https://www.algolia.com/support" target="_blank">Support</a>
</p>

## ✨ Features

- Thin & minimal low-level HTTP client to interact with Algolia's API
- Supports Python: `3.4` to `3.11`
- Contains blazing-fast asynchronous methods built on top of the [Asyncio](https://docs.python.org/3/library/asyncio.html)

## 💡 Getting Started

First, install Algolia Python API Client via the [pip](https://pip.pypa.io/en/stable/installing) package manager:

```bash
pip install --upgrade 'algoliasearch>=2.0,<3.0'
```

Then, create objects on your index:

```py
from algoliasearch.search_client import SearchClient

client = SearchClient.create('YourApplicationID', 'YourAPIKey')
index = client.init_index('your_index_name')

index.save_objects([{'objectID': 1, 'name': 'Foo'}])
```

Finally, you may begin searching a object using the `search` method:

```py
objects = index.search('Fo')
```

For full documentation, visit the **[Algolia Python API Client](https://www.algolia.com/doc/api-client/getting-started/install/python/)**.

## ❓ Troubleshooting

Encountering an issue? Before reaching out to support, we recommend heading to our [FAQ](https://www.algolia.com/doc/api-client/troubleshooting/faq/python/) where you will find answers for the most common issues and gotchas with the client.

## Use the Dockerfile

If you want to contribute to this project without installing all its dependencies, you can use our Docker image. Please check our [dedicated guide](DOCKER_README.MD) to learn more.

## 📄 License

Algolia Python API Client is an open-sourced software licensed under the [MIT license](LICENSE.md).
