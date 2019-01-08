from random import shuffle

from typing import List


class Host(object):
    def __init__(self, url, priority=0):
        # type: (str, int) -> None

        self.url = url
        self.priority = priority
        self.last_use = 0
        self.retry_count = 0
        self.up = True

    def reset(self):
        self.last_use = 0
        self.retry_count = 0
        self.up = True


class HostsCollection(object):
    def __init__(self, hosts):
        # type: (List[Host]) -> None

        self.index = 0
        self._hosts = hosts

        self.reset()

    def reset(self):
        self.index = 0
        for host in self._hosts:
            host.reset()

        shuffle(self._hosts)

        self._hosts = sorted(self._hosts, key=lambda x: x.priority, reverse=True) # inverse... # check php

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self._hosts):
            self.index = 0
            raise StopIteration

        host = self._hosts[self.index]

        self.index += 1

        return host
