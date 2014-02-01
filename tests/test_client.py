# -*- coding: utf-8 -*-

import unittest
import os
import time
import sys


from algoliasearch import algoliasearch

def safe_index_name(name):
  if 'TRAVIS' not in os.environ:
    return name
  id = os.environ['TRAVIS_JOB_NUMBER'].split('.')[-1]
  return "%s_travis-%s" % (name, id)

class ClientTest(unittest.TestCase):
  def setUp(self):
    self.client = algoliasearch.Client(os.environ['ALGOLIA_APPLICATION_ID'], os.environ['ALGOLIA_API_KEY'])
    index_name = safe_index_name('towns')
    try:
      self.client.deleteIndex(index_name)
    except algoliasearch.AlgoliaException:
      pass
    self.index = self.client.initIndex(index_name)

  def test_addObject(self):
    task = self.index.addObject({ 'name': 'Paris' }, "42")
    self.index.waitTask(task['taskID'])
    results = self.index.search('pa')
    self.assertEquals(len(results['hits']), 1)
    self.assertEquals('Paris', results['hits'][0]['name'])

    task = self.index.addObjects([ { 'name': 'Los Angeles' }, { 'name': 'Los Gatos'} ])
    self.index.waitTask(task['taskID'])
    results = self.index.search('los')
    self.assertEquals(len(results['hits']), 2)

    task = self.index.partialUpdateObjects([{ 'name': 'San Francisco', 'objectID': results['hits'][0]['objectID']},
                                { 'name': 'San Marina', 'objectID': results['hits'][1]['objectID']}])
    self.index.waitTask(task['taskID'])
    results = self.index.search('san', { "attributesToRetrieve": ["name"], "hitsPerPage": 20})
    self.assertEquals(len(results['hits']), 2)

  def test_getObject(self):

    task = self.index.saveObject({"name": "San Francisco", "objectID": "32"})
    self.index.waitTask(task['taskID'])
    
    obj = self.index.getObject("32", 'name')
    self.assertEquals(obj['name'], 'San Francisco')

    task = self.index.partialUpdateObject({"name": "San Diego", "objectID": "32"})
    self.index.waitTask(task['taskID'])
    obj = self.index.getObject("32")
    self.assertEquals(obj['name'], 'San Diego')

    task = self.index.saveObjects([{"name": "Los Angeles", "objectID": "32"}])
    self.index.waitTask(task['taskID'])

    obj = self.index.getObject("32")
    self.assertEquals(obj['name'], 'Los Angeles')

  def test_deleteObject(self):
    task = self.index.addObject({'name': 'San Francisco'})
    self.index.waitTask(task['taskID'])
    results = self.index.search('')
    self.assertEquals(len(results['hits']), 1)
    res = self.index.deleteObject(results['hits'][0]['objectID'])
    results = self.index.search('')
    self.assertEquals(len(results['hits']), 0)

    self.assertRaises(algoliasearch.AlgoliaException, self.index.deleteObject, "")

  def test_listIndexes(self):
    new_index = self.client.initIndex(safe_index_name('listIndex'))
    try:
      self.client.deleteIndex(safe_index_name('listIndex'))
      time.sleep(4) # Dirty but temporary
    except algoliasearch.AlgoliaException:
      pass
    res = self.client.listIndexes()
    task = new_index.addObject({'name': 'San Francisco'})
    new_index.waitTask(task['taskID'])
    resAfter = self.client.listIndexes()
    is_present = False
    for it in resAfter['items']:
      is_present = is_present or it['name'] == safe_index_name('listIndex') 
    self.assertEquals(is_present, True)

  def test_clearIndex(self):
    task = self.index.addObject({'name': 'San Francisco'})
    self.index.waitTask(task['taskID'])
    results = self.index.search('')
    self.assertEquals(len(results['hits']), 1)
    task = self.index.clearIndex()
    self.index.waitTask(task['taskID'])
    results = self.index.search('')
    self.assertEquals(len(results['hits']), 0)

  def test_copy(self):
    new_index = self.client.initIndex(safe_index_name('city'))
    try:
      self.client.deleteIndex(safe_index_name('city'))
    except algoliasearch.AlgoliaException:
      pass
    res = self.client.listIndexes()
    task = self.index.addObject({'name': 'San Francisco'})
    self.index.waitTask(task['taskID'])
    task = self.client.copyIndex(safe_index_name('towns'), safe_index_name('city'))
    results = new_index.search('')
    self.assertEquals(len(results['hits']), 1)
    self.assertEquals(results['hits'][0]['name'], 'San Francisco')

  def test_move(self):
    new_index = self.client.initIndex(safe_index_name('city'))
    try:
      self.client.deleteIndex(safe_index_name('city'))
    except algoliasearch.AlgoliaException:
      pass
    res = self.client.listIndexes()
    task = self.index.addObject({'name': 'San Francisco'})
    self.index.waitTask(task['taskID'])
    task = self.client.moveIndex(safe_index_name('towns'), safe_index_name('city'))
    self.index.waitTask(task['taskID'])
    results = new_index.search('')
    self.assertEquals(len(results['hits']), 1)
    self.assertEquals(results['hits'][0]['name'], 'San Francisco')

  def test_browse(self):
    try:
      task = self.index.clearIndex()
      self.index.waitTask(task['taskID'])
    except algoliasearch.AlgoliaException:
      pass
    task = self.index.addObject({'name': 'San Francisco'})
    self.index.waitTask(task['taskID'])
    res = self.index.browse()
    self.assertEquals(len(res['hits']), 1)
    self.assertEquals(res['hits'][0]['name'], 'San Francisco')

  def test_log(self):
    res = self.client.getLogs()
    self.assertTrue(len(res['logs']) > 0)

  def test_batch(self):
    task = self.index.batch({'requests': [{ 'action': 'addObject', 'body':{'name': 'San Francisco'}}   \
      , { 'action': 'addObject', 'body':{'name': 'Los Angeles'}}                          \
      , { 'action': 'updateObject', 'body':{'name': 'San Diego'}, 'objectID':'42'}    \
      , { 'action': 'updateObject', 'body':{'name': 'Los Gatos'}, 'objectID':'43'}    \
      ]})
    self.index.waitTask(task['taskID'])
    obj = self.index.getObject("42")
    self.assertEquals(obj['name'], 'San Diego')

    res = self.index.search('')
    self.assertEquals(len(res['hits']), 4)

  def test_user_key(self):
    res = self.index.listUserKeys()
    newKey = self.index.addUserKey(['search'])
    self.assertTrue(newKey['key'] != "")
    resAfter = self.index.listUserKeys()
    is_present = False
    for it in resAfter['keys']:
      is_present = is_present or it['value'] == newKey['key']
    self.assertTrue(is_present)
    key = self.index.getUserKeyACL(newKey['key'])
    self.assertEquals(key['acl'][0], 'search')
    task = self.index.deleteUserKey(newKey['key'])
    resEnd = self.index.listUserKeys()
    is_present = False
    for it in resEnd['keys']:
      is_present = is_present or it['value'] == newKey['key']
    self.assertTrue(not is_present)


    res = self.client.listUserKeys()
    newKey = self.client.addUserKey(['search'])
    self.assertTrue(newKey['key'] != "")
    resAfter = self.client.listUserKeys()
    is_present = False
    for it in resAfter['keys']:
      is_present = is_present or it['value'] == newKey['key']
    self.assertTrue(is_present)
    key = self.client.getUserKeyACL(newKey['key'])
    self.assertEquals(key['acl'][0], 'search')
    task = self.client.deleteUserKey(newKey['key'])
    resEnd = self.client.listUserKeys()
    is_present = False
    for it in resEnd['keys']:
      is_present = is_present or it['value'] == newKey['key']
    self.assertTrue(not is_present)


  def test_settings(self):
    task = self.index.setSettings({'attributesToRetrieve': ['name']})
    self.index.waitTask(task['taskID'])
    settings = self.index.getSettings()
    self.assertEquals(len(settings['attributesToRetrieve']), 1)
    self.assertEquals(settings['attributesToRetrieve'][0], 'name')
    
  def test_URLEncode(self):

    task = self.index.saveObject({"name": "San Francisco", "objectID": u"a/go/?\xe0"})
    self.index.waitTask(task['taskID'])
    
    obj = self.index.getObject(u"a/go/?\xe0", 'name')
    self.assertEquals(obj['name'], 'San Francisco')

    task = self.index.partialUpdateObject({"name": "San Diego", "objectID": u"a/go/?\xe0"})
    self.index.waitTask(task['taskID'])
    obj = self.index.getObject(u"a/go/?\xe0")
    self.assertEquals(obj['name'], 'San Diego')

    task = self.index.saveObjects([{"name": "Los Angeles", "objectID": u"a/go/?\xe0"}])
    self.index.waitTask(task['taskID'])

    obj = self.index.getObject(u"a/go/?\xe0")
    self.assertEquals(obj['name'], 'Los Angeles')

