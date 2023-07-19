/** Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT. */
package com.algolia.client.model.search

import kotlinx.serialization.*
import kotlinx.serialization.json.*

/**
 * UpdateApiKeyResponse
 *
 * @param key API key.
 * @param updatedAt Timestamp of the last update in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.
 */
@Serializable
public data class UpdateApiKeyResponse(

  /** API key. */
  @SerialName(value = "key") val key: String,

  /** Timestamp of the last update in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. */
  @SerialName(value = "updatedAt") val updatedAt: String,
)
