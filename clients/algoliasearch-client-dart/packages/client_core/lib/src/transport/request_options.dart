/// Represents options for configuring a request to an endpoint.
final class RequestOptions {
  ///  The write timeout for the request in milliseconds.
  final Duration? writeTimeout;

  /// The read timeout for the request in milliseconds.
  final Duration? readTimeout;

  /// Header names to their respective values to be sent with the request.
  final Map<String, dynamic> headers;

  /// URL parameter names to their respective values to be appended to the request URL.
  final Map<String, dynamic> urlParameters;

  /// Custom request body.
  final dynamic body;

  const RequestOptions({
    this.writeTimeout,
    this.readTimeout,
    this.headers = const {},
    this.urlParameters = const {},
    this.body,
  });

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is RequestOptions &&
          runtimeType == other.runtimeType &&
          writeTimeout == other.writeTimeout &&
          readTimeout == other.readTimeout &&
          headers == other.headers &&
          urlParameters == other.urlParameters &&
          body == other.body;

  @override
  int get hashCode =>
      writeTimeout.hashCode ^
      readTimeout.hashCode ^
      headers.hashCode ^
      urlParameters.hashCode ^
      body.hashCode;

  @override
  String toString() {
    return 'RequestOptions{writeTimeout: $writeTimeout, readTimeout: $readTimeout, headers: $headers, urlParameters: $urlParameters, body: $body}';
  }
}
