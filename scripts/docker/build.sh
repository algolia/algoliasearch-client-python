#!/bin/bash

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null && pwd)/../.."

cd $ROOT

JAVA_VERSION=$(cat config/.java-version)
NODE_VERSION=$(cat .nvmrc)
PHP_VERSION=$(cat config/.php-version)
GO_VERSION=$(cat config/.go-version)

docker build \
  --build-arg JAVA_VERSION=$JAVA_VERSION \
  --build-arg NODE_VERSION=$NODE_VERSION \
  --build-arg PHP_VERSION=$PHP_VERSION \
  --build-arg GO_VERSION=$GO_VERSION \
  -t api-clients-automation .
