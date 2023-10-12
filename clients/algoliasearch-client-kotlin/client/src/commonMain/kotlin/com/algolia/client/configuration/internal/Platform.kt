package com.algolia.client.configuration.internal

import com.algolia.client.configuration.AgentSegment
import com.algolia.client.configuration.ClientOptions
import io.ktor.client.*

/**
 * Get platform specific algolia agent segment.
 */
internal expect fun platformAgentSegment(): AgentSegment

/**
 * Platform specific http client configuration
 */
internal expect fun HttpClientConfig<*>.platformConfig(options: ClientOptions)
