package com.algolia.internal;

import com.algolia.config.*;
import com.algolia.exceptions.AlgoliaApiException;
import com.algolia.exceptions.AlgoliaClientException;
import com.algolia.internal.interceptors.GzipRequestInterceptor;
import com.algolia.internal.interceptors.HeaderInterceptor;
import com.algolia.internal.interceptors.LogInterceptor;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.JavaType;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.function.Consumer;
import okhttp3.*;
import okhttp3.internal.http.HttpMethod;
import okio.BufferedSink;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

/**
 * HttpRequester is responsible for making HTTP requests using the OkHttp client. It provides a
 * mechanism for request serialization and deserialization using a given {@link JsonSerializer}.
 */
public final class HttpRequester implements Requester {

  private static final MediaType JSON_MEDIA_TYPE = MediaType.parse("application/json");
  private final OkHttpClient httpClient;
  private final JsonSerializer serializer;
  private final AtomicBoolean isClosed = new AtomicBoolean(false);

  /** Private constructor initialized using the builder pattern. */
  private HttpRequester(Builder builder, ClientConfig config) {
    OkHttpClient.Builder clientBuilder = new OkHttpClient.Builder()
      .connectTimeout(config.getConnectTimeout())
      .readTimeout(config.getReadTimeout())
      .writeTimeout(config.getWriteTimeout())
      .addInterceptor(new HeaderInterceptor(config.getDefaultHeaders()))
      .addNetworkInterceptor(new LogInterceptor(config.getLogger(), config.getLogLevel()));
    builder.interceptors.forEach(clientBuilder::addInterceptor);
    builder.networkInterceptors.forEach(clientBuilder::addNetworkInterceptor);
    if (config.getCompressionType() == CompressionType.GZIP) {
      clientBuilder.addInterceptor(new GzipRequestInterceptor());
    }
    if (builder.clientConfig != null) {
      builder.clientConfig.accept(clientBuilder);
    }
    this.httpClient = clientBuilder.build();
    this.serializer = builder.serializer;
  }

  @Override
  public <T> T execute(HttpRequest httpRequest, RequestOptions requestOptions, Class<?> returnType, Class<?> innerType) {
    return execute(httpRequest, requestOptions, serializer.getJavaType(returnType, innerType));
  }

  @Override
  public <T> T execute(HttpRequest httpRequest, RequestOptions requestOptions, TypeReference<?> returnType) {
    return execute(httpRequest, requestOptions, serializer.getJavaType(returnType));
  }

  /** Core method to execute an HTTP request and handle the response. */
  private <T> T execute(@NotNull HttpRequest httpRequest, RequestOptions requestOptions, JavaType returnType) {
    if (isClosed.get()) {
      throw new IllegalStateException("HttpRequester is closed");
    }

    // Create the request components.
    HttpUrl url = createHttpUrl(httpRequest, requestOptions);
    Headers headers = createHeaders(httpRequest, requestOptions);
    RequestBody requestBody = createRequestBody(httpRequest);

    // Build the HTTP request.
    Request request = new Request.Builder().url(url).headers(headers).method(httpRequest.getMethod(), requestBody).build();

    // Get or adjust the HTTP client according to request options.
    OkHttpClient client = getOkHttpClient(requestOptions);

    // Execute the request.
    Call call = client.newCall(request);
    try (Response response = call.execute()) {
      // Handle unsuccessful responses.
      if (!response.isSuccessful()) {
        throw new AlgoliaApiException(response.message(), response.code());
      }

      // Return null if there's no content or the return type isn't provided.
      if (returnType == null || response.body() == null || response.body().contentLength() == 0) {
        return null; // No need to deserialize, either no content or no type provided
      }

      // Deserialize and return the response.
      return serializer.deserialize(response.body().byteStream(), returnType);
    } catch (IOException exception) {
      throw new AlgoliaClientException(exception);
    }
  }

  /** Constructs the URL for the HTTP request. */
  @NotNull
  private static HttpUrl createHttpUrl(@NotNull HttpRequest request, RequestOptions requestOptions) {
    HttpUrl.Builder urlBuilder = new HttpUrl.Builder()
      .scheme("https")
      .host("algolia.com") // will be overridden by the retry strategy
      .encodedPath(request.getPath());
    request.getQueryParameters().forEach(urlBuilder::addQueryParameter);
    if (requestOptions != null) {
      requestOptions.getQueryParameters().forEach(urlBuilder::addQueryParameter);
    }
    return urlBuilder.build();
  }

  /** Creates a request body for the HTTP request. */
  private RequestBody createRequestBody(HttpRequest httpRequest) {
    String method = httpRequest.getMethod();
    Object body = httpRequest.getBody();
    if (!HttpMethod.permitsRequestBody(method) || (method.equals("DELETE") && body == null)) {
      return null;
    }
    if (body == null) {
      body = HttpMethod.requiresRequestBody(method) ? Collections.emptyMap() : "";
    }
    return buildRequestBody(body);
  }

  /** Serializes the request body into JSON format. */
  @NotNull
  private RequestBody buildRequestBody(Object requestBody) {
    return new RequestBody() {
      @Nullable
      @Override
      public MediaType contentType() {
        return JSON_MEDIA_TYPE;
      }

      @Override
      public void writeTo(@NotNull BufferedSink bufferedSink) {
        serializer.serialize(bufferedSink.outputStream(), requestBody);
      }
    };
  }

  /** Constructs the headers for the HTTP request. */
  @NotNull
  private Headers createHeaders(@NotNull HttpRequest request, RequestOptions requestOptions) {
    Headers.Builder builder = new Headers.Builder();
    request.getHeaders().forEach(builder::add);
    if (requestOptions != null) {
      requestOptions.getHeaders().forEach(builder::add);
    }
    return builder.build();
  }

  /** Returns a suitable OkHttpClient instance based on the provided request options. */
  @NotNull
  private OkHttpClient getOkHttpClient(RequestOptions requestOptions) {
    // Return the default client if no request options are provided.
    if (requestOptions == null) return httpClient;

    // Create a new client builder from the default client and adjust timeouts if provided.
    OkHttpClient.Builder builder = httpClient.newBuilder();
    if (requestOptions.getReadTimeout() != null) {
      builder.readTimeout(requestOptions.getReadTimeout());
    }
    if (requestOptions.getWriteTimeout() != null) {
      builder.writeTimeout(requestOptions.getWriteTimeout());
    }
    return builder.build();
  }

  @Override
  public void close() throws IOException {
    if (isClosed.get()) return;
    httpClient.dispatcher().executorService().shutdown();
    httpClient.connectionPool().evictAll();
    if (httpClient.cache() != null) {
      httpClient.cache().close();
    }
    isClosed.set(true);
  }

  /**
   * The Builder class for HttpRequester. It provides a mechanism for constructing an instance of
   * HttpRequester with customized configurations.
   */
  public static class Builder {

    private final List<Interceptor> interceptors = new ArrayList<>();

    private final List<Interceptor> networkInterceptors = new ArrayList<>();

    private Consumer<OkHttpClient.Builder> clientConfig;

    private final JsonSerializer serializer;

    public Builder(JsonSerializer serializer) {
      this.serializer = serializer;
    }

    /**
     * Adds an interceptor to the OkHttp client.
     *
     * @param interceptor The interceptor to be added.
     */
    public Builder addInterceptor(Interceptor interceptor) {
      interceptors.add(interceptor);
      return this;
    }

    /**
     * Adds a network interceptor to the OkHttp client.
     *
     * @param interceptor The network interceptor to be added.
     */
    public Builder addNetworkInterceptor(Interceptor interceptor) {
      networkInterceptors.add(interceptor);
      return this;
    }

    /** Sets the configuration for the OkHttp client. */
    public Builder setHttpClientConfig(Consumer<OkHttpClient.Builder> config) {
      this.clientConfig = config;
      return this;
    }

    /**
     * Builds and returns a HttpRequester instance.
     *
     * @param config The client configuration for the HttpRequester.
     */
    public HttpRequester build(ClientConfig config) {
      return new HttpRequester(this, config);
    }
  }
}
