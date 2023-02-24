import json
import math
import sys
import time
from typing import Any, Dict, Iterable, Iterator, List, Optional, Union

from algoliasearch.exceptions import MissingObjectIdException

if sys.version_info >= (3, 0):
    from urllib.parse import quote
else:
    from urllib import quote  # pragma: no cover


def endpoint(path, *args):
    # type: (str, Optional[Union[str, int]]) -> str

    arguments = []
    for arg in args:
        if not sys.version_info >= (3, 0) and isinstance(arg, unicode):
            arguments.append(quote(arg.encode("utf-8"), safe=""))  # pragma: no cover
        else:
            arguments.append(quote(str(arg), safe=""))  # pragma: no cover

    return getattr(path, "format")(*arguments)


def get_items(dictionary=None):
    # type: (Optional[dict]) -> Iterable

    if dictionary is None:
        items = []  # type: Iterable
    elif sys.version_info >= (3, 0):
        items = dictionary.items()
    else:
        items = dictionary.iteritems()  # pragma: no cover

    return items


def assert_object_id(objects):
    # type: (Iterable[Dict[str, Any]]) -> None

    for obj in objects:
        if "objectID" not in obj:
            raise MissingObjectIdException(
                "Missing `objectID` in: {}".format(json.dumps(obj)), obj
            )


def build_raw_response_batch(action, objects):
    # type: (str, Union[List[dict], Iterator[dict]]) -> List[dict]

    return [{"action": action, "body": obj} for obj in objects]


def is_async_available():
    # type: () -> bool

    if sys.version_info >= (3, 0):
        try:
            import asyncio

            import aiohttp
            import async_timeout

            return True
        except ImportError:
            pass

    return False


def sleep_for(retries_count, before_retry):
    # type: (int, int) -> None

    factor = math.ceil(retries_count / 10)
    time.sleep(factor * before_retry / 1000000.0)
