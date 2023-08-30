package com.algolia.internal.interceptors;

import com.algolia.config.AlgoliaAgent;
import java.io.IOException;
import okhttp3.Interceptor;
import okhttp3.Response;
import org.jetbrains.annotations.NotNull;

public final class UserAgentInterceptor implements Interceptor {

  private final AlgoliaAgent agent;

  public UserAgentInterceptor(AlgoliaAgent agent) {
    this.agent = agent;
  }

  @NotNull
  @Override
  public Response intercept(Chain chain) throws IOException {
    okhttp3.Request originalRequest = chain.request();
    okhttp3.Request.Builder builder = originalRequest.newBuilder();
    builder.header("user-agent", agent.toString());
    okhttp3.Request newRequest = builder.build();
    return chain.proceed(newRequest);
  }
}
