#!/bin/bash

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null && pwd)/../.."

if ! test -f ".env"; then
    cp .env.example .env
fi

cd $ROOT

JAVA_VERSION=$(cat config/.java-version | awk -F '.' '{ print $1 }')
NODE_VERSION=$(cat .nvmrc)
PHP_VERSION=$(cat config/.php-version)
GO_VERSION=$(cat config/.go-version)
DART_VERSION=$(cat config/.dart-version)
PYTHON_VERSION=$(cat config/.python-version)

docker build \
  --build-arg JAVA_VERSION=$JAVA_VERSION \
  --build-arg NODE_VERSION=$NODE_VERSION \
  --build-arg PHP_VERSION=$PHP_VERSION \
  --build-arg GO_VERSION=$GO_VERSION \
  --build-arg DART_VERSION=$DART_VERSION \
  --build-arg PYTHON_VERSION=$PYTHON_VERSION \
  -t api-clients-automation .
