package com.algolia.exceptions;

/** Exception thrown in case of API failure such as 4XX, 5XX error. */
public class AlgoliaApiException extends AlgoliaRuntimeException {

  private static final long serialVersionUID = 1L;

  public int getStatusCode() {
    return statusCode;
  }

  private final int statusCode;

  public AlgoliaApiException(String message, Throwable cause, int httpErrorCode) {
    super(message, cause);
    this.statusCode = httpErrorCode;
  }

  public AlgoliaApiException(String message, int httpErrorCode) {
    super(message);
    this.statusCode = httpErrorCode;
  }

  public AlgoliaApiException(Throwable cause, int httpErrorCode) {
    super(cause);
    this.statusCode = httpErrorCode;
  }

  @Override
  public String getMessage() {
    String message = super.getMessage();
    return "Status Code: " + getStatusCode() + (message != null ? " - " + message : "");
  }
}
