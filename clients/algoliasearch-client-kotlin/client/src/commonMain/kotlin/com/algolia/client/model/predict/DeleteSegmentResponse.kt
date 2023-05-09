/** Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT. */
package com.algolia.client.model.predict

import kotlinx.serialization.*
import kotlinx.serialization.json.*

/**
 * DeleteSegmentResponse
 *
 * @param segmentID The ID of the segment.
 * @param deletedUntil The date and time at which the segment will be re-ingested.
 */
@Serializable
public data class DeleteSegmentResponse(

  /** The ID of the segment. */
  @SerialName(value = "segmentID") val segmentID: String,

  /** The date and time at which the segment will be re-ingested. */
  @SerialName(value = "deletedUntil") val deletedUntil: String,
)