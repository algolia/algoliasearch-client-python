#!/usr/bin/env python

from distutils.core import setup

setup(  name='algoliasearch',
        version='1.2.4',
        description='Algolia Search API Client for Python',
        url='https://github.com/algolia/algoliasearch-client-python',
        packages = ["algoliasearch"],
        install_requires = ['urllib3'],
        keywords = ['algolia', 'pyalgolia', 'search', 'backend', 'hosted', 'cloud', 'full-text search', 'faceted search'],
        classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
     )
