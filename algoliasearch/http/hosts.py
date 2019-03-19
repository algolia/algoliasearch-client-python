import time
from random import shuffle

from typing import List


class Host(object):
    TTL = 300.0

    def __init__(self, url, priority=0, accept=None):
        # type: (str, Optional[int], Optional[int]) -> None

        self.url = url
        self.priority = priority
        self.accept = ((CallType.WRITE | CallType.READ) if accept is None
                       else accept)
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

    def read(self):
        # type: () -> HostsCollection

        return [host for host in self.__hosts if host.accept & CallType.READ]

    def write(self):
        # type: () -> HostsCollection

        return [host for host in self.__hosts if host.accept & CallType.WRITE]


class CallType(object):
    READ = 1
    WRITE = 2
