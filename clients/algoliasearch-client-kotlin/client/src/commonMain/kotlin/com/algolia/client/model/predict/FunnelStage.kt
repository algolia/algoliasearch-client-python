/** Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT. */
package com.algolia.client.model.predict

import kotlinx.serialization.*
import kotlinx.serialization.json.*

/**
 * FunnelStage
 *
 * @param name
 * @param probability
 */
@Serializable
public data class FunnelStage(

  @SerialName(value = "name") val name: String,

  @SerialName(value = "probability") val probability: Double,
)