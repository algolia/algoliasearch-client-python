package com.algolia.utils

import com.algolia.client.api.ApiClient
import com.algolia.client.exception.AlgoliaClientException
import com.algolia.client.transport.internal.KtorRequester
import io.ktor.client.plugins.*
import io.ktor.client.request.*

/**
 * Executes the given [call] block with the specified [T] as its receiver.
 * The [intercept] block will be used to intercept the HTTP request made by the client.
 *
 * @receiver The [ApiClient] instance to be used as the receiver of the block.
 * @param T The type of [ApiClient] instance.
 * @param call A lambda function that will be executed with the [T] as its receiver.
 * @param intercept A lambda function that will be called with the intercepted [HttpRequestBuilder].
 */
suspend fun <T : ApiClient> T.runTest(
  call: suspend T.() -> Unit,
  intercept: (HttpRequestBuilder) -> Unit
) {
  intercept(intercept)
  try {
    call()
  } catch (e: AlgoliaClientException) {
    when (val cause = e.cause) {
      is AssertionError -> throw cause
      !is InterceptionException -> throw e
    }
  }
}

/**
 * Adds an echo interceptor to the given [ApiClient] instance.
 * The interceptor will call the provided [block] function with the intercepted request.
 * Note: Make sure to use a [KtorRequester]-based ApiClient before using this function.
 */
private fun ApiClient.intercept(block: (HttpRequestBuilder) -> Unit) {
  val ktorRequester = requester as? KtorRequester ?: error("`KtorRequester` requester is expected")
  ktorRequester.httpClient.plugin(HttpSend).intercept { request ->
    block(request)
    throw InterceptionException()
  }
}
