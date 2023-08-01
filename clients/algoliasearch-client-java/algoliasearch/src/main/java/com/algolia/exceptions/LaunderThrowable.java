package com.algolia.exceptions;

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

@SuppressWarnings("WeakerAccess")
public class LaunderThrowable {

  /**
   * Performs a get() on the asynchronous method. Launders both Interrupted and Execution exception
   * to business exception
   *
   * @param f The CompletableFuture to block on.
   */
  public static <T> T await(CompletableFuture<T> f) {
    try {
      return f.get();
    } catch (InterruptedException | ExecutionException e) {
      throw LaunderThrowable.launder(e);
    }
  }

  /** Launders both Interrupted and Execution exception into business exception */
  public static RuntimeException launder(Throwable t) {
    if (t.getCause() instanceof AlgoliaApiException) {
      throw (AlgoliaApiException) t.getCause();
    }

    if (t.getCause() instanceof AlgoliaRetryException) {
      throw (AlgoliaRetryException) t.getCause();
    }

    if (t.getCause() instanceof AlgoliaRuntimeException) {
      throw (AlgoliaRuntimeException) t.getCause();
    }

    throw new AlgoliaRuntimeException(t);
  }
}
