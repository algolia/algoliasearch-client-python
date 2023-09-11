package com.algolia.internal.interceptors;

import com.algolia.config.LogLevel;
import com.algolia.config.Logger;
import java.io.IOException;
import javax.annotation.Nonnull;
import okhttp3.Interceptor;
import okhttp3.Response;
import okhttp3.logging.HttpLoggingInterceptor;

/**
 * An interceptor that facilitates HTTP logging based on the provided logging level. This class
 * wraps around the {@link HttpLoggingInterceptor} to provide additional flexibility in log
 * handling. It allows you to specify a custom {@link Logger} and a desired {@link LogLevel}.
 *
 * <p>Usage of this interceptor ensures that HTTP request and response details are logged according
 * to the specified logging level. For example, setting the log level to {@link LogLevel#BODY} would
 * result in detailed logging of both request and response bodies, while a level of {@link
 * LogLevel#BASIC} would log request method, URL, and response status code.
 */
public final class LogInterceptor implements Interceptor {

  private final HttpLoggingInterceptor logger;

  public LogInterceptor(Logger logger, LogLevel logLevel) {
    HttpLoggingInterceptor.Logger logr = logger != null ? toLogger(logger) : HttpLoggingInterceptor.Logger.DEFAULT;
    HttpLoggingInterceptor.Level level = toLevel(logLevel);
    this.logger = new HttpLoggingInterceptor(logr).setLevel(level);
  }

  public HttpLoggingInterceptor.Logger toLogger(@Nonnull Logger logger) {
    return logger::log;
  }

  public HttpLoggingInterceptor.Level toLevel(@Nonnull LogLevel logLevel) {
    switch (logLevel) {
      case NONE:
        return HttpLoggingInterceptor.Level.NONE;
      case BODY:
        return HttpLoggingInterceptor.Level.BODY;
      case BASIC:
        return HttpLoggingInterceptor.Level.BASIC;
      case HEADERS:
        return HttpLoggingInterceptor.Level.HEADERS;
      default:
        throw new UnsupportedOperationException("Unsupported LogLevel " + logLevel);
    }
  }

  @Nonnull
  @Override
  public Response intercept(@Nonnull Chain chain) throws IOException {
    return logger.intercept(chain);
  }
}
