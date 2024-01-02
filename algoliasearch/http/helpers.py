# coding: utf-8

from asyncio import sleep
from typing import Callable, Protocol, TypeVar

T = TypeVar("T")


class Timeout(Protocol):
    def __call__(self) -> int:
        return 0

    def __init__(self) -> None:
        pass


class RetryTimeout(Timeout):
    def __call__(self, retry_count: int) -> int:
        return min(retry_count * 0.2, 5)

    def __init__(self) -> None:
        pass


async def create_iterable(
    func: Callable[[T], T],
    validate: Callable[[T], bool],
    aggregator: Callable[[T], None],
    timeout: Timeout = Timeout(),
    error_validate: Callable[[T], bool] = None,
    error_message: Callable[[T], str] = None,
) -> T:
    """
    Helper: Iterates until the given `func` until `timeout` or `validate`.
    """

    async def retry(prev: T = None) -> T:
        resp = await func(prev)

        if aggregator:
            aggregator(resp)

        if validate(resp):
            return resp

        if error_validate is not None and error_validate(resp):
            if error_message is None:
                raise Exception("An error occurred")
            raise Exception(error_message(resp))

        await sleep(timeout())
        return await retry(resp)

    return await retry()
