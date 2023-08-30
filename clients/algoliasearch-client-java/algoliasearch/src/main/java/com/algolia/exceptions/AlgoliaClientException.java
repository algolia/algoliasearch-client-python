package com.algolia.exceptions;

/** Exception thrown when an error occurs during API requests. */
public class AlgoliaClientException extends AlgoliaRuntimeException {

  public AlgoliaClientException(String message, Throwable cause) {
    super(message, cause);
  }

  public AlgoliaClientException(String message) {
    super(message);
  }

  public AlgoliaClientException(Throwable cause) {
    super(cause);
  }
}
