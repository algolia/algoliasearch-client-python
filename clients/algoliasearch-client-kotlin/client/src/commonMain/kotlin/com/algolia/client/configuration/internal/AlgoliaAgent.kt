package com.algolia.client.configuration.internal

import com.algolia.client.configuration.AgentSegment
import io.ktor.client.plugins.api.*

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

  fun AgentSegment.formatted(): String = buildString {
    append(value)
    version?.let { version ->
      append(" (")
      append(version)
      append(")")
    }
  }
}

/**
 * A plugin that adds Algolia agent to all requests.
 *
 * @property agent `X-Algolia-Agent` header value.
 */
internal fun algoliaAgent(agent: AlgoliaAgent) =
  createClientPlugin("AlgoliaAgent") {
    onRequest { request, _ ->
      request.url.parameters.apply {
        val parameter = "X-Algolia-Agent"
        val current = getAll(parameter) ?: listOf()
        val updated = listOf(agent.toString()) + current
        remove(parameter)
        append(parameter, updated.joinToString("; "))
      }
    }
  }
