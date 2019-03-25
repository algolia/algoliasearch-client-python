#!/usr/bin/env bash

export TEST_TYPE=async
pip install 'asyncio>=3.4,<4.0' 'aiohttp>=2.0,<4.0' 'async_timeout>=2.0,<4.0'
stestr run --concurrency=20
