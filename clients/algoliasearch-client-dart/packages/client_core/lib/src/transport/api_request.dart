/// Represents an API request to be sent to Algolia.
///
/// This class encapsulates the HTTP method, path, read/write type, headers,
/// query parameters, and body for a request to the Algolia API.
final class ApiRequest {
  /// The HTTP method for the request.
  final RequestMethod method;

  /// The path for the request, relative to the base URL.
  final String path;

  /// A boolean value indicating whether the request is a read operation.
  /// If false, the request is a write operation.
  final bool isRead;

  /// The headers for the request. May be null, in which case no custom headers will be sent.
  final Map<String, dynamic>? headers;

  /// The query parameters for the request. May be null, in which case no query parameters will be sent.
  final Map<String, dynamic>? queryParams;

  /// The body of the request. May be null, in which case no body will be sent.
  final dynamic body;

  /// Constructs an [ApiRequest] with the provided method, path, read/write type, headers, query parameters, and body.
  const ApiRequest({
    required this.method,
    required this.path,
    this.isRead = false,
    this.headers,
    this.queryParams,
    this.body,
  });
}

/// Provides enumerated HTTP verbs
enum RequestMethod { get, delete, head, options, patch, post, put }
