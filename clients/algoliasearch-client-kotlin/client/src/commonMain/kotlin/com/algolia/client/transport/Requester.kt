package com.algolia.client.transport

import io.ktor.util.reflect.*

/**
 * This interface represents a requester capable of executing network requests.
 *
 * Implementations should handle the actual process of making network calls and returning the
 * results based on the provided configuration and options.
 */
public interface Requester {

  /**
   * Executes a network request with the specified configuration and options, then returns the
   * result as the specified type.
   *
   * This is a suspending function, which means it can be used with coroutines for asynchronous
   * execution.
   *
   * @param T The type of the result expected from the request. This should match the returnType
   *   parameter.
   * @param requestConfig The configuration for the network request, including the URL, method,
   *   headers, and body.
   * @param requestOptions Optional settings for the request execution, such as timeouts or cache
   *   policies. Default value is null.
   * @param returnType A TypeInfo object representing the expected return type (T) of the request.
   */
  public suspend fun <T> execute(
    requestConfig: RequestConfig,
    requestOptions: RequestOptions? = null,
    returnType: TypeInfo,
  ): T
}
