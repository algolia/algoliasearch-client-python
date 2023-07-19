---
title: Add a new API client
---

:::info

Make sure to first [setup the repository tooling](/docs/contributing/setup-repository) to ease your journey!

:::

Adding a new API client requires some manual steps in order to have a properly working client:

1. [Writing specs](#1-writing-specs)
2. [Configuring the generator](#2-configuring-the-generator)
3. [Generate the client](#3-generate-the-client)
4. [Adding tests](#4-adding-tests-with-the-common-test-suite)

## 1. Writing specs

We recommend to have a look at [existing spec files](https://github.com/algolia/api-clients-automation/blob/main/specs/).

> **The `bundled` folder is automatically generated, manual changes shouldn't be done in these files.**

### Guidelines

- **Endpoints**: Each file in [the `paths` folder](https://github.com/algolia/api-clients-automation/tree/main/specs/search/paths) should contain `operationId`s for a single endpoint, multiple methods are allowed.
- **File name**:
  - When the `path` file only contain one method (e.g. `GET`), we name the file after the `operationId`
  - When multiple methods are present (e.g. `PUT` and `DELETE`), we pick a more generic name that is related to the endpoint itself.
- **Description/Summary**: `operationId`s must have both description and summary.
- **Complex objects**: Complex objects (nested arrays, nested objects, `oneOf`, `allOf`, etc.) must be referenced (`$ref`) in the `operationId` file and not inlined. This is required to provide a accurate naming and improve readability.

### `common` spec folder

[The `common` folder](https://github.com/algolia/api-clients-automation/blob/main/specs/common/) hosts properties that are common to Algolia and/or used in multiple clients.

### `<clientName>` spec folder

> Example with the [search client spec](https://github.com/algolia/api-clients-automation/blob/main/specs/search/)

#### **`spec.yml` file**

The `spec.yml` file is the entry point of the client spec, it contains `servers`, `paths` and other specific information of the API. We recommend to copy an existing [`spec.yml` file](https://github.com/algolia/api-clients-automation/blob/main/specs/search/spec.yml) to get started.

#### **`<clientName>`/common folder**

Same as [the `common` folder](#common-spec-folder) but only related to the current client.

#### **`<clientName>`/paths folder**

Path definition of the paths defined in the [spec file](#specyml-file). See [guidelines](#guidelines).

### Troubleshooting

#### **Force the name of a `requestBody`**

> [Detailed issue](https://github.com/algolia/api-clients-automation/issues/891)

In some cases, you can encounter wrongly named `requestBody` from the specs, which could be due to:

- The type is too complex/too broad to be generated. (e.g. [An object with `additionalProperties`](https://github.com/algolia/api-clients-automation/tree/main/specs/search/paths/objects/partialUpdate.yml#L24-L33))
- The type is an alias of its model (e.g. [A list of `model`](https://github.com/algolia/api-clients-automation/tree/main/specs/search/paths/rules/saveRules.yml#L12-L20))

The [`x-codegen-request-body-name`](https://openapi-generator.tech/docs/swagger-codegen-migration/#body-parameter-name) property can be added at the root of the spec, to force the name of the generated `requestBody` property.

You can find an example of this implementation [on this PR](https://github.com/algolia/api-clients-automation/pull/896).

#### **Send additional options to the template**

You might want to send additional information to the generators. To do so, you can add parameters starting with an `x-` at the root level of your spec, which will be available in the `mustache` template under the `vendorExtensions` object.

[Example in the `search.yml` spec](https://github.com/algolia/api-clients-automation/blob/main/specs/search/paths/search/search.yml#L5-L7) and how it is used [in a mustache file](https://github.com/algolia/api-clients-automation/blob/bf4271246f9282d3c11dd46918e74cb86d9c96dc/templates/java/libraries/okhttp-gson/api.mustache#L196).

## 2. Configuring the generator

> The generator follows its own configuration file named `config/openapitools.json`

### Configs

[`config/openapitools.json`](https://github.com/algolia/api-clients-automation/blob/main/config/openapitools.json) and [`config/clients.config.json`](https://github.com/algolia/api-clients-automation/blob/main/config/clients.config.json) hosts the configuration of all of the generated clients with their available languages and extra information.

#### Settings

Generators are referenced by key with the following pattern `<languageName>-<clientName>`. You can copy an existing object of a client and replace the `<clientName>` value with the one you'd like to generate.

Below are the options you need to **make sure to define for your client**, other options are automatically added by our generator.

| Option                |         File          |        Language         | Description                                                                                                          |
| --------------------- | :-------------------: | :---------------------: | -------------------------------------------------------------------------------------------------------------------- |
| `output`              |  `openapitools.json`  |           All           | The output path of the client.                                                                                       |
| `packageVersion`      | `clients.config.json` |           All           | The version you'd like to publish the first iteration of the generated client. It will be automatically incremented. |
| `gitRepoId`           | `clients.config.json` |           All           | The name of the repository.                                                                                          |
| `folder`              | `clients.config.json` |           All           | The path to the folder that will host the generated code.                                                            |
| `modelFolder`         | `clients.config.json` |           All           | The path to the `model` folder that will host the generated code.                                                    |
| `apiFolder`           | `clients.config.json` |           All           | The path to the `api` folder that will host the generated code.                                                      |
| `customGenerator`     | `clients.config.json` |           All           | The name of the generator used to generate code.                                                                     |

## 3. Generate the client

You can find all the commands in the [CLI > clients commands page](/docs/contributing/CLI/clients-commands) and [CLI > specs commands page](/docs/contributing/CLI/specs-commands).

## 4. Adding tests with the Common Test Suite

Clients needs to be tested, you can read more in the [Common Test Suite](/docs/contributing/testing/common-test-suite) guide.
