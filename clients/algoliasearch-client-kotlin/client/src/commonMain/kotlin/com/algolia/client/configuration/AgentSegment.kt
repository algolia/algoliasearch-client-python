package com.algolia.client.configuration

/**
 * Represents a segment of algolia agent header.
 *
 * @property value segment string value
 * @property version optional version
 */
public data class AgentSegment(val value: String, val version: String? = null)
