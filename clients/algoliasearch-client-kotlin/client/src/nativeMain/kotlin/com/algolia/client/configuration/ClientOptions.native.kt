package com.algolia.client.configuration

import com.algolia.client.transport.Requester
import io.ktor.client.*
import io.ktor.client.engine.*
import io.ktor.client.plugins.logging.*
import kotlinx.serialization.json.JsonBuilder
import kotlin.time.Duration

public actual class ClientOptions actual constructor(
  public actual val connectTimeout: Duration,
  public actual val writeTimeout: Duration,
  public actual val readTimeout: Duration,
  public actual val logLevel: LogLevel,
  public actual val logger: Logger,
  public actual val hosts: List<Host>?,
  public actual val defaultHeaders: Map<String, String>?,
  public actual val engine: HttpClientEngine?,
  public actual val httpClientConfig: ((HttpClientConfig<*>) -> Unit)?,
  public actual val jsonConfig: ((JsonBuilder) -> Unit)?,
  public actual val requester: Requester?,
  public actual val algoliaAgentSegments: List<AgentSegment>
)
