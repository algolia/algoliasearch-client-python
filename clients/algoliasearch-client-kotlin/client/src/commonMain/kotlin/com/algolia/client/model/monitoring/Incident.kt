/** Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT. */
package com.algolia.client.model.monitoring

import kotlinx.serialization.*
import kotlinx.serialization.json.*

/**
 * Incident details.
 *
 * @param title Description of the incident.
 * @param status
 */
@Serializable
public data class Incident(

  /** Description of the incident. */
  @SerialName(value = "title") val title: String? = null,

  @SerialName(value = "status") val status: Status? = null,
)