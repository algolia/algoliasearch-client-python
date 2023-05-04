package com.algolia.client.transport

import io.ktor.util.reflect.*

/** Defines a config object for a given request. */
public data class RequestConfig(
  val method: RequestMethod,
  val path: List<String>,
  val isRead: Boolean = false,
  val headers: Map<String, Any> = emptyMap(),
  val query: Map<String, Any> = emptyMap(),
  val body: RequestBody? = null,
) {

  public constructor(
    method: RequestMethod,
    path: String,
    isRead: Boolean = false,
    headers: Map<String, Any> = emptyMap(),
    query: Map<String, Any> = emptyMap(),
    body: RequestBody? = null,
  ) : this(
    method = method,
    path = path.split("/").filter { it.isNotBlank() },
    isRead = isRead,
    headers = headers,
    query = query,
    body = body,
  )
}

/** Represents a request body with it type. */
public data class RequestBody(
  val body: Any? = null,
  val bodyType: TypeInfo,
)

/** Create a [RequestConfig] instance. */
public inline fun <reified T> RequestConfig(
  method: RequestMethod,
  path: String,
  isRead: Boolean = false,
  headers: Map<String, String> = emptyMap(),
  query: Map<String, Any> = emptyMap(),
  body: T?,
): RequestConfig = RequestConfig(
  method = method,
  path = path,
  isRead = isRead,
  headers = headers,
  query = query,
  body = body?.let { RequestBody(it, bodyType = typeInfo<T>()) },
)

/** Create a [RequestConfig] instance. */
public inline fun <reified T> RequestConfig(
  method: RequestMethod,
  path: List<String>,
  isRead: Boolean = false,
  headers: Map<String, String> = emptyMap(),
  query: Map<String, Any> = emptyMap(),
  body: T?,
): RequestConfig = RequestConfig(
  method = method,
  path = path,
  isRead = isRead,
  headers = headers,
  query = query,
  body = body?.let { RequestBody(it, bodyType = typeInfo<T>()) },
)
