import asyncio
import os
import types

from algoliasearch.iterators import Iterator


class SyncDecorator(object):
    @property
    def name(self):

        return self._base.name

    def __init__(self, base):

        self._base = base

    def __getattr__(self, name):

        method = getattr(self._base, name)

        if not callable(method):
            return method

        method = getattr(self._base, '{}_async'.format(name))

        def closure(*args, **kwargs):
            result = method(*args, **kwargs)

            if isinstance(result, types.GeneratorType):
                return asyncio.get_event_loop().run_until_complete(
                    asyncio.gather(result))[0]

            if isinstance(result, Iterator):
                return self.iterator_to_array(result)

            return result

        return closure

    def init_index(self, name):

        search_index = self._base.init_index(name)

        return SyncDecorator(search_index)

    def user(self, user_token):

        user_insights_client = self._base.user(user_token)
        user_insights_client._transporter = self._base._transporter
        if os.environ.get('TEST_TYPE', False) == 'async':
            user_insights_client._transporter_async = self._base._transporter_async  # noqa: E501

        return SyncDecorator(user_insights_client)

    def iterator_to_array(self, iterator):

        def closure():

            objects = []

            while True:
                try:
                    obj = yield from iterator.__anext__()
                except Exception:
                    break
                else:
                    objects.append(obj)

            return objects

        return asyncio.get_event_loop().run_until_complete(closure())

    def __del__(self):

        self._base._transporter.close()

        if os.environ.get('TEST_TYPE', False) == 'async':
            asyncio.get_event_loop().run_until_complete(
                asyncio.gather(self._base._transporter_async.close())
            )
