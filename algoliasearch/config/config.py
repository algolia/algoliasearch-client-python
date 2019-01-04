import abc


class Config(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, app_id, api_key):
        # type: (str, str) -> None

        self.app_id = app_id
        self.api_key = api_key
        self.read_timeout = 5
        self.write_timeout = 5
        self.connect_timeout = 5

        self.hosts = self.build_hosts()

    @abc.abstractmethod
    def build_hosts(self):
        return
