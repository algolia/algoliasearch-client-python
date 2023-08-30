package com.algolia.exceptions;

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

public class LaunderThrowable {

  private LaunderThrowable() {
    // Empty.
  }

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
      throw launder(e);
    }
  }

  /** Launders both Interrupted and Execution exception into business exception */
  public static AlgoliaRuntimeException launder(Throwable t) {
    Throwable cause = t.getCause();
    if (cause instanceof AlgoliaRuntimeException) {
      return (AlgoliaRuntimeException) cause;
    }
    return new AlgoliaRuntimeException(t);
  }
}
