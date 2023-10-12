package com.algolia.client.configuration.internal

import com.algolia.client.configuration.AgentSegment

/** Handles to handle algolia agent segments. */
internal class AlgoliaAgent(clientVersion: String) {

  private val segments =
    mutableSetOf(
      AgentSegment("Algolia for Kotlin", clientVersion),
    )

  fun add(segment: AgentSegment): Boolean {
    return segments.add(segment)
  }

  fun add(segments: List<AgentSegment>): Boolean {
    return this.segments.addAll(segments)
  }

  fun remove(segment: AgentSegment): Boolean {
    return segments.remove(segment)
  }

  override fun toString(): String {
    return segments.joinToString("; ") { it.formatted() }
  }

  private fun AgentSegment.formatted(): String = buildString {
    append(value)
    version?.let { version ->
      append(" (")
      append(version)
      append(")")
    }
  }
}
