from typing import Optional, Union, Dict, Any

from algoliasearch.exceptions import AlgoliaException, RequestException
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.responses import MultipleResponse
from algoliasearch.search_index import SearchIndex


class AccountClient(object):
    @staticmethod
    def copy_index(source_index, destination_index, request_options=None):
        # type: (SearchIndex, SearchIndex, Optional[Union[Dict[str, Any], RequestOptions]]) -> MultipleResponse  # noqa: E501

        if source_index.app_id == destination_index.app_id:
            raise AlgoliaException(
                "The indices are on the same application. "
                "Use client.copy_index instead."
            )

        try:
            destination_index.get_settings()
        except RequestException:
            pass
        else:
            raise AlgoliaException(
                "Destination index already exists. Please "
                "delete it before copying index across applications."
            )

        responses = MultipleResponse()

        # Copy settings
        settings = source_index.get_settings()
        responses.push(destination_index.set_settings(settings, request_options))

        # Copy synonyms
        synonyms = source_index.browse_synonyms()
        responses.push(destination_index.save_synonyms(synonyms, request_options))

        # Copy rules
        rules = source_index.browse_rules()
        responses.push(destination_index.save_rules(rules, request_options))

        # Copy objects
        objects = source_index.browse_objects()
        responses.push(destination_index.save_objects(objects, request_options))

        return responses
