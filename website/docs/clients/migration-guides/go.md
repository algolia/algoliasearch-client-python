---
title: Go
---

### Methods targeting an `indexName`

Prior to the `initIndex` removal stated in the [common breaking changes](/docs/clients/migration-guides/#common-breaking-changes), all methods previously available at the `initIndex` level requires the `indexName` to be sent with the query.

That also mean you need to explicit the type you want to be returned from your queries, when it applies.

```go
// TBD
```
