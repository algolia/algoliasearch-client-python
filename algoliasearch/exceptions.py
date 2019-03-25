from typing import Optional


class AlgoliaException(Exception):
    pass


class MissingObjectIdException(AlgoliaException):
    def __init__(self, message, obj):
        # type: (str, dict) -> None

        super(AlgoliaException, self).__init__(message)
        self.obj = obj


class RequestException(AlgoliaException):
    def __init__(self, message, status_code):
        # type: (str, Optional[int]) -> None

        super(AlgoliaException, self).__init__(message)
        self.status_code = status_code


class AlgoliaUnreachableHostException(Exception):
    pass
