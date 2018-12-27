#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from io import open

from setuptools import setup


def read(f):
    return open(f, 'r', encoding='utf-8').read()


VERSION = None
path_version = os.path.join(os.path.dirname(__file__),
                            'algoliasearch/version.py')

exec(open(path_version).read())

setup(
    name='algoliasearch',
    version=VERSION,
    license='MIT',
    description='Algolia Search API Client for Python.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Algolia Team',
    author_email='support@algolia.com',
    packages=['algoliasearch'],
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.4",
    url='https://github.com/algolia/algoliasearch-client-python',
    keywords=['algolia', 'pyalgolia', 'search', 'backend', 'hosted', 'cloud',
              'full-text search', 'faceted search'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Development Status :: 5 - Production/Stable',
    ]
)
