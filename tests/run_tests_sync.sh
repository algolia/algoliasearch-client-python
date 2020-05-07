#!/usr/bin/env bash

export TEST_TYPE=sync
pip uninstall asyncio aiohttp async_timeout
python -m unittest --verbose
