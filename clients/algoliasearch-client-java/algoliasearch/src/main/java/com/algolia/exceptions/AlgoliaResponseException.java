package com.algolia.exceptions;

/** Exception thrown in case of API failure such as 4XX, 5XX error. */
public class AlgoliaResponseException extends AlgoliaRuntimeException {

  private static final long serialVersionUID = 1L;

  public int getHttpErrorCode() {
    return httpErrorCode;
  }

  private final int httpErrorCode;

  public AlgoliaResponseException(String message, Throwable cause, int httpErrorCode) {
    super(message, cause);
    this.httpErrorCode = httpErrorCode;
  }

  public AlgoliaResponseException(String message, int httpErrorCode) {
    super(message);
    this.httpErrorCode = httpErrorCode;
  }

  public AlgoliaResponseException(Throwable cause, int httpErrorCode) {
    super(cause);
    this.httpErrorCode = httpErrorCode;
  }
}
