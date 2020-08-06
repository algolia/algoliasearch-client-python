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
        self.message = message

    def __hash__(self):
        # type: () -> int
        return id(self)

    def __eq__(self, other):
        # type: (object) -> bool
        if isinstance(other, RequestException):
            return (
                self.message == other.message and self.status_code == other.status_code
            )  # noqa: E501
        return False

    def __ne__(self, other):
        # type: (object) -> bool
        return not self.__eq__(other)


class AlgoliaUnreachableHostException(AlgoliaException):
    pass


class ObjectNotFoundException(AlgoliaException):
    pass


class ValidUntilNotFoundException(AlgoliaException):
    pass
