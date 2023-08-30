package com.algolia;

import com.algolia.config.*;
import com.algolia.exceptions.AlgoliaRuntimeException;
import com.algolia.internal.HttpRequester;
import com.algolia.internal.JsonSerializer;
import com.algolia.internal.StatefulHost;
import com.algolia.internal.interceptors.AuthInterceptor;
import com.algolia.internal.interceptors.RetryStrategy;
import com.algolia.internal.interceptors.UserAgentInterceptor;
import com.fasterxml.jackson.core.type.TypeReference;
import java.io.Closeable;
import java.io.IOException;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.stream.Collectors;
import org.jetbrains.annotations.Nullable;

/**
 * Represents a base client for making API requests. The client uses a {@link Requester} for
 * executing requests and an {@link ExecutorService} for asynchronous operations. It is designed to
 * be extended by concrete API client implementations.
 */
public abstract class ApiClient implements Closeable {

  private final Requester requester;
  private final ExecutorService executor;

  /** Constructs a new instance of the {@link ApiClient}. */
  protected ApiClient(String appId, String apiKey, String clientName, @Nullable ClientOptions options, List<Host> defaultHosts) {
    if (appId == null || appId.isEmpty()) {
      throw new AlgoliaRuntimeException("`appId` is missing.");
    }
    if (apiKey == null || apiKey.isEmpty()) {
      throw new AlgoliaRuntimeException("`apiKey` is missing.");
    }
    final ClientOptions clientOptions = options != null ? options : new ClientOptions();
    this.executor = clientOptions.getExecutor();
    this.requester =
    clientOptions.getCustomRequester() != null
      ? clientOptions.getCustomRequester()
      : defaultRequester(appId, apiKey, clientName, clientOptions, defaultHosts);
  }

  /** Creates a default {@link Requester} for executing API requests. */
  private Requester defaultRequester(String appId, String apiKey, String clientName, ClientOptions options, List<Host> defaultHosts) {
    AlgoliaAgent algoliaAgent = new AlgoliaAgent(BuildConfig.VERSION)
      .addSegment(new AlgoliaAgent.Segment(clientName, BuildConfig.VERSION))
      .addSegments(options.getAlgoliaAgentSegments());

    List<Host> hosts = options.getHosts() != null && !options.getHosts().isEmpty() ? options.getHosts() : defaultHosts;
    List<StatefulHost> statefulHosts = hosts.stream().map(StatefulHost::new).collect(Collectors.toList());

    JsonSerializer serializer = JsonSerializer.builder().setCustomConfig(options.getMapperConfig()).build();
    HttpRequester.Builder builder = new HttpRequester.Builder(serializer)
      .addInterceptor(new AuthInterceptor(appId, apiKey))
      .addInterceptor(new UserAgentInterceptor(algoliaAgent))
      .addInterceptor(new RetryStrategy(statefulHosts));
    if (options.getRequesterConfig() != null) {
      options.getRequesterConfig().accept(builder);
    }
    return builder.build(options);
  }

  /**
   * Executes an HTTP request asynchronously and returns a {@link CompletableFuture} of the response
   * deserialized into a specified type.
   */
  protected <T> CompletableFuture<T> executeAsync(HttpRequest httpRequest, RequestOptions requestOptions, TypeReference<T> returnType) {
    return CompletableFuture.supplyAsync(() -> requester.execute(httpRequest, requestOptions, returnType), executor);
  }

  /**
   * Executes an HTTP request asynchronously and returns a {@link CompletableFuture} of the response
   * deserialized into a specified type.
   */
  protected <T> CompletableFuture<T> executeAsync(
    HttpRequest httpRequest,
    RequestOptions requestOptions,
    Class<?> returnType,
    Class<?> innerType
  ) {
    return CompletableFuture.supplyAsync(() -> requester.execute(httpRequest, requestOptions, returnType, innerType), executor);
  }

  @Override
  public void close() throws IOException {
    executor.shutdown();
    requester.close();
  }
}
