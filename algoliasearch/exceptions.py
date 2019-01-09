from typing import Optional


class AlgoliaException(Exception):
    def __init__(self, message, status_code):
        # type: (str, Optional[int]) -> None

        self.message = message
        self.status_code = status_code


class AlgoliaUnreachableHostException(Exception):
    pass
