package com.algolia.playground

import com.algolia.client.api.SearchClient
import com.algolia.client.configuration.ClientOptions
import com.algolia.client.configuration.CompressionType
import com.algolia.client.model.search.SearchForHits
import com.algolia.client.model.search.SearchMethodParams
import com.algolia.client.model.search.SearchResponse
import io.github.cdimascio.dotenv.Dotenv
import io.ktor.client.plugins.logging.*
import kotlin.system.exitProcess

suspend fun main() {
    val dotenv = Dotenv.configure().directory("../").load()

    val client = SearchClient(
        appId = dotenv["ALGOLIA_APPLICATION_ID"],
        apiKey = dotenv["ALGOLIA_SEARCH_KEY"],
        options = ClientOptions(logLevel = LogLevel.HEADERS, compressionType = CompressionType.GZIP)
    )
    val indexName = dotenv["SEARCH_INDEX"]

    // search index
    val params = SearchMethodParams(
        requests = listOf(
            SearchForHits(
                indexName = indexName,
                query = "a",
            )
        )
    )
    val searchResponses = client.search(params)
    val result = searchResponses.results[0] as SearchResponse
    val hits = result.hits
    println(hits)

    exitProcess(0)
}
