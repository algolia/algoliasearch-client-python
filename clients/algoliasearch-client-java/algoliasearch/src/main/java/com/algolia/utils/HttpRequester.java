package com.algolia.utils;

import com.algolia.exceptions.*;
import com.algolia.utils.retry.RetryStrategy;
import com.algolia.utils.retry.StatefulHost;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JavaType;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.IOException;
import java.util.List;
import java.util.concurrent.TimeUnit;
import okhttp3.Call;
import okhttp3.Interceptor;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import okhttp3.logging.HttpLoggingInterceptor;

public class HttpRequester implements Requester {

  private RetryStrategy retryStrategy;
  private OkHttpClient httpClient;
  private HttpLoggingInterceptor loggingInterceptor;
  private LogLevel level;
  private ObjectMapper json;

  public HttpRequester() {
    this.retryStrategy = new RetryStrategy();

    OkHttpClient.Builder builder = new OkHttpClient.Builder();
    builder.addInterceptor(retryStrategy.getRetryInterceptor());

    this.loggingInterceptor = new HttpLoggingInterceptor();
    loggingInterceptor.setLevel(LogLevel.NONE.value());
    builder.addInterceptor(this.loggingInterceptor);

    builder.retryOnConnectionFailure(false);

    httpClient = builder.build();

    this.json = new JSONBuilder().build();
  }

  @Override
  public Call newCall(Request request) {
    return httpClient.newCall(request);
  }

  @Override
  public <T> T handleResponse(Response response, JavaType returnType) throws AlgoliaRuntimeException {
    if (response.isSuccessful()) {
      if (returnType == null || response.code() == 204) {
        // returning null if the returnType is not defined, or the status code is 204 (No Content)
        if (response.body() != null) {
          try {
            response.body().close();
          } catch (Exception e) {
            throw new AlgoliaApiException(response.message(), e, response.code());
          }
        }
        return null;
      } else {
        return deserialize(response, returnType);
      }
    } else {
      if (response.body() != null) {
        try {
          response.body().string();
        } catch (IOException e) {
          throw new AlgoliaApiException(response.message(), e, response.code());
        }
      }
      throw new AlgoliaApiException(response.message(), response.code());
    }
  }

  private <T> T deserialize(Response response, JavaType returnType) throws AlgoliaRuntimeException {
    if (response == null || returnType == null) {
      return null;
    }

    if ("[byte".equals(returnType.getRawClass().getName())) {
      // Handle binary response (byte array).
      try {
        return (T) response.body().bytes();
      } catch (IOException e) {
        throw new AlgoliaRuntimeException(e);
      }
    }

    String respBody;
    try {
      if (response.body() != null) respBody = response.body().string(); else respBody = null;
    } catch (IOException e) {
      throw new AlgoliaRuntimeException(e);
    }

    if (respBody == null || "".equals(respBody)) {
      return null;
    }

    String contentType = response.headers().get("Content-Type");
    if (contentType == null) {
      contentType = "application/json";
    }
    try {
      return (T) json.readValue(respBody, returnType);
    } catch (JsonProcessingException e) {
      throw new AlgoliaRuntimeException(e);
    }
  }

  @Override
  public void setLogLevel(LogLevel level) {
    if (level != this.level) {
      this.loggingInterceptor.setLevel(level.value());
    }
    this.level = level;
  }

  @Override
  public int getConnectTimeout() {
    return httpClient.connectTimeoutMillis();
  }

  @Override
  public void setConnectTimeout(int connectionTimeout) {
    httpClient = httpClient.newBuilder().connectTimeout(connectionTimeout, TimeUnit.MILLISECONDS).build();
  }

  @Override
  public int getReadTimeout() {
    return httpClient.readTimeoutMillis();
  }

  public void setReadTimeout(int readTimeout) {
    httpClient = httpClient.newBuilder().readTimeout(readTimeout, TimeUnit.MILLISECONDS).build();
  }

  @Override
  public int getWriteTimeout() {
    return httpClient.writeTimeoutMillis();
  }

  @Override
  public void setWriteTimeout(int writeTimeout) {
    httpClient = httpClient.newBuilder().writeTimeout(writeTimeout, TimeUnit.MILLISECONDS).build();
  }

  @Override
  public void setHosts(List<StatefulHost> hosts) {
    this.retryStrategy.setHosts(hosts);
  }

  public void addInterceptor(Interceptor interceptor) {
    httpClient = httpClient.newBuilder().addInterceptor(interceptor).build();
  }
}
