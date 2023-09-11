package com.algolia.config;

import java.time.Duration;
import java.util.Map;
import javax.annotation.Nonnull;

public interface ClientConfig {
  public @Nonnull LogLevel getLogLevel();

  public Logger getLogger();

  public @Nonnull Duration getConnectTimeout();

  public @Nonnull Duration getWriteTimeout();

  public @Nonnull Duration getReadTimeout();

  public @Nonnull Map<String, String> getDefaultHeaders();

  public @Nonnull CompressionType getCompressionType();
}
