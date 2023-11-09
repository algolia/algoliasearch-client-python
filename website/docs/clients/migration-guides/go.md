---
title: Go
---

### Methods targeting an `indexName`

Prior to the `initIndex` removal stated in the [common breaking changes](/docs/clients/migration-guides/#common-breaking-changes), all methods previously available at the `initIndex` level requires the `indexName` to be sent with the query.

That also mean you need to explicit the type you want to be returned from your queries, when it applies.

```go
import (
  "github.com/algolia/algoliasearch-client-go/v4/algolia/search"
)

indexName := "<INDEX_NAME>"
appID := "<APPLICATION_ID>"
apiKey := "<API_KEY>"

searchClient := search.NewClient(appID, apiKey)

results, err := searchClient.Search(
  searchClient.NewApiSearchRequest(
    search.NewSearchMethodParams(
      []search.SearchQuery{
        search.SearchForHitsAsSearchQuery(
          search.NewSearchForHits(
            indexName,
            search.WithSearchForHitsQuery("<YOUR_QUERY>"),
          ),
        ),
      },
    ),
  ),
)
```
