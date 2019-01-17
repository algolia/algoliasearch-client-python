from typing import Optional

from algoliasearch.configs import Config
from algoliasearch.helpers import get_items


class RequestOptions(object):
    def __init__(self, headers, query_parameters, timeouts, data):
        # type: (dict, dict, dict, dict) -> None

        self.headers = headers
        self.query_parameters = query_parameters
        self.timeouts = timeouts
        self.data = data

    def __setitem__(self, option, value):
        if option in Params.HEADERS:
            self.headers[option] = value
        elif option in Params.QUERY_PARAMETERS:
            self.query_parameters[option] = value
        elif option in Params.TIMEOUTS:
            self.timeouts[option] = value
        else:
            self.data[option] = value

    @staticmethod
    def create(config, options=None):
        # type: (Config, Optional[dict]) -> RequestOptions

        headers = config.headers

        timeouts = {
            'readTimeout': config.read_timeout,
            'writeTimeout': config.write_timeout,
            'connectTimeout': config.connect_timeout,
        }

        request_options = RequestOptions(headers, {}, timeouts, {})

        for option, value in get_items(options):
            request_options[option] = value

        return request_options


class Params(object):
    HEADERS = [
        'Content-type',
        'User-Agent',
    ]

    QUERY_PARAMETERS = [
        'createIfNotExists',
        'forwardToReplicas',
        'replaceExistingSynonyms',
        'clearExistingRules',
        'getVersion',
    ]

    TIMEOUTS = [
        'readTimeout',
        'writeTimeout',
        'connectTimeout',
    ]
