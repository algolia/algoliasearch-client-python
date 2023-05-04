package com.algolia.client.extensions.internal

import kotlinx.serialization.SerializationException
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder
import kotlinx.serialization.json.JsonDecoder
import kotlinx.serialization.json.JsonEncoder
import kotlinx.serialization.json.JsonObject

/**
 * Casts the [Decoder] instance to a [JsonDecoder] if possible, otherwise throws a
 * [SerializationException].
 */
internal fun Decoder.asJsonDecoder() =
  this as? JsonDecoder
    ?: throw SerializationException("This class can be decoded only by Json format")

/** Decodes the current JSON element as a [JsonObject] using the [JsonDecoder] instance. */
internal fun JsonDecoder.decodeJsonObject() =
  decodeJsonElement() as? JsonObject ?: throw SerializationException("Expected JsonObject")

/**
 * Casts the [Encoder] instance to a [JsonEncoder] if possible, otherwise throws a
 * [SerializationException].
 */
internal fun Encoder.asJsonEncoder() =
  this as? JsonEncoder
    ?: throw SerializationException("This class can be encoded only by Json format")
