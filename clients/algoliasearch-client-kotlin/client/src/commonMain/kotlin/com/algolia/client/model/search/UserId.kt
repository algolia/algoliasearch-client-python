/** Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT. */
package com.algolia.client.model.search

import kotlinx.serialization.*
import kotlinx.serialization.json.*

/**
 * Unique user ID.
 *
 * @param userID userID of the user.
 * @param clusterName Cluster to which the user is assigned.
 * @param nbRecords Number of records belonging to the user.
 * @param dataSize Data size used by the user.
 */
@Serializable
public data class UserId(

  /** userID of the user. */
  @SerialName(value = "userID") val userID: String,

  /** Cluster to which the user is assigned. */
  @SerialName(value = "clusterName") val clusterName: String,

  /** Number of records belonging to the user. */
  @SerialName(value = "nbRecords") val nbRecords: Int,

  /** Data size used by the user. */
  @SerialName(value = "dataSize") val dataSize: Int,
)
