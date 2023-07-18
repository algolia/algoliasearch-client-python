---
title: Release process
---

# Release process

## 1. Setup your `GITHUB_TOKEN`

You need a `GITHUB_TOKEN` in your [`.env`](https://github.com/algolia/api-clients-automation/blob/main/.env.example) file at the root of the repository. You can generate one from the [personal access token page](https://github.com/settings/tokens/new) with `Repo (Full control of private repositories)` scope.

```
GITHUB_TOKEN=<YOUR-PERSONAL-ACCESS-TOKEN>
```

Once setup, you can run:

```bash
# make sure to run `yarn docker:setup` first
yarn docker:release
```

It will create [a release PR](https://github.com/algolia/api-clients-automation/pull/545).

## 2. Review the release PR.

You need to review the release PR, in two parts:

1.  version changes
2.  CHANGELOGs

You need approval from a member of the [`@algolia/api-clients-automation`](https://github.com/orgs/algolia/teams/api-clients-automation) team to release clients.

## 3. The release process.

After a full CI run, a release commit will be sent to every repository and spread changes to their `next` branch.

Each language repository should have their own release process, and should run only when the latest commit starts with `chore: release`. By doing so, we have a way to just update the repository, for example READMEs, without having to release.

## Releasing manually

### Java

Java is released to [sonatype](https://oss.sonatype.org/) before being sent to [Maven](https://search.maven.org/artifact/com.algolia/algoliasearch-client-java) central repository, the `jar` need to be signed before publishing, and then verified on sonatype by using `closeAndRelease` target on Gradle.
All of this is handled in the [release action](https://github.com/algolia/algoliasearch-client-java-2/tree/next/.github/workflows/release.yml), executed on the [Java repository](https://github.com/algolia/algoliasearch-client-java-2).
If you want to release manually, you need to copy some secrets to either:

- `clients/algoliasearch-client-java-2/gradle.properties` /!\ make sure to remove them before committing !
- `~/.gradle/gradle.properties` which is safer because it's not committed and can stay on your computer.

The secrets are fetched from the vault, make sure you have access to `api-clients-squad`, and then read the value and place them in the `gradle.properties` file you want (don't copy this file verbatim):

```bash
signingInMemoryKey="$(vault read -field sub_private_key secret/algolia/api-clients-squad/maven-signing | awk 'NR == 1 { } 1' ORS='\\n')"
signingInMemoryKeyId=$(vault read -field subkey_id secret/algolia/api-clients-squad/maven-signing)
signingInMemoryKeyPassword=$(vault read -field password secret/algolia/api-clients-squad/maven-signing)

mavenCentralUsername=$(vault read -field user secret/algolia/api-clients-squad/sonatype)
mavenCentralPassword=$(vault read -field password secret/algolia/api-clients-squad/sonatype)
```

To release a snapshot, you need to add `-SNAPSHOT` to the `VERSION_NAME` in `clients/algoliasearch-client-java-2/gradle.properties`, then to release run:
` ./gradle/gradlew -p clients/algoliasearch-client-java-2 --no-parallel publish`

And if it's not a snapshot, run:
` ./gradle/gradlew -p clients/algoliasearch-client-java-2 closeAndReleaseRepository`

Once the package is published, it can be used in gradle file as:

```gradle
repositories {
    mavenCentral()
    maven { url = "https://oss.sonatype.org/content/repositories/snapshots/" }
}

dependencies {
    implementation 'com.algolia:algoliasearch-client-java:0.0.1-SNAPSHOT'
}
```

If it's not a snapshot, you can ignore the sonatype repository.

### JavaScript

1. [Get an NPM `publish` token](https://www.npmjs.com/settings/YOUR_USER_NAME/tokens) and put it in your `.env` file at the root of the repository
2. Go to `config/openapitools.json` and update every `packageVersion` and `utilsPackageVersion` fields for the `javascript-` generators
3. Run and build the JavaScript clients `yarn docker generate javascript && yarn docker build clients javascript`
4. Update the [JavaScript CTS package](https://github.com/algolia/api-clients-automation/blob/main/tests/output/javascript/package.json) and the [playground package]([JavaScript CTS package](https://github.com/algolia/api-clients-automation/blob/main/playground/javascript/node/package.json))
5. Go to each folder of the packages, at the `package.json` level (e.g. [this folder](https://github.com/algolia/api-clients-automation/tree/main/clients/algoliasearch-client-javascript/packages/algoliasearch/)) and run `npm publish --access public`
