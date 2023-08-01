package com.algolia.utils;

import okhttp3.logging.HttpLoggingInterceptor.Level;

public enum LogLevel {
  /** No logs. */
  NONE(Level.NONE),

  /** Logs request and response lines and their respective headers. */
  HEADERS(Level.HEADERS),

  /** Logs request and response lines and their respective headers and bodies (if present). */
  BODY(Level.BODY),

  /** Logs request and response lines. */
  BASIC(Level.BASIC);

  private Level value;

  private LogLevel(Level value) {
    this.value = value;
  }

  public Level value() {
    return this.value;
  }
}
