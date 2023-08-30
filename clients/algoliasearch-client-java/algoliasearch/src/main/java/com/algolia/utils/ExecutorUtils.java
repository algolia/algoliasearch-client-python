package com.algolia.utils;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.SynchronousQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

public class ExecutorUtils {

  private ExecutorUtils() {
    // Empty.
  }

  private static final String THREAD_NAME = "algolia-worker";

  public static ExecutorService newThreadPool() {
    return new ThreadPoolExecutor(
      0,
      Integer.MAX_VALUE,
      60,
      TimeUnit.SECONDS,
      new SynchronousQueue<>(),
      runnable -> {
        Thread thread = new Thread(runnable, THREAD_NAME);
        thread.setDaemon(false);
        return thread;
      }
    );
  }
}
