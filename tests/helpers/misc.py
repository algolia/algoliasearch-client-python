import json
import time

from algoliasearch.exceptions import RequestException


class RetryableClient:

    def __init__(self, base, retryable_messages):
        self._base = base
        self.retryable_messages = retryable_messages

    def __getattr__(self, name):
        method = getattr(self._base, name)

        def closure(*args, **kwargs):
            result = None
            while result is None:
                try:
                    result = method(*args, **kwargs)
                except RequestException as e:
                    if str(e) not in self.retryable_messages:
                        raise e
                    time.sleep(1)
            return result

        return closure


class Unicode:

    @staticmethod
    def convert_dict_to_unicode(d):
        tmp = json.dumps(d)
        tmp = json.loads(tmp)
        return tmp
