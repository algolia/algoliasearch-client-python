#!/usr/bin/env python

from distutils.core import setup

setup(  name='algoliasearch',
        version='1.1.3',
        description='Algolia Search API Client for Python',
        url='https://github.com/algolia/algoliasearch-client-python',
        packages = ["algoliasearch"],
        install_requires = ['urllib3'],
        keywords = ['algolia', 'pyalgolia', 'search', 'backend'],
        classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
     )
