from typing import Optional, Union

from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.verbs import Verbs
from algoliasearch.responses import IndexingResponse, AssignUserIdResponse, \
    RemoveUserIdResponse
from algoliasearch.search_index import SearchIndex
from algoliasearch.configs import SearchConfig
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.requester import Requester


class SearchClient(object):
    @property
    def app_id(self):
        # type: () -> str

        return self.__config.app_id

    def __init__(self, transporter, search_config):
        # type: (Transporter, SearchConfig) -> None

        self.__transporter = transporter
        self.__config = search_config

    def init_index(self, name):
        # type: (str) -> SearchIndex

        return SearchIndex(self.__transporter, self.__config, name)

    @staticmethod
    def create(app_id, api_key):
        # type: (str, str) -> SearchClient

        config = SearchConfig(app_id, api_key)
        requester = Requester()
        transporter = Transporter(requester, config)

        return SearchClient(transporter, config)

    def copy_index(self, src_index_name, dst_index_name, request_options=None):
        # type: (str, str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self.__transporter.write(
            Verbs.POST,
            '1/indexes/%s/operation' % src_index_name,
            {
                'operation': 'copy',
                'destination': dst_index_name
            },
            request_options
        )

        return IndexingResponse(self.init_index(src_index_name),
                                [raw_response])

    def copy_settings(self, src_index_name, dst_index_name,
                      request_options=None):
        # type: (str, str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        if request_options is None:
            request_options = {}

        request_options['scope'] = ['settings']

        return self.copy_index(src_index_name, dst_index_name, request_options)

    def copy_synonyms(self, src_index_name, dst_index_name,
                      request_options=None):
        # type: (str, str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        if request_options is None:
            request_options = {}

        request_options['scope'] = ['synonyms']

        return self.copy_index(src_index_name, dst_index_name, request_options)

    def copy_rules(self, src_index_name, dst_index_name, request_options=None):
        # type: (str, str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        if request_options is None:
            request_options = {}

        request_options['scope'] = ['rules']

        return self.copy_index(src_index_name, dst_index_name, request_options)

    def assign_user_id(self, user_id, cluster, request_options=None):
        # type: (str, str,Optional[Union[dict, RequestOptions]]) -> AssignUserIdResponse  # noqa: E501

        if request_options is None:
            request_options = RequestOptions.create(self.__config)

        request_options['X-Algolia-User-ID'] = user_id

        self.__transporter.write(
            Verbs.POST,
            '1/clusters/mapping',
            {'cluster': cluster},
            request_options
        )

        return AssignUserIdResponse(self, user_id)

    def remove_user_id(self, user_id, request_options=None):
        # type: (str,Optional[Union[dict, RequestOptions]]) -> RemoveUserIdResponse  # noqa: E501

        if request_options is None:
            request_options = RequestOptions.create(self.__config)

        request_options['X-Algolia-User-ID'] = user_id

        self.__transporter.write(
            Verbs.DELETE,
            '1/clusters/mapping',
            None,
            request_options
        )

        return RemoveUserIdResponse(self, user_id)

    def list_clusters(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict

        return self.__transporter.read(
            Verbs.GET,
            '1/clusters',
            {},
            request_options
        )

    def get_user_id(self, user_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        return self.__transporter.read(
            Verbs.GET,
            '1/clusters/mapping/%s' % user_id,
            None,
            request_options
        )

    def list_user_ids(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict

        return self.__transporter.read(
            Verbs.GET,
            '1/clusters/mapping',
            None,
            request_options
        )

    def get_top_user_ids(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict

        return self.__transporter.read(
            Verbs.GET,
            '1/clusters/mapping/top',
            None,
            request_options
        )

    def search_user_ids(self, query, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        return self.__transporter.read(
            Verbs.POST,
            '1/clusters/mapping/search',
            {'query': query},
            request_options
        )git
