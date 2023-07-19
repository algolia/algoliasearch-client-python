/** Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT. */
package com.algolia.client.model.recommend

import kotlinx.serialization.*

@Serializable
public enum class RecommendModels(public val value: kotlin.String) {

  @SerialName(value = "related-products")
  RelatedProducts("related-products"),

  @SerialName(value = "bought-together")
  BoughtTogether("bought-together"),

  @SerialName(value = "trending-facets")
  TrendingFacets("trending-facets"),

  @SerialName(value = "trending-items")
  TrendingItems("trending-items");

  override fun toString(): kotlin.String = value
}
