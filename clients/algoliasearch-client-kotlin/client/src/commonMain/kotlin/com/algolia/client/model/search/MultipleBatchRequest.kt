/** Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT. */
package com.algolia.client.model.search

import kotlinx.serialization.*
import kotlinx.serialization.json.*

/**
 * MultipleBatchRequest
 *
 * @param action
 * @param body Operation arguments (varies with specified `action`).
 * @param indexName Index to target for this operation.
 */
@Serializable
public data class MultipleBatchRequest(

  @SerialName(value = "action") val action: Action,

  /** Operation arguments (varies with specified `action`). */
  @SerialName(value = "body") val body: JsonObject,

  /** Index to target for this operation. */
  @SerialName(value = "indexName") val indexName: String,
)
