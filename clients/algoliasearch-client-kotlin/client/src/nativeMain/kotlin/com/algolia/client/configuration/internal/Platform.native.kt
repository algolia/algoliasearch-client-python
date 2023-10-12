package com.algolia.client.configuration.internal

import com.algolia.client.configuration.AgentSegment
import com.algolia.client.configuration.ClientOptions
import io.ktor.client.*
import kotlin.experimental.ExperimentalNativeApi

internal actual fun platformAgentSegment(): AgentSegment {
  @OptIn(ExperimentalNativeApi::class)
  val os = "${Platform.osFamily.name} (${Platform.cpuArchitecture.name})"
  return AgentSegment(os)
}

internal actual fun HttpClientConfig<*>.platformConfig(options: ClientOptions) {
  // NO-OP
}
