from platform import python_version
from sys import version_info
from typing import Optional

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

from algoliasearch import __version__


class UserAgent:
    def get(self) -> str:
        return self.value

    def add(self, segment: str, version: Optional[str] = __version__) -> Self:
        self.value += "; {} ({})".format(segment, version)
        return self

    def __init__(self) -> None:
        self.value = "Algolia for Python ({}); Python ({})".format(
            __version__, str(python_version())
        )
