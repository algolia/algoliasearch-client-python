import 'dart:async';

import 'package:algolia_client_core/src/algolia_exception.dart';
import 'package:algolia_client_core/src/config/agent_segment.dart';
import 'package:algolia_client_core/src/transport/algolia_agent.dart';
import 'package:algolia_client_core/src/transport/dio/agent_interceptor.dart';
import 'package:algolia_client_core/src/transport/dio/auth_interceptor.dart';
import 'package:algolia_client_core/src/transport/dio/platform/platform.dart';
import 'package:algolia_client_core/src/transport/requester.dart';
import 'package:algolia_client_core/src/version.dart';
import 'package:dio/dio.dart';

/// A [Requester] implementation using the Dio library.
///
/// This class sends HTTP requests using the Dio library and handles
/// response conversion and error handling.
class DioRequester implements Requester {
  /// The underlying Dio client.
  final Dio _client;

  /// Constructs a [DioRequester] with the given [appId], [apiKey], and [options].
  DioRequester({
    required String appId,
    required String apiKey,
    Map<String, dynamic>? headers,
    Duration? connectTimeout,
    Iterable<AgentSegment>? clientSegments,
    Function(Object?)? logger,
  }) : _client = Dio(
          BaseOptions(
            headers: headers,
            connectTimeout: connectTimeout,
          ),
        )..interceptors.addAll([
            AuthInterceptor(
              appId: appId,
              apiKey: apiKey,
            ),
            AgentInterceptor(
              agent: AlgoliaAgent(packageVersion)
                ..addAll(clientSegments ?? const [])
                ..addAll(Platform.agentSegments()),
            ),
            if (logger != null)
              LogInterceptor(
                requestBody: true,
                responseBody: true,
                logPrint: logger,
              ),
          ]);

  @override
  Future<HttpResponse> perform(HttpRequest request) async {
    try {
      return await execute(request);
    } on DioError catch (e) {
      switch (e.type) {
        case DioErrorType.connectionTimeout:
        case DioErrorType.sendTimeout:
        case DioErrorType.receiveTimeout:
          throw AlgoliaTimeoutException(e);
        case DioErrorType.badResponse:
          throw AlgoliaApiException(
            e.response?.statusCode ?? 0,
            e.error ?? e.response,
          );
        case DioErrorType.badCertificate:
        case DioErrorType.cancel:
        case DioErrorType.connectionError:
        case DioErrorType.unknown:
          throw AlgoliaIOException(e);
      }
    }
  }

  /// Executes the [request] and returns the response as an [HttpResponse].
  Future<HttpResponse> execute(HttpRequest request) async {
    final response = await _client.requestUri<Map<String, dynamic>>(
      requestUri(request),
      data: request.body,
      options: Options(
        method: request.method,
        sendTimeout: request.timeout,
        receiveTimeout: request.timeout,
      ),
    );
    return HttpResponse(response.statusCode, response.data);
  }

  /// Constructs the request URI from the [request] details.
  Uri requestUri(HttpRequest request) => Uri(
        scheme: request.host.scheme,
        host: request.host.url,
        path: request.path,
        queryParameters: request.queryParameters,
      );

  @override
  void close() => _client.close();
}
