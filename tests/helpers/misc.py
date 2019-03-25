import time

from algoliasearch.exceptions import RequestException


class RetryableClient:

    def __init__(self, base):

        self._base = base

    def __getattr__(self, name):

        method = getattr(self._base, name)

        def closure(*args, **kwargs):
            result = None

            while result is None:

                try:
                    result = method(*args, **kwargs)
                except RequestException as e:
                    if str(e) != 'Too Many Requests':
                        raise e
                    time.sleep(1)

            return result

        return closure
