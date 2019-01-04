from platform import python_version
from typing import Optional

from algoliasearch.config.config import Config
from algoliasearch.helpers import Interpreter
from algoliasearch.version import VERSION
from algoliasearch.http.params import Params


class RequestOptions(object):
    def __init__(self, headers, query_parameters, timeouts, data):
        # type: (dict, dict, dict, dict) -> None

        self.headers = headers
        self.query_parameters = query_parameters
        self.timeouts = timeouts
        self.data = data

    @staticmethod
    def create(config, options=None):
        # type: (Config, Optional[dict]) -> RequestOptions

        headers = {
            'X-Algolia-Application-Id': config.app_id,
            'X-Algolia-API-Key': config.api_key,
            'User-Agent': 'Algolia for Python (%s); Python (%s)' % (
                VERSION, python_version()),
            'Content-Type': 'application/json',
        }

        timeouts = {
            'readTimeout': config.read_timeout,
            'writeTimeout': config.write_timeout,
            'connectTimeout': config.connect_timeout,
        }

        request_options = RequestOptions(headers, {}, timeouts, {})

        if options is None:
            items = {}
        elif Interpreter.python3():
            items = options.items()
        else:
            items = options.iteritems()

        for option, value in items:
            if option in Params.HEADERS:
                request_options.headers[option] = value
            elif option in Params.QUERY_PARAMETERS:
                request_options.query_parameters[option] = value
            elif option in Params.TIMEOUTS:
                request_options.timeouts[option] = value
            else:
                request_options.data[option] = value

        return request_options
