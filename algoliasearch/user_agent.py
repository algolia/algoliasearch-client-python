from platform import python_version

from algoliasearch.version import VERSION


class UserAgent(object):
    value = "Algolia for Python ({}); Python ({})".format(
        VERSION, str(python_version())
    )

    @staticmethod
    def get():
        # type: () -> str

        return UserAgent.value

    @staticmethod
    def add(segment, version):
        # type: (str, str) -> None

        UserAgent.value += "; {} ({})".format(segment, version)
