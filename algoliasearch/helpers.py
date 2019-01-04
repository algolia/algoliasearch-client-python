import sys


class Interpreter(object):
    @staticmethod
    def python3():
        return sys.version_info >= (3, 0)
