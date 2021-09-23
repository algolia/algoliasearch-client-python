import datetime
import os
import platform
import sys
from time import time
from random import shuffle

from typing import Optional

from algoliasearch.analytics_client import AnalyticsClient
from algoliasearch.insights_client import InsightsClient
from algoliasearch.search_client import SearchClient, SearchConfig
from algoliasearch.recommend_client import RecommendClient
from algoliasearch.recommendation_client import RecommendationClient
from algoliasearch.http.hosts import HostsCollection, Host
from faker import Faker

from algoliasearch.search_index import SearchIndex


class Factory(object):
    @staticmethod
    def search_client(app_id=None, api_key=None):
        # type: (Optional[str], Optional[str]) -> SearchClient

        app_id = app_id if app_id is not None else Factory.get_app_id()
        api_key = api_key if api_key is not None else Factory.get_api_key()

        config = SearchConfig(app_id, api_key)
        # To ensure `Consistency` during the Common Test Suite,
        # we force the transporter to work with a single
        # host in the { host-1, host-2, host-3 }
        config.hosts = Factory.hosts(app_id)
        return Factory.decide(SearchClient.create_with_config(config))

    @staticmethod
    def search_client2():
        # type: () -> SearchClient

        app_id = os.environ["ALGOLIA_APPLICATION_ID_2"]
        api_key = os.environ["ALGOLIA_ADMIN_KEY_2"]

        return Factory.search_client(app_id, api_key)

    @staticmethod
    def search_client_mcm():
        # type: () -> SearchClient

        app_id = os.environ["ALGOLIA_APPLICATION_ID_MCM"]
        api_key = os.environ["ALGOLIA_ADMIN_KEY_MCM"]

        return Factory.search_client(app_id, api_key)

    @staticmethod
    def index(search_client, index_name):
        # type: (SearchClient, str) -> SearchIndex

        return search_client.init_index(Factory.get_index_name(index_name))

    @staticmethod
    def hosts(app_id):
        # type: (str) -> HostsCollection

        hosts = [
            Host("{}-1.algolianet.com".format(app_id)),
            Host("{}-2.algolianet.com".format(app_id)),
            Host("{}-3.algolianet.com".format(app_id)),
        ]
        shuffle(hosts)

        return HostsCollection([hosts[0]])

    @staticmethod
    def analytics_client(app_id=None, api_key=None):
        # type: (Optional[str], Optional[str]) -> AnalyticsClient

        app_id = app_id if app_id is not None else Factory.get_app_id()
        api_key = api_key if api_key is not None else Factory.get_api_key()

        return Factory.decide(AnalyticsClient.create(app_id, api_key))

    @staticmethod
    def recommend_client(app_id=None, api_key=None):
        # type: (Optional[str], Optional[str]) -> RecommendClient

        app_id = app_id if app_id is not None else Factory.get_app_id()
        api_key = api_key if api_key is not None else Factory.get_api_key()

        return Factory.decide(RecommendClient.create(app_id, api_key))

    @staticmethod
    def recommendation_client(app_id=None, api_key=None):
        # type: (Optional[str], Optional[str]) -> RecommendationClient

        app_id = app_id if app_id is not None else Factory.get_app_id()
        api_key = api_key if api_key is not None else Factory.get_api_key()

        return Factory.decide(RecommendationClient.create(app_id, api_key))

    @staticmethod
    def insights_client(app_id=None, api_key=None):
        # type: (Optional[str], Optional[str]) -> InsightsClient

        app_id = app_id if app_id is not None else Factory.get_app_id()
        api_key = api_key if api_key is not None else Factory.get_api_key()

        return Factory.decide(InsightsClient.create(app_id, api_key))

    @staticmethod
    def get_app_id():
        # type: () -> str

        return os.environ["ALGOLIA_APPLICATION_ID_1"]

    @staticmethod
    def get_api_key():
        # type: () -> str

        return os.environ["ALGOLIA_ADMIN_KEY_1"]

    @staticmethod
    def get_index_name(test_name):
        # type: (str) -> str

        date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

        if "CIRCLE_BUILD_NUM" in os.environ:
            instance = os.environ["CIRCLE_BUILD_NUM"]
        else:
            instance = "unknown"

        python_version = platform.python_version().replace(".", "")[:2]

        python_version += os.environ.get("TEST_TYPE", "sync")

        return "python{}_{}_{}_{}".format(python_version, date, instance, test_name)

    @staticmethod
    def obj(data=None, object_id=True):
        # type: (Optional[dict], Optional[bool, str, int]) -> dict

        fake = Faker()

        data = {} if data is None else data

        data["name"] = fake.name()

        if isinstance(object_id, bool):
            if object_id:
                data["objectID"] = fake.md5()
        elif isinstance(object_id, (str, int)):
            data["objectID"] = object_id

        return data

    @staticmethod
    def synonym(data=None, object_id=True):
        # type: (Optional[dict], Optional[bool, str, int]) -> dict

        fake = Faker()

        data = {} if data is None else data

        data["type"] = "synonym"
        if "type" not in data:
            data["type"] = "synonym"

        if "synonyms" not in data:
            data["synonyms"] = fake.words(nb=3)

        if isinstance(object_id, bool):
            if object_id:
                data["objectID"] = fake.md5()
        elif isinstance(object_id, (str, int)):
            data["objectID"] = object_id

        return data

    @staticmethod
    def rule(data=None, object_id=True):
        # type: (Optional[dict], Optional[bool, str, int]) -> dict

        fake = Faker()

        data = {} if data is None else data

        data.update(
            {
                "condition": {"anchoring": "is", "pattern": "pattern"},
                "consequence": {
                    "params": {
                        "query": {"edits": [{"type": "remove", "delete": "pattern"}]}
                    }
                },
            }
        )

        if isinstance(object_id, bool):
            if object_id:
                data["objectID"] = fake.md5()
        elif isinstance(object_id, (str, int)):
            data["objectID"] = object_id

        return data

    @staticmethod
    def decide(client):

        if os.environ.get("TEST_TYPE", False) == "async":
            from tests.helpers.misc_async import SyncDecorator

            return SyncDecorator(client)

        return client

    @staticmethod
    def two_days_ago_timestamp():
        # type: () -> int

        if sys.version_info >= (3, 0):
            timestamp = (
                datetime.datetime.now() - datetime.timedelta(days=2)
            ).timestamp()
        else:
            timestamp = time()

        return int(timestamp) * 1000
