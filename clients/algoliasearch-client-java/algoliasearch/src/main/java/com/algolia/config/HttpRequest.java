package com.algolia.config;

import com.algolia.utils.StringUtils;
import java.util.*;

public class HttpRequest {

  public static Builder builder() {
    return new Builder();
  }

  private final String method;
  private final String path;
  private final boolean read;
  private final Map<String, String> headers;
  private final Map<String, String> queryParameters;
  private final Object body;

  public HttpRequest(
    String method,
    String path,
    boolean isRead,
    Map<String, String> headers,
    Map<String, String> queryParameters,
    Object body
  ) {
    this.method = method;
    this.path = path;
    this.read = isRead;
    this.headers = headers;
    this.queryParameters = queryParameters;
    this.body = body;
  }

  public String getMethod() {
    return method;
  }

  public String getPath() {
    return path;
  }

  public boolean isRead() {
    return read;
  }

  public Map<String, String> getHeaders() {
    return headers;
  }

  public Map<String, String> getQueryParameters() {
    return queryParameters;
  }

  public Object getBody() {
    return body;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    HttpRequest that = (HttpRequest) o;
    return (
      read == that.read &&
      Objects.equals(method, that.method) &&
      Objects.equals(path, that.path) &&
      Objects.equals(headers, that.headers) &&
      Objects.equals(queryParameters, that.queryParameters) &&
      Objects.equals(body, that.body)
    );
  }

  @Override
  public int hashCode() {
    return Objects.hash(method, path, read, headers, queryParameters, body);
  }

  @Override
  public String toString() {
    return (
      "HttpRequest{" +
      "method='" +
      method +
      '\'' +
      ", path=" +
      path +
      ", isRead=" +
      read +
      ", headers=" +
      headers +
      ", queryParameters=" +
      queryParameters +
      ", body=" +
      body +
      '}'
    );
  }

  public static class Builder {

    private String method;
    private String path;
    private boolean read;
    private final Map<String, String> headers = new HashMap<>();
    private final Map<String, String> queryParameters = new HashMap<>();
    private Object body;

    public Builder() {
      // Empty.
    }

    public Builder(HttpRequest request) {
      this.method = request.method;
      this.path = request.path;
      this.read = request.read;
      this.body = request.body;
    }

    public Builder setMethod(String method) {
      this.method = method;
      return this;
    }

    public Builder addQueryParameter(String key, Object value) {
      if (value == null) return this;
      this.queryParameters.put(key, StringUtils.paramToString(value));
      return this;
    }

    public Builder addQueryParameters(Map<String, Object> queryParameters) {
      if (queryParameters == null) return this;
      queryParameters.forEach(this::addQueryParameter);
      return this;
    }

    public Builder setPath(String path) {
      this.path = path;
      return this;
    }

    public Builder setPath(String template, Object... values) {
      this.path = StringUtils.pathFormat(template, true, values);
      return this;
    }

    public Builder setPathEncoded(String template, Object... values) {
      this.path = StringUtils.pathFormat(template, false, values);
      return this;
    }

    public Builder setRead(boolean read) {
      this.read = read;
      return this;
    }

    public Builder setBody(Object body) {
      this.body = body;
      return this;
    }

    public Builder addHeader(String key, Object value) {
      if (value == null) return this;
      this.headers.put(key.toLowerCase(), StringUtils.paramToString(value));
      return this;
    }

    public Builder addHeaders(Map<String, Object> headers) {
      if (headers == null) return this;
      headers.forEach(this::addHeader);
      return this;
    }

    public HttpRequest build() {
      return new HttpRequest(method, path, read, headers, queryParameters, body);
    }
  }
}
