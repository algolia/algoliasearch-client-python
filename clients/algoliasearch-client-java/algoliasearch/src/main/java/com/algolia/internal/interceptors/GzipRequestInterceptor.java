package com.algolia.internal.interceptors;

import java.io.IOException;
import javax.annotation.Nonnull;
import okhttp3.*;
import okio.BufferedSink;
import okio.GzipSink;
import okio.Okio;

/** This interceptor compresses the HTTP request body. */
public final class GzipRequestInterceptor implements Interceptor {

  @Nonnull
  @Override
  public Response intercept(Interceptor.Chain chain) throws IOException {
    Request originalRequest = chain.request();
    if (originalRequest.body() == null || originalRequest.header("Content-Encoding") != null) {
      return chain.proceed(originalRequest);
    }

    Request compressedRequest = originalRequest
      .newBuilder()
      .header("Content-Encoding", "gzip")
      .method(originalRequest.method(), gzip(originalRequest.body()))
      .build();
    return chain.proceed(compressedRequest);
  }

  private RequestBody gzip(final RequestBody body) {
    return new RequestBody() {
      @Override
      public MediaType contentType() {
        return body.contentType();
      }

      @Override
      public long contentLength() {
        return -1; // We don't know the compressed length in advance!
      }

      @Override
      public void writeTo(@Nonnull BufferedSink sink) throws IOException {
        BufferedSink gzipSink = Okio.buffer(new GzipSink(sink));
        body.writeTo(gzipSink);
        gzipSink.close();
      }
    };
  }
}
