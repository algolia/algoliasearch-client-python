import 'package:algolia_client_core/src/config/host.dart';

/// This contract allows you to run http requests and get response.
abstract interface class Requester {
  /// Run an http request and get the result.
  Future<HttpResponse> perform(HttpRequest request);

  /// Close underlying resources.
  void close();
}

/// Represents an Http request.
final class HttpRequest {
  /// HTTP method of the request, such as "GET", "POST", etc.
  final String method;

  /// The host to which the request will be sent.
  final Host host;

  /// Path of the request on the host.
  final String path;

  /// Maximum duration before the request is automatically cancelled.
  final Duration timeout;

  /// Headers to be included in the request. Can be null if no headers are needed.
  final Map<String, String>? headers;

  /// Body of the request. Can be any object which can be serialized to JSON.
  final dynamic body;

  /// Query parameters to be included in the request URL.
  final Map<String, String> queryParameters;

  /// Constructs an [HttpRequest] instance with the provided parameters.
  const HttpRequest({
    required this.method,
    required this.host,
    required this.path,
    required this.timeout,
    this.headers,
    this.body,
    required this.queryParameters,
  });

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is HttpRequest &&
          runtimeType == other.runtimeType &&
          method == other.method &&
          host == other.host &&
          path == other.path &&
          timeout == other.timeout &&
          headers == other.headers &&
          body == other.body &&
          queryParameters == other.queryParameters;

  @override
  int get hashCode =>
      method.hashCode ^
      host.hashCode ^
      path.hashCode ^
      timeout.hashCode ^
      headers.hashCode ^
      body.hashCode ^
      queryParameters.hashCode;

  @override
  String toString() {
    return 'HttpRequest{method: $method, host: $host, path: $path, timeout: $timeout, headers: $headers, body: $body, queryParameters: $queryParameters}';
  }
}

/// Represents an Http response
final class HttpResponse {
  /// The status code returned by the HTTP response. Can be null if no status
  /// code was received.
  final int? statusCode;

  /// The body of the HTTP response. Can be a map of `String` to `dynamic`
  /// if a body was received, or null otherwise.
  final Map<String, dynamic>? body;

  /// Constructs an [HttpResponse] instance with the provided status code
  /// and body.
  const HttpResponse(this.statusCode, this.body);

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is HttpResponse &&
          runtimeType == other.runtimeType &&
          statusCode == other.statusCode &&
          body == other.body;

  @override
  int get hashCode => statusCode.hashCode ^ body.hashCode;

  @override
  String toString() {
    return 'HttpResponse{statusCode: $statusCode, body: $body}';
  }
}
