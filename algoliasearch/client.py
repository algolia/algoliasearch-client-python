import json
import sys
import hashlib
import hmac

if sys.version < '3':
    from urllib import quote
    from urllib import urlencode
else:
    from urllib.parse import quote
    from urllib.parse import urlencode

import urllib3

from .version import VERSION
from .index import Index
from .helpers import deprecated, AlgoliaUtils_request, JSONEncoderWithDatetimeAndDefaultToString
from .helpers import AlgoliaException


class Client(object):
    '''
    Entry point in the Python API.
    You should instanciate a Client object with your ApplicationID, ApiKey and
    Hosts to start using Algolia Search API
    '''

    def __init__(self, application_id, api_key, hosts_array=None):
        '''
        Algolia Search Client initialization

        @param application_id the application ID you have in your admin interface
        @param api_key a valid API key for the service
        @param hosts_array the list of hosts that you have received for the service
        '''
        if not hosts_array:
            self.read_hosts = ['%s-dsn.algolia.net' % application_id,
                               '%s-1.algolianet.com' % application_id,
                               '%s-2.algolianet.com' % application_id,
                               '%s-3.algolianet.com' % application_id]
            self.write_hosts = ['%s.algolia.net' % application_id,
                                '%s-1.algolianet.com' % application_id,
                                '%s-2.algolianet.com' % application_id,
                                '%s-3.algolianet.com' % application_id]
        else:
            self.read_hosts = hosts_array
            self.write_hosts = hosts_array

        self.application_id = application_id
        self.api_key = api_key
        self.timeout = urllib3.util.timeout.Timeout(connect=1.0, read=30.0)
        self.search_timeout = urllib3.util.timeout.Timeout(connect=1.0,
                                                           read=5.0)

        self.headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'X-Algolia-API-Key': self.api_key,
            'X-Algolia-Application-Id': self.application_id,
            'User-Agent': ('Algolia Search for Python %s' % VERSION)
        }

    @deprecated
    def enableRateLimitForward(self, admin_api_key, end_user_ip,
                               rate_limit_api_key):
        return self.enable_rate_limit_forward(admin_api_key, end_user_ip,
                                              rate_limit_api_key)

    def enable_rate_limit_forward(self, admin_api_key, end_user_ip,
                                  rate_limit_api_key):
        '''
        Allow to use IP rate limit when you have a proxy between end-user and
        Algolia. This option will set the X-Forwarded-For HTTP header with the
        client IP and the X-Forwarded-API-Key with the API Key having rate limits.

        @param admin_api_key the admin API Key you can find in your dashboard
        @param end_user_ip the end user IP (you can use both IPV4 or IPV6 syntax)
        @param rate_limit_api_key the API key on which you have a rate limit
        '''
        self.headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'X-Algolia-API-Key': admin_api_key,
            'X-Forwarded-For': end_user_ip,
            'X-Forwarded-API-Key': rate_limit_api_key,
            'X-Algolia-Application-Id': self.application_id,
            'User-Agent': ('Algolia Search for python %s' % VERSION)
        }

    def set_end_user_ip(self, end_user_ip):
        '''
        Allow to forward an end user IP to the backend for geoip geoloc.
        This option will set the X-Forwarded-For HTTP header with the client IP.

        @param end_user_ip the end user IP (you can use both IPV4 or IPV6 syntax)
        '''
        self.headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'X-Algolia-API-Key': self.api_key,
            'X-Forwarded-For': end_user_ip,
            'X-Algolia-Application-Id': self.application_id,
            'User-Agent': ('Algolia Search for python %s' % VERSION)
        }

    @deprecated
    def disableRateLimitForward(self):
        return self.disable_rate_limit_forward()

    def disable_rate_limit_forward(self):
        '''
        Disable IP rate limit enabled with enable_rate_limit_forward() function.
        '''
        self.headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'X-Algolia-API-Key': self.api_key,
            'X-Algolia-Application-Id': self.application_id,
            'User-Agent': ('Algolia Search for python %s' % VERSION)
        }

    def set_extra_header(self, key, value):
        '''Allow to set custom header.'''
        self.headers[key] = value

    def set_timeout(self, connect_timeout, read_timeout, search_timeout=None):
        '''Allow to set the connection timeout in second.'''
        self.timeout = urllib3.util.timeout.Timeout(connect=connect_timeout,
                                                    read=read_timeout)
        if search_timeout:
            self.search_timeout = urllib3.util.timeout.Timeout(
                connect=connect_timeout,
                read=search_timeout)

    @deprecated
    def multipleQueries(self, queries, index_name_key='indexName'):
        return self.multiple_queries(queries, index_name_key)

    def multiple_queries(self, queries,
                         index_name_key='indexName',
                         strategy='none'):
        '''This method allows to query multiple indexes with one API call.'''
        requests = []
        for query in queries:
            index_name = query[index_name_key]
            del query[index_name_key]
            for key in query.keys():
                if isinstance(query[key], (list, dict, tuple, bool)):
                    query[key] = json.dumps(
                        query[key],
                        cls=JSONEncoderWithDatetimeAndDefaultToString)
            requests.append(
                {'indexName': index_name,
                 'params': urlencode(query)})
        body = {'requests': requests}
        return AlgoliaUtils_request(
            self.headers, self.read_hosts, 'POST',
            '/1/indexes/*/queries?strategy=' + strategy, self.search_timeout,
            body)

    def batch(self, requests):
        '''Send a batch request targetting multiple indices.'''
        return AlgoliaUtils_request(self.headers, self.write_hosts, 'POST',
                                    '/1/indexes/*/batch', self.timeout,
                                    {'requests': requests})

    @deprecated
    def listIndexes(self):
        return self.list_indexes()

    def list_indexes(self):
        '''
        List all existing indexes.
        Return an object of the form:
           {'items': [{ 'name': 'contacts', 'created_at': '2013-01-18T15:33:13.556Z'},
                      {'name': 'notes', 'created_at': '2013-01-18T15:33:13.556Z'}]}
        '''
        return AlgoliaUtils_request(self.headers, self.read_hosts, 'GET',
                                    '/1/indexes/', self.timeout)

    @deprecated
    def deleteIndex(self, index_name):
        return self.delete_index(index_name)

    def delete_index(self, index_name):
        '''
        Delete an index.
        Return an object of the form: {'deleted_at': '2013-01-18T15:33:13.556Z'}

        @param index_name the name of index to delete
        '''
        return AlgoliaUtils_request(self.headers, self.write_hosts, 'DELETE',
                                    '/1/indexes/%s' %
                                    quote(index_name.encode('utf8'),
                                          safe=''), self.timeout)

    @deprecated
    def moveIndex(self, src_index_name, dst_index_name):
        return self.move_index(src_index_name, dst_index_name)

    def move_index(self, src_index_name, dst_index_name):
        '''
        Move an existing index.

        @param src_index_name the name of index to copy.
        @param dst_index_name the new index name that will contains a copy
            of src_index_name (destination will be overriten if it already exist).
        '''
        request = {'operation': 'move', 'destination': dst_index_name}
        return AlgoliaUtils_request(self.headers, self.write_hosts, 'POST',
                                    '/1/indexes/%s/operation' %
                                    quote(src_index_name.encode('utf8'),
                                          safe=''), self.timeout, request)

    @deprecated
    def copyIndex(self, src_index_name, dst_index_name):
        return self.copy_index(src_index_name, dst_index_name)

    def copy_index(self, src_index_name, dst_index_name):
        '''
        Copy an existing index.

        @param src_index_name the name of index to copy.
        @param dst_index_name the new index name that will contains a copy of
            src_index_name (destination will be overriten if it already exist).
        '''
        request = {'operation': 'copy', 'destination': dst_index_name}
        return AlgoliaUtils_request(self.headers, self.write_hosts, 'POST',
                                    '/1/indexes/%s/operation' % (
                                        quote(src_index_name.encode('utf8'),
                                              safe='')
                                    ), self.timeout, request)

    @deprecated
    def getLogs(self, offset=0, length=10, type='all'):
        return self.get_logs(offset, length, type)

    def get_logs(self, offset=0, length=10, type='all'):
        '''
        Return last logs entries.

        @param offset Specify the first entry to retrieve (0-based,
            0 is the most recent log entry).
        @param length Specify the maximum number of entries to retrieve
            starting at offset. Maximum allowed value: 1000.
        '''
        if isinstance(type, bool):
            if type:
                type = 'error'
            else:
                type = 'all'
        return AlgoliaUtils_request(self.headers, self.write_hosts, 'GET',
                                    '/1/logs?offset=%d&length=%d&type=%s' %
                                    (offset, length, type), self.timeout)

    @deprecated
    def initIndex(self, index_name):
        return self.init_index(index_name)

    def init_index(self, index_name):
        '''
        Get the index object initialized (no server call needed for
        initialization).

        @param index_name the name of index
        '''
        return Index(self, index_name)

    @deprecated
    def listUserKeys(self):
        return self.list_user_keys()

    def list_user_keys(self):
        '''List all existing user keys with their associated ACLs.'''
        return AlgoliaUtils_request(self.headers, self.read_hosts, 'GET',
                                    '/1/keys', self.timeout)

    @deprecated
    def getUserKeyACL(self, key):
        return self.get_user_key_acl(key)

    def get_user_key_acl(self, key):
        ''''Get ACL of a user key.'''
        return AlgoliaUtils_request(self.headers, self.read_hosts, 'GET',
                                    '/1/keys/%s' % key, self.timeout)

    @deprecated
    def deleteUserKey(self, key):
        return self.delete_user_key(key)

    def delete_user_key(self, key):
        '''Delete an existing user key.'''
        return AlgoliaUtils_request(self.headers, self.write_hosts, 'DELETE',
                                    '/1/keys/%s' % key, self.timeout)

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
        '''
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
        '''
        if obj is dict:
            params = obj
        else:
            params = {'acl': obj}
        if validity != 0:
            params['validity'] = validity
        if max_queries_per_ip_per_hour != 0:
            params['maxQueriesPerIPPerHour'] = max_queries_per_ip_per_hour
        if max_hits_per_query != 0:
            params['maxHitsPerQuery'] = max_hits_per_query
        if indexes:
            params['indexes'] = indexes
        return AlgoliaUtils_request(self.headers, self.write_hosts, 'POST',
                                    '/1/keys', self.timeout, params)

    def update_user_key(self, key, obj,
                        validity=0,
                        max_queries_per_ip_per_hour=0,
                        max_hits_per_query=0,
                        indexes=None):
        '''
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
        '''
        if obj is dict:
            params = obj
        else:
            params = {'acl': obj}
        if validity != 0:
            params['validity'] = validity
        if max_queries_per_ip_per_hour != 0:
            params['maxQueriesPerIPPerHour'] = max_queries_per_ip_per_hour
        if max_hits_per_query != 0:
            params['maxHitsPerQuery'] = max_hits_per_query
        if indexes:
            params['indexes'] = indexes
        return AlgoliaUtils_request(self.headers, self.write_hosts, 'PUT',
                                    '/1/keys/' + key, self.timeout, params)

    @deprecated
    def generateSecuredApiKey(self, private_api_key, tag_filters,
                              user_token=None):
        return self.generate_secured_api_key(private_api_key, tag_filters,
                                             user_token)

    def generate_secured_api_key(self, private_api_key, tag_filters,
                                 user_token=None):
        '''
        Generate a secured and public API Key from a list of tag_filters and an
        optional user token identifying the current user.

        @param private_api_key your private API Key
        @param tag_filters the list of tags applied to the query (used as security)
        @param user_token an optional token identifying the current user
        '''
        if type(tag_filters) is list:
            tag_filters = ','.join(
                map(lambda t: ''.join(['(', ','.join(t), ')']) if
                    type(t) is list else str(t), tag_filters))
        if type(tag_filters) is dict:
            try:
                iteritems = tag_filters.iteritems()
                #  Python3.X Fix
            except AttributeError:
                iteritems = tag_filters.items()
            tag_filters = {}
            for k, v in iteritems:
                if isinstance(v, (list, dict, tuple, bool)):
                    tag_filters[k] = json.dumps(v)
                else:
                    tag_filters[k] = v
            tag_filters = urlencode(tag_filters)
        return hmac.new(str.encode(private_api_key), str.encode(''.join([
            str(tag_filters), str(user_token or '')
        ])), hashlib.sha256).hexdigest()

