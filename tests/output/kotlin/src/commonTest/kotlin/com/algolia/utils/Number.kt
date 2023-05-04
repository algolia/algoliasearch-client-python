package com.algolia.utils

/** Generic extension function to convert any Number to its corresponding type */
inline fun <reified T : Number> Number.toNumberType(): T {
  return when (T::class) {
    Long::class -> this.toLong()
    Double::class -> this.toDouble()
    Int::class -> this.toInt()
    Float::class -> this.toFloat()
    Short::class -> this.toShort()
    Byte::class -> this.toByte()
    else -> throw IllegalArgumentException("Unsupported number type")
  } as T
}
