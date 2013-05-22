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

# Object returned by all API method
class Answer:
    def __init__(self, hasError, errorMsg, content):
        self.error = hasError
        self.errorMsg = errorMsg
        self.content = content

    # Returns True if the API call failed
    def hasError(self):
        return self.error

    # Returns error message when hasError() == True
    def getErrorMessage(self):
        return self.errorMsg

    # Returns answer content when hasError() == False
    def getContent(self):
        return self.content

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
    def __init__(self, applicationID, apiKey, hostsArray):
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
    return an Answer object with answer in the form 
       {"items": [{ "name": "contacts", "createdAt": "2013-01-18T15:33:13.556Z"},
                  {"name": "notes", "createdAt": "2013-01-18T15:33:13.556Z"}]}
    """
    def listIndexes(self):
        return AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/indexes/")

    """
    Delete an index

    @param indexName the name of index to delete
    Return an Answer object whith answer in the form {"deletedAt": "2013-01-18T15:33:13.556Z"}
    """
    def deleteIndex(self, indexName):
        return AlgoliaUtils_request(self.headers, self.hosts, "DELETE", "/1/indexes/%s" % urllib.quote(indexName))

    """
    Get the index object initialized (no server call needed for initialization)

    @param indexName the name of index
    @param callback the result callback with one argument (the Index instance)
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
             - addObject: allows to add a new object in the index (https only)
             - updateObject : allows to change content of an existing object (https only)
             - deleteObject : allows to delete an existing object (https only)
             - deleteIndex : allows to delete index content (https only)
             - settings : allows to get index settings (https only)
             - editSettings : allows to change index settings (https only)
    """
    def addUserKey(self, acls):
        return AlgoliaUtils_request(self.headers, self.hosts, "POST", "/1/keys", acls)

"""
Contains all the functions related to one index
You should use Client.initIndex(indexName) to retrieve this object
"""
class Index:
    def __init__(self, headers, hosts, indexName):
        self.hosts = hosts
        self.headers = headers
        self.indexName = indexName
        self.urlIndexName = urllib.quote(self.indexName)

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
            return AlgoliaUtils_request(self.headers, self.hosts, "PUT", "/1/indexes/%s/%s" % (self.urlIndexName, urllib.quote(objectID)), content)

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
        objID = urllib.quote(objectID)
        if (attributesToRetrieve == None):
            return AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/indexes/%s/%s" % (self.urlIndexName, objID))
        else:
            return AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/indexes/%s/%s?attributes=%s" % (self.urlIndexName, objID, attributesToRetrieve))

    """
    Update partially an object (only update attributes passed in argument)
    
    @param partialObject contains the javascript attributes to override, the 
           object must contains an objectID attribute
    """
    def partialUpdateObject(self, partialObject):
        return AlgoliaUtils_request(self.headers, self.hosts, "POST", "/1/indexes/%s/%s/partial" % (self.urlIndexName, urllib.quote(partialObject["objectID"])), partialObject)

    """
    Override the content of object
    
    @param object contains the javascript object to save, the object must contains an objectID attribute
    @param callback (optional) the result callback with two arguments:
           success: boolean set to true if the request was successfull
           content: the server answer that updateAt and taskID
    """
    def saveObject(self, obj):
        return AlgoliaUtils_request(self.headers, self.hosts, "PUT", "/1/indexes/%s/%s" % (self.urlIndexName, urllib.quote(obj["objectID"])), obj)

    """
    Override the content of several objects

    @param objects contains an array of objects to update (each object must contains a objectID attribute)
    """
    def saveObjects(self, objects):
        requests = []
        for obj in objects:
            requests.append({"action": "updateObject", "objetID": obj["objectID"], "body": obj})
        request = {"requests": requests}
        return AlgoliaUtils_request(self.headers, self.hosts, "POST", "/1/indexes/%s/batch" % self.urlIndexName, request)

    """
    Delete an object from the index 

    @param objectID the unique identifier of object to delete
    """
    def deleteObject(self, objectID):
        return AlgoliaUtils_request(self.headers, self.hosts, "DELETE", "/1/indexes/%s/%s" % (self.urlIndexName, urllib.quote(objectID)))

    """
    Search inside the index
    
    @param query the full text query
    @param args (optional) if set, contains an associative array with query parameters:
      - attributes: a string that contains attribute names to retrieve separated by a comma. 
        By default all attributes are retrieved.
      - attributesToHighlight: a string that contains attribute names to highlight separated by a comma. 
        By default all attributes are highlighted.
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
      - tags let you filter the query by a set of tags (contains a list of tags separated by ','). 
        At indexing, tags should be added in _tags attribute of objects (for example {"_tags":["tag1","tag2"]} )
    """
    def search(self, query, args = None):
        if args == None:
            return AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/indexes/%s?query=%s" % (self.urlIndexName, urllib.quote(query)))
        else:
            return AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/indexes/%s?query=%s&%s" % (self.urlIndexName, urllib.quote(query), urllib.urlencode(args)))

    """
    Wait the publication of a task on the server. 
    All server task are asynchronous and you can check with this method that the task is published.

    @param taskID the id of the task returned by server
    @param timeBeforeRetry the time in milliseconds before retry (default = 100ms)
    """
    def waitTask(self, taskID, timeBeforeRetry = 100):
        while True:
            res = AlgoliaUtils_request(self.headers, self.hosts, "GET", "/1/indexes/%s/task/%d/" % (self.urlIndexName, taskID))
            if res.hasError():
                return res;
            content = res.getContent()
            if (content["status"] == "published"):
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
            - position (sort according to the matching attribute), 
            - custom which is user defined
          (the standard order is ["typo", "geo", position", "custom"])
       - customRanking: (array of strings) lets you specify part of the ranking. 
         The syntax of this condition is an array of strings containing attributes prefixed 
         by asc (ascending order) or desc (descending order) operator.
     """
    def setSettings(self, settings):
        return AlgoliaUtils_request(self.headers, self.hosts, "PUT", "/1/indexes/%s/settings" % self.urlIndexName, settings)

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
                return Answer(True, content["message"], None)
            elif response.status == 403:
                return Answer(True, "Invalid Application-ID or API-Key", None)
            elif response.status == 404:
                return Answer(True, "Resource does not exist", None)
            elif response.status == 200:
                return Answer(False, None, json.loads(response.data))
        except:
            pass
    return Answer(True, "Unreachable host", None)

