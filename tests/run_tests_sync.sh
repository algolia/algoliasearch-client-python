#!/usr/bin/env bash

export TEST_TYPE=sync
pip uninstall asyncio aiohttp
stestr run --concurrency=20
