import json
import sys
import time

if sys.version < '3':
    from urllib import quote
    from urllib import urlencode
else:
    from urllib.parse import quote
    from urllib.parse import urlencode

from .helpers import deprecated, AlgoliaUtils_request, AlgoliaException


class IndexIterator:
    '''Iterator on index.'''

    def __init__(self, index, params={}, cursor=None):
        self.index = index
        self.params = params
        self.cursor = cursor
        self.pos = 0
        self.answer = None

    def __iter__(self):
        self.__load_next_page()
        return self

    def __next__(self):
        return self.next()

    def next(self):
        while True:
            if self.pos < len(self.answer['hits']):
                self.pos += 1
                return self.answer['hits'][self.pos - 1]
            elif self.cursor and len(self.cursor) > 0:
                self.__load_next_page()
                continue
            else:
                raise StopIteration

    def __load_next_page(self):
        self.answer = self.index.browse_from(self.params, self.cursor)
        self.pos = 0
        self.cursor = self.answer.get('cursor', None)


class Index(object):
    '''
    Contains all the functions related to one index.
    You should use yourClient.init_index(index_name) to retrieve this object.
    '''

    def __init__(self, client, index_name):
        self.read_hosts = client.read_hosts
        self.write_hosts = client.write_hosts
        self.client = client
        self.index_name = index_name
        self.url_index_name = quote(self.index_name.encode('utf8'), safe='')

    @deprecated
    def addObject(self, content, object_id=None):
        return self.add_object(content, object_id)

    def add_object(self, content, object_id=None):
        '''
        Add an object in this index.

        @param content contains the object to add inside the index.
            The object is represented by an associative array
        @param object_id (optional) an object_id you want to attribute to this object
            (if the attribute already exist the old object will be overwrite)
        '''
        if object_id is None:
            return AlgoliaUtils_request(
                self.client.headers, self.write_hosts, 'POST', '/1/indexes/%s'
                % self.url_index_name, self.client.timeout, content)
        else:
            return AlgoliaUtils_request(
                self.client.headers, self.write_hosts, 'PUT',
                '/1/indexes/%s/%s' % (self.url_index_name, quote(
                    ('%s' % object_id).encode('utf8'),
                    safe='')), self.client.timeout, content)

    @deprecated
    def addObjects(self, objects):
        return self.add_objects(objects)

    def add_objects(self, objects):
        '''
        Add several objects.

        @param objects contains an array of objects to add
        '''
        requests = []
        for obj in objects:
            requests.append({'action': 'addObject', 'body': obj})
        request = {'requests': requests}
        return self.batch(request)

    @deprecated
    def getObject(self, object_id, attributes_to_retrieve=None):
        return self.get_object(object_id, attributes_to_retrieve)

    def get_object(self, object_id, attributes_to_retrieve=None):
        '''
        Get an object from this index.

        @param object_id the unique identifier of the object to retrieve
        @param attributes_to_retrieve (optional) if set, contains the list
            of attributes to retrieve as a string separated by a comma
        '''
        obj_id = quote(('%s' % object_id).encode('utf8'), safe='')
        if not attributes_to_retrieve:
            return AlgoliaUtils_request(
                self.client.headers, self.read_hosts, 'GET', '/1/indexes/%s/%s'
                % (self.url_index_name, obj_id), self.client.timeout)
        else:
            return AlgoliaUtils_request(
                self.client.headers, self.read_hosts, 'GET',
                '/1/indexes/%s/%s?attributes=%s' % (
                    self.url_index_name, obj_id, attributes_to_retrieve
                ), self.client.timeout)

    @deprecated
    def getObjects(self, object_ids):
        return self.get_objects(object_ids)

    def get_objects(self, object_ids):
        '''
        Get several objects from this index.

        @param object_ids the array of unique identifier of objects to retrieve
        '''
        requests = []
        for object_id in object_ids:
            req = {'indexName': self.index_name, 'objectID': object_id}
            requests.append(req)
        return AlgoliaUtils_request(self.client.headers, self.read_hosts,
                                    'POST', '/1/indexes/*/objects',
                                    self.client.timeout,
                                    {'requests': requests})

    @deprecated
    def partialUpdateObject(self, partial_object):
        return self.partial_update_object(partial_object)

    def partial_update_object(self, partial_object):
        '''
        Update partially an object (only update attributes passed in argument).

        @param partial_object contains the object attributes to override, the
            object must contains an objectID attribute
        '''
        return AlgoliaUtils_request(
            self.client.headers, self.write_hosts, 'POST',
            '/1/indexes/%s/%s/partial' % (self.url_index_name, quote(
                ('%s' % partial_object['objectID']).encode('utf8'),
                safe='')), self.client.timeout, partial_object)

    @deprecated
    def partialUpdateObjects(self, objects):
        return self.partial_update_objects(objects)

    def partial_update_objects(self, objects):
        '''
        Partially Override the content of several objects.

        @param objects contains an array of objects to update (each object
            must contains a objectID attribute)
        '''
        requests = []
        for obj in objects:
            requests.append({
                'action': 'partialUpdateObject',
                'objectID': obj['objectID'],
                'body': obj
            })
        request = {'requests': requests}
        return self.batch(request)

    @deprecated
    def saveObject(self, obj):
        return self.save_object(obj)

    def save_object(self, obj):
        '''
        Override the content of object.

        @param object contains the object to save, the object must contains
            an objectID attribute
        '''
        return AlgoliaUtils_request(
            self.client.headers, self.write_hosts, 'PUT',
            '/1/indexes/%s/%s' % (self.url_index_name, quote(
                ('%s' % obj['objectID']).encode('utf8'),
                safe='')), self.client.timeout, obj)

    @deprecated
    def saveObjects(self, objects):
        return self.save_objects(objects)

    def save_objects(self, objects):
        '''
        Override the content of several objects.

        @param objects contains an array of objects to update (each object
            must contains a objectID attribute)
        '''
        requests = []
        for obj in objects:
            requests.append({
                'action': 'updateObject',
                'objectID': obj['objectID'],
                'body': obj
            })
        request = {'requests': requests}
        return self.batch(request)

    @deprecated
    def deleteByQuery(self, query, params={}):
        return self.delete_by_query(query, params)

    def delete_by_query(self, query, params={}):
        '''
        Delete all objects matching a query.

        @param query the query string
        @param params the optional query parameters
        '''
        params['hitsPerPage'] = 1000
        params['attributesToRetrieve'] = ['objectID']

        res = self.search(query, params)
        while (res['nbHits'] != 0):
            object_ids = []
            for elt in res['hits']:
                object_ids.append(elt['objectID'])
            task = self.delete_objects(object_ids)
            self.wait_task(task['taskID'])
            res = self.search(query, params)

    @deprecated
    def deleteObjects(self, objects):
        return self.delete_objects(objects)

    def delete_objects(self, objects):
        '''
        delete several objects.

        @param objects contains an array of object_id to delete
        '''
        requests = []
        for obj in objects:
            requests.append(
                {'action': 'deleteObject',
                 'body': {'objectID': obj}})
        request = {'requests': requests}
        return self.batch(request)

    @deprecated
    def deleteObject(self, object_id):
        return self.delete_object(object_id)

    def delete_object(self, object_id):
        '''
        Delete an object from the index.

        @param object_id the unique identifier of object to delete
        '''
        if (len('%s' % object_id) == 0):
            raise AlgoliaException('object_id is required')
        return AlgoliaUtils_request(self.client.headers, self.write_hosts,
                                    'DELETE', '/1/indexes/%s/%s' % (
                                        self.url_index_name, quote(
                                            ('%s' % object_id).encode('utf8'),
                                            safe='')
                                    ), self.client.timeout)

    def search(self, query, args=None):
        '''
        Search inside the index.

        @param query the full text query
        @param args (optional) if set, contains an associative array with
            query parameters:
                - page: (integer) Pagination parameter used to select the
                page to retrieve. Page is zero-based and defaults to 0. Thus,
                to retrieve the 10th page you need to set page=9
                - hitsPerPage: (integer) Pagination parameter used to select
                the number of hits per page. Defaults to 20.
                - attributesToRetrieve: a string that contains the list of
                object attributes you want to retrieve (let you minimize the
                answer size). Attributes are separated with a comma (for
                example 'name,address'). You can also use a string array
                encoding (for example ['name','address']). By default, all
                attributes are retrieved. You can also use '*' to retrieve all
                values when an attributesToRetrieve setting is specified for
                your index.
                - attributesToHighlight: a string that contains the list of
                attributes you want to highlight according to the query.
                Attributes are separated by a comma. You can also use a string
                array encoding (for example ['name','address']). If an
                attribute has no match for the query, the raw value is returned.
                By default all indexed text attributes are highlighted. You
                can use `*` if you want to highlight all textual attributes.
                Numerical attributes are not highlighted. A matchLevel is
                returned for each highlighted attribute and can contain:
                    - full: if all the query terms were found in the attribute,
                    - partial: if only some of the query terms were found,
                    - none: if none of the query terms were found.
                - attributesToSnippet: a string that contains the list of
                attributes to snippet alongside the number of words to return
                (syntax is `attributeName:nbWords`). Attributes are separated
                by a comma (Example: attributesToSnippet=name:10,content:10).
                You can also use a string array encoding
                (Example: attributesToSnippet: ['name:10','content:10']).
                By default no snippet is computed.
                - minWordSizefor1Typo: the minimum number of characters in a
                query word to accept one typo in this word. Defaults to 3.
                - minWordSizefor2Typos: the minimum number of characters in a
                query word to accept two typos in this word. Defaults to 7.
                - getRankingInfo: if set to 1, the result hits will contain
                ranking information in _rankingInfo attribute.
                - aroundLatLng: search for entries around a given
                latitude/longitude (specified as two floats separated by a comma).
                For example aroundLatLng=47.316669,5.016670). You can specify
                the maximum distance in meters with the aroundRadius parameter
                (in meters) and the precision for ranking with aroundPrecision
                (for example if you set aroundPrecision=100, two objects that
                are distant of less than 100m will be considered as identical
                for 'geo' ranking parameter). At indexing, you should specify
                geoloc of an object with the _geoloc attribute (in the form
                {'_geoloc':{'lat':48.853409, 'lng':2.348800}})
                - insideBoundingBox: search entries inside a given area defined
                by the two extreme points of a rectangle (defined by 4 floats:
                p1Lat,p1Lng,p2Lat,p2Lng). For example
                insideBoundingBox=47.3165,4.9665,47.3424,5.0201). At indexing,
                you should specify geoloc of an object with the _geoloc
                attribute (in the form {'_geoloc':{'lat':48.853409, 'lng':2.348800}})
                - numericFilters: a string that contains the list of numeric
                filters you want to apply separated by a comma. The syntax of
                one filter is `attributeName` followed by `operand` followed by
                `value`. Supported operands are `<`, `<=`, `=`, `>` and `>=`.
                You can have multiple conditions on one attribute like for
                example numericFilters=price>100,price<1000. You can also use
                a string array encoding (for example numericFilters:
                ['price>100','price<1000']).
                - tagFilters: filter the query by a set of tags. You can AND
                tags by separating them by commas. To OR tags, you must add
                parentheses. For example, tags=tag1,(tag2,tag3) means
                tag1 AND (tag2 OR tag3). You can also use a string array encoding,
                for example tagFilters: ['tag1',['tag2','tag3']] means
                tag1 AND (tag2 OR tag3). At indexing, tags should be added in
                the _tags** attribute of objects (for example
                {'_tags':['tag1','tag2']}).
                - facetFilters: filter the query by a list of facets. Facets
                are separated by commas and each facet is encoded as
                `attributeName:value`. For example:
                `facetFilters=category:Book,author:John%20Doe`. You can also
                use a string array encoding (for example
                `['category:Book','author:John%20Doe']`).
                - facets: List of object attributes that you want to use for faceting.
                Attributes are separated with a comma (for example `'category,author'` ).
                You can also use a JSON string array encoding (for example
                ['category','author']). Only attributes that have been added
                in **attributesForFaceting** index setting can be used in
                this parameter. You can also use `*` to perform faceting on
                all attributes specified in **attributesForFaceting**.
                - queryType: select how the query words are interpreted, it
                can be one of the following value:
                    - prefixAll: all query words are interpreted as prefixes,
                    - prefixLast: only the last word is interpreted as a prefix
                    (default behavior),
                    - prefixNone: no query word is interpreted as a prefix.
                    This option is not recommended.
                - optionalWords: a string that contains the list of words that
                should be considered as optional when found in the query.
                The list of words is comma separated.
                - distinct: If set to 1, enable the distinct feature (disabled
                by default) if the attributeForDistinct index setting is set.
                This feature is similar to the SQL 'distinct' keyword: when
                enabled in a query with the distinct=1 parameter, all hits
                containing a duplicate value for the attributeForDistinct
                attribute are removed from results. For example, if the chosen
                attribute is show_name and several hits have the same value
                for show_name, then only the best one is kept and others are
                removed.
        '''
        if not args:
            return AlgoliaUtils_request(self.client.headers, self.read_hosts,
                                        'GET', '/1/indexes/%s?query=%s' % (
                                            self.url_index_name,
                                            quote(query.encode('utf8'),
                                                  safe='')
                                        ), self.client.search_timeout)
        else:
            params = {}
            try:
                iteritems = args.iteritems()
                #  Python3.X Fix
            except AttributeError:
                iteritems = args.items()
            for k, v in iteritems:
                if isinstance(v, (list, dict, tuple, bool)):
                    params[k] = json.dumps(v)
                else:
                    params[k] = v

            return AlgoliaUtils_request(self.client.headers, self.read_hosts,
                                        'GET', '/1/indexes/%s?query=%s&%s' % (
                                            self.url_index_name,
                                            quote(query.encode('utf8'),
                                                  safe=''), urlencode(params)
                                        ), self.client.search_timeout)

    @deprecated
    def searchDisjunctiveFaceting(self, query, disjunctive_facets,
                                  params={},
                                  refinements={}):
        return self.search_disjunctive_faceting(query, disjunctive_facets,
                                                params, refinements)

    def search_disjunctive_faceting(self, query, disjunctive_facets,
                                    params={},
                                    refinements={}):
        '''
        Perform a search with disjunctive facets generating as many queries as
        number of disjunctive facets.

        @param query the query
        @param disjunctive_facets the array of disjunctive facets
        @param params a hash representing the regular query parameters
        @param refinements a hash ('string' -> ['array', 'of', 'refined', 'values'])
            representing the current refinements. Ex:
            { 'my_facet1' => ['my_value1', ['my_value2'], 'my_disjunctive_facet1' => ['my_value1', 'my_value2'] }
        '''
        if not (isinstance(disjunctive_facets, str)) and not (
                isinstance(disjunctive_facets, list)):
            raise AlgoliaException(
                'Argument \'disjunctive_facets\' must be a String or an Array')
        if not (isinstance(refinements, dict)):
            raise AlgoliaException(
                'Argument \'refinements\' must be a Hash of Arrays')

        if isinstance(disjunctive_facets, str):
            disjunctive_facets = disjunctive_facets.split(',')

        disjunctive_refinements = {}
        for key in refinements.keys():
            if (key in disjunctive_facets):
                disjunctive_refinements[key] = refinements[key]

        queries = []
        filters = []

        for key in refinements:
            r = list(map(lambda x: key + ':' + x, refinements[key]))

            if (str(key) in disjunctive_refinements):
                filters.append(r)
            else:
                filters += r
        params['indexName'] = self.index_name
        params['query'] = query
        params['facetFilters'] = filters
        queries.append(dict(params))
        for disjunctive_facet in disjunctive_facets:
            filters = []

            for key in refinements:
                if key != disjunctive_facet:
                    r = list(map(lambda x: key + ':' + x, refinements[key]))

                    if (str(key) in disjunctive_refinements):
                        filters.append(r)
                    else:
                        filters += r

            params['indexName'] = self.index_name
            params['query'] = query
            params['facetFilters'] = filters
            params['page'] = 0
            params['hitsPerPage'] = 0
            params['attributesToRetrieve'] = []
            params['attributesToHighlight'] = []
            params['attributesToSnippet'] = []
            params['facets'] = disjunctive_facet
            params['analytics'] = False
            queries.append(dict(params))
        answers = self.client.multiple_queries(queries)

        aggregated_answer = answers['results'][0]
        aggregated_answer['disjunctiveFacets'] = {}
        for i in range(1, len(answers['results'])):
            for facet in answers['results'][i]['facets']:
                aggregated_answer['disjunctiveFacets'][
                    facet
                ] = answers['results'][i]['facets'][facet]
                if facet not in disjunctive_refinements:
                    continue
                for r in disjunctive_refinements[facet]:
                    if not aggregated_answer['disjunctiveFacets'][facet].get(
                            r, None):
                        aggregated_answer['disjunctiveFacets'][facet][r] = 0
        return aggregated_answer

    @deprecated
    def browse(self, page=0, hits_per_page=1000):
        '''
         Browse all index content.

         @param page Pagination parameter used to select the page to retrieve.
            Page is zero-based and defaults to 0. Thus, to retrieve the 10th
            page you need to set page=9
         @param hits_per_page: Pagination parameter used to select the number
            of hits per page. Defaults to 1000.
        '''
        return AlgoliaUtils_request(
            self.client.headers, self.read_hosts, 'GET',
            '/1/indexes/%s/browse?page=%d&hitsPerPage=%d' %
            (self.url_index_name, page, hits_per_page), self.client.timeout)

    def browse_from(self, params={}, cursor=None):
        '''
         Browse all index content.

         @param params contains the list of query parameter in a dictionary
         @param cursor the position to start the browse
        '''
        try:
            iteritems = params.iteritems()
        except AttributeError:
            iteritems = params.items()
        # Impossible to use dict comprehensions because of py26...
        params = dict((k, json.dumps(v)) for k, v in iteritems)

        if cursor and len(cursor) > 0:
            url_params = 'cursor=%s' % cursor
        else:
            url_params = urlencode(params)

        return AlgoliaUtils_request(self.client.headers, self.read_hosts,
                                    'GET', '/1/indexes/%s/browse?%s' %
                                    (self.url_index_name, url_params),
                                    self.client.timeout)

    def browse_all(self, params={}):
        '''
         Browse all index content.

         @param params contains the list of query parameter in a dictionary
         @return an iterator on the index content
        '''
        return IndexIterator(self, params=params)

    @deprecated
    def waitTask(self, task_id, time_before_retry=100):
        return self.wait_task(task_id, time_before_retry)

    def wait_task(self, task_id, time_before_retry=100):
        '''
        Wait the publication of a task on the server.
        All server task are asynchronous and you can check with this method
        that the task is published.

        @param task_id the id of the task returned by server
        @param time_before_retry the time in milliseconds before retry (default = 100ms)
        '''
        while True:
            res = AlgoliaUtils_request(self.client.headers, self.read_hosts,
                                       'GET', '/1/indexes/%s/task/%d/' % (
                                           self.url_index_name, task_id
                                       ), self.client.timeout)
            if (res['status'] == 'published'):
                return res
            time.sleep(time_before_retry / 1000.)

    @deprecated
    def getSettings(self):
        return self.get_settings()

    def get_settings(self):
        '''Get settings of this index.'''
        return AlgoliaUtils_request(self.client.headers, self.read_hosts,
                                    'GET', '/1/indexes/%s/settings' %
                                    self.url_index_name, self.client.timeout)

    @deprecated
    def clearIndex(self):
        return self.clear_index()

    def clear_index(self):
        '''
        This function deletes the index content. Settings and index specific
        API keys are kept untouched.
        '''
        return AlgoliaUtils_request(self.client.headers, self.write_hosts,
                                    'POST', '/1/indexes/%s/clear' %
                                    self.url_index_name, self.client.timeout)

    @deprecated
    def setSettings(self, settings):
        return self.set_settings(settings)

    def set_settings(self, settings):
        '''
        Set settings for this index.

        @param settigns the settings object that can contains :
            - minWordSizefor1Typo: (integer) the minimum number of characters
            to accept one typo (default = 3).
            - minWordSizefor2Typos: (integer) the minimum number of characters
            to accept two typos (default = 7).
            - hitsPerPage: (integer) the number of hits per page (default = 10).
            - attributesToRetrieve: (array of strings) default list of attributes
            to retrieve in objects. If set to null, all attributes are retrieved.
            - attributesToHighlight: (array of strings) default list of attributes
            to highlight. If set to null, all indexed attributes are highlighted.
            - attributesToSnippet**: (array of strings) default list of attributes
            to snippet alongside the number of words to return (syntax is
            attributeName:nbWords). By default no snippet is computed. If set to
            null, no snippet is computed.
            - attributesToIndex: (array of strings) the list of fields you want
            to index. If set to null, all textual and numerical attributes of
            your objects are indexed, but you should update it to get optimal
            results. This parameter has two important uses:
                - Limit the attributes to index: For example if you store a
                binary image in base64, you want to store it and be able to
                retrieve it but you don't want to search in the base64 string.
                - Control part of the ranking*: (see the ranking parameter for
                full explanation) Matches in attributes at the beginning of the
                list will be considered more important than matches in
                attributes further down the list. In one attribute, matching
                text at the beginning of the attribute will be considered more
                important than text after, you can disable this behavior if you
                add your attribute inside `unordered(AttributeName)`, for
                example attributesToIndex: ['title', 'unordered(text)'].
            - attributesForFaceting: (array of strings) The list of fields you
            want to use for faceting. All strings in the attribute selected for
            faceting are extracted and added as a facet. If set to null, no
            attribute is used for faceting.
            - attributeForDistinct: (string) The attribute name used for the
            Distinct feature. This feature is similar to the SQL 'distinct'
            keyword: when enabled in query with the distinct=1 parameter, all
            hits containing a duplicate value for this attribute are removed
            from results. For example, if the chosen attribute is show_name
            and several hits have the same value for show_name, then only the
            best one is kept and others are removed.
            - ranking: (array of strings) controls the way results are sorted.
            We have six available criteria:
                - typo: sort according to number of typos,
                - geo: sort according to decreassing distance when performing
                a geo-location based search,
                - proximity: sort according to the proximity of query words in hits,
                - attribute: sort according to the order of attributes defined
                by attributesToIndex,
                - exact:
                    - if the user query contains one word: sort objects having
                    an attribute that is exactly the query word before others.
                    For example if you search for the 'V' TV show, you want
                    to find it with the 'V' query and avoid to have all popular TV
                    show starting by the v letter before it.
                    - if the user query contains multiple words: sort according
                    to the number of words that matched exactly (and not as
                    a prefix).
                - custom: sort according to a user defined formula set in
                **customRanking** attribute. The standard order is
                ['typo', 'geo', 'proximity', 'attribute', 'exact', 'custom']
            - customRanking: (array of strings) lets you specify part of the ranking.
            The syntax of this condition is an array of strings containing
            attributes prefixed by asc (ascending order) or desc (descending
            order) operator. For example `'customRanking' =>
            ['desc(population)', 'asc(name)']`.
            - queryType: Select how the query words are interpreted, it can be
            one of the following value:
                - prefixAll: all query words are interpreted as prefixes,
                - prefixLast: only the last word is interpreted as a prefix
                (default behavior),
                - prefixNone: no query word is interpreted as a prefix.
                This option is not recommended.
            - highlightPreTag: (string) Specify the string that is inserted
            before the highlighted parts in the query result (default to '<em>').
            - highlightPostTag: (string) Specify the string that is inserted
            after the highlighted parts in the query result (default to '</em>').
            - optionalWords: (array of strings) Specify a list of words that
            should be considered as optional when found in the query.
        '''
        return AlgoliaUtils_request(self.client.headers, self.write_hosts,
                                    'PUT', '/1/indexes/%s/settings' %
                                    self.url_index_name, self.client.timeout,
                                    settings)

    @deprecated
    def listUserKeys(self):
        return self.list_user_keys()

    def list_user_keys(self):
        '''
        List all existing user keys of this index with their associated ACLs.
        '''
        return AlgoliaUtils_request(self.client.headers, self.read_hosts,
                                    'GET', '/1/indexes/%s/keys' %
                                    self.url_index_name, self.client.timeout)

    @deprecated
    def getUserKeyACL(self, key):
        return self.get_user_key_acl(key)

    def get_user_key_acl(self, key):
        '''Get ACL of a user key associated to this index.'''
        return AlgoliaUtils_request(self.client.headers, self.read_hosts,
                                    'GET', '/1/indexes/%s/keys/%s' % (
                                        self.url_index_name, key
                                    ), self.client.timeout)

    @deprecated
    def deleteUserKey(self, key):
        return self.delete_user_key(key)

    def delete_user_key(self, key):
        '''Delete an existing user key associated to this index.'''
        return AlgoliaUtils_request(self.client.headers, self.write_hosts,
                                    'DELETE', '/1/indexes/%s/keys/%s' % (
                                        self.url_index_name, key
                                    ), self.client.timeout)

    @deprecated
    def addUserKey(self, obj,
                   validity=0,
                   max_queries_per_ip_per_hour=0,
                   max_hits_per_query=0):
        return self.add_user_key(obj, validity, max_queries_per_ip_per_hour,
                                 max_hits_per_query)

    def add_user_key(self, obj,
                     validity=0,
                     max_queries_per_ip_per_hour=0,
                     max_hits_per_query=0):
        '''
        Create a new user key associated to this index (can only access to
        this index).

        @param obj can be two different parameters:
            The list of parameters for this key. Defined by a dictionary that
            can contains the following values:
                - acl: array of string
                - indices: array of string
                - validity: int
                - referers: array of string
                - description: string
                - maxHitsPerQuery: integer
                - queryParameters: string
                - maxQueriesPerIPPerHour: integer
            Or the list of ACL for this key. Defined by an array of string that
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
            calls allowed from an IP address per hour.  Defaults to 0 (no
            rate limit)
        @param max_hits_per_query Specify the maximum number of hits this
            API key can retrieve in one call. Defaults to 0 (unlimited)
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
        return AlgoliaUtils_request(
            self.client.headers, self.write_hosts, 'POST', '/1/indexes/%s/keys'
            % self.url_index_name, self.client.timeout, params)

    def update_user_key(self, key, obj,
                        validity=0,
                        max_queries_per_ip_per_hour=0,
                        max_hits_per_query=0):
        '''
        Update a user key associated to this index (can only access to this index).

        @param obj can be two different parameters:
            The list of parameters for this key. Defined by a dictionary that
            can contains the following values:
                - acl: array of string
                - indices: array of string
                - validity: int
                - referers: array of string
                - description: string
                - maxHitsPerQuery: integer
                - queryParameters: string
                - maxQueriesPerIPPerHour: integer
            Or the list of ACL for this key. Defined by an array of string that
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
            calls allowed from an IP address per hour.  Defaults to 0 (no rate
            limit).
        @param max_hits_per_query Specify the maximum number of hits this API
            key can retrieve in one call. Defaults to 0 (unlimited)
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
        return AlgoliaUtils_request(self.client.headers, self.write_hosts,
                                    'PUT', '/1/indexes/%s/keys/%s' % (
                                        self.url_index_name, key
                                    ), self.client.timeout, params)

    def batch(self, request):
        '''Send a batch request.'''
        return AlgoliaUtils_request(self.client.headers, self.write_hosts,
                                    'POST', '/1/indexes/%s/batch' %
                                    self.url_index_name, self.client.timeout,
                                    request)

