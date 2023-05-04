package com.algolia.client.extensions.internal

import com.algolia.client.exception.AlgoliaWaitException
import kotlinx.coroutines.delay
import kotlinx.coroutines.withTimeoutOrNull
import kotlin.math.min

/**
 * Retries the given [retry] function until the [until] condition is satisfied or the maximum number
 * of [maxRetries] or [timeout] is reached.
 *
 * @param retry The suspend function to be retried.
 * @param until The condition to be satisfied for the [retry] function to stop retrying.
 * @param maxRetries The maximum number of retries allowed. If null, it will default to 50 retries.
 * @param timeout The maximum time allowed for the retries in milliseconds. If null, no timeout is
 *   applied.
 * @param initialDelay The initial delay between retries in milliseconds (default: 200 ms).
 * @param maxDelay The maximum delay between retries in milliseconds (default: 5000 ms).
 */
internal suspend fun <T> retryUntil(
  retry: suspend () -> T,
  until: (T) -> Boolean,
  maxRetries: Int? = null,
  timeout: Long? = null,
  initialDelay: Long = 200L,
  maxDelay: Long = 5000L,
): T {
  suspend fun wait(): T {
    var currentDelay = initialDelay
    repeat(maxRetries ?: 50) {
      val result = retry()
      if (until(result)) return result
      delay(currentDelay)
      currentDelay = min(currentDelay * 2, maxDelay)
    }
    throw AlgoliaWaitException("The maximum number of retries ($maxRetries) exceeded")
  }

  return if (timeout != null) {
    withTimeoutOrNull(timeout) { wait() }
      ?: throw AlgoliaWaitException("Timeout of $timeout ms exceeded")
  } else {
    wait()
  }
}
