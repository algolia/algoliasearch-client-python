---
title: Support a new language
---

:::info

Make sure to first [setup the repository tooling](/docs/contributing/setup-repository) to ease your journey!

You will also need to have the [openapi-generator](https://openapi-generator.tech/docs/installation/) installed.

:::

This repository leverages [openapi-generator](https://openapi-generator.tech/) to generate API clients.

## Find a template to start with

Provided templates should be a good starting point to generate a client but make sure to implement the [Algolia requirements](#algolia-requirements) to make it work properly.

You can pick a default template on the [openapi-generator's "generators" page](https://openapi-generator.tech/docs/generators)

### Extract the template locally

```bash
yarn docker:exec yarn openapi-generator-cli author template -g <templateName> -o templates/<languageName>
```

Example for the `JavaScript` client with the `typescript-node` template:

```bash
yarn docker:exec yarn openapi-generator-cli author template -g typescript-node -o templates/javascript/
```

## Update the generator config

Please read the [`add a new client guide`](/docs/contributing/add-new-api-client) for information on how to structure your new client and setup the configuration files.

### Algolia requirements

:::caution

**DX is key.**

**We require the generated API clients to have an up-to-date usage with their ecosystem, make sure to provide correct tooling to lint and format generated code.**

:::

### Strip code

The default generators includes **a lot** of features that won't be used with the Algolia engine:

- Multiple authentication methods: `appId`/`apiKey` are the only authentication methods, located in the requests headers.
- Built-in transporters: A [retry strategy](#retry-strategy) is required to target the DSNs of an `appId`, along with other transporter details listed below.
  - Regional clients are handled differently: [Different client hosts](#different-client-hosts)
- File support, payload format etc.: Requests only require `JSON` support to communicate with the engine.

### Init method

By default, OpenAPI will put the `AppId` and `ApiKey` in every method parameters, but the clients needs to be initialized with those values and put them in the header of every requests, with the right hosts.

The constructor of the client can be edited (from the `.mustache` files) to accept and store those values.

- [First implementation on the JavaScript client](https://github.com/algolia/api-clients-automation/pull/7)
- [Current implementation on the JavaScript client](https://github.com/algolia/api-clients-automation/blob/main/clients/algoliasearch-client-javascript/packages/client-search/src/searchClient.ts#L123)

### Retry strategy

The retry strategy cannot be generated and needs to be implemented outside of the generated client folder. You can achieve this by creating a `utils` (_or any naming that you find relevant_) folder and add a transporter and retry strategy logic to it.

- [First implementation on the JavaScript client](https://github.com/algolia/api-clients-automation/pull/9)
- [Current implementation on the PHP client](https://github.com/algolia/api-clients-automation/tree/main/clients/algoliasearch-client-php/lib/RetryStrategy)

### Different client hosts

Some Algolia clients (search and recommend) targets the default appId host (`${appId}-dsn.algolia.net`, `${appId}.algolia.net`, etc.), while clients like `personalization` have their own regional `host` (`eu` | `us` | `de`).

As the generator does not support reading `servers` in a spec file **yet**, hosts methods and variables are extracted with a custom script and create variables for you to use in the mustache templates, [read more here](/docs/contributing/add-new-api-client#generators).

### User Agent

The header 'User-Agent' must respect a strict pattern of a base, client, plus additional user defined segments:

```
base: `Algolia for <language> (<apiVersion>)`
client: `; <clientName> (<clientVersion>)`
segment: `; <Description> ([version])`
```

> The version is optional for segments.

The resulting User Agent is the concatenation of `base`, then `client` and all the `segments` in any order.

For example, if we have:

- base: `Algolia for Java (4.0.0)`
- client: `; Search (4.0.0)`
- segment:
  - `; JVM (11.0.14)`
  - `; experimental`
  - `; test (8.0.0-beta)`

Then the resulting User Agent is (the order is arbitrary):

```
Algolia for Java (4.0.0); JVM (11.0.14); Search (4.0.0); experimental ; test (8.0.0-beta)
```

You can take a look at the Java implementation [here](https://github.com/algolia/api-clients-automation/pull/347).

The `User-Agent` MUST match the following regular expression:

```regex
^Algolia for <LANGUAGE> \\(\\d+\\.\\d+\\.\\d+(-.*)?\\)(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*(; <CLIENT> (\\(\\d+\\.\\d+\\.\\d+(-.*)?\\)))(; [a-zA-Z. ]+ (\\(\\d+((\\.\\d+)?\\.\\d+)?(-.*)?\\))?)*$
```

The function MUST be named `addAlgoliaAgent` because of JavaScript exception that doesn't allow custom `User-Agent` in the header, and must use `x-algolia-agent` for JavaScript.

### Dependencies

You can use any dependency you want to create the client, it can be Json parser or HTTP client, but it's important to never expose those dependencies through the client, meaning:

- a function cannot return an object from a dependency
- a function cannot accept an object from a dependency as a parameter
- and so on

It matters because when a dependency is exposed, a breaking change from our deps can affect the user code while the API client is still working correctly (because they have to use the dependency in their code),
and that prevent us from upgrading our deps. In some languages it also requires the user to add our internal dependencies to his build system, which is very inconvenient and our clients should always be standalone.

To achieve this you can create interfaces that can be exposed, and wrap the method you want to be exposed, for an HTTP client for example.

### `useReadTransporter`

Some methods of our REST API send `POST` requests via the `read` transporter of the API client, to reflect this implementation, we provide a variable in the template for you to distinguish those methods, called `vendorExtensions.x-use-read-transporter`.

This option is provided [at the spec level](https://github.com/algolia/api-clients-automation/blob/main/specs/search/paths/search/search.yml#L5) and [used in the mustache files](https://github.com/algolia/api-clients-automation/blob/bf4271246f9282d3c11dd46918e74cb86d9c96dc/templates/javascript/api-single.mustache#L221-L223).

You can take a look at the implementation over all clients, [in this pull request](https://github.com/algolia/api-clients-automation/pull/525).

### `requestOptions`

Every methods of every clients provide a parameter that does not exist in the REST API, called `requestOptions`.

This parameter MUST be the last parameter of a method, and allow a user to override/merge additional `query parameters` or `headers` with the transporter ones.

### Requesters

The requester needs to be configurable and capable to be overwritten to use a user defined requester.
The default requester must be the classic HTTP requester, and it's possible to provide other alternatives like an [Echo Requester](https://github.com/algolia/api-clients-automation/blob/main/clients/algoliasearch-client-javascript/packages/client-common/src/createEchoRequester.ts) that just send the request back.

### Logger

> TODO: information

### Generated file banner

The banner SHOULD be added at the very top of every generated files, to avoid confusion for our users, but also redirect them to the `api-clients-automation` monorepo, where the contribution happens.

To do so, a `generationBanner` variable is available on every `mustache` templates, see [the initial implementation](https://github.com/algolia/api-clients-automation/pull/816) for more context.
