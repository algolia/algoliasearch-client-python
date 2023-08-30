package com.algolia.exceptions;

/** Exception thrown when an error occurs during the Serialization/Deserialization process */
public class AlgoliaRuntimeException extends RuntimeException {

  private static final long serialVersionUID = 1L;

  public AlgoliaRuntimeException(String message, Throwable cause) {
    super(message, cause);
  }

  public AlgoliaRuntimeException(String message) {
    super(message);
  }

  public AlgoliaRuntimeException(Throwable cause) {
    super(cause);
  }
}
