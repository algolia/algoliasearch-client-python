import os


class Env(object):
    @staticmethod
    def is_community():
        # type: () -> bool

        return 'IS_COMMUNITY' in os.environ
