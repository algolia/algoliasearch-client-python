from platform import python_version
from sys import version_info
from typing import Optional

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

from algoliasearch import __version__


class UserAgent:
    def __init__(self) -> None:
        self.value = "Algolia for Python ({}); Python ({})".format(
            __version__, str(python_version())
        )

    def get(self) -> str:
        return self.value

    def add(self, segment: str, version: Optional[str] = None) -> Self:
        self.value += "; {}".format(segment)

        if version is not None:
            self.value += " ({})".format(version)

        return self
