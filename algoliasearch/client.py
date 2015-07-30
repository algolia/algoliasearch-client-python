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

import os
import json
import hmac
import hashlib

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from requests import Session
from requests import exceptions

from .version import VERSION
from .index import Index

from .helpers import AlgoliaException
from .helpers import CustomJSONEncoder
from .helpers import deprecated
from .helpers import safe
from .helpers import urlify


class Client(object):
    """
    Entry point in the Python Client API.
    You should instanciate a Client object with your ApplicationID, ApiKey to
    start using Algolia Search API.
    """

    def __init__(self, app_id, api_key, hosts_array=None):
        """
        Algolia Search Client initialization

        @param app_id the application ID you have in your admin interface
        @param api_key a valid API key for the service
        @param hosts_array the list of hosts that you have received for the service
        """
        if not hosts_array:
            self.read_hosts = ['%s-dsn.algolia.net' % app_id,
                               '%s-1.algolianet.com' % app_id,
                               '%s-2.algolianet.com' % app_id,
                               '%s-3.algolianet.com' % app_id]
            self.write_hosts = ['%s.algolia.net' % app_id,
                                '%s-1.algolianet.com' % app_id,
                                '%s-2.algolianet.com' % app_id,
                                '%s-3.algolianet.com' % app_id]
        else:
            self.read_hosts = hosts_array
            self.write_hosts = hosts_array

        self._app_id = app_id
        self._api_key = api_key
        self.timeout = (1, 30)
        self.search_timeout = (1, 5)

        self._session = Session()
        self._session.verify = os.path.join(os.path.dirname(__file__),
                                            'resources/ca-bundle.crt')
        self._session.headers = {
            'X-Algolia-API-Key': self.api_key,
            'X-Algolia-Application-Id': self.app_id,
            'Content-Type': 'application/json',
            'User-Agent': 'Algolia Search for Python %s' % VERSION
        }

    @property
    def app_id(self):
        return self._app_id

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value
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
        return self._session.headers

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
                         strategy='none'):
        """This method allows to query multiple indexes with one API call."""
        path = '/1/indexes/*/queries'
        params = {'strategy': strategy}

        requests = []
        for query in queries:
            index_name = query.pop(index_name_key)

            requests.append({
                'indexName': index_name,
                'params': urlencode(urlify(query))
            })

        return self._perform_request(
                    self.read_hosts, path, 'POST', params=params,
                    body={'requests': requests}, is_search=True)

    def batch(self, requests):
        """Send a batch request targetting multiple indices."""
        if isinstance(requests, (list, tuple)):
            requests = {'requests': requests}

        return self._perform_request(self.write_hosts, '/1/indexes/*/batch',
                                     'POST', body=requests)

    @deprecated
    def listIndexes(self):
        return self.list_indexes()

    def list_indexes(self):
        """
        List all existing indexes.
        Return an object of the form:
           {'items': [{ 'name': 'contacts', 'created_at': '2013-01-18T15:33:13.556Z'},
                      {'name': 'notes', 'created_at': '2013-01-18T15:33:13.556Z'}]}
        """
        return self._perform_request(self.read_hosts, '/1/indexes', 'GET')

    @deprecated
    def deleteIndex(self, index_name):
        return self.delete_index(index_name)

    def delete_index(self, index_name):
        """
        Delete an index.
        Return an object of the form: {'deleted_at': '2013-01-18T15:33:13.556Z'}

        @param index_name the name of index to delete
        """
        path = '/1/indexes/%s' % safe(index_name)
        return self._perform_request(self.write_hosts, path, 'DELETE')

    @deprecated
    def moveIndex(self, src_index_name, dst_index_name):
        return self.move_index(src_index_name, dst_index_name)

    def move_index(self, src_index_name, dst_index_name):
        """
        Move an existing index.

        @param src_index_name the name of index to copy.
        @param dst_index_name the new index name that will contains a copy
            of src_index_name (destination will be overriten if it already exist).
        """
        path = '/1/indexes/%s/operation' % safe(src_index_name)
        request = {'operation': 'move', 'destination': dst_index_name}
        return self._perform_request(self.write_hosts, path, 'POST',
                                     body=request)

    @deprecated
    def copyIndex(self, src_index_name, dst_index_name):
        return self.copy_index(src_index_name, dst_index_name)

    def copy_index(self, src_index_name, dst_index_name):
        """
        Copy an existing index.

        @param src_index_name the name of index to copy.
        @param dst_index_name the new index name that will contains a copy of
            src_index_name (destination will be overriten if it already exist).
        """
        path = '/1/indexes/%s/operation' % safe(src_index_name)
        request = {'operation': 'copy', 'destination': dst_index_name}
        return self._perform_request(self.write_hosts, path, 'POST',
                                     body=request)

    @deprecated
    def getLogs(self, offset=0, length=10, type='all'):
        return self.get_logs(offset, length, type)

    def get_logs(self, offset=0, length=10, type='all'):
        """
        Return last logs entries.

        @param offset Specify the first entry to retrieve (0-based,
            0 is the most recent log entry).
        @param length Specify the maximum number of entries to retrieve
            starting at offset. Maximum allowed value: 1000.
        """
        params = {
            'offset': offset,
            'length': length,
            'type': type
        }
        return self._perform_request(self.write_hosts, '/1/logs', 'GET',
                                     params=params)

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

    @deprecated
    def listUserKeys(self):
        return self.list_user_keys()

    def list_user_keys(self):
        """List all existing user keys with their associated ACLs."""
        return self._perform_request(self.read_hosts, '/1/keys', 'GET')

    @deprecated
    def getUserKeyACL(self, key):
        return self.get_user_key_acl(key)

    def get_user_key_acl(self, key):
        """'Get ACL of a user key."""
        path = '/1/keys/%s' % key
        return self._perform_request(self.read_hosts, path, 'GET')

    @deprecated
    def deleteUserKey(self, key):
        return self.delete_user_key(key)

    def delete_user_key(self, key):
        """Delete an existing user key."""
        path = '/1/keys/%s' % key
        return self._perform_request(self.write_hosts, path, 'DELETE')

    @deprecated
    def addUserKey(self, obj,
                   validity=0,
                   max_queries_per_ip_per_hour=0,
                   max_hits_per_query=0,
                   indexes=None):
        return self.add_user_key(obj, validity, max_queries_per_ip_per_hour,
                                 max_hits_per_query, indexes)

    def add_user_key(self, obj,
                     validity=0,
                     max_queries_per_ip_per_hour=0,
                     max_hits_per_query=0,
                     indexes=None):
        """
        Create a new user key.

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

        obj.update({
            'validity': validity,
            'maxQueriesPerIPPerHour': max_queries_per_ip_per_hour,
            'maxHitsPerQuery': max_hits_per_query
        })

        if indexes:
            obj['indexes'] = indexes

        return self._perform_request(self.write_hosts, '/1/keys', 'POST',
                                     body=obj)

    def update_user_key(self, key, obj,
                        validity=None,
                        max_queries_per_ip_per_hour=None,
                        max_hits_per_query=None,
                        indexes=None):
        """
        Update a user key.

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

        path = '/1/keys/%s' % key
        return self._perform_request(self.write_hosts, path, 'PUT',
                                     body=obj)

    @deprecated
    def generateSecuredApiKey(self, private_api_key, tag_filters,
                              user_token=''):
        return self.generate_secured_api_key(private_api_key, tag_filters,
                                             user_token)

    def generate_secured_api_key(self, private_api_key, tag_filters,
                                 user_token=''):
        """
        Generate a secured and public API Key from a list of tag_filters and an
        optional user token identifying the current user.

        @param private_api_key your private API Key
        @param tag_filters the list of tags applied to the query (used as security)
        @param user_token an optional token identifying the current user
        """
        if isinstance(tag_filters, (list, tuple)):
            tag_filters = ','.join(
                    map(lambda t: ''.join(['(', ','.join(t), ')']) if
                        isinstance(t, (list, tuple)) else t, tag_filters))
        elif isinstance(tag_filters, dict):
            tag_filters = urlencode(urlify(tag_filters))

        return hmac.new(str.encode(private_api_key),
                        str.encode(''.join([tag_filters, str(user_token)])),
                        hashlib.sha256).hexdigest()

    def _perform_request(self, hosts, path, method, params=None, body=None,
                         is_search=False):
        """Perform an HTTPS request with retry logic."""
        if params:
            params = urlify(params)
        if body:
            body = json.dumps(body, cls=CustomJSONEncoder)

        timeout = self.search_timeout if is_search else self.timeout
        exceptions_hosts = {}
        for i, host in enumerate(hosts):
            if i > 1:
                if isinstance(timeout, tuple):
                    timeout = (timeout[0] + 2, timeout[1] + 10)
                else:
                    timeout += 10

            try:
                res = self._session.request(
                            method, 'https://%s%s' % (host, path),
                            params=params, data=body, timeout=timeout)

                res.raise_for_status()
                return res.json()
            except exceptions.HTTPError:
                raise AlgoliaException(res.json()['message'])
            except exceptions.Timeout as e:
                exceptions_hosts[host] = str(e)
                pass

        # Impossible to connect
        raise AlgoliaException('%s %s' % ('Unreachable hosts:',
                               exceptions_hosts))
