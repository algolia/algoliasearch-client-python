package com.algolia.config;

public enum LogLevel {
  /** No logs. */
  NONE,

  /** Logs request and response lines and their respective headers. */
  HEADERS,

  /** Logs request and response lines and their respective headers and bodies (if present). */
  BODY,

  /** Logs request and response lines. */
  BASIC,
}
