import unittest
import os

from algoliasearch import algoliasearch

def safe_index_name(name):
  if 'TRAVIS' not in os.environ:
    return name
  id = os.environ['TRAVIS_JOB_NUMBER'].split('.')[-1]
  return "%s_travis-%s" % (name, id)

class ClientTest(unittest.TestCase):
  def setUp(self):
    self.client = algoliasearch.Client(os.environ['ALGOLIA_APPLICATION_ID'], os.environ['ALGOLIA_API_KEY'])

  def test_addObject(self):
    index_name = safe_index_name('towns')
    try:
      self.client.deleteIndex(index_name)
    except algoliasearch.AlgoliaException:
      pass
    index = self.client.initIndex(index_name)
    index.addObject({ 'name': 'Paris' })
    results = index.search('pa')
    self.assertEquals(len(results['hits']), 1)
    self.assertEquals('Paris', results['hits'][0]['name'])

    index.addObjects([ { 'name': 'Los Angeles' }, { 'name': 'Los Gatos'} ])
    results = index.search('los')
    self.assertEquals(len(results['hits']), 2)
