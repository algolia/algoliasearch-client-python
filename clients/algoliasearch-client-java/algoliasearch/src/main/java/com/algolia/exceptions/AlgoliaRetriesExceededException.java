package com.algolia.exceptions;

/**
 * Exception thrown when an error occurs during the waitForTask strategy. For example: maximum
 * number of retry exceeded
 */
public class AlgoliaRetriesExceededException extends AlgoliaRuntimeException {

  private static final long serialVersionUID = 1L;

  public AlgoliaRetriesExceededException(String message, Throwable cause) {
    super(message, cause);
  }

  public AlgoliaRetriesExceededException(String message) {
    super(message);
  }

  public AlgoliaRetriesExceededException(Throwable cause) {
    super(cause);
  }
}
