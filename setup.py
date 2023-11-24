import sys

if sys.version_info < (3, 8):
    raise RuntimeError("algoliasearch 4.x requires Python 3.8+")
