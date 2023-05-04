package com.algolia.client.configuration

/**
 * Indicate whether the HTTP call performed is of type [Read] (GET) or [Write] (POST, PUT ..). Used
 * to determined which timeout duration to use.
 */
public enum class CallType {
  Read,
  Write,
}
