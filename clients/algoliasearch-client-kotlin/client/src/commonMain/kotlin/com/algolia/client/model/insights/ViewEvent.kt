/** Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT. */
package com.algolia.client.model.insights

import kotlinx.serialization.*

@Serializable
public enum class ViewEvent(public val value: kotlin.String) {

  @SerialName(value = "view")
  View("view");

  override fun toString(): kotlin.String = value
}