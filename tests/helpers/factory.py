import datetime
import os
import platform

from algoliasearch.search_client import SearchClient
from faker import Faker


class Factory(object):
    @staticmethod
    def client(app_id=None, api_key=None):
        app_id = app_id if app_id is not None else os.environ[
            'ALGOLIA_APPLICATION_ID_1']
        api_key = api_key if api_key is not None else os.environ[
            'ALGOLIA_ADMIN_KEY_1']

        return SearchClient.create(app_id, api_key)

    @staticmethod
    def index(name):
        date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

        if 'TRAVIS' in os.environ:
            instance = os.environ['TRAVIS_JOB_NUMBER']
        else:
            instance = 'unknown'

        client = Factory.client()

        python_version = platform.python_version()

        index_name = 'python%s_%s_%s_%s' % (
            python_version, date, instance, name)

        return client.init_index(index_name)

    @staticmethod
    def mcm(name):
        date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

        if 'TRAVIS' in os.environ:
            instance = os.environ['TRAVIS_JOB_NUMBER']
        else:
            instance = 'unknown'

        app_id = os.environ['ALGOLIA_APPLICATION_ID_MCM']
        api_key = os.environ['ALGOLIA_ADMIN_KEY_MCM']

        client = Factory.client(app_id, api_key)

        python_version = platform.python_version()

        index_name = 'python%s_%s_%s_%s' % (
            python_version, date, instance, name)

        return client.init_index(index_name)

    @staticmethod
    def obj(data=None, object_id=True):
        fake = Faker()

        data = {} if data is None else data

        data['name'] = fake.name()

        if isinstance(object_id, bool):
            if object_id:
                data['objectID'] = fake.md5()
        elif isinstance(object_id, (str, int)):
            data['objectID'] = object_id

        return data

    @staticmethod
    def synonym(data=None, object_id=True):
        fake = Faker()

        data = {} if data is None else data

        data['type'] = 'synonym'
        if 'type' not in data:
            data['type'] = 'synonym'

        if 'synonyms' not in data:
            data['synonyms'] = fake.words(nb=3)

        if isinstance(object_id, bool):
            if object_id:
                data['objectID'] = fake.md5()
        elif isinstance(object_id, (str, int)):
            data['objectID'] = object_id

        return data
