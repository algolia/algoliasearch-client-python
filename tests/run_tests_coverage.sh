#!/usr/bin/env bash

coverage erase

# Runs non sync tests
export TEST_TYPE=snyc
pip uninstall asyncio aiohttp async_timeout
coverage run --source algoliasearch ./setup.py test

# Runs async tests
export TEST_TYPE=async
pip install --user 'asyncio>=3.4,<4.0' 'aiohttp>=2.0,<4.0' 'async_timeout>=2.0,<4.0'
coverage run -a --source algoliasearch ./setup.py test

# Tests coverage
coverage report --fail-under=99
