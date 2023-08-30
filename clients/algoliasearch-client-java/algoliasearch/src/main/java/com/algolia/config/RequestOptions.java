package com.algolia.config;

import com.algolia.utils.StringUtils;
import java.time.Duration;
import java.util.HashMap;
import java.util.Map;

/**
 * Request options are used to pass extra parameters, headers, timeout to the request. Parameters
 * set in the request option will override default parameter.
 */
public final class RequestOptions {

  private final Map<String, String> headers = new HashMap<>();
  private final Map<String, String> queryParameters = new HashMap<>();
  private Duration readTimeout;
  private Duration writeTimeout;

  public RequestOptions addExtraHeader(String key, Object value) {
    if (value == null) return this;
    headers.put(key.toLowerCase(), StringUtils.paramToString(value));
    return this;
  }

  public RequestOptions addExtraQueryParameters(String key, Object value) {
    if (value == null) return this;
    queryParameters.put(key, StringUtils.paramToString((value)));
    return this;
  }

  public Map<String, String> getExtraHeaders() {
    return headers;
  }

  public Map<String, String> getExtraQueryParameters() {
    return queryParameters;
  }

  public Map<String, String> getHeaders() {
    return headers;
  }

  public Map<String, String> getQueryParameters() {
    return queryParameters;
  }

  public Duration getReadTimeout() {
    return readTimeout;
  }

  public RequestOptions setReadTimeout(Duration readTimeout) {
    this.readTimeout = readTimeout;
    return this;
  }

  public Duration getWriteTimeout() {
    return writeTimeout;
  }

  public RequestOptions setWriteTimeout(Duration writeTimeout) {
    this.writeTimeout = writeTimeout;
    return this;
  }

  @Override
  public String toString() {
    return (
      "RequestOptions{" +
      "headers=" +
      headers +
      ", queryParameters=" +
      queryParameters +
      ", readTimeout=" +
      readTimeout +
      ", writeTimeout=" +
      writeTimeout +
      '}'
    );
  }
}
