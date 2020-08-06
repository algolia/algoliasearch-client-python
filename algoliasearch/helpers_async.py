import asyncio
import types

from typing import Callable


def _create_async_methods_in(async_client, sync_client):
    # type: (object, object) -> None

    # First, we get the methods from the sync class (the parent class)
    methods = [
        func for func in dir(async_client) if callable(getattr(async_client, func))
    ]

    # Then, we get methods from the async_client
    async_client_methods = list(async_client.__class__.__dict__.keys())

    # Finally, for each method we create a {method}_async version of it
    for method in methods:
        if method not in async_client_methods and not method.startswith("_"):
            if "{}_async".format(method) not in async_client_methods:
                async_client.__setattr__(
                    "{}_async".format(method), _gen_async(sync_client, method)
                )


def _gen_async(client, method):
    # type: (object, str) -> Callable

    m = getattr(client, method)

    def closure(*args, **kwargs):
        result = m(*args, **kwargs)

        # We make sure we resolve the promise from the raw_responses
        if hasattr(result, "raw_responses"):
            for i, raw_response, in enumerate(result.raw_responses):
                result.raw_responses[i] = yield from raw_response

        # We make sure we resolve the promise from the raw_response
        if hasattr(result, "raw_response"):
            result.raw_response = yield from result.raw_response

        # We make sure we resolve the promise
        if isinstance(result, types.GeneratorType):
            result = yield from result

        return result

    return asyncio.coroutine(closure)
