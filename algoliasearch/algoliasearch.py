"""
Copyright (c) 2013 Algolia
http://www.algolia.com/
Thanks to Arthur Lenoir <arthur (at) lenoir.me> for the initial version.

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
import json
import random
import urllib
import urllib3
import time

POOL_MANAGER = urllib3.PoolManager()

# Exception launched by Algolia Client when an error occured
class AlgoliaException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

""" 
Entry point in the Python API.
You should instanciate a Client object with your ApplicationID, ApiKey and Hosts 
to start using Algolia Search API
"""
class Client:
    """
    Algolia Search library initialization
    @param applicationID the application ID you have in your admin interface
    @param apiKey a valid API key for the service
    @param hostsArray the list of hosts that you have received for the service
    """
    def __init__(self, applicationID, apiKey, hostsArray = None):
        if (hostsArray == None):
          self.hosts = ["%s-1.algolia.io" % applicationID, "%s-2.algolia.io" % applicationID, "%s-3.algolia.io" % applicationID]
        else:
          self.hosts = hostsArray
        random.shuffle(self.hosts)
        self.applicationID = applicationID
        self.apiKey = apiKey
        self.headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'X-Algolia-API-Key': self.apiKey,
            'X-Algolia-Application-Id': self.applicationID
        }

    """
    List all existing indexes
    return an object of the form 
       {"items": [{ "name": "contacts", "createdAt": "2013-01-18T15:33:13.556Z"},
                  {"name": "notes", "createdAt": "2013-01-18T15:33:13.556Z"}]}
    """
    def listIndexes(self):
        return AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/indexes/")

    """
    Delete an index

    @param indexName the name of index to delete
    Return an object of the form {"deletedAt": "2013-01-18T15:33:13.556Z"}
    """
    def deleteIndex(self, indexName):
        return AlgoliaUtils_request(self.headers, self.hosts, "DELETE", "/1/indexes/%s" % urllib.quote(indexName.encode('utf8')))

    """
    Get the index object initialized (no server call needed for initialization)

    @param indexName the name of index
    """
    def initIndex(self, indexName):
        return Index(self.headers, self.hosts, indexName)

    """
    List all existing user keys with their associated ACLs
    """
    def listUserKeys(self):
        return AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/keys")

    # Get ACL of a user key
    def getUserKeyACL(self, key):
        return AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/keys/%s" % key)

    # Delete an existing user key
    def deleteUserKey(self, key):
        return AlgoliaUtils_request(self.headers, self.hosts, "DELETE", "/1/keys/%s" % key)

    """
    Create a new user key

    @param acls the list of ACL for this key. Defined by an array of strings that 
           can contains the following values:
             - search: allow to search (https and http)
             - addObject: allows to add/update an object in the index (https only)
             - deleteObject : allows to delete an existing object (https only)
             - deleteIndex : allows to delete index content (https only)
             - settings : allows to get index settings (https only)
             - editSettings : allows to change index settings (https only)
    @param validity the number of seconds after which the key will be automatically removed (0 means no time limit for this key)
    """
    def addUserKey(self, acls, validity = 0):
        return AlgoliaUtils_request(self.headers, self.hosts, "POST", "/1/keys", {"acl": acls, "validity": validity} )          

"""
Contains all the functions related to one index
You should use Client.initIndex(indexName) to retrieve this object
"""
class Index:
    def __init__(self, headers, hosts, indexName):
        self.hosts = hosts
        self.headers = headers
        self.indexName = indexName
        self.urlIndexName = urllib.quote(self.indexName.encode('utf8'))

    """
    Add an object in this index
     
    @param content contains the object to add inside the index. 
      The object is represented by an associative array
    @param objectID (optional) an objectID you want to attribute to this object 
      (if the attribute already exist the old object will be overwrite)
    """
    def addObject(self, content, objectID = None):
        if objectID is None:
            return AlgoliaUtils_request(self.headers, self.hosts, "POST", "/1/indexes/%s" % self.urlIndexName, content)
        else:
            return AlgoliaUtils_request(self.headers, self.hosts, "PUT", "/1/indexes/%s/%s" % (self.urlIndexName, urllib.quote(objectID.encode('utf8'))), content)

    """
    Add several objects

    @param objects contains an array of objects to add
    """
    def addObjects(self, objects):
        requests = []
        for obj in objects:
            requests.append({"action": "addObject", "body": obj})
        request = {"requests": requests}
        return AlgoliaUtils_request(self.headers, self.hosts, "POST", "/1/indexes/%s/batch" % self.urlIndexName, request)

    """
    Get an object from this index

    @param objectID the unique identifier of the object to retrieve
    @param attributesToRetrieve (optional) if set, contains the list of attributes to retrieve as a string separated by a comma
    """
    def getObject(self, objectID, attributesToRetrieve = None):
        objID = urllib.quote(objectID.encode('utf8'))
        if (attributesToRetrieve == None):
            return AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/indexes/%s/%s" % (self.urlIndexName, objID))
        else:
            return AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/indexes/%s/%s?attributes=%s" % (self.urlIndexName, objID, attributesToRetrieve))

    """
    Update partially an object (only update attributes passed in argument)
    
    @param partialObject contains the object attributes to override, the 
           object must contains an objectID attribute
    """
    def partialUpdateObject(self, partialObject):
        return AlgoliaUtils_request(self.headers, self.hosts, "POST", "/1/indexes/%s/%s/partial" % (self.urlIndexName, urllib.quote(partialObject["objectID"].encode('utf8'))), partialObject)

    """
    Override the content of object
    
    @param object contains the object to save, the object must contains an objectID attribute
    """
    def saveObject(self, obj):
        return AlgoliaUtils_request(self.headers, self.hosts, "PUT", "/1/indexes/%s/%s" % (self.urlIndexName, urllib.quote(obj["objectID"].encode('utf8'))), obj)

    """
    Override the content of several objects

    @param objects contains an array of objects to update (each object must contains a objectID attribute)
    """
    def saveObjects(self, objects):
        requests = []
        for obj in objects:
            requests.append({"action": "updateObject", "objectID": obj["objectID"], "body": obj})
        request = {"requests": requests}
        return AlgoliaUtils_request(self.headers, self.hosts, "POST", "/1/indexes/%s/batch" % self.urlIndexName, request)

    """
    Delete an object from the index 

    @param objectID the unique identifier of object to delete
    """
    def deleteObject(self, objectID):
        return AlgoliaUtils_request(self.headers, self.hosts, "DELETE", "/1/indexes/%s/%s" % (self.urlIndexName, urllib.quote(objectID.encode('utf8'))))

    """
    Search inside the index
    
    @param query the full text query
    @param args (optional) if set, contains an associative array with query parameters:
      - attributes: a string that contains attribute names to retrieve separated by a comma. 
        By default all attributes are retrieved.
      - attributesToHighlight: a string that contains attribute names to highlight separated by a comma. 
        By default indexed attributes are highlighted.
      - attributesToSnippet: a string that contains the names of attributes to snippet alongside the 
        number of words to return (syntax is 'attributeName:nbWords'). 
        Attributes are separated by a comma (Example: "attributesToSnippet=name:10,content:10").
        By default no snippet is computed.
      - minWordSizeForApprox1: the minimum number of characters in a query word to accept one typo in this word. 
        Defaults to 3.
      - minWordSizeForApprox2: the minimum number of characters in a query word to accept two typos in this word.
         Defaults to 7.
      - getRankingInfo: if set to 1, the result hits will contain ranking information in 
         _rankingInfo attribute
      - page: (pagination parameter) page to retrieve (zero base). Defaults to 0.
      - hitsPerPage: (pagination parameter) number of hits per page. Defaults to 10.
      - aroundLatLng let you search for entries around a given latitude/longitude (two float separated 
        by a ',' for example aroundLatLng=47.316669,5.016670). 
        You can specify the maximum distance in meters with aroundRadius parameter (in meters).
        At indexing, geoloc of an object should be set with _geoloc attribute containing lat and lng attributes (for example {"_geoloc":{"lat":48.853409, "lng":2.348800}})
      - insideBoundingBox let you search entries inside a given area defined by the two extreme points of 
        a rectangle (defined by 4 floats: p1Lat,p1Lng,p2Lat, p2Lng.
        For example insideBoundingBox=47.3165,4.9665,47.3424,5.0201).
        At indexing, geoloc of an object should be set with _geoloc attribute containing lat and lng attributes (for example {"_geoloc":{"lat":48.853409, "lng":2.348800}})
      - queryType: select how the query words are interpreted:
         - prefixAll: all query words are interpreted as prefixes (default behavior).
         - prefixLast: only the last word is interpreted as a prefix. This option is recommended if you have a lot of content to speedup the processing.
         - prefixNone: no query word is interpreted as a prefix. This option is not recommended.
      - tags filter the query by a set of tags. You can AND tags by separating them by commas. To OR tags, you must add parentheses. For example, tags=tag1,(tag2,tag3) means tag1 AND (tag2 OR tag3).
        At indexing, tags should be added in the _tags attribute of objects (for example {"_tags":["tag1","tag2"]} )

    """
    def search(self, query, args = None):
        if args == None:
            return AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/indexes/%s?query=%s" % (self.urlIndexName, urllib.quote(query.encode('utf8'))))
        else:
            return AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/indexes/%s?query=%s&%s" % (self.urlIndexName, urllib.quote(query.encode('utf8')), urllib.urlencode(args)))

    """
    Wait the publication of a task on the server. 
    All server task are asynchronous and you can check with this method that the task is published.

    @param taskID the id of the task returned by server
    @param timeBeforeRetry the time in milliseconds before retry (default = 100ms)
    """
    def waitTask(self, taskID, timeBeforeRetry = 100):
        while True:
            res = AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/indexes/%s/task/%d/" % (self.urlIndexName, taskID))
            if (res["status"] == "published"):
                return res
            time.sleep(timeBeforeRetry / 1000)

    # Get settings of this index
    def getSettings(self):
        return AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/indexes/%s/settings" % self.urlIndexName)

    """
      Set settings for this index
      
      @param settigns the settings object that can contains :
       - minWordSizeForApprox1 (integer) the minimum number of characters to accept one typo (default = 3)
       - minWordSizeForApprox2: (integer) the minimum number of characters to accept two typos (default = 7)
       - hitsPerPage: (integer) the number of hits per page (default = 10)
       - attributesToRetrieve: (array of strings) default list of attributes to retrieve for objects
       - attributesToHighlight: (array of strings) default list of attributes to highlight
       - attributesToSnippet: (array of strings) default list of attributes to snippet alongside the number of 
         words to return (syntax is 'attributeName:nbWords').
         By default no snippet is computed.
       - attributesToIndex: (array of strings) the list of fields you want to index. 
         By default all textual attributes of your objects are indexed, but you should update it to get optimal 
         results. This parameter has two important uses:
            - Limit the attributes to index. 
              For example if you store a binary image in base64, you want to store it in the index but you 
              don't want to use the base64 string for search.
            - Control part of the ranking (see the ranking parameter for full explanation). 
              Matches in attributes at the beginning of the list will be considered more important than matches 
              in attributes further down the list.
       - ranking: (array of strings) controls the way results are sorted. 
          We have four available criteria: 
            - typo (sort according to number of typos), 
            - geo: (sort according to decreassing distance when performing a geo-location based search),
            - proximity: sort according to the proximity of query words in hits, 
            - attribute: sort according to the order of attributes defined by **attributesToIndex**,
            - exact: sort according to the number of words that are matched identical to query word (and not as a prefix),
            - custom which is user defined
          (the standard order is ["typo", "geo", "proximity", "attribute", "exact", "custom"])
       - queryType: select how the query words are interpreted:
            - prefixAll: all query words are interpreted as prefixes (default behavior).
            - prefixLast: only the last word is interpreted as a prefix. This option is recommended if you have a lot of content to speedup the processing.
            - prefixNone: no query word is interpreted as a prefix. This option is not recommended.
       - customRanking: (array of strings) lets you specify part of the ranking. 
         The syntax of this condition is an array of strings containing attributes prefixed 
         by asc (ascending order) or desc (descending order) operator.
     """
    def setSettings(self, settings):
        return AlgoliaUtils_request(self.headers, self.hosts, "PUT", "/1/indexes/%s/settings" % self.urlIndexName, settings)

    """
    List all existing user keys of this index with their associated ACLs
    """
    def listUserKeys(self):
        return AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/indexes/%s/keys" % self.urlIndexName)

    # Get ACL of a user key associated to this index
    def getUserKeyACL(self, key):
        return AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/indexes/%s/keys/%s" % (self.urlIndexName, key))

    # Delete an existing user key associated to this index
    def deleteUserKey(self, key):
        return AlgoliaUtils_request(self.headers, self.hosts, "DELETE", "/1/indexes/%s/keys/%s" % (self.urlIndexName, key))

    """
    Create a new user key associated to this index (can only access to this index)

    @param acls the list of ACL for this key. Defined by an array of strings that 
           can contains the following values:
             - search: allow to search (https and http)
             - addObject: allows to add/update an object in the index (https only)
             - deleteObject : allows to delete an existing object (https only)
             - deleteIndex : allows to delete index content (https only)
             - settings : allows to get index settings (https only)
             - editSettings : allows to change index settings (https only)
    @param validity the number of seconds after which the key will be automatically removed (0 means no time limit for this key)
    """
    def addUserKey(self, acls, validity = 0):
        return AlgoliaUtils_request(self.headers, self.hosts, "POST", "/1/indexes/%s/keys" % self.urlIndexName, {"acl": acls, "validity": validity} )   

# Util function used to send request
def AlgoliaUtils_request(headers, hosts, method, request, body = None):
    for host in hosts:
        try:
            obj = None
            if body != None:
                obj = json.dumps(body)
            conn = POOL_MANAGER.connection_from_host(host, scheme = 'https')
            response = conn.urlopen(method, request, headers = headers, body = obj)
            content = json.loads(response.data)
            if response.status == 400:
                raise AlgoliaException(content["message"])
            elif response.status == 403:
                raise AlgoliaException("Invalid Application-ID or API-Key")
            elif response.status == 404:
                raise AlgoliaException("Resource does not exist")
            elif response.status == 200 or response.status == 201:
                return json.loads(response.data)
        except AlgoliaException, e:
            raise e
        except:
            pass
    raise AlgoliaException("Unreachable host")

