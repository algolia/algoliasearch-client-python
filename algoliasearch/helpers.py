import sys

from typing import Optional, Iterable


class Items(object):
    @staticmethod
    def get(dictionary=None):
        # type: (Optional[dict]) -> Iterable

        if dictionary is None:
            items = []  # type: Iterable
        elif sys.version_info >= (3, 0):
            items = dictionary.items()
        else:
            items = dictionary.iteritems()

        return items
