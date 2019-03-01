from typing import Optional, Union

from algoliasearch.configs import AnalyticsConfig
from algoliasearch.helpers import endpoint
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.requester import Requester
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verbs import Verbs


class AnalyticsClient(object):
    def __init__(self, transporter, search_config):
        # type: (Transporter, AnalyticsConfig) -> None

        self.__transporter = transporter
        self.__config = search_config

    @staticmethod
    def create(app_id, api_key, region='us'):
        # type: (str, str, str) -> AnalyticsClient

        config = AnalyticsConfig(app_id, api_key, region)
        requester = Requester()
        transporter = Transporter(requester, config)

        return AnalyticsClient(transporter, config)

    def get_ab_tests(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict

        return self.__transporter.read(
            Verbs.GET,
            '2/abtests',
            None,
            request_options
        )

    def get_ab_test(self, ab_test_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        if not ab_test_id:
            raise ValueError('ab_test_id cannot be empty')

        return self.__transporter.read(
            Verbs.GET,
            endpoint('2/abtests/%s', ab_test_id),
            None,
            request_options
        )

    def add_ab_test(self, ab_test, request_options=None):
        # type: (dict, Optional[Union[dict, RequestOptions]]) -> dict

        return self.__transporter.write(
            Verbs.POST,
            '2/abtests',
            ab_test,
            request_options
        )

    def stop_ab_test(self, ab_test_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        if not ab_test_id:
            raise ValueError('ab_test_id cannot be empty')

        return self.__transporter.write(
            Verbs.POST,
            endpoint('2/abtests/%s/stop', ab_test_id),
            None,
            request_options
        )

    def delete_ab_test(self, ab_test_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        if not ab_test_id:
            raise ValueError('ab_test_id cannot be empty')

        return self.__transporter.write(
            Verbs.DELETE,
            endpoint('2/abtests/%s', ab_test_id),
            None,
            request_options
        )
