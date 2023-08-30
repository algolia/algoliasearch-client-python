package com.algolia.utils;

import com.algolia.exceptions.*;
import java.util.function.IntUnaryOperator;
import java.util.function.Predicate;
import java.util.function.Supplier;

public class TaskUtils {

  private TaskUtils() {
    // Empty.
  }

  public static final int DEFAULT_MAX_RETRIES = 50;
  public static final IntUnaryOperator DEFAULT_TIMEOUT = (int retries) -> Math.min(retries * 200, 5000);

  public static <T> T retryUntil(Supplier<T> func, Predicate<T> validate, int maxRetries, IntUnaryOperator timeout)
    throws AlgoliaRuntimeException {
    int retryCount = 0;
    while (retryCount < maxRetries) {
      T resp = func.get();
      if (validate.test(resp)) {
        return resp;
      }
      try {
        Thread.sleep(timeout.applyAsInt(retryCount));
      } catch (InterruptedException ignored) {
        // Restore interrupted state...
        Thread.currentThread().interrupt();
      }

      retryCount++;
    }
    throw new AlgoliaRetriesExceededException("The maximum number of retries exceeded. (" + (retryCount + 1) + "/" + maxRetries + ")");
  }
}
