package com.algolia.utils

import kotlinx.serialization.json.JsonObject
import kotlinx.serialization.json.buildJsonObject

internal inline fun <reified T> empty(): T {
  return when (T::class) {
    String::class -> "" as T
    JsonObject::class -> buildJsonObject { } as T
    else -> throw SkipException("Can't create an empty instance of ${T::class}")
  }
}
