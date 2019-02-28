import asyncio
import copy

from algoliasearch.responses import IndexingResponse


def _create_async_methods_in(instance):
    # type: (object) -> None

    # First, we get the methods from the sync class (the parent class)
    methods = [func for func in dir(instance) if
               callable(getattr(instance, func))]

    # Then, we get methods from the instance
    instance_methods = [func for func in instance.__class__.__dict__.keys()]
    instance_copy = copy.copy(instance)

    # Finally, for each method we create a {method}_async version of it
    for method in methods:
        if method not in instance_methods and not method.startswith('_'):
            if method + '_async' not in instance_methods:
                instance.__setattr__(method + '_async',
                                     _gen_async(instance_copy, method))


def _gen_async(instance, method):
    # type: (object, str) -> None

    m = getattr(instance, method)

    def closure(*args, **kwargs):
        result = m(*args, **kwargs)

        # We make sure we resolve the promise from the raw_responses
        if hasattr(result, 'raw_responses'):
            i = 0
            for raw_response in result.raw_responses:
                result.raw_responses[i] = yield from raw_response
                i += 1

        # We make sure we resolve the promise from the raw_response
        if hasattr(result, 'raw_response'):
            result.raw_response = yield from result.raw_response

        # We make sure we resolve the promise
        if str(type(result)) == "<class 'generator'>":
            result = yield from result

        return result

    return asyncio.coroutine(closure)
