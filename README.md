# Algolia Search API Client for Python

[Algolia Search](https://www.algolia.com) is a hosted full-text, numerical,
and faceted search engine capable of delivering realtime results from the first keystroke.

The **Algolia Search API Client for Python** lets
you easily use the [Algolia Search REST API](https://www.algolia.com/doc/rest-api/search) from
your Python code.

[![Build Status](https://travis-ci.org/algolia/algoliasearch-client-python.svg?branch=master)](https://travis-ci.org/algolia/algoliasearch-client-python) [![PyPI version](https://badge.fury.io/py/algoliasearch.svg?branch=master)](http://badge.fury.io/py/algoliasearch) [![Coverage Status](https://coveralls.io/repos/algolia/algoliasearch-client-python/badge.svg?branch=master)](https://coveralls.io/r/algolia/algoliasearch-client-python)


We implemented an asynchronous version of the client that may suit your need if
you are using a framework such as `aiohttp` in your backend. This version can
be found [here](https://github.com/algolia/algoliasearch-client-python-async).




## API Documentation

You can find the full reference on [Algolia's website](https://www.algolia.com/doc/api-client/python/).



1. **[Install](#install)**


1. **[Quick Start](#quick-start)**


1. **[Push data](#push-data)**


1. **[Configure](#configure)**


1. **[Search](#search)**


1. **[Search UI](#search-ui)**


1. **[List of available methods](#list-of-available-methods)**


# Getting Started



## Install

Install AlgoliaSearch using pip:

```bash
pip install --upgrade algoliasearch
```

## Quick Start

In 30 seconds, this quick start tutorial will show you how to index and search objects.

### Initialize the client

To begin, you will need to initialize the client. In order to do this you will need your **Application ID** and **API Key**.
You can find both on [your Algolia account](https://www.algolia.com/api-keys).

```python
from algoliasearch import algoliasearch

client = algoliasearch.Client("YourApplicationID", 'YourAPIKey')
index = client.init_index('your_index_name')
```

**Note:** If you use this API Client with Google AppEngine (Thanks [@apassant](https://github.com/apassant)), it will use `urlfetch` instead of using the `request` module. Please be aware of [urlfetch's limits](https://cloud.google.com/appengine/docs/python/urlfetch/), and note that SSL certificates will not be verified for calls to domains other than algolia.net due to the lack of SNI support in `urlfetch`. To run unit tests on the AppEngine stub, please define an `APPENGINE_RUNTIME` enviroment variable.

## Push data

Without any prior configuration, you can start indexing [500 contacts](https://github.com/algolia/datasets/blob/master/contacts/contacts.json) in the ```contacts``` index using the following code:
```python
index = client.init_index("contact")
batch = json.load(open('contacts.json'))
index.add_objects(batch)
```

## Configure

Settings can be customized to fine tune the search behavior. For example, you can add a custom sort by number of followers to further enhance the built-in relevance:

```python
index.set_settings({"customRanking": ["desc(followers)"]})
```

You can also configure the list of attributes you want to index by order of importance (most important first).

**Note:** The Algolia engine is designed to suggest results as you type, which means you'll generally search by prefix.
In this case, the order of attributes is very important to decide which hit is the best:

```python
index.set_settings({"searchableAttributes": ["lastname", "firstname", "company",
                                         "email", "city", "address"]})
```

## Search

You can now search for contacts using `firstname`, `lastname`, `company`, etc. (even with typos):

```python
# search by firstname
print index.search("jimmie")
# search a firstname with typo
print index.search("jimie")
# search for a company
print index.search("california paint")
# search for a firstname & company
print index.search("jimmie paint")
```

## Search UI

**Warning:** If you are building a web application, you may be more interested in using one of our
[frontend search UI libraries](https://www.algolia.com/doc/guides/search-ui/search-libraries/)

The following example shows how to build a front-end search quickly using
[InstantSearch.js](https://community.algolia.com/instantsearch.js/)

### index.html

```html
<!doctype html>
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/instantsearch.js@2.3/dist/instantsearch.min.css">
  <!-- Always use `2.x` versions in production rather than `2` to mitigate any side effects on your website,
  Find the latest version on InstantSearch.js website: https://community.algolia.com/instantsearch.js/v2/guides/usage.html -->
</head>
<body>
  <header>
    <div>
       <input id="search-input" placeholder="Search for products">
       <!-- We use a specific placeholder in the input to guides users in their search. -->
    
  </header>
  <main>
      
      
  </main>

  <script type="text/html" id="hit-template">
    
      <p class="hit-name">{{{_highlightResult.firstname.value}}} {{{_highlightResult.lastname.value}}}</p>
    
  </script>

  <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@2.3/dist/instantsearch.min.js"></script>
  <script src="app.js"></script>
</body>
```

### app.js

```js
var search = instantsearch({
  // Replace with your own values
  appId: 'YourApplicationID',
  apiKey: 'YourSearchOnlyAPIKey', // search only API key, no ADMIN key
  indexName: 'contacts',
  urlSync: true,
  searchParameters: {
    hitsPerPage: 10
  }
});

search.addWidget(
  instantsearch.widgets.searchBox({
    container: '#search-input'
  })
);

search.addWidget(
  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
      item: document.getElementById('hit-template').innerHTML,
      empty: "We didn't find any results for the search <em>\"{{query}}\"</em>"
    }
  })
);

search.start();
```




## List of available methods





### Search

- [Search index](https://algolia.com/doc/api-reference/api-methods/search/?language=python)
- [Search for facet values](https://algolia.com/doc/api-reference/api-methods/search-for-facet-values/?language=python)
- [Search multiple indexes](https://algolia.com/doc/api-reference/api-methods/multiple-queries/?language=python)
- [Browse index](https://algolia.com/doc/api-reference/api-methods/browse/?language=python)




### Indexing

- [Add objects](https://algolia.com/doc/api-reference/api-methods/add-objects/?language=python)
- [Update objects](https://algolia.com/doc/api-reference/api-methods/update-objects/?language=python)
- [Partial update objects](https://algolia.com/doc/api-reference/api-methods/partial-update-objects/?language=python)
- [Delete objects](https://algolia.com/doc/api-reference/api-methods/delete-objects/?language=python)
- [Delete by](https://algolia.com/doc/api-reference/api-methods/delete-by/?language=python)
- [Get objects](https://algolia.com/doc/api-reference/api-methods/get-objects/?language=python)
- [Custom batch](https://algolia.com/doc/api-reference/api-methods/batch/?language=python)




### Settings

- [Get settings](https://algolia.com/doc/api-reference/api-methods/get-settings/?language=python)
- [Set settings](https://algolia.com/doc/api-reference/api-methods/set-settings/?language=python)




### Manage indices

- [List indexes](https://algolia.com/doc/api-reference/api-methods/list-indices/?language=python)
- [Delete index](https://algolia.com/doc/api-reference/api-methods/delete-index/?language=python)
- [Copy index](https://algolia.com/doc/api-reference/api-methods/copy-index/?language=python)
- [Move index](https://algolia.com/doc/api-reference/api-methods/move-index/?language=python)
- [Clear index](https://algolia.com/doc/api-reference/api-methods/clear-index/?language=python)




### API Keys

- [Create secured API Key](https://algolia.com/doc/api-reference/api-methods/generate-secured-api-key/?language=python)
- [Add API Key](https://algolia.com/doc/api-reference/api-methods/add-api-key/?language=python)
- [Update API Key](https://algolia.com/doc/api-reference/api-methods/update-api-key/?language=python)
- [Delete API Key](https://algolia.com/doc/api-reference/api-methods/delete-api-key/?language=python)
- [Get API Key permissions](https://algolia.com/doc/api-reference/api-methods/get-api-key/?language=python)
- [List API Keys](https://algolia.com/doc/api-reference/api-methods/list-api-keys/?language=python)




### Synonyms

- [Save synonym](https://algolia.com/doc/api-reference/api-methods/save-synonym/?language=python)
- [Batch synonyms](https://algolia.com/doc/api-reference/api-methods/batch-synonyms/?language=python)
- [Delete synonym](https://algolia.com/doc/api-reference/api-methods/delete-synonym/?language=python)
- [Clear all synonyms](https://algolia.com/doc/api-reference/api-methods/clear-synonyms/?language=python)
- [Get synonym](https://algolia.com/doc/api-reference/api-methods/get-synonym/?language=python)
- [Search synonyms](https://algolia.com/doc/api-reference/api-methods/search-synonyms/?language=python)
- [Export Synonyms](https://algolia.com/doc/api-reference/api-methods/export-synonyms/?language=python)




### Query rules

- [Save rule](https://algolia.com/doc/api-reference/api-methods/rules-save/?language=python)
- [Batch rules](https://algolia.com/doc/api-reference/api-methods/rules-save-batch/?language=python)
- [Get rule](https://algolia.com/doc/api-reference/api-methods/rules-get/?language=python)
- [Delete rule](https://algolia.com/doc/api-reference/api-methods/rules-delete/?language=python)
- [Clear rules](https://algolia.com/doc/api-reference/api-methods/rules-clear/?language=python)
- [Search rules](https://algolia.com/doc/api-reference/api-methods/rules-search/?language=python)
- [Export rules](https://algolia.com/doc/api-reference/api-methods/rules-export/?language=python)




### A/B Test

- [Add A/B test](https://algolia.com/doc/api-reference/api-methods/add-ab-test/?language=python)
- [Get A/B test](https://algolia.com/doc/api-reference/api-methods/get-ab-test/?language=python)
- [List A/B tests](https://algolia.com/doc/api-reference/api-methods/list-ab-tests/?language=python)
- [Stop A/B test](https://algolia.com/doc/api-reference/api-methods/stop-ab-test/?language=python)
- [Delete A/B test](https://algolia.com/doc/api-reference/api-methods/delete-ab-test/?language=python)




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





## Getting Help

- **Need help**? Ask a question to the [Algolia Community](https://discourse.algolia.com/) or on [Stack Overflow](http://stackoverflow.com/questions/tagged/algolia).
- **Found a bug?** You can open a [GitHub issue](https://github.com/algolia/algoliasearch-client-python/issues).

