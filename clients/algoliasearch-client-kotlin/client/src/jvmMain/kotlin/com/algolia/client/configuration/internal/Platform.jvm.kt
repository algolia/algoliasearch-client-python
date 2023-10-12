package com.algolia.client.configuration.internal

import com.algolia.client.configuration.AgentSegment
import com.algolia.client.configuration.ClientOptions
import com.algolia.client.configuration.CompressionType
import io.ktor.client.*

internal actual fun platformAgentSegment(): AgentSegment {
  return AgentSegment("JVM", System.getProperty("java.version"))
}

internal actual fun HttpClientConfig<*>.platformConfig(options: ClientOptions) {
  if (options.compressionType == CompressionType.GZIP) {
    install(GzipCompression)
  }
}
