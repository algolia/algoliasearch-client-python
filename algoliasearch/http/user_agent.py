from platform import python_version
from typing import Optional

from algoliasearch import __version__


class UserAgent:
    value = "Algolia for Python ({}); Python ({})".format(
        __version__, str(python_version())
    )

    def get() -> str:
        return UserAgent.value

    def add(segment: str, version: Optional[str] = __version__) -> None:
        UserAgent.value += "; {} ({})".format(segment, version)
