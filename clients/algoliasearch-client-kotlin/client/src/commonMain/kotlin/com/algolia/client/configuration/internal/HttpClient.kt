package com.algolia.client.configuration.internal

import com.algolia.client.configuration.ClientOptions
import io.ktor.client.*
import io.ktor.client.plugins.*
import io.ktor.client.plugins.contentnegotiation.*
import io.ktor.client.plugins.logging.*
import io.ktor.client.request.*
import io.ktor.serialization.kotlinx.json.*
import kotlinx.serialization.json.Json

private const val HeaderApplicationID = "x-algolia-application-id"
private const val HeaderAPIKey = "x-algolia-api-key"

internal fun algoliaHttpClient(
  appId: String,
  apiKey: String,
  options: ClientOptions,
  agent: AlgoliaAgent,
) = httpClientOf(options) { configure(appId, apiKey, options, agent) }

private fun httpClientOf(options: ClientOptions, block: HttpClientConfig<*>.() -> Unit) =
  options.engine?.let { HttpClient(it, block) } ?: HttpClient(block)

internal fun HttpClientConfig<*>.configure(
  appId: String,
  apiKey: String,
  options: ClientOptions,
  agent: AlgoliaAgent,
) {
  // Custom configuration
  options.httpClientConfig?.invoke(this)

  // Content negotiation and serialization
  install(ContentNegotiation) {
    json(
      Json {
        isLenient = true
        ignoreUnknownKeys = true
        allowSpecialFloatingPointValues = true
        coerceInputValues = true
      },
    )
  }

  // Logging
  installLogging(options.logLevel, options.logger)

  // Algolia user agent
  install(algoliaAgent(agent))

  // Timeout
  install(HttpTimeout)

  // Defaults
  defaultRequest {
    if (!headers.contains(HeaderApplicationID)) header(HeaderApplicationID, appId)
    if (!headers.contains(HeaderAPIKey)) header(HeaderAPIKey, apiKey)
    options.defaultHeaders?.forEach { (key, value) -> header(key, value) }
  }

  // Enable default (2XX) validation
  expectSuccess = true
}

/** Installs [Logging] if logging level is superior to [LogLevel.NONE]. */
private fun HttpClientConfig<*>.installLogging(logLevel: LogLevel, customLogger: Logger) {
  if (LogLevel.NONE == logLevel) return
  install(Logging) {
    level = logLevel
    logger = customLogger
  }
}
