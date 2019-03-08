#!/usr/bin/env bash

export TEST_TYPE=async
pip install 'asyncio>=3.4,<4.0' 'aiohttp>=3.5,<4.0'
stestr run --concurrency=20
