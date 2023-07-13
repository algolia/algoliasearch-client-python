---
title: Setup repository
---

# Setup repository

:::info

Make sure to have Docker installed so you don't have to install the tooling for every API clients. [Installation guide](https://docs.docker.com/desktop/mac/install/)

:::

## Install the dependencies

```bash
nvm use && yarn
```

## Mounting the docker image

> You can also execute docker commands one by one, see [Docker commands](#docker)

```bash
yarn docker:setup
```

### Docker

#### Build

> Image is built from the [Dockerfile](https://github.com/algolia/api-clients-automation/blob/main/Dockerfile)

```bash
yarn docker:build
```

#### Mount

> Mount docker image on `api-clients-automation` container

```bash
yarn docker:mount
```

#### Clean

> Stops `api-clients-automation` container and clean the built image

```bash
yarn docker:clean
```

## Contribute

Once you've successfully built and mounted the Docker image, you can now play with the repository! Read our guides on:

- [How to add a new client](/docs/contributing/add-new-api-client)
- [How to add a new language](/docs/contributing/add-new-language)
- [Use CLI specs commands](/docs/contributing/CLI/specs-commands)
- [Use CLI clients commands](/docs/contributing/CLI/clients-commands)
- [Use CLI Common Test Suite commands](/docs/contributing/CLI/specs-commands)

## Troubleshooting

:::caution

You should run the commands via the [Docker container](#mounting-the-docker-image) to avoid issues.

:::

> `Error: The operation couldn't be completed. Unable to locate a Java Runtime.`

Java is not located in your PATH, either source the right `.bash_profile`, `.zshrc`, etc. file or do the following command in this repository:

```bash
echo 'export PATH="/usr/local/opt/openjdk/bin:$PATH"' > .bash_profile && source .bash_profile
```

### Running renovate locally

Running renovate on github can be tidious because it only works on the branch `main`, but you can run it locally with the CLI:
```sh
npm install -g renovate

LOG_LEVEL=debug renovate --dry-run --platform local
```
