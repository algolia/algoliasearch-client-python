import datetime
import os

from algoliasearch.search_client import SearchClient
from algoliasearch.search_index import SearchIndex
from faker import Faker


class Factory(object):
    @staticmethod
    def client(app_id, api_key):
        # type: (str, str) -> SearchClient

        return SearchClient.create(app_id, api_key)

    @staticmethod
    def index(client, name):
        # type: (SearchClient, str) -> SearchIndex

        date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

        if 'TRAVIS' in os.environ:
            instance = os.environ['TRAVIS_JOB_NUMBER']
        else:
            instance = 'unknown'

        return client.init_index('python_%s_%s_%s' % (date, instance, name))

    @staticmethod
    def obj():
        # type: () -> dict

        fake = Faker()
        return {
            'objectID': fake.md5(),
            'name': fake.name(),
        }
