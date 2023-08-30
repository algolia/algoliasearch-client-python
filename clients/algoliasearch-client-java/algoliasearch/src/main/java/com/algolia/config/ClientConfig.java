package com.algolia.config;

import java.time.Duration;
import java.util.Map;
import org.jetbrains.annotations.NotNull;

public interface ClientConfig {
  public @NotNull LogLevel getLogLevel();

  public Logger getLogger();

  public @NotNull Duration getConnectTimeout();

  public @NotNull Duration getWriteTimeout();

  public @NotNull Duration getReadTimeout();

  public @NotNull Map<String, String> getDefaultHeaders();

  public @NotNull CompressionType getCompressionType();
}
