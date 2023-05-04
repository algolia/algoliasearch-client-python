package com.algolia.playground

import com.algolia.client.api.InsightsClient
import com.algolia.client.configuration.ClientOptions
import com.algolia.client.model.insights.EventType
import com.algolia.client.model.insights.InsightEvent
import com.algolia.client.model.insights.InsightEvents
import io.github.cdimascio.dotenv.Dotenv
import io.ktor.client.plugins.logging.*
import kotlin.system.exitProcess

suspend fun main() {
    val dotenv = Dotenv.configure().directory("../").load()

    val client = InsightsClient(
        appId = dotenv["ALGOLIA_APPLICATION_ID"],
        apiKey = dotenv["ALGOLIA_SEARCH_KEY"],
        options = ClientOptions(logLevel = LogLevel.BODY),
    )
    val indexName = dotenv["SEARCH_INDEX"]

    val events = InsightEvents(
        events = listOf(
            InsightEvent(
                eventType = EventType.Click,
                eventName = "click",
                index = indexName,
                userToken = "playground_user",
                objectIDs = listOf("6445156")
            )
        )
    )

    val response = client.pushEvents(events)
    println(response)

    exitProcess(0)
}
