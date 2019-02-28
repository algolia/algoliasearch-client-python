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

        self.__index = 0
        self.__hosts = hosts

        for host in self.__hosts:
            host.reset()

        shuffle(self.__hosts)

        self.__hosts = sorted(self.__hosts, key=lambda x: x.priority,
                              reverse=True)

    def reset(self):
        # type: () -> Hosts

        self.__index = 0

        return self

    def next(self):  # Python 2
        # type: () -> Host

        return self.__next__()  # pragma: no cover

    def __now(self):
        # type: () -> float

        return time.time()

    def __iter__(self):
        # type: () -> HostsCollection

        return self

    def __next__(self):
        # type: () -> Host

        if self.__index == len(self.__hosts):
            self.__index = 0
            raise StopIteration

        host = self.__hosts[self.__index]

        self.__index += 1

        if not host.up and self.__now() - host.last_use > Host.TTL:
            host.up = True

        if not host.up:
            return self.__next__()

        return host
