from random import shuffle
from typing import List, Optional, cast


class Host(object):
    TTL = 300.0

    def __init__(
        self, url: str, priority: Optional[int] = 0, accept: Optional[int] = None
    ) -> None:
        self.url = url
        self.priority = cast(int, priority)
        self.accept = (CallType.WRITE | CallType.READ) if accept is None else accept

        self.reset()

    def reset(self) -> None:
        self.last_use = 0.0
        self.retry_count = 0
        self.up = True


class HostsCollection(object):
    def __init__(self, hosts: List[Host]) -> None:
        self._hosts = hosts

        for host in self._hosts:
            host.reset()

        shuffle(self._hosts)

        self._hosts = sorted(self._hosts, key=lambda x: x.priority, reverse=True)

    def read(self) -> List[Host]:
        return [host for host in self._hosts if host.accept & CallType.READ]

    def write(self) -> List[Host]:
        return [host for host in self._hosts if host.accept & CallType.WRITE]


class CallType(object):
    READ = 1
    WRITE = 2
