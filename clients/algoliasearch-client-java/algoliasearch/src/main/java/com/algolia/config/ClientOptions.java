package com.algolia.config;

import com.algolia.internal.HttpRequester;
import com.algolia.utils.ExecutorUtils;
import com.fasterxml.jackson.databind.json.JsonMapper;
import java.time.Duration;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.function.Consumer;
import org.jetbrains.annotations.NotNull;

public final class ClientOptions implements ClientConfig {

  public static Builder builder() {
    return new Builder();
  }

  private final List<AlgoliaAgent.Segment> algoliaAgentSegments;
  private final List<Host> hosts;
  private final LogLevel logLevel;
  private final Duration connectTimeout;
  private final Duration writeTimeout;
  private final Duration readTimeout;
  private final Map<String, String> defaultHeaders;
  private final CompressionType compressionType;
  private final Requester customRequester;
  private final Logger logger;
  private final Consumer<HttpRequester.Builder> requesterConfig;
  private final Consumer<JsonMapper.Builder> mapperConfig;

  private final ExecutorService executor;

  public ClientOptions() {
    this(new Builder());
  }

  ClientOptions(Builder builder) {
    this.algoliaAgentSegments = builder.algoliaAgentSegments;
    this.hosts = builder.hosts;
    this.customRequester = builder.customRequester;
    this.logLevel = builder.logLevel;
    this.connectTimeout = builder.connectTimeout;
    this.writeTimeout = builder.writeTimeout;
    this.readTimeout = builder.readTimeout;
    this.defaultHeaders = builder.defaultHeaders;
    this.compressionType = builder.compressionType;
    this.logger = builder.logger;
    this.requesterConfig = builder.requesterConfig;
    this.mapperConfig = builder.mapperConfig;
    this.executor = builder.executor != null ? builder.executor : ExecutorUtils.newThreadPool();
  }

  @NotNull
  public List<AlgoliaAgent.Segment> getAlgoliaAgentSegments() {
    return algoliaAgentSegments;
  }

  public List<Host> getHosts() {
    return hosts;
  }

  @NotNull
  public LogLevel getLogLevel() {
    return logLevel;
  }

  @NotNull
  public Duration getConnectTimeout() {
    return connectTimeout;
  }

  @NotNull
  public Duration getWriteTimeout() {
    return writeTimeout;
  }

  @NotNull
  public Duration getReadTimeout() {
    return readTimeout;
  }

  @NotNull
  public Map<String, String> getDefaultHeaders() {
    return defaultHeaders;
  }

  @NotNull
  public CompressionType getCompressionType() {
    return compressionType;
  }

  public Requester getCustomRequester() {
    return customRequester;
  }

  @NotNull
  public Logger getLogger() {
    return logger;
  }

  public Consumer<HttpRequester.Builder> getRequesterConfig() {
    return requesterConfig;
  }

  public Consumer<JsonMapper.Builder> getMapperConfig() {
    return mapperConfig;
  }

  public ExecutorService getExecutor() {
    return executor;
  }

  public static class Builder {

    public ExecutorService executor;
    private Requester customRequester;
    private List<Host> hosts;
    private Logger logger;
    private Consumer<HttpRequester.Builder> requesterConfig;
    private Consumer<JsonMapper.Builder> mapperConfig;
    private final List<AlgoliaAgent.Segment> algoliaAgentSegments = new ArrayList<>();
    private final Map<String, String> defaultHeaders = new HashMap<>();
    private LogLevel logLevel = LogLevel.NONE;
    private Duration connectTimeout = Duration.ofSeconds(2);
    private Duration writeTimeout = Duration.ofSeconds(30);
    private Duration readTimeout = Duration.ofSeconds(5);
    private CompressionType compressionType = CompressionType.NONE;

    public Builder setRequester(Requester requester) {
      this.customRequester = requester;
      return this;
    }

    public Builder addAlgoliaAgentSegment(AlgoliaAgent.Segment segment) {
      this.algoliaAgentSegments.add(segment);
      return this;
    }

    public Builder addAlgoliaAgentSegment(String value, String version) {
      AlgoliaAgent.Segment segment = new AlgoliaAgent.Segment(value, version);
      return addAlgoliaAgentSegment(segment);
    }

    public Builder addAlgoliaAgentSegment(String value) {
      AlgoliaAgent.Segment segment = new AlgoliaAgent.Segment(value);
      return addAlgoliaAgentSegment(segment);
    }

    public Builder addAlgoliaAgentSegments(List<AlgoliaAgent.Segment> segments) {
      this.algoliaAgentSegments.addAll(segments);
      return this;
    }

    public Builder addDefaultHeader(String header, String value) {
      this.defaultHeaders.put(header, value);
      return this;
    }

    public Builder setHosts(List<Host> hosts) {
      this.hosts = hosts;
      return this;
    }

    public Builder setLogLevel(LogLevel logLevel) {
      this.logLevel = logLevel;
      return this;
    }

    public Builder setConnectTimeout(Duration connectTimeout) {
      this.connectTimeout = connectTimeout;
      return this;
    }

    public Builder setWriteTimeout(Duration writeTimeout) {
      this.writeTimeout = writeTimeout;
      return this;
    }

    public Builder setReadTimeout(Duration readTimeout) {
      this.readTimeout = readTimeout;
      return this;
    }

    public Builder setCompressionType(CompressionType compressionType) {
      this.compressionType = compressionType;
      return this;
    }

    public Builder setCustomRequester(Requester customRequester) {
      this.customRequester = customRequester;
      return this;
    }

    public Builder setLogger(Logger logger) {
      this.logger = logger;
      return this;
    }

    public Builder setRequesterConfig(Consumer<HttpRequester.Builder> requesterConfig) {
      this.requesterConfig = requesterConfig;
      return this;
    }

    public Builder setMapperConfig(Consumer<JsonMapper.Builder> mapperConfig) {
      this.mapperConfig = mapperConfig;
      return this;
    }

    public Builder setExecutor(ExecutorService executor) {
      this.executor = executor;
      return this;
    }

    public ClientOptions build() {
      return new ClientOptions(this);
    }
  }
}
