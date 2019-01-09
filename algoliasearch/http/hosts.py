import time
from random import shuffle

from typing import List


class Host(object):
    TTL = 300.0

    def __init__(self, url, priority=0):
        # type: (str, int) -> None

        self.url = url
        self.priority = priority
        self.last_use = 0.0
        self.retry_count = 0
        self.up = True

    def reset(self):
        # type: () -> None

        self.last_use = 0.0
        self.retry_count = 0
        self.up = True


class HostsCollection(object):
    def __init__(self, hosts):
        # type: (List[Host]) -> None

        self.index = 0
        self._hosts = hosts

        for host in self._hosts:
            host.reset()

        shuffle(self._hosts)

        self._hosts = sorted(self._hosts, key=lambda x: x.priority,
                             reverse=True)

    def reset(self):
        # type: () -> None

        self.index = 0

    def next(self):  # Python 2
        # type: () -> Host

        return self.__next__()

    def __now(self):
        # type: () -> float

        return time.time()

    def __iter__(self):
        # type: () -> HostsCollection

        return self

    def __next__(self):
        # type: () -> Host

        if self.index == len(self._hosts):
            self.index = 0
            raise StopIteration

        host = self._hosts[self.index]

        self.index += 1

        if not host.up and self.__now() - host.last_use > Host.TTL:
            host.up = True

        if not host.up:
            return self.__next__()

        return host
