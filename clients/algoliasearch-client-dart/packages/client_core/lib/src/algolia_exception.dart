/// Abstract base class for all Algolia exceptions.
sealed class AlgoliaException implements Exception {}

/// Exception thrown when the Algolia API returns an error.
///
/// Contains the HTTP status code and the error message returned by the API.
final class AlgoliaApiException implements AlgoliaException {
  /// The HTTP status code returned by the API.
  final int statusCode;

  /// The error message returned by the API.
  final dynamic error;

  /// Constructs an [AlgoliaApiException] with the provided status code and error message.
  const AlgoliaApiException(this.statusCode, this.error);

  @override
  String toString() {
    return 'AlgoliaApiException{statusCode: $statusCode, error: $error}';
  }
}

/// Exception thrown when a request to the Algolia API times out.
///
/// Contains the error message associated with the timeout.
final class AlgoliaTimeoutException implements AlgoliaException {
  /// The error message associated with the timeout.
  final dynamic error;

  /// Constructs an [AlgoliaTimeoutException] with the provided error message.
  const AlgoliaTimeoutException(this.error);

  @override
  String toString() {
    return 'AlgoliaTimeoutException{error: $error}';
  }
}

/// Exception thrown when there is an input/output error during a request to the Algolia API.
///
/// Contains the error message associated with the I/O error.
final class AlgoliaIOException implements AlgoliaException {
  /// The error message associated with the I/O error.
  final dynamic error;

  /// Constructs an [AlgoliaIOException] with the provided error message.
  const AlgoliaIOException(this.error);

  @override
  String toString() {
    return 'AlgoliaIOException{error: $error}';
  }
}

/// Exception thrown when all hosts for the Algolia API are unreachable.
///
/// Contains a list of the errors associated with each unreachable host.
final class UnreachableHostsException implements AlgoliaException {
  /// The list of errors associated with each unreachable host.
  final List<AlgoliaException> errors;

  /// Constructs an [UnreachableHostsException] with the provided list of errors.
  const UnreachableHostsException(this.errors);

  @override
  String toString() {
    return 'UnreachableHostsException{errors: $errors}';
  }
}
