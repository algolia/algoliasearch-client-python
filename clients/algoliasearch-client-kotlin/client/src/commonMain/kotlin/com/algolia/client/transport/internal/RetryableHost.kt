package com.algolia.client.transport.internal

import com.algolia.client.configuration.Host

/**
 * This internal data class represents a host that supports retrying requests.
 *
 * It wraps a Host object and provides additional information about the host's status, such as
 * whether it is up, when it was last updated, and how many times it has been retried.
 *
 * @property host The [Host] object that this RetryableHost is wrapping.
 */
internal data class RetryableHost(
  private val host: Host,
) {

  val url
    get() = host.url
  val callType
    get() = host.callType

  var isUp: Boolean = true
  var lastUpdated: Long = currentTimeMillis()
  var retryCount: Int = 0

  fun reset() {
    lastUpdated = currentTimeMillis()
    isUp = true
    retryCount = 0
  }

  fun hasTimedOut() {
    isUp = true
    lastUpdated = currentTimeMillis()
    retryCount += 1
  }

  fun hasFailed() {
    isUp = false
    lastUpdated = currentTimeMillis()
  }
}
