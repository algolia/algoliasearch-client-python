---
title: Kotlin
---

### Methods targeting an `indexName`

Prior to the `initIndex` removal stated in the [common breaking changes](/docs/clients/migration-guides/#common-breaking-changes), all methods previously available at the `initIndex` level requires the `indexName` to be sent with the query.

That also mean you need to explicit the type you want to be returned from your queries, when it applies.

```kotlin
import com.algolia.client.api.SearchClient
import com.algolia.client.model.search.*

val client = SearchClient("<YOUR_APP_ID>", "<YOUR_API_KEY>")
val response = client.search(
    SearchMethodParams(
        requests = listOf(SearchForHits(indexName = "<YOUR_INDEX_NAME>", query = "<YOUR_QUERY>"))
    )
)
```
