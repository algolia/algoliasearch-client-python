import 'dart:async';

import 'package:algolia_client_core/algolia_client_core.dart';
import 'package:algolia_client_core/src/transport/dio/dio_requester.dart';
import 'package:algolia_client_core/src/transport/retryable_host.dart';

/// Component to run http requests with retry logic.
final class RetryStrategy {
  final Requester requester;
  final Duration readTimeout;
  final Duration writeTimeout;
  final Iterable<RetryableHost> _hosts;

  /// Constructs a [RetryStrategy].
  RetryStrategy({
    required this.requester,
    required this.readTimeout,
    required this.writeTimeout,
    required Iterable<Host> hosts,
  }) : _hosts = hosts.map((host) => RetryableHost(host));

  /// Creates [RetryStrategy], defaults to [DioRequester].
  RetryStrategy.create({
    required AgentSegment segment,
    required String appId,
    required String apiKey,
    required Iterable<Host> Function() defaultHosts,
    ClientOptions options = const ClientOptions(),
  }) : this(
          readTimeout: options.readTimeout,
          writeTimeout: options.writeTimeout,
          hosts: options.hosts ?? defaultHosts.call(),
          requester: options.requester ??
              DioRequester(
                appId: appId,
                apiKey: apiKey,
                headers: options.headers,
                connectTimeout: options.connectTimeout,
                clientSegments: [segment, ...?options.agentSegments],
                logger: options.logger,
              ),
        );

  /// Run an request and get a response.
  Future<Map<String, dynamic>> execute({
    required ApiRequest request,
    RequestOptions? options,
  }) async {
    final callType = _callTypeOf(request);
    final hosts = _callableHosts(callType);
    final List<AlgoliaException> errors = [];
    for (final host in hosts) {
      final httpRequest = _buildRequest(host, request, callType, options);
      try {
        final response = await requester.perform(httpRequest);
        return response.body ?? const {};
      } on AlgoliaTimeoutException catch (e) {
        host.timedOut();
        errors.add(e);
      } on AlgoliaIOException catch (e) {
        host.failed();
        errors.add(e);
      } on AlgoliaApiException catch (e) {
        if (e.statusCode ~/ 100 == 4) rethrow;
        host.failed();
        errors.add(e);
      }
    }
    throw UnreachableHostsException(errors);
  }

  /// Returns a list of callable hosts.
  /// If there are hosts that are up, it returns these hosts.
  /// Otherwise, it resets all hosts and returns them.
  Iterable<RetryableHost> _callableHosts(CallType callType) {
    _expireHosts();
    final hostsCallType = _hosts
        .where((e) => e.host.callType == callType || e.host.callType == null);
    final upHosts = hostsCallType.where((host) => host.isUp);
    if (upHosts.isNotEmpty) return upHosts;
    return hostsCallType..forEach((host) => host.reset());
  }

  /// Checks if any hosts have been inactive for more than 5 minutes and resets
  /// them if they have.
  void _expireHosts() {
    for (final host in _hosts) {
      final delay = DateTime.now().difference(host.lastUpdated);
      if (delay > const Duration(minutes: 5)) host.reset();
    }
  }

  /// Constructs an HTTP request for a given [host], [request] and [options].
  HttpRequest _buildRequest(
    RetryableHost host,
    ApiRequest request,
    CallType callType,
    RequestOptions? options,
  ) {
    final baseTimeout = _timeoutOf(callType, options);
    final timeout = baseTimeout * (host.retryCount + 1);
    return HttpRequest(
      method: request.method.name,
      host: host.host,
      path: request.path,
      timeout: timeout,
      headers: {...?options?.headers, ...?request.headers},
      body: options?.body ?? request.body != null
          ? request.body
          : _requiresBody(request)
              ? const <String, dynamic>{}
              : null,
      queryParameters: {...?request.queryParams, ...?options?.urlParameters},
    );
  }

  /// Determines the call type of a given [config].
  CallType _callTypeOf(ApiRequest config) =>
      config.isRead || config.method == RequestMethod.get
          ? CallType.read
          : CallType.write;

  /// Determines the timeout for a given [callType].
  Duration _timeoutOf(CallType callType, RequestOptions? requestOptions) {
    switch (callType) {
      case CallType.read:
        return requestOptions?.readTimeout ?? readTimeout;
      case CallType.write:
        return requestOptions?.writeTimeout ?? writeTimeout;
    }
  }

  /// Checks if a given [request] requires a body
  bool _requiresBody(ApiRequest request) =>
      request.method == RequestMethod.post ||
      request.method == RequestMethod.put;

  /// Release underlying resources.
  void dispose() => requester.close();
}
