package com.algolia.client.configuration.internal

import com.algolia.client.configuration.AgentSegment

internal actual fun platformAgentSegment(): AgentSegment {
  return AgentSegment("JVM", System.getProperty("java.version"))
}
