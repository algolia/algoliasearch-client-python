package com.algolia.playground

import com.algolia.client.api.RecommendClient
import com.algolia.client.configuration.ClientOptions
import com.algolia.client.model.recommend.GetRecommendationsParams
import com.algolia.client.model.recommend.RecommendationModels
import com.algolia.client.model.recommend.RecommendationRequest
import io.github.cdimascio.dotenv.Dotenv
import io.ktor.client.plugins.logging.*
import kotlin.system.exitProcess

suspend fun main() {

    val dotenv = Dotenv.configure().directory("../").load()

    val client = RecommendClient(
        appId = dotenv["ALGOLIA_APPLICATION_ID"],
        apiKey = dotenv["ALGOLIA_SEARCH_KEY"],
        options = ClientOptions(logLevel = LogLevel.BODY),
    )

    val searchIndex = dotenv["SEARCH_INDEX"]

    val recommendations = client.getRecommendations(
        getRecommendationsParams = GetRecommendationsParams(
            requests = listOf(
                RecommendationRequest(
                    indexName = searchIndex,
                    model = RecommendationModels.BoughtTogether,
                    objectID = "6445156",
                    threshold = 0,
                )
            )
        )
    )
    println(recommendations)

    exitProcess(0)
}
