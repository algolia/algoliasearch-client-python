#!/usr/bin/env bash

export TEST_TYPE=async
pip install --user 'asyncio>=3.4,<4.0' 'aiohttp>=2.0,<4.0' 'async_timeout>=2.0,<4.0'
python -m unittest

