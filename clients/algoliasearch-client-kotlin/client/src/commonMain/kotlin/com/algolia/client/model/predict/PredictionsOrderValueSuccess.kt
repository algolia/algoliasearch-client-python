/** Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT. */
package com.algolia.client.model.predict

import kotlinx.serialization.*
import kotlinx.serialization.json.*

/**
 * Prediction for the **order_value** model.
 *
 * @param `value`
 * @param lastUpdatedAt
 */
@Serializable
public data class PredictionsOrderValueSuccess(

  @SerialName(value = "value") val `value`: Double,

  @SerialName(value = "lastUpdatedAt") val lastUpdatedAt: String,
) : PredictionsOrderValue