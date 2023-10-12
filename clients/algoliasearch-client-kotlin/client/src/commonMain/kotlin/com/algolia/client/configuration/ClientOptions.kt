package com.algolia.client.configuration

import com.algolia.client.transport.Requester
import io.ktor.client.*
import io.ktor.client.engine.*
import io.ktor.client.plugins.logging.*
import kotlinx.serialization.json.JsonBuilder
import kotlin.time.Duration
import kotlin.time.Duration.Companion.seconds

public expect class ClientOptions(
  connectTimeout: Duration = 2.seconds,
  writeTimeout: Duration = 30.seconds,
  readTimeout: Duration = 5.seconds,
  logLevel: LogLevel = LogLevel.NONE,
  logger: Logger = Logger.DEFAULT,
  hosts: List<Host>? = null,
  defaultHeaders: Map<String, String>? = null,
  engine: HttpClientEngine? = null,
  httpClientConfig: ((HttpClientConfig<*>) -> Unit)? = null,
  jsonConfig: ((JsonBuilder) -> Unit)? = null,
  requester: Requester? = null,
  algoliaAgentSegments: List<AgentSegment> = emptyList()
) {

  /** Connect timeout for each request */
  public val connectTimeout: Duration

  /** The timeout for each request when performing write operations. */
  public val writeTimeout: Duration

  /** The timeout for each request when performing read operations. */
  public val readTimeout: Duration

  /** [LogLevel] to display in the console. */
  public val logLevel: LogLevel

  /** [Logger] to use for logs. */
  public val logger: Logger

  /** Custom list of hosts and back-up host used to perform a custom retry logic. */
  public val hosts: List<Host>?

  /** Optional default headers that should be applied to every request. */
  public val defaultHeaders: Map<String, String>?

  /** An optional [HttpClientEngine] to specify which HttpEngine should be used by Ktor. */
  public val engine: HttpClientEngine?

  /** An optional [HttpClientConfig] used by Ktor for advanced HttpClient configuration. */
  public val httpClientConfig: ((HttpClientConfig<*>) -> Unit)?

  /** An optional [JsonBuilder] configuration. */
  public val jsonConfig: ((JsonBuilder) -> Unit)?

  /** Custom Http Requester. */
  public val requester: Requester?

  /** List of Algolia agent segments */
  public val algoliaAgentSegments: List<AgentSegment>
}
