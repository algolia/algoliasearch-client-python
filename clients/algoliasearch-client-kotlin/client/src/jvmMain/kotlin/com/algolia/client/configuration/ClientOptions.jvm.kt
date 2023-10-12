package com.algolia.client.configuration

import com.algolia.client.transport.Requester
import io.ktor.client.*
import io.ktor.client.engine.*
import io.ktor.client.plugins.logging.*
import kotlinx.serialization.json.JsonBuilder
import kotlin.time.Duration
import kotlin.time.Duration.Companion.seconds

public actual class ClientOptions(
  public actual val connectTimeout: Duration = 2.seconds,
  public actual val writeTimeout: Duration = 30.seconds,
  public actual val readTimeout: Duration = 5.seconds,
  public actual val logLevel: LogLevel = LogLevel.NONE,
  public actual val logger: Logger = Logger.DEFAULT,
  public actual val hosts: List<Host>? = null,
  public actual val defaultHeaders: Map<String, String>? = null,
  public actual val engine: HttpClientEngine? = null,
  public actual val httpClientConfig: ((HttpClientConfig<*>) -> Unit)? = null,
  public actual val jsonConfig: ((JsonBuilder) -> Unit)? = null,
  public actual val requester: Requester? = null,
  public actual val algoliaAgentSegments: List<AgentSegment> = emptyList(),
  public val compressionType: CompressionType,
) {

  public actual constructor(
    connectTimeout: Duration,
    writeTimeout: Duration,
    readTimeout: Duration,
    logLevel: LogLevel,
    logger: Logger,
    hosts: List<Host>?,
    defaultHeaders: Map<String, String>?,
    engine: HttpClientEngine?,
    httpClientConfig: ((HttpClientConfig<*>) -> Unit)?,
    jsonConfig: ((JsonBuilder) -> Unit)?,
    requester: Requester?,
    algoliaAgentSegments: List<AgentSegment>,
  ) : this(
    connectTimeout = connectTimeout,
    writeTimeout = writeTimeout,
    readTimeout = readTimeout,
    logLevel = logLevel,
    logger = logger,
    hosts = hosts,
    defaultHeaders = defaultHeaders,
    engine = engine,
    httpClientConfig = httpClientConfig,
    jsonConfig = jsonConfig,
    requester = requester,
    algoliaAgentSegments = algoliaAgentSegments,
    compressionType = CompressionType.NONE,
  )
}
