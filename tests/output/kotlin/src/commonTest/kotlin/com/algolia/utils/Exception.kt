package com.algolia.utils

/**
 * Represents an exception thrown when an interceptor is executed.
 */
internal class InterceptionException : RuntimeException()

/**
 * Exception to be skipped
 */
internal class SkipException(message: String? = null) : RuntimeException(message)
