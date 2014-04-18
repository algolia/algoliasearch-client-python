#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
import sys

if sys.version < '3':
    execfile(os.path.join('algoliasearch', 'version.py'))
else:
    exec(open("algoliasearch/version.py").read())

setup(  name='algoliasearch',
        version=VERSION,
        description='Algolia Search API Client for Python',
        url='https://github.com/algolia/algoliasearch-client-python',
        packages = ["algoliasearch"],
        install_requires = ['urllib3 >= 1.8.2'],
        keywords = ['algolia', 'pyalgolia', 'search', 'backend', 'hosted', 'cloud', 'full-text search', 'faceted search'],
        classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
     )
