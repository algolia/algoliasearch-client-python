package com.algolia.playground

import com.algolia.client.api.QuerySuggestionsClient
import com.algolia.client.configuration.ClientOptions
import io.github.cdimascio.dotenv.Dotenv
import io.ktor.client.plugins.logging.*
import kotlin.system.exitProcess

suspend fun main() {

    val dotenv = Dotenv.configure().directory("../").load()

    val client = QuerySuggestionsClient(
        appId = dotenv["ALGOLIA_APPLICATION_ID"],
        apiKey = dotenv["ALGOLIA_ADMIN_KEY"],
        region = "us",
        options = ClientOptions(logLevel = LogLevel.BODY),
    )

    val configs = client.getAllConfigs()
    println(configs)

    exitProcess(0)
}