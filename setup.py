#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

path_readme = os.path.join(os.path.dirname(__file__), 'README.md')
try:
    import pypandoc
    README = pypandoc.convert(path_readme, 'rst')
except (IOError, ImportError):
    with open(path_readme) as readme:
        README = readme.read()

path_version = os.path.join(os.path.dirname(__file__), 'algoliasearch/version.py')
if sys.version_info[0] == 3:
    exec(open(path_version).read())
else:
    execfile(path_version)


setup(
    name = 'algoliasearch',
    version = VERSION,
    license = 'MIT License',
    packages = ['algoliasearch'],
    package_dir = {'algoliasearch': 'algoliasearch'},
    packages_data = {'algoliasearch': ['ressources/*.crt']},
    include_package_data = True,
    install_requires = ['urllib3 >= 1.8.2'],
    description = 'Algolia Search API Client for Python',
    long_description = README,
    author = 'Algolia Team',
    author_email = 'support@algolia.com',
    url = 'https://github.com/algolia/algoliasearch-client-python',
    keywords = ['algolia', 'pyalgolia', 'search', 'backend', 'hosted', 'cloud',
        'full-text search', 'faceted search'],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
