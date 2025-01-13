# coding: utf-8


class AlgoliaException(Exception):
    """The base exception class for all AlgoliaExceptions"""


class MissingObjectIdException(AlgoliaException):
    def __init__(self, message, obj):
        super(AlgoliaException, self).__init__(message)
        self.obj = obj


class RequestException(AlgoliaException):
    def __init__(self, message, status_code):
        super(AlgoliaException, self).__init__(message)
        self.status_code = status_code
        self.message = message

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        if isinstance(other, RequestException):
            return (
                self.message == other.message and self.status_code == other.status_code
            )
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class AlgoliaUnreachableHostException(AlgoliaException):
    pass


class ObjectNotFoundException(AlgoliaException):
    pass


class ValidUntilNotFoundException(AlgoliaException):
    pass


class ApiTypeError(AlgoliaException, TypeError):
    def __init__(
        self, msg, path_to_item=None, valid_classes=None, key_type=None
    ) -> None:
        """Raises an exception for TypeErrors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(AlgoliaException, ValueError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list) the path to the exception in the
                received_data dict. None if unset
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiAttributeError(AlgoliaException, AttributeError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Raised when an attribute reference or assignment fails.

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiAttributeError, self).__init__(full_msg)


class ApiKeyError(AlgoliaException, KeyError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


class ApiException(AlgoliaException):
    def __init__(
        self,
        status_code: int = -1,
        error_message: str = "Unknown error",
        raw_data: bytes = b"",
    ) -> None:
        self.status_code = status_code
        self.error_message = error_message
        self.body = raw_data.decode("utf-8")

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\nReason: {1}\n".format(
            self.status_code, self.error_message
        )

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message


def render_path(path_to_item):
    """Returns a string representation of a path"""
    result = ""
    for pth in path_to_item:
        if isinstance(pth, int):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result
