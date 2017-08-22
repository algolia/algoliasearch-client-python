# Algolia Search API Client for Python

[Algolia Search](https://www.algolia.com) is a hosted full-text, numerical, and faceted search engine capable of delivering realtime results from the first keystroke.
The **Algolia Search API Client for Python** lets you easily use the [Algolia Search REST API](https://www.algolia.com/doc/rest-api/search) from your Python code.

[![Build Status](https://travis-ci.org/algolia/algoliasearch-client-python.svg?branch=master)](https://travis-ci.org/algolia/algoliasearch-client-python) [![PyPI version](https://badge.fury.io/py/algoliasearch.svg?branch=master)](http://badge.fury.io/py/algoliasearch) [![Coverage Status](https://coveralls.io/repos/algolia/algoliasearch-client-python/badge.svg?branch=master)](https://coveralls.io/r/algolia/algoliasearch-client-python)


We implemented an asynchronous version of the client that may suit your need if
you are using a framework such as `aiohttp` in your backend. This version can
be found [here](https://github.com/algolia/algoliasearch-client-python-async).




## API Documentation

You can find the full reference on [Algolia's website](https://www.algolia.com/doc/api-client/python/).


## Table of Contents


1. **[Install](#install)**


1. **[Quick Start](#quick-start)**

    * [Initialize the client](#initialize-the-client)
    * [Push data](#push-data)
    * [Search](#search)
    * [Configure](#configure)
    * [Frontend search](#frontend-search)

1. **[Getting Help](#getting-help)**





# Getting Started



## Install

Install AlgoliaSearch using pip:

```bash
pip install --upgrade algoliasearch
```

## Quick Start

In 30 seconds, this quick start tutorial will show you how to index and search objects.

### Initialize the client

You first need to initialize the client. For that you need your **Application ID** and **API Key**.
You can find both of them on [your Algolia account](https://www.algolia.com/api-keys).

```python
from algoliasearch import algoliasearch

client = algoliasearch.Client("YourApplicationID", 'YourAPIKey')
```

**Note:** If you use this API Client with Google AppEngine (Thanks [@apassant](https://github.com/apassant)), it will use `urlfetch` instead of using the `request` module. Please be aware of [urlfetch's limits](https://cloud.google.com/appengine/docs/python/urlfetch/), and note that SSL certificates will not be verified for calls to domains other than algolia.net due to the lack of SNI support in `urlfetch`. To run unit tests on the AppEngine stub, please define an `APPENGINE_RUNTIME` enviroment variable.

### Push data

Without any prior configuration, you can start indexing [500 contacts](https://github.com/algolia/algoliasearch-client-python/blob/master/contacts.json) in the ```contacts``` index using the following code:
```python
index = client.init_index("contact")
batch = json.load(open('contacts.json'))
index.add_objects(batch)
```

### Search

You can now search for contacts using firstname, lastname, company, etc. (even with typos):

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

### Configure

Settings can be customized to tune the search behavior. For example, you can add a custom sort by number of followers to the already great built-in relevance:

```python
index.set_settings({"customRanking": ["desc(followers)"]})
```

You can also configure the list of attributes you want to index by order of importance (first = most important):

**Note:** Since the engine is designed to suggest results as you type, you'll generally search by prefix.
In this case the order of attributes is very important to decide which hit is the best:

```python
index.set_settings({"searchableAttributes": ["lastname", "firstname", "company",
                                         "email", "city", "address"]})
```

### Frontend search

**Note:** If you are building a web application, you may be more interested in using our [JavaScript client](https://github.com/algolia/algoliasearch-client-javascript) to perform queries.

It brings two benefits:
  * Your users get a better response time by not going through your servers
  * It will offload unnecessary tasks from your servers

```html
<script src="https://cdn.jsdelivr.net/algoliasearch/3/algoliasearch.min.js"></script>
<script>
var client = algoliasearch('ApplicationID', 'apiKey');
var index = client.initIndex('indexName');

// perform query "jim"
index.search('jim', searchCallback);

// the last optional argument can be used to add search parameters
index.search(
  'jim', {
    hitsPerPage: 5,
    facets: '*',
    maxValuesPerFacet: 10
  },
  searchCallback
);

function searchCallback(err, content) {
  if (err) {
    console.error(err);
    return;
  }

  console.log(content);
}
</script>
```

## Getting Help

- **Need help**? Ask a question to the [Algolia Community](https://discourse.algolia.com/) or on [Stack Overflow](http://stackoverflow.com/questions/tagged/algolia).
- **Found a bug?** You can open a [GitHub issue](https://github.com/algolia/algoliasearch-client-python/issues).



