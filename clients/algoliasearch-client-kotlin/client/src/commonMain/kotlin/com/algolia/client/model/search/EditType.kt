/** Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT. */
package com.algolia.client.model.search

import kotlinx.serialization.*

/**
 * Type of edit.
 */
@Serializable
public enum class EditType(public val value: kotlin.String) {

  @SerialName(value = "remove")
  Remove("remove"),

  @SerialName(value = "replace")
  Replace("replace");

  override fun toString(): kotlin.String = value
}