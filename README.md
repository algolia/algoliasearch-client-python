# Algolia Search API Client for Python

[Algolia Search](https://www.algolia.com) is a hosted search engine capable of delivering realtime results from the first keystroke.

The **Algolia Search API Client for Python** lets
you easily use the [Algolia Search REST API](https://www.algolia.com/doc/rest-api/search) from
your Python code.

[![Build Status](https://travis-ci.org/algolia/algoliasearch-client-python.svg?branch=master)](https://travis-ci.org/algolia/algoliasearch-client-python) [![PyPI version](https://badge.fury.io/py/algoliasearch.svg?branch=master)](http://badge.fury.io/py/algoliasearch) [![Coverage Status](https://coveralls.io/repos/algolia/algoliasearch-client-python/badge.svg?branch=master)](https://coveralls.io/r/algolia/algoliasearch-client-python)



  ## Contributing

  ### Migration note from v1.x to v2.x

In April 2019, we released v2.x of our Python client. If you are using version 1.x of the client, read the [migration guide to version 2.x](https://www.algolia.com/doc/api-client/getting-started/upgrade-guides/python).
The version 1.x is no longer supported.





## API Documentation

You can find the full reference on [Algolia's website](https://www.algolia.com/doc/api-client/python/).



1. **[Install](#install)**


1. **[Quick Start](#quick-start)**


1. **[Push data](#push-data)**


1. **[Configure](#configure)**


1. **[Search](#search)**


1. **[Search UI](#search-ui)**


1. **[List of available methods](#list-of-available-methods)**


1. **[Getting Help](#getting-help)**


1. **[List of available methods](#list-of-available-methods)**


# Getting Started



## Install

Install the Python client using [pip](https://pypi.org/project/pip/):

```bash
pip install --upgrade 'algoliasearch>=2.0,<3.0'
```

## Quick Start

In 30 seconds, this quick start tutorial will show you how to index and search objects.

### Initialize the client

To start, you need to initialize the client. To do this, you need your **Application ID** and **API Key**.
You can find both on [your Algolia account](https://www.algolia.com/api-keys).

```python
from algoliasearch.search_client import SearchClient

client = SearchClient.create('YourApplicationID', 'YourAdminAPIKey')
index = client.init_index('your_index_name')
```

## Push data

Without any prior configuration, you can start indexing [500 contacts](https://github.com/algolia/datasets/blob/master/contacts/contacts.json) in the ```contacts``` index using the following code:
```python
index = client.init_index('contacts')
batch = json.load(open('contacts.json'))
index.save_objects(batch, {'autoGenerateObjectIDIfNotExist': True})
```

## Configure

You can customize settings to fine tune the search behavior. For example, you can add a custom ranking by number of followers to further enhance the built-in relevance:

```python
index.set_settings({"customRanking": ["desc(followers)"]})
```

You can also configure the list of attributes you want to index by order of importance (most important first).

**Note:** Algolia is designed to suggest results as you type, which means you'll generally search by prefix.
In this case, the order of attributes is crucial to decide which hit is the best.

```python
index.set_settings({"searchableAttributes": ["lastname", "firstname", "company",
                                         "email", "city", "address"]})
```

## Search

You can now search for contacts by `firstname`, `lastname`, `company`, etc. (even with typos):

```python
# Search for a first name
print(index.search('jimmie'))
# Search for a first name with typo
print(index.search('jimie'))
# Search for a company
print(index.search('california paint'))
# Search for a first name and a company
print(index.search('jimmie paint'))
```

## Search UI

**Warning:** If you're building a web application, you may be interested in using one of our
[front-end search UI libraries](https://www.algolia.com/doc/guides/building-search-ui/what-is-instantsearch/js/).

The following example shows how to quickly build a front-end search using
[InstantSearch.js](https://www.algolia.com/doc/guides/building-search-ui/what-is-instantsearch/js/)

### index.html

```html
<!doctype html>
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/instantsearch.css@7.1.1/themes/algolia.css" integrity="sha256-4SlodglhMbXjGQfNWiCBLSGNiq90FUw3Mtre9u4vLG8=" crossorigin="anonymous">
</head>
<body>
  <header>
    
  </header>

  <main>
      
      
  </main>

  <script type="text/html" id="hit-template">
    
      <p class="hit-name">
        {}{ "attribute": "firstname" }{{/helpers.highlight}}
        {}{ "attribute": "lastname" }{{/helpers.highlight}}
      </p>
    
  </script>

  <script src="https://cdn.jsdelivr.net/npm/algoliasearch@3.32.1/dist/algoliasearchLite.min.js" integrity="sha256-NSTRUP9bvh8kBKi7IHQSmOrMAdVEoSJFBbTA+LoRr3A=" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@3.2.0" integrity="sha256-/8usMtTwZ01jujD7KAZctG0UMk2S2NDNirGFVBbBZCM=" crossorigin="anonymous"></script>
  <script src="app.js"></script>
</body>
```

### app.js

```js
// Replace with your own values
const searchClient = algoliasearch(
  'YourApplicationID',
  'YourSearchOnlyAPIKey' // search only API key, not admin API key
);

const search = instantsearch({
  indexName: 'instant_search',
  searchClient,
  routing: true,
});

search.addWidget(
  instantsearch.widgets.configure({
    hitsPerPage: 10,
  })
);

search.addWidget(
  instantsearch.widgets.searchBox({
    container: '#search-box',
    placeholder: 'Search for products',
  })
);

search.addWidget(
  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
      item: document.getElementById('hit-template').innerHTML,
      empty: `We didn't find any results for the search <em>"{{query}}"</em>`,
    },
  })
);

search.start();
```




## List of available methods





### Personalization

- [Add strategy](https://algolia.com/doc/api-reference/api-methods/add-strategy/?language=python)
- [Get strategy](https://algolia.com/doc/api-reference/api-methods/get-strategy/?language=python)




### Search

- [Search index](https://algolia.com/doc/api-reference/api-methods/search/?language=python)
- [Search for facet values](https://algolia.com/doc/api-reference/api-methods/search-for-facet-values/?language=python)
- [Search multiple indices](https://algolia.com/doc/api-reference/api-methods/multiple-queries/?language=python)
- [Browse index](https://algolia.com/doc/api-reference/api-methods/browse/?language=python)




### Indexing

- [Add objects](https://algolia.com/doc/api-reference/api-methods/add-objects/?language=python)
- [Save objects](https://algolia.com/doc/api-reference/api-methods/save-objects/?language=python)
- [Partial update objects](https://algolia.com/doc/api-reference/api-methods/partial-update-objects/?language=python)
- [Delete objects](https://algolia.com/doc/api-reference/api-methods/delete-objects/?language=python)
- [Replace all objects](https://algolia.com/doc/api-reference/api-methods/replace-all-objects/?language=python)
- [Delete by](https://algolia.com/doc/api-reference/api-methods/delete-by/?language=python)
- [Clear objects](https://algolia.com/doc/api-reference/api-methods/clear-objects/?language=python)
- [Get objects](https://algolia.com/doc/api-reference/api-methods/get-objects/?language=python)
- [Custom batch](https://algolia.com/doc/api-reference/api-methods/batch/?language=python)




### Settings

- [Get settings](https://algolia.com/doc/api-reference/api-methods/get-settings/?language=python)
- [Set settings](https://algolia.com/doc/api-reference/api-methods/set-settings/?language=python)
- [Copy settings](https://algolia.com/doc/api-reference/api-methods/copy-settings/?language=python)




### Manage indices

- [List indices](https://algolia.com/doc/api-reference/api-methods/list-indices/?language=python)
- [Delete index](https://algolia.com/doc/api-reference/api-methods/delete-index/?language=python)
- [Copy index](https://algolia.com/doc/api-reference/api-methods/copy-index/?language=python)
- [Move index](https://algolia.com/doc/api-reference/api-methods/move-index/?language=python)




### API keys

- [Create secured API Key](https://algolia.com/doc/api-reference/api-methods/generate-secured-api-key/?language=python)
- [Add API Key](https://algolia.com/doc/api-reference/api-methods/add-api-key/?language=python)
- [Update API Key](https://algolia.com/doc/api-reference/api-methods/update-api-key/?language=python)
- [Delete API Key](https://algolia.com/doc/api-reference/api-methods/delete-api-key/?language=python)
- [Restore API Key](https://algolia.com/doc/api-reference/api-methods/restore-api-key/?language=python)
- [Get API Key permissions](https://algolia.com/doc/api-reference/api-methods/get-api-key/?language=python)
- [List API Keys](https://algolia.com/doc/api-reference/api-methods/list-api-keys/?language=python)




### Synonyms

- [Save synonym](https://algolia.com/doc/api-reference/api-methods/save-synonym/?language=python)
- [Batch synonyms](https://algolia.com/doc/api-reference/api-methods/batch-synonyms/?language=python)
- [Delete synonym](https://algolia.com/doc/api-reference/api-methods/delete-synonym/?language=python)
- [Clear all synonyms](https://algolia.com/doc/api-reference/api-methods/clear-synonyms/?language=python)
- [Get synonym](https://algolia.com/doc/api-reference/api-methods/get-synonym/?language=python)
- [Search synonyms](https://algolia.com/doc/api-reference/api-methods/search-synonyms/?language=python)
- [Replace all synonyms](https://algolia.com/doc/api-reference/api-methods/replace-all-synonyms/?language=python)
- [Copy synonyms](https://algolia.com/doc/api-reference/api-methods/copy-synonyms/?language=python)
- [Export Synonyms](https://algolia.com/doc/api-reference/api-methods/export-synonyms/?language=python)




### Query rules

- [Save rule](https://algolia.com/doc/api-reference/api-methods/save-rule/?language=python)
- [Batch rules](https://algolia.com/doc/api-reference/api-methods/batch-rules/?language=python)
- [Get rule](https://algolia.com/doc/api-reference/api-methods/get-rule/?language=python)
- [Delete rule](https://algolia.com/doc/api-reference/api-methods/delete-rule/?language=python)
- [Clear rules](https://algolia.com/doc/api-reference/api-methods/clear-rules/?language=python)
- [Search rules](https://algolia.com/doc/api-reference/api-methods/search-rules/?language=python)
- [Replace all rules](https://algolia.com/doc/api-reference/api-methods/replace-all-rules/?language=python)
- [Copy rules](https://algolia.com/doc/api-reference/api-methods/copy-rules/?language=python)
- [Export rules](https://algolia.com/doc/api-reference/api-methods/export-rules/?language=python)




### A/B Test

- [Add A/B test](https://algolia.com/doc/api-reference/api-methods/add-ab-test/?language=python)
- [Get A/B test](https://algolia.com/doc/api-reference/api-methods/get-ab-test/?language=python)
- [List A/B tests](https://algolia.com/doc/api-reference/api-methods/list-ab-tests/?language=python)
- [Stop A/B test](https://algolia.com/doc/api-reference/api-methods/stop-ab-test/?language=python)
- [Delete A/B test](https://algolia.com/doc/api-reference/api-methods/delete-ab-test/?language=python)




### Insights

- [Clicked Object IDs After Search](https://algolia.com/doc/api-reference/api-methods/clicked-object-ids-after-search/?language=python)
- [Clicked Object IDs](https://algolia.com/doc/api-reference/api-methods/clicked-object-ids/?language=python)
- [Clicked Filters](https://algolia.com/doc/api-reference/api-methods/clicked-filters/?language=python)
- [Converted Objects IDs After Search](https://algolia.com/doc/api-reference/api-methods/converted-object-ids-after-search/?language=python)
- [Converted Object IDs](https://algolia.com/doc/api-reference/api-methods/converted-object-ids/?language=python)
- [Converted Filters](https://algolia.com/doc/api-reference/api-methods/converted-filters/?language=python)
- [Viewed Object IDs](https://algolia.com/doc/api-reference/api-methods/viewed-object-ids/?language=python)
- [Viewed Filters](https://algolia.com/doc/api-reference/api-methods/viewed-filters/?language=python)




### MultiClusters

- [Assign or Move userID](https://algolia.com/doc/api-reference/api-methods/assign-user-id/?language=python)
- [Get top userID](https://algolia.com/doc/api-reference/api-methods/get-top-user-id/?language=python)
- [Get userID](https://algolia.com/doc/api-reference/api-methods/get-user-id/?language=python)
- [List clusters](https://algolia.com/doc/api-reference/api-methods/list-clusters/?language=python)
- [List userIDs](https://algolia.com/doc/api-reference/api-methods/list-user-id/?language=python)
- [Remove userID](https://algolia.com/doc/api-reference/api-methods/remove-user-id/?language=python)
- [Search userID](https://algolia.com/doc/api-reference/api-methods/search-user-id/?language=python)




### Advanced

- [Get logs](https://algolia.com/doc/api-reference/api-methods/get-logs/?language=python)
- [Configuring timeouts](https://algolia.com/doc/api-reference/api-methods/configuring-timeouts/?language=python)
- [Set extra header](https://algolia.com/doc/api-reference/api-methods/set-extra-header/?language=python)
- [Wait for operations](https://algolia.com/doc/api-reference/api-methods/wait-task/?language=python)




### Vault






## Getting Help

- **Need help**? Ask a question to the [Algolia Community](https://discourse.algolia.com/) or on [Stack Overflow](http://stackoverflow.com/questions/tagged/algolia).
- **Found a bug?** You can open a [GitHub issue](https://github.com/algolia/algoliasearch-client-python/issues).

