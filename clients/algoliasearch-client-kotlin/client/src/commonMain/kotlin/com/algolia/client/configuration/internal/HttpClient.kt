package com.algolia.client.configuration.internal

import com.algolia.client.configuration.ClientOptions
import io.ktor.client.*
import io.ktor.client.plugins.*
import io.ktor.client.plugins.contentnegotiation.*
import io.ktor.client.plugins.logging.*
import io.ktor.client.request.*
import io.ktor.serialization.kotlinx.json.*
import kotlinx.serialization.json.Json

private const val HEADER_APPLICATION_ID = "x-algolia-application-id"
private const val HEADER_APIKEY = "x-algolia-api-key"

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
  algoliaAgent: AlgoliaAgent,
) {
  // Custom configuration
  options.httpClientConfig?.invoke(this)

  // Content negotiation and serialization
  install(ContentNegotiation) {
    json(
      Json {
        options.jsonConfig?.invoke(this)
        isLenient = true
        ignoreUnknownKeys = true
        allowSpecialFloatingPointValues = true
        coerceInputValues = true
      },
    )
  }

  // Logging
  if (options.logLevel != LogLevel.NONE) {
    install(Logging) {
      level = options.logLevel
      logger = options.logger
    }
  }

  // Algolia user agent
  install(UserAgent) {
    agent = algoliaAgent.toString()
  }

  // Timeout
  install(HttpTimeout)

  // Defaults
  defaultRequest {
    if (!headers.contains(HEADER_APPLICATION_ID)) {
      header(HEADER_APPLICATION_ID, appId)
    }
    if (!headers.contains(HEADER_APIKEY)) {
      header(HEADER_APIKEY, apiKey)
    }
    options.defaultHeaders?.forEach { (key, value) -> header(key, value) }
  }

  // Enable default (2XX) validation
  expectSuccess = true

  // Platform specific configuration
  platformConfig(options)
}
