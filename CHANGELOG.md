# CHANGELOG

### UNRELEASED


<Contributors, please add your changes below this line>

* Adds move method on index - PR [#386](https://github.com/algolia/algoliasearch-client-python/pull/386)
    You can now move an index to a new destination directly on the index object. Usage:
        ```python
        index = client.init_index('name');
        index.move_to('new_name')
        index.get_settings() # Get the settings of the `new_name` index
        ```

### 1.17.0 - 2018-06-19

* Introduce AB Testing feature - PR [#408](https://github.com/algolia/algoliasearch-client-php/pull/#408)
    List/Create/Stop/Delete AB Tests programmatically
    Introduce new Analytics object, wrapper around the
    [Analytics API](https://www.algolia.com/doc/rest-api/analytics/) (more methods to come).

* 2 methods about taskID initially available in the `Index` moved to the `Client`.
    You could get some taskID from the engine without necessarily have an instance of Index,
    instead of instantiating an index that you won't need, you can now call wait_task and get_task_status on the client.
    The original methods on the index still work and are **not** deprecated.

    ```python
    client.wait_ask(index_name, taskID)
    client.get_task_status(index_name, taskID)
    ```

### 1.16.0 - 2018-06-07

🎉 Note to contributors:
Everybody is now able to run the test on Travis, since we moved to temporary credentials.️ ⤵️
https://blog.algolia.com/travis-encrypted-variables-external-contributions/

* **Deprecation**: Keys should not be managed at the Index level but at the Client level

    All methods `Index.(list|get|add|update)_api_keys()` are now
    deprecated. If you already have keys on the Index, it would be best
    to delete them and regenerate new keys with client, adding the `indexes`
    restriction.

    Example:
    ```python
    client.add_api_key({
        'acl': 'search',
        'indexes': 'my_index_name',
    })
    ```

* Feat: Let you define all API keys capabilities in one map for `update_api_key` and `add_api_key`

    Example:
    ```python
    client.add_api_key({
        'acl': ['search'],
        'validity': 300,
        'maxQueriesPerIPPerHour': 100,
        'maxHitsPerQuery': 20,
        'indexes': ['dev_*'],
        'referers': ['algolia.com/*'],
        'queryParameters': 'typoTolerance=strict&ignorePlurals=false',
        'description': 'Limited search only API key for algolia.com'
    })
    ```
    instead of
    ```python
    client.add_api_key(['search'], 300, 100, 20, ['dev_*'])
    ```

* Fix: Adding a rule with an empty ID failed silently, it will now raise an exception

* Fix: `Index.get_objects` requires an array for `attributes_to_retrieve`
    strings could be passed before but it would fail silently every time
    See [#299](https://github.com/algolia/algoliasearch-client-python/issues/299)

* Fix: When browsing, ensure cursor is passed in the body
    Cursor can become so long that the generated URL fails (error HTTP 414).

* Chore: Add Python version to the UserAgent

### 1.15.3 - 2018-03-15

* Remove the `[security]` flair of `requests`

### 1.15.2 - 2017-12-18

* Add 'page' and 'hitsPerPage' to list_user_ids

### 1.15.1 - 2017-12-05

* Implement delete_by, an atomic delete_by_query
* Deprecate delete_by_query

### 1.15.0 - 2017-12-05

* Implement iter_synonyms to browse synonyms
* Implement iter_rules to browse rules
* Implement an optional parameter for copy_index that allows a partial copy of an index

### 1.14.1 - 2017-11-06

* Fix request_options not always optional

### 1.14.0 - 2017-10-29

* Add per-request parameters
* Add multi-cluster support

### 1.13.0 - 2017-01-31

* Add rules endpoints

### 1.12.0 - 2017-01-31

* Do not ship the certificates anymore

### 1.11.2 - 2017-01-31

* Decode the README with utf-8 encoding in setup.py

### 1.11.1 - 2017-01-02

* Add `forward_to_replicas` on top of `forward_to_slaves`

### 1.11.0 - 2016-12-02

* Configure DNS resolvinf timeout
* Implement new retry logic

### 1.10.1 - 2016-11-29

* Add `search_for_facet_value` to supplant `search_facet`

### 1.10.0 - 2016-10-19

* Add `attribute_to_retrieve` to `get_objects`
* Add `no_create` with `partial_update_object`
* Implement the search in facet API end point

### 1.9.2 - 2016-08-08

* Fix error on large API keys by including them in the JSON body instead of as a header
* Fix potential parsing error in case of httpCode == 4XX

### 1.9.1 - 2016-07-05

* Fix the `strategy` parameter of `mutliple_queries`
* Add the `forwardToSlaves` parameter of `set_settings`

### 1.9.0 - 2016-06-15

* Implement the new synonym API functions
* Ensure the hosts are chosen randomly when retrying for better balancing

### 1.8.0 - 2016-02-11

* Upgrade to requests[security]>=2.9.1 to fix the underlying SNI issues

### 1.7.1 - 2015-10-23

* Add compatibility with Google Appengine

### 1.7.0 - 2015-10-16

* Remove the retry on 4XX errors
* Add new secured api key
* Fix bug with distinct on the deleteByQuery method

### 1.6.8 - 2015-10-07

* Catch all exceptions in the retry strategy

### 1.6.7 - 2015-10-06

* Fix an issue with the handling of connection errors

### 1.6.6 - 2015-09-08

* Fix an issue with ObjectID that are not string
* Fix an issue with default dict parameter

### 1.6.4 - 2015-08-17

* The JSON encoder fallback to unicode/str if it raises TypeError

### 1.6.3 - 2015-08-13

* Fix issue with unicode query

### 1.6.2 - 2015-08-02

* Search now uses POST request instead of GET

### 1.6.1 - 2015-07-30

* Fix PyPI build

### 1.6.0 - 2015-07-30

* Rewrite all the package. The API Client is 100% backward compatible.
* Switch from urllib3 to requests
* Various fix

### 1.5.9 - 2015-07-23

* Fix browse_all and browse_from methods

### 1.5.8 - 2015-07-10

* Add the ability to use the api behind a proxy

### 1.5.5 - 2015-06-16

* Fix issue with non existing facet in the result set for the disjunctive faceting method
* Add browse_from and browse_all methods

### 1.5.4 - 2015-05-04
* Add new methods to add/update api key
* Add batch method to target multiple indices
* Add strategy parameter for the multipleQueries
* Add new method to generate secured api key from query parameters

### 1.5.3 - 2015-04-24

* Add method to forward the end user ip

### 1.5.2 - 2015-04-09

* Better retry strategy using two different provider (Improve high-availability of the solution, retry is done on algolianet.com)
* Read operations are performed to APPID-dsn.algolia.net domain first to leverage Distributed Search Network (select the closest location)
* Improved timeout strategy: increasse timeout after 2 trials & have a different read timeout for search operations

### 1.5.1 - 2015-03-13

* Fixed ImportError with Python 3.4

### 1.5.0 - 2014-12-26

* Added timeout (connect timeout = 1s & read timeout = 30s). Can be overridden with set_timeout method

### 1.4.0 - 2014-11-29

* Moved API calls to algolia.net domain instead of algolia.io domain

### 1.3.11 - 2014-10-22

* Add more information when hosts are unreachable

### 1.3.10 - 2014-10-11

* Do not assume that objectIDs are strings.

### 1.3.9 - 2014-09-17

* Making Client and Index new-style python classes for easier extension

### 1.3.{2,3,4,5,6,7,8} - 2014-09-15

* Fixed resources/ca-bundle.crt inclusion

### 1.3.1 - 2014-09-14

* Added update_user_key & update_user_key

### 1.3.0 - 2014-08-25

* Use snake-case everywhere (backward compatible)

### 1.2.14 - 2014-08-22

* More fixes around bool/json serialization

### 1.2.13 - 2014-08-21

* Fixed waitTask's sleep

### 1.2.12 - 2014-08-20

* Fixed boolean-based query parameter encoding

### 1.2.11 - 2014-07-17

* Added getObjects
* Added deleteByQuery

### 1.2.10 - 2014-04-18

* Fixed decimal JSON serialization
* Force urllib3>=1.8.1 dependency to work-around a GAE bug (https://github.com/shazow/urllib3/issues/356)

### 1.2.9 - 2014-03-30

* Fixed invalid date->timestamp conversion

### 1.2.8 - 2014-02-24

* Fixed python3 compatibility

### 1.2.7 - 2014-02-24

* Added deleteObjects
* Added generateSecuredApiKey based on an API Key, tagFilters and optional user token
* Ability to specify a list of indexes targeted by a user API key
* Missing UTF-8 encoding while generating DELETE URL

### 1.2.6 - 2014-02-01

* Fixed encoding of objectID with slash

### 1.2.5 - 2014-01-30

* Fallback on str() if JSON encoding fails

### 1.2.4 - 2014-01-11

* Fixed bug on batch commands introduced in 1.2.3

### 1.2.3 - 2014-01-11

* Fixed doc strings
* Refactor of batch commands

### 1.2.2 - 2013-12-23

* Fixed encoding of dates

### 1.2.1 - 2013-12-1

* Documentation of distinct feature
* Store last exception and raise it instead of generic 'unreachable host' exception

### 1.1.6 - 2013-12-10

* Improved readability of search & settings parameters

### 1.1.5 - 2013-12-06

* Added browse method

### 1.1.3 - 2013-12-06

* Added partialUpdateObjects method

### 1.1.1 - 2013-11-08

* Encode array-based search params.

### 1.1.0 - 2013-11-07

* Added clearIndex method
* Added support of maxQueriesPerIPPerHour and maxHitsPerQuery in creation of API keys

### 1.0.2 - 2013-10-11

* Fixed urlencode problem

### 1.0.1 - 2013-10-09

* Fixed dependencies

### 1.0.0 - 2013-10-09
* Make python client compatible with python 2.6+ (including Python 3.x)
