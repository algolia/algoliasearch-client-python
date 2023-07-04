#!/bin/bash

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null && pwd)/../.."

docker run -d -it --name api-clients-automation \
-v ~/.ssh:/root/.ssh:ro \
--mount type=bind,source=$ROOT/,target=/app api-clients-automation
