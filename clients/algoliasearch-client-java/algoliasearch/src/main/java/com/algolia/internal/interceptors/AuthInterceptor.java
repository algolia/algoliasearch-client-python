package com.algolia.internal.interceptors;

import java.io.IOException;
import okhttp3.Headers;
import okhttp3.Interceptor;
import okhttp3.Response;
import org.jetbrains.annotations.NotNull;

public final class AuthInterceptor implements Interceptor {

  private static final String HEADER_APPLICATION_ID = "x-algolia-application-id";
  private static final String HEADER_API_KEY = "x-algolia-api-key";

  private final String applicationId;
  private final String apiKey;

  public AuthInterceptor(String applicationId, String apiKey) {
    this.applicationId = applicationId;
    this.apiKey = apiKey;
  }

  @NotNull
  @Override
  public Response intercept(Chain chain) throws IOException {
    okhttp3.Request originalRequest = chain.request();
    okhttp3.Request.Builder builder = originalRequest.newBuilder();
    Headers headers = originalRequest.headers();
    if (headers.get(HEADER_APPLICATION_ID) == null) {
      builder.header(HEADER_APPLICATION_ID, applicationId);
    }
    if (headers.get(HEADER_API_KEY) == null) {
      builder.header(HEADER_API_KEY, apiKey);
    }
    okhttp3.Request newRequest = builder.build();
    return chain.proceed(newRequest);
  }
}
