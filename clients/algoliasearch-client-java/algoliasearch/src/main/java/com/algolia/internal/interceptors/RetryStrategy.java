package com.algolia.internal.interceptors;

import com.algolia.config.CallType;
import com.algolia.exceptions.AlgoliaApiException;
import com.algolia.exceptions.AlgoliaClientException;
import com.algolia.exceptions.AlgoliaRequestException;
import com.algolia.exceptions.AlgoliaRetryException;
import com.algolia.internal.StatefulHost;
import com.algolia.utils.DateTimeUtils;
import com.algolia.utils.UseReadTransporter;
import java.io.IOException;
import java.net.SocketTimeoutException;
import java.time.Duration;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import javax.annotation.Nonnull;
import okhttp3.HttpUrl;
import okhttp3.Interceptor;
import okhttp3.Request;
import okhttp3.Response;

/**
 * A retry strategy that implements {@link Interceptor}, responsible for routing requests to hosts
 * based on their state and call type.
 */
public final class RetryStrategy implements Interceptor {

  /** Threshold duration after which a host is considered expired. */
  private static final long EXPIRATION_THRESHOLD_SECONDS = 5 * 60;

  /** The list of stateful hosts to route requests to. */
  private final List<StatefulHost> hosts;

  /**
   * @param hosts List of stateful hosts.
   */
  public RetryStrategy(List<StatefulHost> hosts) {
    this.hosts = Collections.unmodifiableList(hosts);
  }

  @Nonnull
  @Override
  public Response intercept(@Nonnull Chain chain) {
    Request request = chain.request();
    UseReadTransporter useReadTransporter = (UseReadTransporter) request.tag();
    CallType callType = (useReadTransporter != null || request.method().equals("GET")) ? CallType.READ : CallType.WRITE;
    List<Throwable> errors = new ArrayList<>();
    for (StatefulHost currentHost : callableHosts(callType)) {
      try {
        return processRequest(chain, request, currentHost);
      } catch (Exception e) {
        errors.add(e);
        handleException(currentHost, e);
      }
    }
    throw new AlgoliaRetryException(errors);
  }

  /** Processes the request for a given host. */
  @Nonnull
  private Response processRequest(@Nonnull Chain chain, @Nonnull Request request, StatefulHost host) throws IOException {
    HttpUrl newUrl = request.url().newBuilder().scheme(host.getScheme()).host(host.getHost()).build();
    Request newRequest = request.newBuilder().url(newUrl).build();
    chain.withConnectTimeout(chain.connectTimeoutMillis() * (host.getRetryCount() + 1), TimeUnit.MILLISECONDS);
    Response response = chain.proceed(newRequest);
    return handleResponse(host, response);
  }

  /** Handles the response from the host. */
  @Nonnull
  private Response handleResponse(StatefulHost host, @Nonnull Response response) throws IOException {
    if (response.isSuccessful()) {
      host.reset();
      return response;
    }

    try {
      String message = response.body() != null ? response.body().string() : response.message();
      throw isRetryable(response)
        ? new AlgoliaRequestException(message, response.code())
        : new AlgoliaApiException(message, response.code());
    } finally {
      response.close();
    }
  }

  /** Determines if a response should be retried. */
  private boolean isRetryable(@Nonnull Response response) {
    int statusCode = response.code();
    return (statusCode < 200 || statusCode >= 300) && (statusCode < 400 || statusCode >= 500);
  }

  /** Handles exceptions that occurred during request processing. */
  private void handleException(StatefulHost host, Exception exception) {
    if (exception instanceof SocketTimeoutException) {
      host.hasTimedOut();
    } else if (exception instanceof AlgoliaRequestException || exception instanceof IOException) {
      host.hasFailed();
    } else if (exception instanceof AlgoliaApiException) {
      throw (AlgoliaApiException) exception;
    } else {
      throw new AlgoliaClientException(exception);
    }
  }

  /** Fetches a list of hosts that can be used for a specific call type. */
  private synchronized List<StatefulHost> callableHosts(CallType callType) {
    resetExpiredHosts();
    List<StatefulHost> hostsCallType = hosts.stream().filter(h -> h.getAccept().contains(callType)).collect(Collectors.toList());
    List<StatefulHost> hostsCallTypeAreUp = hostsCallType.stream().filter(StatefulHost::isUp).collect(Collectors.toList());
    if (hostsCallTypeAreUp.isEmpty()) {
      hostsCallType.forEach(StatefulHost::reset);
      return hostsCallType;
    }
    return hostsCallTypeAreUp;
  }

  /** Resets hosts that have been down for longer than the defined expiration threshold. */
  private void resetExpiredHosts() {
    OffsetDateTime now = DateTimeUtils.nowUTC();
    for (StatefulHost host : hosts) {
      long lastUse = Duration.between(host.getLastUse(), now).getSeconds();
      if (!host.isUp() && lastUse > EXPIRATION_THRESHOLD_SECONDS) {
        host.reset();
      }
    }
  }
}
