package com.algolia.internal.interceptors;

import java.io.IOException;
import java.util.Collections;
import java.util.Map;
import javax.annotation.Nonnull;
import okhttp3.Headers;
import okhttp3.Interceptor;
import okhttp3.Response;

public final class HeaderInterceptor implements Interceptor {

  private final Map<String, String> headers;

  public HeaderInterceptor(Map<String, String> headers) {
    this.headers = Collections.unmodifiableMap(headers);
  }

  @Nonnull
  @Override
  public Response intercept(Chain chain) throws IOException {
    okhttp3.Request request = chain.request();
    okhttp3.Request.Builder builder = request.newBuilder();
    Headers requestHeaders = request.headers();
    for (Map.Entry<String, String> header : headers.entrySet()) {
      String key = header.getKey();
      if (requestHeaders.get(key) != null) {
        builder.header(key, header.getValue());
      }
    }
    okhttp3.Request newRequest = builder.build();
    return chain.proceed(newRequest);
  }
}
