import datetime
import os
import platform

from typing import Optional

from algoliasearch.analytics_client import AnalyticsClient
from algoliasearch.insights_client import InsightsClient
from algoliasearch.search_client import SearchClient
from faker import Faker

from algoliasearch.search_index import SearchIndex


class Factory(object):
    @staticmethod
    def search_client(app_id=None, api_key=None):
        # type: (Optional[str], Optional[str]) -> SearchClient

        app_id = app_id if app_id is not None else Factory.get_app_id()
        api_key = api_key if api_key is not None else Factory.get_api_key()

        return SearchClient.create(app_id, api_key)

    @staticmethod
    def get_app_id():
        # type: () -> str

        return os.environ['ALGOLIA_APPLICATION_ID_1']

    @staticmethod
    def get_api_key():
        # type: () -> str

        return os.environ['ALGOLIA_ADMIN_KEY_1']

    @staticmethod
    def index(name):
        # type: (str) -> SearchIndex

        date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

        if 'TRAVIS' in os.environ:
            instance = os.environ['TRAVIS_JOB_NUMBER']
        else:
            instance = 'unknown'

        python_version = platform.python_version().replace('.', '')[:2]

        return Factory.search_client().init_index(
            'python%s_%s_%s_%s' % (python_version, date, instance, name)
        )

    @staticmethod
    def mcm():
        # type: () -> SearchClient

        app_id = os.environ['ALGOLIA_APPLICATION_ID_MCM']
        api_key = os.environ['ALGOLIA_ADMIN_KEY_MCM']

        return Factory.search_client(app_id, api_key)

    @staticmethod
    def obj(data=None, object_id=True):
        # type: (Optional[dict], Optional[bool, str, int]) -> dict

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
        # type: (Optional[dict], Optional[bool, str, int]) -> dict

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

    @staticmethod
    def analytics_client(app_id=None, api_key=None):
        # type: (Optional[str], Optional[str]) -> AnalyticsClient

        app_id = app_id if app_id is not None else Factory.get_app_id()
        api_key = api_key if api_key is not None else Factory.get_api_key()

        return AnalyticsClient.create(app_id, api_key)

    @staticmethod
    def insights_client(app_id=None, api_key=None):
        # type: (Optional[str], Optional[str]) -> InsightsClient

        app_id = app_id if app_id is not None else Factory.get_app_id()
        api_key = api_key if api_key is not None else Factory.get_api_key()

        return InsightsClient.create(app_id, api_key)
