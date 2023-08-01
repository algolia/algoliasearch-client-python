package com.algolia;

import com.algolia.exceptions.*;
import com.algolia.utils.*;
import com.algolia.utils.retry.StatefulHost;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.JavaType;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.*;
import java.util.Map.Entry;
import java.util.concurrent.CompletableFuture;
import okhttp3.*;
import okhttp3.internal.http.HttpMethod;

public abstract class ApiClient {

  private boolean debugging = false;
  private Map<String, String> defaultHeaderMap = new HashMap<String, String>();
  private AlgoliaAgent algoliaAgent;

  private String contentType;

  private Requester requester;
  protected ObjectMapper json;

  public ApiClient(String appId, String apiKey, String clientName, String version, ClientOptions options) {
    if (appId == null || appId.length() == 0) {
      throw new AlgoliaRuntimeException("`appId` is missing.");
    }
    if (apiKey == null || apiKey.length() == 0) {
      throw new AlgoliaRuntimeException("`apiKey` is missing.");
    }

    this.contentType = "application/json";

    this.algoliaAgent = new AlgoliaAgent(version);
    this.algoliaAgent.addSegment(new AlgoliaAgent.Segment(clientName, version));
    if (options != null && options.getAlgoliaAgentSegments() != null) {
      for (AlgoliaAgent.Segment segment : options.getAlgoliaAgentSegments()) {
        this.algoliaAgent.addSegment(segment);
      }
    }
    refreshUserAgent();

    addDefaultHeader("X-Algolia-Application-Id", appId);
    addDefaultHeader("X-Algolia-API-Key", apiKey);
    addDefaultHeader("Accept", this.contentType);
    addDefaultHeader("Content-Type", this.contentType);

    if (options != null && options.getRequester() != null) {
      this.requester = options.getRequester();
    } else {
      this.requester = new HttpRequester();
    }

    this.json = new JSONBuilder().build();
  }

  private void refreshUserAgent() {
    addDefaultHeader("User-Agent", this.algoliaAgent.toString());
  }

  /**
   * Add a custom user agent segment
   *
   * @param segment Algolia Agent Segment
   * @return ApiClient
   */
  public ApiClient addAlgoliaAgent(AlgoliaAgent.Segment segment) {
    algoliaAgent.addSegment(segment);
    refreshUserAgent();
    return this;
  }

  /**
   * Remove a user agent segment
   *
   * @param segment Algolia Agent Segment
   * @return ApiClient
   */
  public ApiClient removeAlgoliaAgent(AlgoliaAgent.Segment segment) {
    algoliaAgent.removeSegment(segment);
    refreshUserAgent();
    return this;
  }

  /**
   * Add a default header.
   *
   * @param key The header's key
   * @param value The header's value
   * @return ApiClient
   */
  public ApiClient addDefaultHeader(String key, String value) {
    defaultHeaderMap.put(key, value);
    return this;
  }

  /**
   * Check that whether debugging is enabled for this API client.
   *
   * @return True if debugging is enabled, false otherwise.
   */
  public boolean isDebugging() {
    return debugging;
  }

  /**
   * Set the log level of the requester
   *
   * @return ApiClient
   */
  public ApiClient setLogLevel(LogLevel level) {
    requester.setLogLevel(level);
    return this;
  }

  /**
   * Get connection timeout (in milliseconds).
   *
   * @return Timeout in milliseconds
   */
  public int getConnectTimeout() {
    return requester.getConnectTimeout();
  }

  /**
   * Sets the connect timeout (in milliseconds). A value of 0 means no timeout, otherwise values
   * must be between 1 and {@link Integer#MAX_VALUE}.
   *
   * @param connectionTimeout connection timeout in milliseconds
   * @return Api client
   */
  public ApiClient setConnectTimeout(int connectionTimeout) {
    requester.setConnectTimeout(connectionTimeout);
    return this;
  }

  /**
   * Get read timeout (in milliseconds).
   *
   * @return Timeout in milliseconds
   */
  public int getReadTimeout() {
    return requester.getReadTimeout();
  }

  /**
   * Sets the read timeout (in milliseconds). A value of 0 means no timeout, otherwise values must
   * be between 1 and {@link Integer#MAX_VALUE}.
   *
   * @param readTimeout read timeout in milliseconds
   * @return Api client
   */
  public ApiClient setReadTimeout(int readTimeout) {
    requester.setReadTimeout(readTimeout);
    return this;
  }

  /**
   * Get write timeout (in milliseconds).
   *
   * @return Timeout in milliseconds
   */
  public int getWriteTimeout() {
    return requester.getWriteTimeout();
  }

  /**
   * Sets the write timeout (in milliseconds). A value of 0 means no timeout, otherwise values must
   * be between 1 and {@link Integer#MAX_VALUE}.
   *
   * @param writeTimeout connection timeout in milliseconds
   * @return Api client
   */
  public ApiClient setWriteTimeout(int writeTimeout) {
    requester.setWriteTimeout(writeTimeout);
    return this;
  }

  public ApiClient setHosts(List<StatefulHost> hosts) {
    this.requester.setHosts(hosts);
    return this;
  }

  /**
   * Format the given parameter object into string.
   *
   * @param param Parameter
   * @return String representation of the parameter
   */
  public String parameterToString(Object param) throws UnsupportedOperationException {
    if (param == null) {
      return "";
    } else if (param instanceof Date || param instanceof OffsetDateTime || param instanceof LocalDate) {
      // note: date comes as string for now, we should never have to serialize one
      // maybe we could accept them as Date object and in that case use jackson serialization
      throw new UnsupportedOperationException("Date must come as string (already serialized)");
    } else if (param instanceof Collection) {
      StringJoiner b = new StringJoiner(",");
      for (Object o : (Collection) param) {
        b.add(String.valueOf(o));
      }
      return b.toString();
    } else {
      return String.valueOf(param);
    }
  }

  /**
   * Escape the given string to be used as URL query value.
   *
   * @param str String to be escaped
   * @return Escaped string
   */
  public String escapeString(String str) {
    try {
      return URLEncoder.encode(str, "utf8").replaceAll("\\+", "%20");
    } catch (UnsupportedEncodingException e) {
      return str;
    }
  }

  /**
   * Serialize the given Java object into request body according to the object's class and the
   * request Content-Type.
   *
   * @param obj The Java object
   * @return The serialized request body
   * @throws AlgoliaRuntimeException If fail to serialize the given object
   */
  public RequestBody serialize(Object obj) throws AlgoliaRuntimeException {
    String content;

    if (obj != null) {
      try {
        if (obj.getClass().getName().equals("java.lang.Object")) {
          content = "{}";
        } else {
          content = json.writeValueAsString(obj);
        }
      } catch (JsonProcessingException e) {
        throw new AlgoliaRuntimeException(e);
      }
    } else {
      // We can't send a null body with okhttp, so we default it to an empty string
      content = "";
    }

    return RequestBody.create(content, MediaType.parse(this.contentType));
  }

  /**
   * Execute HTTP call asynchronously.
   *
   * @param <T> Type
   * @param returnType Return type
   * @see #execute(Call, TypeReference)
   */
  public <T> CompletableFuture<T> executeAsync(Call call, final JavaType returnType) {
    final CompletableFuture<T> future = new CompletableFuture<>();
    call.enqueue(
      new Callback() {
        @Override
        public void onFailure(Call call, IOException e) {
          future.completeExceptionally(e.getCause());
        }

        @Override
        public void onResponse(Call call, Response response) throws IOException {
          try {
            T result = requester.handleResponse(response, returnType);
            future.complete(result);
          } catch (AlgoliaRuntimeException e) {
            future.completeExceptionally(e);
          } catch (Exception e) {
            future.completeExceptionally(new AlgoliaRuntimeException(e));
          }
        }
      }
    );
    return future;
  }

  public <T> CompletableFuture<T> executeAsync(Call call, final Class<?> returnType, final Class<?> innerType) {
    return executeAsync(call, json.getTypeFactory().constructParametricType(returnType, innerType));
  }

  public <T> CompletableFuture<T> executeAsync(Call call, final TypeReference returnType) {
    return executeAsync(call, json.getTypeFactory().constructType(returnType));
  }

  /**
   * Build HTTP call with the given options.
   *
   * @param path The sub-path of the HTTP URL
   * @param method The request method, one of "GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH" and
   *     "DELETE"
   * @param queryParameters The query parameters
   * @param body The request body object
   * @param headerParams The header parameters
   * @param requestOptions The requestOptions to send along with the query, they will be merged with
   *     the transporter requestOptions.
   * @param useReadTransporter Some POST methods in the Algolia REST API uses the `read`
   *     transporter. This information is defined at the spec level.
   * @return The HTTP call
   * @throws AlgoliaRuntimeException If fail to serialize the request body object
   */
  public Call buildCall(
    String path,
    String method,
    Map<String, Object> queryParameters,
    Object body,
    Map<String, String> headerParams,
    RequestOptions requestOptions,
    Boolean useReadTransporter
  ) throws AlgoliaRuntimeException {
    Request request = buildRequest(path, method, queryParameters, body, headerParams, requestOptions, useReadTransporter);

    return requester.newCall(request);
  }

  /**
   * Build an HTTP request with the given options.
   *
   * @param path The sub-path of the HTTP URL
   * @param method The request method, one of "GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH" and
   *     "DELETE"
   * @param queryParameters The query parameters
   * @param body The request body object
   * @param headerParams The header parameters
   * @param requestOptions The requestOptions to send along with the query, they will be merged with
   *     the transporter requestOptions.
   * @param useReadTransporter Some POST methods in the Algolia REST API uses the `read`
   *     transporter. This information is defined at the spec level.
   * @return The HTTP request
   * @throws AlgoliaRuntimeException If fail to serialize the request body object
   */
  public Request buildRequest(
    String path,
    String method,
    Map<String, Object> queryParameters,
    Object body,
    Map<String, String> headerParams,
    RequestOptions requestOptions,
    Boolean useReadTransporter
  ) throws AlgoliaRuntimeException {
    boolean hasRequestOptions = requestOptions != null;
    final String url = buildUrl(path, queryParameters, hasRequestOptions ? requestOptions.getExtraQueryParameters() : null);
    final Request.Builder reqBuilder = new Request.Builder().url(url);
    processHeaderParams(headerParams, hasRequestOptions ? requestOptions.getExtraHeaders() : null, reqBuilder);

    RequestBody reqBody;
    // We rely on `permitsRequestBody` to tell us if we should provide a body
    // but also set it for DELETE methods
    if (!HttpMethod.permitsRequestBody(method) || (method.equals("DELETE") && body == null)) {
      reqBody = null;
    } else {
      reqBody = serialize(body);
    }

    if (useReadTransporter) {
      reqBuilder.tag(new UseReadTransporter());
    }

    return reqBuilder.method(method, reqBody).build();
  }

  /**
   * Build full URL by concatenating base path, the given sub path and query parameters.
   *
   * @param path The sub path
   * @param queryParameters The query parameters
   * @param extraQueryParameters The query parameters, coming from the requestOptions
   * @return The full URL
   */
  public String buildUrl(String path, Map<String, Object> queryParameters, Map<String, Object> extraQueryParameters) {
    if (extraQueryParameters != null) {
      for (Entry<String, Object> param : extraQueryParameters.entrySet()) {
        queryParameters.put(param.getKey(), param.getValue());
      }
    }

    final StringBuilder url = new StringBuilder();

    // The real host will be assigned by the retry strategy
    url.append("http://temp.path").append(path);

    if (queryParameters != null && !queryParameters.isEmpty()) {
      // support (constant) query string in `path`, e.g. "/posts?draft=1"
      String prefix = path.contains("?") ? "&" : "?";
      for (Entry<String, Object> param : queryParameters.entrySet()) {
        if (param.getValue() != null) {
          if (prefix != null) {
            url.append(prefix);
            prefix = null;
          } else {
            url.append("&");
          }
          String value = parameterToString(param.getValue());
          url.append(escapeString(param.getKey())).append("=").append(escapeString(value));
        }
      }
    }

    return url.toString();
  }

  /**
   * Set header parameters to the request builder, including default headers.
   *
   * @param headerParams Header parameters in the form of Map
   * @param extraHeaderParams Header parameters in the form of Map, coming from RequestOptions
   * @param reqBuilder Request.Builder
   */
  public void processHeaderParams(Map<String, String> headerParams, Map<String, String> extraHeaderParams, Request.Builder reqBuilder) {
    for (Entry<String, String> param : headerParams.entrySet()) {
      reqBuilder.header(param.getKey().toLowerCase(), parameterToString(param.getValue()));
    }
    for (Entry<String, String> header : defaultHeaderMap.entrySet()) {
      if (!headerParams.containsKey(header.getKey())) {
        reqBuilder.header(header.getKey().toLowerCase(), parameterToString(header.getValue()));
      }
    }
    if (extraHeaderParams != null) {
      for (Entry<String, String> header : extraHeaderParams.entrySet()) {
        reqBuilder.header(header.getKey().toLowerCase(), parameterToString(header.getValue()));
      }
    }
  }
}
