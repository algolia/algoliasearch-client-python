# coding: utf-8

import asyncio
import time
from typing import Awaitable, Callable, Optional, TypeVar

T = TypeVar("T")


class Timeout:
    def __call__(self, retry_count: int = 0) -> int:
        return retry_count

    def __init__(self) -> None:
        pass


class RetryTimeout(Timeout):
    def __call__(self, retry_count: int = 0) -> int:
        return int(min(retry_count * 0.2, 5))


async def create_iterable(
    func: Callable[[Optional[T]], Awaitable[T]],
    validate: Callable[[T], bool],
    aggregator: Optional[Callable[[T], None]],
    timeout: Callable[[], int] = Timeout(),
    error_validate: Optional[Callable[[T], bool]] = None,
    error_message: Optional[Callable[[T], str]] = None,
) -> T:
    """
    Helper: Iterates until the given `func` until `timeout` or `validate`.
    """

    async def retry(prev: Optional[T] = None) -> T:
        resp = await func(prev)

        if aggregator:
            aggregator(resp)

        if validate(resp):
            return resp

        if error_validate is not None and error_validate(resp):
            if error_message is None:
                raise Exception("An error occurred")
            raise Exception(error_message(resp))

        await asyncio.sleep(timeout())
        return await retry(resp)

    return await retry()


def create_iterable_sync(
    func: Callable[[Optional[T]], T],
    validate: Callable[[T], bool],
    aggregator: Optional[Callable[[T], None]],
    timeout: Callable[[], int] = Timeout(),
    error_validate: Optional[Callable[[T], bool]] = None,
    error_message: Optional[Callable[[T], str]] = None,
) -> T:
    """
    Helper: Iterates until the given `func` until `timeout` or `validate`.
    """

    def retry(prev: Optional[T] = None) -> T:
        resp = func(prev)

        if aggregator:
            aggregator(resp)

        if validate(resp):
            return resp

        if error_validate is not None and error_validate(resp):
            if error_message is None:
                raise Exception("An error occurred")
            raise Exception(error_message(resp))

        time.sleep(timeout())
        return retry(resp)

    return retry()
