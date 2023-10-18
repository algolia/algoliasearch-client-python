package com.algolia.client.extensions

import com.algolia.client.api.SearchClient
import com.algolia.client.exception.AlgoliaApiException
import com.algolia.client.extensions.internal.retryUntil
import com.algolia.client.model.search.ApiKey
import com.algolia.client.model.search.GetApiKeyResponse
import com.algolia.client.model.search.TaskStatus
import com.algolia.client.transport.RequestOptions
import kotlin.time.Duration

/**
 * Wait for a [taskID] to complete before executing the next line of code, to synchronize index
 * updates. All write operations in Algolia are asynchronous by design. It means that when you add
 * or update an object to your index, our servers will reply to your request with a [taskID] as soon
 * as they understood the write operation. The actual insert and indexing will be done after
 * replying to your code. You can wait for a task to complete by using the [taskID] and this method.
 *
 * @param indexName The index in which to perform the request.
 * @param taskID The ID of the task to wait for.
 * @param timeout If specified, the method will throw a
 *   [kotlinx.coroutines.TimeoutCancellationException] after the timeout value in milliseconds is
 *   elapsed.
 * @param maxRetries maximum number of retry attempts.
 * @param requestOptions additional request configuration.
 */
public suspend fun SearchClient.waitTask(
  indexName: String,
  taskID: Long,
  timeout: Duration? = null,
  maxRetries: Int? = null,
  requestOptions: RequestOptions? = null,
): TaskStatus {
  return retryUntil(
    timeout = timeout,
    maxRetries = maxRetries,
    retry = { getTask(indexName, taskID, requestOptions).status },
    until = { it == TaskStatus.Published },
  )
}

/**
 * Wait on an API key update operation.
 *
 * @param key The key that has been updated.
 * @param apiKey Necessary to know if an `update` operation has been processed, compare fields of
 *   the response with it.
 * @param timeout If specified, the method will throw a
 *   [kotlinx.coroutines.TimeoutCancellationException] after the timeout value in milliseconds is
 *   elapsed.
 * @param maxRetries Maximum number of retry attempts.
 * @param requestOptions Additional request configuration.
 */
public suspend fun SearchClient.waitKeyUpdate(
  key: String,
  apiKey: ApiKey,
  timeout: Duration? = null,
  maxRetries: Int? = null,
  requestOptions: RequestOptions? = null,
): GetApiKeyResponse {
  return retryUntil(
    timeout = timeout,
    maxRetries = maxRetries,
    retry = { getApiKey(key, requestOptions) },
    until = {
      apiKey ==
        ApiKey(
          acl = it.acl,
          description = it.description,
          indexes = it.indexes,
          maxHitsPerQuery = it.maxHitsPerQuery,
          maxQueriesPerIPPerHour = it.maxQueriesPerIPPerHour,
          queryParameters = it.queryParameters,
          referers = it.referers,
          validity = it.validity,
        )
    },
  )
}

/**
 * Wait on an API key creation operation.
 *
 * @param timeout If specified, the method will throw a
 *   [kotlinx.coroutines.TimeoutCancellationException] after the timeout value in milliseconds is
 *   elapsed.
 * @param maxRetries Maximum number of retry attempts.
 * @param requestOptions Additional request configuration.
 */
public suspend fun SearchClient.waitKeyCreation(
  key: String,
  maxRetries: Int? = null,
  timeout: Duration? = null,
  requestOptions: RequestOptions? = null,
): GetApiKeyResponse {
  return retryUntil(
    timeout = timeout,
    maxRetries = maxRetries,
    retry = {
      try {
        val response = getApiKey(key, requestOptions)
        Result.success(response)
      } catch (e: AlgoliaApiException) {
        Result.failure(e)
      }
    },
    until = { it.isSuccess },
  )
    .getOrThrow()
}

/**
 * Wait on a delete API ket operation.
 *
 * @param maxRetries Maximum number of retry attempts.
 * @param timeout If specified, the method will throw a
 *   [kotlinx.coroutines.TimeoutCancellationException] after the timeout value in milliseconds is
 *   elapsed.
 * @param requestOptions Additional request configuration.
 */
public suspend fun SearchClient.waitKeyDelete(
  key: String,
  maxRetries: Int? = null,
  timeout: Duration? = null,
  requestOptions: RequestOptions? = null,
): Boolean {
  retryUntil(
    timeout = timeout,
    maxRetries = maxRetries,
    retry = {
      try {
        val response = getApiKey(key, requestOptions)
        Result.success(response)
      } catch (e: AlgoliaApiException) {
        Result.failure(e)
      }
    },
    until = { result ->
      result.fold(
        onSuccess = { false },
        onFailure = { (it as AlgoliaApiException).httpErrorCode == 404 },
      )
    },
  )
  return true
}
