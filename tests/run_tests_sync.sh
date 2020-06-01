#!/usr/bin/env bash

export TEST_TYPE=sync
pip uninstall --user asyncio aiohttp async_timeout
stestr run --concurrency=20 -v
