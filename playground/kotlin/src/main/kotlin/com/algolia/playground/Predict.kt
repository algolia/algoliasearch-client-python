package com.algolia.playground

import com.algolia.client.api.PredictClient
import com.algolia.client.configuration.ClientOptions
import com.algolia.client.model.predict.*
import io.github.cdimascio.dotenv.Dotenv
import io.ktor.client.plugins.logging.*
import kotlin.system.exitProcess

suspend fun main() {
    val dotenv = Dotenv.configure().directory("../").load()

    val client = PredictClient(
        appId = dotenv["ALGOLIA_PREDICT_APP_ID"],
        apiKey = dotenv["ALGOLIA_PREDICT_KEY"],
        region = "us",
        options = ClientOptions(logLevel = LogLevel.BODY),
    )

    val updateSegment = client.updateSegment(
        segmentID = "segment1",
        updateSegmentParams = SegmentConditionsParam(
            conditions = SegmentParentConditions(
                operator = SegmentConditionOperator.values().first { it.value == "AND" },
                operands = listOf(
                    SegmentOperandAffinity(
                        name = "predictions.order_value",
                        filters = listOf(
                            SegmentAffinityFilter(
                                operator = SegmentFilterOperatorNumerical.values().first { it.value == "GT" },
                                value = SegmentAffinityFilterValue.Number(200.0),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
    println(updateSegment)

    //val userProfile = client.fetchUserProfile(
    //    userID = userId, params = AllParams(
    //        modelsToRetrieve = listOf(
    //            ModelsToRetrieve.FunnelStage,
    //            ModelsToRetrieve.OrderValue,
    //            ModelsToRetrieve.Affinities,
    //        ),
    //        typesToRetrieve = listOf(TypesToRetrieve.Properties, TypesToRetrieve.Segments),
    //    )
    //)
    //println(userProfile)

    exitProcess(0)
}
