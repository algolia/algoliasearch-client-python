# -*- coding: utf-8 -*-
"""
Copyright (c) 2013 Algolia
http://www.algolia.com/

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import hmac
import hashlib
import base64
import random
import sys
import time
import copy
from platform import python_version

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from .version import VERSION
from .index import Index
from .analytics import Analytics
from .insights_client import InsightsClient
from .transport import Transport
from .helpers import deprecated
from .helpers import safe
from .helpers import urlify


MAX_API_KEY_LENGTH = 500


class RequestOptions:
    HEADERS = {
        'forwardedFor': 'X-Forwarded-For',
        'algoliaUserID': 'X-Algolia-User-ID'
    }

    def __init__(self, options):
        self.headers = {}
        self.parameters = {}

        for k, v in options.items():
            if k in self.HEADERS:
                self.headers[self.HEADERS[k]] = v
            else:
                self.parameters[k] = v


class Client(object):
    """
    Entry point in the Python Client API.
    You should instantiate a Client object with your ApplicationID, ApiKey to
    start using Algolia Search API.
    """

    def __init__(self, app_id, api_key, hosts=None, _transport=None):
        """
        Algolia Search Client initialization

        @param app_id the application ID you have in your admin interface
        @param api_key a valid API key for the service
        @param hosts_array the list of hosts that you have received for the service
        """
        self._transport = Transport() if _transport is None else _transport

        if not hosts:
            fallbacks = [
                '%s-1.algolianet.com' % app_id,
                '%s-2.algolianet.com' % app_id,
                '%s-3.algolianet.com' % app_id,
            ]
            random.shuffle(fallbacks)

            self._transport.read_hosts = ['%s-dsn.algolia.net' % app_id]
            self._transport.read_hosts.extend(fallbacks)
            self._transport.write_hosts = ['%s.algolia.net' % app_id]
            self._transport.write_hosts.extend(fallbacks)
        else:
            self._transport.read_hosts = hosts
            self._transport.write_hosts = hosts

        self._transport.headers = {
            'X-Algolia-Application-Id': app_id,
            'Content-Type': 'gzip',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'Algolia for Python (%s); Python (%s)' % (VERSION, python_version()),
        }

        self._app_id = app_id
        self.api_key = api_key

        # Fix for AppEngine bug when using urlfetch_stub
        if 'google.appengine.api.apiproxy_stub_map' in sys.modules.keys():
            self.headers.pop('Accept-Encoding', None)

    @property
    def timeout(self):
        return self._transport.timeout

    @timeout.setter
    def timeout(self, t):
        self._transport.timeout = t

    @property
    def search_timeout(self):
        return self._transport.search_timeout

    @search_timeout.setter
    def search_timeout(self, t):
        self._transport.search_timeout = t

    @property
    def app_id(self):
        return self._app_id

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value
        if len(value) > MAX_API_KEY_LENGTH:
            # If it was previously set, remove the header
            self.headers.pop('X-Algolia-API-Key', None)
        else:
            self.set_extra_headers(**{'X-Algolia-API-Key': value})

    @deprecated
    def enableRateLimitForward(self, admin_api_key, end_user_ip,
                               rate_limit_api_key):
        return self.enable_rate_limit_forward(end_user_ip, rate_limit_api_key)

    def enable_rate_limit_forward(self, end_user_ip, rate_limit_api_key):
        """
        Allow to use IP rate limit when you have a proxy between end-user and
        Algolia. This option will set the X-Forwarded-For HTTP header with the
        client IP and the X-Forwarded-API-Key with the API Key having rate limits.

        @param end_user_ip the end user IP (you can use both IPV4 or IPV6 syntax)
        @param rate_limit_api_key the API key on which you have a rate limit
        """
        self.headers.update({
            'X-Forwarded-For': end_user_ip,
            'X-Forwarded-API-Key': rate_limit_api_key,
        })

    def set_end_user_ip(self, end_user_ip):
        """
        Allow to forward an end user IP to the backend for geoip geoloc.
        This option will set the X-Forwarded-For HTTP header with the client IP.

        @param end_user_ip the end user IP (you can use both IPV4 or IPV6 syntax)
        """
        self.headers['X-Forwarded-For'] = end_user_ip

    @deprecated
    def disableRateLimitForward(self):
        return self.disable_rate_limit_forward()

    def disable_rate_limit_forward(self):
        """Disable IP rate limit."""
        self.headers.pop('X-Forwarded-For', None)
        self.headers.pop('X-Forwarded-API-Key', None)

    @deprecated
    def set_extra_header(self, key, value):
        """
        Allow to set custom header.

        This API is deprecated, please use `set_extra_headers(**kwargs)`.
        """
        self.set_extra_headers(**{key: value})

    def set_extra_headers(self, **kwargs):
        """
        Allow to set custom headers.

        >>> client.set_extra_header(Private=True)
        >>> myHeaders = {
        ...     'X-User': 223254,
        ...     'X-Privacy-Settings': 'NSA-Free'
        ... }
        >>> client.set_extra_header(**myHeaders)
        """
        self.headers.update(kwargs)

    @property
    def headers(self):
        return self._transport.headers

    @deprecated
    def set_timeout(self, connect_timeout, read_timeout, search_timeout=5):
        """
        Allow to set the connection timeout in second.

        This API is deprecated. The new API allows you to set directly the
        timeout. For example, if `connect_timeout=1`, `read_timeout=30` and
        `search_timeout=5`:

        >>> client.timeout = (1, 30)
        >>> client.search_timeout = (1, 5)

        `connect_timeout` is not mandatory:

        >>> client.timeout = 30
        >>> client.search_timeout = 5
        """
        self.timeout = (connect_timeout, read_timeout)
        self.search_timeout = (connect_timeout, search_timeout)

    @deprecated
    def multipleQueries(self, queries, index_name_key='indexName'):
        return self.multiple_queries(queries, index_name_key)

    def multiple_queries(self, queries,
                         index_name_key='indexName',
                         strategy='none',
                         request_options=None):
        """This method allows to query multiple indexes with one API call."""
        path = '/1/indexes/*/queries'

        requests = []
        for query in queries:
            index_name = query.pop(index_name_key)

            requests.append({
                'indexName': index_name,
                'params': urlencode(urlify(query))
            })

        data = {'requests': requests, 'strategy': strategy}
        return self._req(True, path, 'POST', request_options, data=data)

    def multiple_get_objects(self, requests, request_options=None):
        """
        Send a get objects targeting multiple indices.

        @param requests the list of requests
        @param request_options
        """
        if isinstance(requests, (list, tuple)):
            requests = {'requests': requests}

        path = '/1/indexes/*/objects'
        return self._req(True, path, 'POST', request_options, data=requests)

    def multiple_batch(self, operations, request_options=None):
        """
        Send a batch of write operations targeting multiple indices.

        @param requests the list of requests
        @param request_options
        """
        return self.batch(operations, request_options)

    def batch(self, requests, request_options=None):
        """Send a batch request targeting multiple indices."""
        if isinstance(requests, (list, tuple)):
            requests = {'requests': requests}

        path = '/1/indexes/*/batch'
        return self._req(False, path, 'POST', request_options, data=requests)

    def wait_task(self, index_name, task_id, time_before_retry=100, request_options=None):
        """
        Wait the publication of a task on the server.
        All server task are asynchronous and you can check with this method
        that the task is published.

        @param index_name the index name associated with the taskID
        @param task_id the id of the task returned by server
        @param time_before_retry the time in milliseconds before retry (default = 100ms)
        @param request_options
        """
        while True:
            task = self.get_task(index_name, task_id, request_options)
            if task['status'] == 'published':
                return task
            time.sleep(time_before_retry / 1000.0)

    def get_task(self, index_name, task_id, request_options=None):
        path = '/1/indexes/%s/task/%d' % (safe(index_name), task_id)
        return self._req(True, path, 'GET', request_options)

    def is_task_published(self, index_name, task_id, request_options=None):
        task = self.get_task(index_name, task_id, request_options)
        return task['status'] == 'published'

    @deprecated
    def listIndexes(self):
        return self.list_indexes()

    def list_indexes(self, request_options=None):
        """
        List all existing indexes.
        Return an object of the form:
           {'items': [{ 'name': 'contacts', 'created_at': '2013-01-18T15:33:13.556Z'},
                      {'name': 'notes', 'created_at': '2013-01-18T15:33:13.556Z'}]}
        """
        return self._req(True, '/1/indexes', 'GET', request_options)

    @deprecated
    def deleteIndex(self, index_name):
        return self.delete_index(index_name)

    def delete_index(self, index_name, request_options=None):
        """
        Delete an index.
        Return an object of the form: {'deleted_at': '2013-01-18T15:33:13.556Z'}

        @param index_name the name of index to delete
        """
        path = '/1/indexes/%s' % safe(index_name)
        return self._req(False, path, 'DELETE', request_options)

    @deprecated
    def moveIndex(self, src_index_name, dst_index_name):
        return self.move_index(src_index_name, dst_index_name)

    def move_index(self, src_index_name, dst_index_name, request_options=None):
        """
        Move an existing index.

        @param src_index_name the name of index to copy.
        @param dst_index_name the new index name that will contains a copy
            of src_index_name (destination will be overriten if it already exist).
        """
        path = '/1/indexes/%s/operation' % safe(src_index_name)
        request = {'operation': 'move', 'destination': dst_index_name}
        return self._req(False, path, 'POST', request_options, data=request)

    @deprecated
    def copyIndex(self, src_index_name, dst_index_name):
        return self.copy_index(src_index_name, dst_index_name)

    def copy_index(self, src_index_name, dst_index_name, request_options=None, scope=None):
        """
        Copy an existing index.

        @param src_index_name the name of index to copy.
        @param dst_index_name the new index name that will contains a copy of
            src_index_name (destination will be overriten if it already exist).
        @param scope the scope of the copy, as a list. Possible items are:
            settings, rules, synonyms.
        """
        path = '/1/indexes/%s/operation' % safe(src_index_name)
        request = {'operation': 'copy', 'destination': dst_index_name}

        if scope is not None:
            request['scope'] = scope

        return self._req(False, path, 'POST', request_options, data=request)

    def copy_settings(self, src_index_name, dst_index_name, request_options=None):
        """
        Copy an existing index's settings to other index.

        @param src_index_name the name of index to copy.
        @param dst_index_name the new index name that will contains a copy of
            src_index_name's settings (destination's settings will be overriten if it already exist).
        """

        return self.copy_index(src_index_name, dst_index_name, request_options, scope=['settings'])

    def copy_synonyms(self, src_index_name, dst_index_name, request_options=None):
        """
        Copy an existing index's synonyms to other index.

        @param src_index_name the name of index to copy.
        @param dst_index_name the new index name that will contains a copy of
            src_index_name's synonyms (destination's synonyms will be overriten if it already exist).
        """

        return self.copy_index(src_index_name, dst_index_name, request_options, scope=['synonyms'])

    def copy_rules(self, src_index_name, dst_index_name, request_options=None):
        """
        Copy an existing index's rules to other index.

        @param src_index_name the name of index to copy.
        @param dst_index_name the new index name that will contains a copy of
            src_index_name's rules (destination's rules will be overriten if it already exist).
        """

        return self.copy_index(src_index_name, dst_index_name, request_options, scope=['rules'])

    @deprecated
    def getLogs(self, offset=0, length=10, type='all'):
        return self.get_logs(offset, length, type)

    def get_logs(self, offset=0, length=10, type='all', request_options=None):
        """
        Return last logs entries.

        @param offset Specify the first entry to retrieve (0-based,
            0 is the most recent log entry).
        @param length Specify the maximum number of entries to retrieve
            starting at offset. Maximum allowed value: 1000.
        """
        params = {'offset': offset, 'length': length, 'type': type}
        return self._req(False, '/1/logs', 'GET', request_options, params)

    @deprecated
    def initIndex(self, index_name):
        return self.init_index(index_name)

    def init_index(self, index_name):
        """
        Get the index object initialized (no server call needed for
        initialization).

        @param index_name the name of index
        """
        return Index(self, index_name)

    def init_analytics(self):
        return Analytics(self, copy.deepcopy(self._transport))

    def init_insights_client(self, region='us'):
        return InsightsClient(copy.deepcopy(self._transport), region)

    @deprecated
    def listUserKeys(self):
        return self.list_user_keys()

    @deprecated
    def list_user_keys(self):
        """Use `list_api_keys`"""
        return self.list_api_keys()

    def list_api_keys(self, request_options=None):
        """List all existing api keys with their associated ACLs."""
        return self._req(True, '/1/keys', 'GET', request_options)

    @deprecated
    def getUserKeyACL(self, api_key):
        return self.get_user_key_acl(api_key)

    @deprecated
    def get_user_key_acl(self, api_key):
        """Use `get_api_key_acl`"""
        return self.get_api_key_acl(api_key)

    @deprecated
    def get_api_key_acl(self, api_key, request_options=None):
        """Use `get_api_key`"""
        return self.get_api_key(api_key, request_options)

    def get_api_key(self, api_key, request_options=None):
        """'Get ACL of an api key."""
        path = '/1/keys/%s' % api_key
        return self._req(True, path, 'GET', request_options)

    @deprecated
    def deleteUserKey(self, api_key):
        return self.delete_user_key(api_key)

    @deprecated
    def delete_user_key(self, api_key):
        """Use `delete_api_key`"""
        return self.delete_api_key(api_key)

    def delete_api_key(self, api_key, request_options=None):
        """Delete an existing api key."""
        path = '/1/keys/%s' % api_key
        return self._req(False, path, 'DELETE', request_options)

    @deprecated
    def addUserKey(self, obj,
                   validity=0,
                   max_queries_per_ip_per_hour=0,
                   max_hits_per_query=0,
                   indexes=None):
        return self.add_user_key(obj, validity, max_queries_per_ip_per_hour,
                                 max_hits_per_query, indexes)

    @deprecated
    def add_user_key(self, obj,
                     validity=0,
                     max_queries_per_ip_per_hour=0,
                     max_hits_per_query=0,
                     indexes=None):
        """Use `add_api_key`"""
        return self.add_api_key(
            obj, validity, max_queries_per_ip_per_hour, max_hits_per_query,
            indexes
        )

    def add_api_key(self, obj,
                    validity=0,
                    max_queries_per_ip_per_hour=0,
                    max_hits_per_query=0,
                    indexes=None,
                    request_options=None):
        """
        Create a new api key.

        @param obj can be two different parameters:
            The list of parameters for this key. Defined by a NSDictionary that
            can contains the following values:
                - acl: array of string
                - indices: array of string
                - validity: int
                - referers: array of string
                - description: string
                - maxHitsPerQuery: integer
                - queryParameters: string
                - maxQueriesPerIPPerHour: integer
            Or the list of ACL for this key. Defined by an array of NSString that
            can contains the following values:
                - search: allow to search (https and http)
                - addObject: allows to add/update an object in the index (https only)
                - deleteObject : allows to delete an existing object (https only)
                - deleteIndex : allows to delete index content (https only)
                - settings : allows to get index settings (https only)
                - editSettings : allows to change index settings (https only)
        @param validity the number of seconds after which the key will be
            automatically removed (0 means no time limit for this key)
        @param max_queries_per_ip_per_hour Specify the maximum number of API
            calls allowed from an IP address per hour.  Defaults to 0 (no rate limit).
        @param max_hits_per_query Specify the maximum number of hits this API
            key can retrieve in one call. Defaults to 0 (unlimited)
        @param indexes the optional list of targeted indexes
        """
        if not isinstance(obj, dict):
            obj = {'acl': obj}

        # Check with `is not None`, because 0 is evaluated to False
        if validity is not None:
            obj['validity'] = validity
        if max_queries_per_ip_per_hour is not None:
            obj['maxQueriesPerIPPerHour'] = max_queries_per_ip_per_hour
        if max_hits_per_query is not None:
            obj['maxHitsPerQuery'] = max_hits_per_query

        if indexes:
            obj['indexes'] = indexes

        return self._req(False, '/1/keys', 'POST', request_options, data=obj)

    @deprecated
    def update_user_key(self, api_key, obj,
                        validity=None,
                        max_queries_per_ip_per_hour=None,
                        max_hits_per_query=None,
                        indexes=None):
        """Use `update_api_key`"""
        return self.update_api_key(
            api_key, obj, validity, max_queries_per_ip_per_hour,
            max_hits_per_query, indexes
        )


    def update_api_key(self, api_key, obj,
                        validity=None,
                        max_queries_per_ip_per_hour=None,
                        max_hits_per_query=None,
                        indexes=None,
                        request_options=None):
        """
        Update a api key.

        @param obj can be two different parameters:
            The list of parameters for this key. Defined by a NSDictionary that
            can contains the following values:
                - acl: array of string
                - indices: array of string
                - validity: int
                - referers: array of string
                - description: string
                - maxHitsPerQuery: integer
                - queryParameters: string
                - maxQueriesPerIPPerHour: integer
            Or the list of ACL for this key. Defined by an array of NSString that
            can contains the following values:
                - search: allow to search (https and http)
                - addObject: allows to add/update an object in the index (https only)
                - deleteObject : allows to delete an existing object (https only)
                - deleteIndex : allows to delete index content (https only)
                - settings : allows to get index settings (https only)
                - editSettings : allows to change index settings (https only)
        @param validity the number of seconds after which the key will be
            automatically removed (0 means no time limit for this key)
        @param max_queries_per_ip_per_hour Specify the maximum number of API
            calls allowed from an IP address per hour.  Defaults to 0 (no rate limit).
        @param max_hits_per_query Specify the maximum number of hits this API
            key can retrieve in one call. Defaults to 0 (unlimited)
        @param indexes the optional list of targeted indexes
        """
        if not isinstance(obj, dict):
            obj = {'acl': obj}

        # Check with `is not None`, because 0 is evaluated to False
        if validity is not None:
            obj['validity'] = validity
        if max_queries_per_ip_per_hour is not None:
            obj['maxQueriesPerIPPerHour'] = max_queries_per_ip_per_hour
        if max_hits_per_query is not None:
            obj['maxHitsPerQuery'] = max_hits_per_query

        if indexes:
            obj['indexes'] = indexes

        path = '/1/keys/%s' % api_key
        return self._req(False, path, 'PUT', request_options, data=obj)


    def assign_user_id(self, user_id, cluster, request_options=None):
        """
        Assign a userID to a cluster
        Return an object of the form:
           {'updatedAt': 'XXXX'}
        """
        if request_options is None:
            request_options = RequestOptions({})
        request_options.headers['X-Algolia-User-ID'] = user_id
        body = {'cluster': cluster}

        return self._req(False, '/1/clusters/mapping', 'POST', request_options, data=body)

    def remove_user_id(self, user_id, request_options=None):
        """
        Remove a userID from the mapping
        Return an object of the form:
           {'deleteAt': 'XXXX'}
        """
        if request_options is None:
            request_options = RequestOptions({})
        request_options.headers['X-Algolia-User-ID'] = user_id

        return self._req(False, '/1/clusters/mapping', 'DELETE', request_options)

    def list_clusters(self, request_options=None):
        """
        List available cluster in the mapping
        Return an object of the form:
            {'clusters': [{
                "clusterName": "XXXX",
                "nbRecords": 0,
                "nbUserIDs": 0,
                "dataSize": 0
            }]}
        """

        return self._req(True, '/1/clusters', 'GET', request_options)

    def get_user_id(self, user_id, request_options=None):
        """
        Get one userID in the mapping
        Return an object in the form:
        {
           "userID": "XXXX",
           "clusterName": "XXXX",
           "nbRecords": 0,
           "dataSize": 0
        }
        """
        return self._req(True, '/1/clusters/mapping/%s' % safe(user_id), 'GET', request_options)

    def list_user_ids(self, page = 0, hits_per_page = 20, request_options=None):
        """
        List userIDs in the mapping
        Return an object in the form:
        {
            "userIDs": [{
                "userID": "userName",
                "clusterName": "name",
                "nbRecords": 0,
                "dataSize": 0
            }],
            "page": 0,
            "hitsPerPage": 20
        }
        """
        body={}
        if page is not  None:
            body["page"] = page
        if hits_per_page is not None:
            body["hitsPerPage"] = hits_per_page

        return self._req(True, '/1/clusters/mapping/', 'GET', request_options, data=body)

    def get_top_user_id(self, request_options=None):
        """
        Get top userID in the mapping
        Return an object in the form:
        {
            "topUsers": {
                "XXXX": [{
                    "userID": "userName",
                    "nbRecords": 0,
                    "dataSize": 0
                }]
            },
            "page": 0,
            "hitsPerPage": 20
        }
        """
        return self._req(True, '/1/clusters/mapping/top', 'GET', request_options)

    def search_user_ids(self, query, cluster=None, page=None, hits_per_page=None, request_options=None):
        """
        Search userIDs in the mapping
        Return an object in the form:
        {
            "hits": [{
                    "userID": "userName",
                    "clusterName": "name",
                    "nbRecords": 0,
                    "dataSize": 0
            }],
            "nbHits":0,
            "page": 0,
            "hitsPerPage": 20
        }
        """
        body={}
        if query is not None:
            body["query"] = query
        if cluster is not None:
            body["cluster"] = cluster
        if page is not  None:
            body["page"] = page
        if hits_per_page is not None:
            body["hitsPerPage"] = hits_per_page

        return self._req(True, '/1/clusters/mapping/search', 'POST', request_options, data=body)

    @deprecated
    def generateSecuredApiKey(self, private_api_key, tag_filters,
                              user_token=''):
        return self.generate_secured_api_key(private_api_key, tag_filters,
                                             user_token)

    def generate_secured_api_key(self, private_api_key, queryParameters,
                                 user_token=''):
        """
        Generate a secured and public API Key from a dict of query parameters and an
        optional user token identifying the current user.

        @param private_api_key your private API Key
        @param queryParameters the dict of query parameters applied to the query (used as security)
        @param user_token an optional token identifying the current user
        """
        if isinstance(queryParameters, (list, tuple)): #List of tags
            queryParameters = ','.join(
                    map(lambda t: ''.join(['(', ','.join(t), ')']) if
                        isinstance(t, (list, tuple)) else t, queryParameters))
            queryParameters = {'tagFilters': queryParameters}
        elif not isinstance(queryParameters, dict) and not '=' in queryParameters: #TagFilter
            queryParameters = {'tagFilters': queryParameters}

        if isinstance(queryParameters, dict): #New API Key generator
            if user_token != None and user_token != '':
                queryParameters['userToken'] = user_token
            queryParameters = urlencode(urlify(queryParameters))

        securedKey = hmac.new(private_api_key.encode('utf-8'), queryParameters.encode('utf-8'), hashlib.sha256).hexdigest()
        return str(base64.b64encode(("%s%s" % (securedKey, queryParameters)).encode('utf-8')).decode('utf-8'))

    def is_alive(self, request_options=None):
        """
        Test if the server is alive.
        This performs a simple application-level ping. If up and running, the server answers with a basic message.
        """
        return self._req(True, '/1/isalive', 'GET', request_options)

    def set_personalization_strategy(self, strategy, request_options=None):
        return self._req(False, '/1/recommendation/personalization/strategy', 'POST', request_options, data=strategy)

    def get_personalization_strategy(self, request_options=None):
        return self._req(True, '/1/recommendation/personalization/strategy', 'GET', request_options)

    def _req(self, is_search, path, meth, request_options=None, params=None, data=None):
        if len(self.api_key) > MAX_API_KEY_LENGTH:
            if data is None:
                data = {}
            data['apiKey'] = self.api_key
        return self._transport.req(is_search, path, meth, params, data, request_options)
