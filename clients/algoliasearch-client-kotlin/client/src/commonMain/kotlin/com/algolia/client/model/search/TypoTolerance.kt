/** Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT. */
package com.algolia.client.model.search

import com.algolia.client.exception.AlgoliaClientException
import com.algolia.client.extensions.internal.*
import kotlinx.serialization.*
import kotlinx.serialization.builtins.*
import kotlinx.serialization.descriptors.*
import kotlinx.serialization.encoding.*
import kotlinx.serialization.json.*

/**
 * Controls whether [typo tolerance](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/typo-tolerance/) is enabled and how it is applied.
 */
@Serializable(TypoToleranceSerializer::class)
public sealed interface TypoTolerance {

  public data class BooleanWrapper(val value: Boolean) : TypoTolerance

  public companion object {

    /**
     * TypoTolerance as Boolean
     *
     */
    public fun Boolean(
      value: Boolean,
    ): BooleanWrapper = BooleanWrapper(
      value = value,
    )

    /**
     * TypoToleranceEnum
     */
    public fun of(value: TypoToleranceEnum): TypoToleranceEnum = value
  }
}

internal class TypoToleranceSerializer : KSerializer<TypoTolerance> {

  override val descriptor: SerialDescriptor = buildClassSerialDescriptor("TypoTolerance")

  override fun serialize(encoder: Encoder, value: TypoTolerance) {
    when (value) {
      is TypoTolerance.BooleanWrapper -> Boolean.serializer().serialize(encoder, value.value)
      is TypoToleranceEnum -> TypoToleranceEnum.serializer().serialize(encoder, value)
    }
  }

  override fun deserialize(decoder: Decoder): TypoTolerance {
    val codec = decoder.asJsonDecoder()
    val tree = codec.decodeJsonElement()

    // deserialize Boolean
    if (tree is JsonPrimitive) {
      try {
        return codec.json.decodeFromJsonElement<TypoTolerance.BooleanWrapper>(tree)
      } catch (e: Exception) {
        // deserialization failed, continue
        println("Failed to deserialize Boolean (error: ${e.message})")
      }
    }

    // deserialize TypoToleranceEnum
    if (tree is JsonObject) {
      try {
        return codec.json.decodeFromJsonElement<TypoToleranceEnum>(tree)
      } catch (e: Exception) {
        // deserialization failed, continue
        println("Failed to deserialize TypoToleranceEnum (error: ${e.message})")
      }
    }

    throw AlgoliaClientException("Failed to deserialize json element: $tree")
  }
}
