from . import client
from . import index
from . import helpers


# Compatibility with old import
class algoliasearch(object):
    Client = client.Client
    Index = index.Index
    AlgoliaException = helpers.AlgoliaException
