import datetime
import os

from algoliasearch.search_client import SearchClient
from faker import Faker


class Factory(object):
    @staticmethod
    def client():
        app_id = os.environ['ALGOLIA_APPLICATION_ID_1']
        api_key = os.environ['ALGOLIA_ADMIN_KEY_1']

        return SearchClient.create(app_id, api_key)

    @staticmethod
    def index(name):
        date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

        if 'TRAVIS' in os.environ:
            instance = os.environ['TRAVIS_JOB_NUMBER']
        else:
            instance = 'unknown'

        client = Factory.client()

        return client.init_index('python_%s_%s_%s' % (date, instance, name))

    @staticmethod
    def obj():
        fake = Faker()
        return {
            'objectID': fake.md5(),
            'name': fake.name(),
        }
