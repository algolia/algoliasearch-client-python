package com.algolia.playground

import com.algolia.client.api.AbtestingClient
import com.algolia.client.configuration.ClientOptions
import com.algolia.client.model.abtesting.AbTestsVariant
import com.algolia.client.model.abtesting.AddABTestsRequest
import io.github.cdimascio.dotenv.Dotenv
import io.ktor.client.plugins.logging.*

suspend fun main() {
    val dotenv = Dotenv.configure().directory("../").load()

    val client = AbtestingClient(
        appId = dotenv["ALGOLIA_APPLICATION_ID"],
        apiKey = dotenv["ALGOLIA_ANALYTICS_KEY"],
        region = "de",
        options = ClientOptions(logLevel = LogLevel.BODY)
    )

    val request = AddABTestsRequest(
        name = "testing",
        endAt = "2023-04-08T05:10:00Z",
        variants = listOf(
            AbTestsVariant(index = dotenv["ANALYTICS_INDEX"], trafficPercentage = 30),
            AbTestsVariant(index = dotenv["ANALYTICS_INDEX_B"], trafficPercentage = 70),
        )
    )
    val response = client.addABTests(request)
    println(response)
}
