package com.algolia.playground

import com.algolia.client.api.AnalyticsClient
import com.algolia.client.configuration.ClientOptions
import io.github.cdimascio.dotenv.Dotenv
import io.ktor.client.plugins.logging.*
import kotlin.system.exitProcess

suspend fun main() {
    val dotenv = Dotenv.configure().directory("../").load()
    val client = AnalyticsClient(
        appId = dotenv["ALGOLIA_APPLICATION_ID"],
        apiKey = dotenv["ALGOLIA_ANALYTICS_KEY"],
        options = ClientOptions(logLevel = LogLevel.BODY),
    )

    val index = dotenv["ANALYTICS_INDEX"]
    val topFilters = client.getTopFilterAttributes(index = index)
    println(topFilters)

    val topFilter = client.getTopFilterForAttribute(attribute = topFilters.attributes[0].attribute, index = index)
    println(topFilter)

    exitProcess(0)
}