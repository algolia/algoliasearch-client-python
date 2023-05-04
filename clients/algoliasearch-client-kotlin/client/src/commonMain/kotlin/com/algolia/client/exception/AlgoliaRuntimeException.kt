package com.algolia.client.exception

/**
 * Algolia runtime exception.
 *
 * @param message the detail message
 * @param cause the cause of the exception
 */
public sealed class AlgoliaRuntimeException(
  message: String? = null,
  cause: Throwable? = null,
) : RuntimeException(message, cause)

/**
 * Exception thrown when an error occurs during API requests.
 *
 * @param message the detail message
 * @param cause the cause of the exception
 */
public class AlgoliaClientException(
  message: String? = null,
  cause: Throwable? = null,
) : AlgoliaRuntimeException(message, cause)

/**
 * Exception thrown in case of API failure.
 *
 * @param message the detail message
 * @param cause the cause of the exception
 * @param httpErrorCode
 */
public class AlgoliaApiException(
  message: String? = null,
  cause: Throwable? = null,
  public val httpErrorCode: Int? = null,
) : AlgoliaRuntimeException(message, cause)

/**
 * Exception thrown when all hosts are unreachable. When several errors occurred, use the last one
 * as the cause for the returned exception.
 *
 * @param exceptions list of thrown exceptions
 */
public class AlgoliaRetryException(
  public val exceptions: List<Throwable>,
) : AlgoliaRuntimeException("Error(s) while processing the retry strategy", exceptions.last())

/**
 * Exception thrown when an error occurs during the wait strategy. For example: maximum number of
 * retry exceeded.
 *
 * @param message the detail message
 */
public class AlgoliaWaitException(
  message: String? = null,
) : AlgoliaRuntimeException(message)
