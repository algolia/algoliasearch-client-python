package com.algolia.client.transport.internal

import com.algolia.client.BuildConfig
import com.algolia.client.configuration.AgentSegment
import com.algolia.client.configuration.ClientOptions
import com.algolia.client.configuration.Host
import com.algolia.client.configuration.internal.AlgoliaAgent
import com.algolia.client.configuration.internal.algoliaHttpClient
import com.algolia.client.configuration.internal.platformAgentSegment
import com.algolia.client.transport.RequestConfig
import com.algolia.client.transport.RequestOptions
import com.algolia.client.transport.Requester
import io.ktor.util.reflect.*

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
 */
internal suspend inline fun <reified T> Requester.execute(
  requestConfig: RequestConfig,
  requestOptions: RequestOptions? = null,
): T {
  return execute(requestConfig, requestOptions, typeInfo<T>())
}

/**
 * Creates a [Requester] instance.
 */
internal fun requesterOf(
  clientName: String,
  appId: String,
  apiKey: String,
  options: ClientOptions,
  defaultHosts: () -> List<Host>,
) = options.requester ?: KtorRequester(
  httpClient = algoliaHttpClient(
    appId = appId,
    apiKey = apiKey,
    options = options,
    agent = AlgoliaAgent(BuildConfig.version).apply {
      add(platformAgentSegment())
      add(AgentSegment(clientName, BuildConfig.version))
    },
  ),
  connectTimeout = options.connectTimeout,
  readTimeout = options.readTimeout,
  writeTimeout = options.writeTimeout,
  hosts = options.hosts ?: defaultHosts(),
)
