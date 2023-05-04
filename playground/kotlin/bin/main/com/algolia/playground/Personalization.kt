package com.algolia.playground

import com.algolia.client.api.PersonalizationClient
import com.algolia.client.configuration.ClientOptions
import io.github.cdimascio.dotenv.Dotenv
import io.ktor.client.plugins.logging.*
import kotlin.system.exitProcess

suspend fun main() {
    val dotenv = Dotenv.configure().directory("../").load()

    val client = PersonalizationClient(
        appId = dotenv["ALGOLIA_APPLICATION_ID"],
        apiKey = dotenv["ALGOLIA_RECOMMENDATION_KEY"],
        region = "us",
        options = ClientOptions(logLevel = LogLevel.BODY),
    )

    val response = client.getUserTokenProfile(userToken = "user1")
    println(response)

    exitProcess(0)
}
