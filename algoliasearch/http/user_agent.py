from platform import python_version

from algoliasearch import __version__


class UserAgent:
    value = "Algolia for Python ({}); Python ({})".format(
        __version__, str(python_version())
    )

    def get() -> str:
        return UserAgent.value

    def add(segment: str, version: str) -> None:
        UserAgent.value += "; {} ({})".format(segment, version)
