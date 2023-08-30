<p align="center">
  <a href="https://www.algolia.com">
    <img alt="Algolia for Java" src="https://user-images.githubusercontent.com/22633119/59595532-4c6bd280-90f6-11e9-9d83-9afda3c85e96.png" >
  </a>

<h4 align="center">The perfect starting point to integrate <a href="https://algolia.com" target="_blank">Algolia</a> within your Java project</h4>

  <p align="center">
    <a href="https://search.maven.org/artifact/com.algolia/algoliasearch/"><img src="https://img.shields.io/maven-central/v/com.algolia/algoliasearch.svg" alt="CircleCI"></img></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="Licence"></img></a>
  </p>
</p>

<p align="center">
  <a href="https://www.algolia.com/doc/api-client/getting-started/install/java/" target="_blank">Documentation</a>  •
  <a href="https://discourse.algolia.com" target="_blank">Community Forum</a>  •
  <a href="http://stackoverflow.com/questions/tagged/algolia" target="_blank">Stack Overflow</a>  •
  <a href="https://github.com/algolia/algoliasearch-client-java/issues" target="_blank">Report a bug</a>  •
  <a href="https://www.algolia.com/doc/api-client/troubleshooting/faq/java/" target="_blank">FAQ</a>  •
  <a href="https://www.algolia.com/support" target="_blank">Support</a>
</p>

## ✨ Features

* Support Java 8 and above
* Asynchronous and synchronous methods to interact with Algolia's API
* Thread-safe clients
* Typed requests and responses

**Migration note from v2.x to v3.x**
>
> In June 2019, we released v3 of our Java client. If you are using version 2.x of the client, read the [migration guide to version 3.x](https://www.algolia.com/doc/api-client/getting-started/upgrade-guides/java/).
Version 2.x will **no longer** be under active development.

## 💡 Getting Started

### Install

* **Maven**: add the following to your `pom.xml` file:

    ```xml
    <dependency>
        <groupId>com.algolia</groupId>
        <artifactId>algoliasearch</artifactId>
        <version>LATEST</version>
    </dependency>
    ```
* **Gradle**: add the following to your `build.gradle` file:
  ```groovy
  implementation "com.algolia:algoliasearch:$version"
  ```

### Initialize the client

To start, you need to initialize the client. To do this, you need your **Application ID** and **API Key**.
You can find both on [your Algolia account](https://www.algolia.com/api-keys).

```java
SearchClient client = new SearchClient("MY_APPLICATION_ID", "MY_API_KEY");
```

If you need to customize the configuration of the client, use
`ClientOptions` when instantiating the Algolia `SearchClient` instance.

```java
ClientOptions options = ClientOptions.builder().setLogLevel(LogLevel.BODY).build();
SearchClient client = new SearchClient("MY_APPLICATION_ID", "MY_API_KEY", options);
```

### Push data

Without any prior configuration, you can start indexing contacts in the `contacts` index using the following code:

```java
class Contact {
  private String firstname;
  private String lastname;
  private int followers;
  private String company;
  private String objectID;
  // Getters/setters ommitted
}

Contact contact = new Contact()
        .setObjectID("one")
        .setFirstname("Jimmie")
        .setLastname("Barninger")
        .setFollowers(93)
        .setCompany("California Paint");

List<Contact> records = Arrays.asList(contact);
List<BatchRequest> batch = records.stream()
        .map(entry -> new BatchRequest().setAction(Action.ADD_OBJECT).setBody(entry))
        .toList();
BatchResponse response = client.batch("contacts", new BatchWriteParams().setRequests(batch));
```

### Search

You can now search for contacts by `firstname`, `lastname`, `company`, etc. (even with typos):

```java
SearchParams params = SearchParams.of(new SearchParamsObject().setQuery("jimmie"));

// Synchronous search
client.searchSingleIndex("contacts", params, Contact.class);

// Asynchronous search
client.searchSingleIndexAsync("contacts", params, Contact.class);
```

For full documentation, visit the [Algolia Java API Client's documentation](https://www.algolia.com/doc/api-client/getting-started/install/java/).

## 📝 Examples

You can find code samples in the [Algolia's API Clients playground](https://github.com/algolia/api-clients-playground/tree/master/java/src/main/java).

## ❓ Troubleshooting

Encountering an issue? Before reaching out to support, we recommend heading to our [FAQ](https://www.algolia.com/doc/api-client/troubleshooting/faq/java/) where you will find answers for the most common issues and gotchas with the client.

## Use the Dockerfile

If you want to contribute to this project without installing all its dependencies, you can use our Docker image. Please check our [dedicated guide](DOCKER_README.MD) to learn more.

## 📄 License
Algolia Java API Client is an open-sourced software licensed under the [MIT license](LICENSE).
