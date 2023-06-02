import 'package:algolia_client_core/src/transport/algolia_agent.dart';
import 'package:algolia_client_core/src/transport/dio/platform/platform.dart';
import 'package:dio/dio.dart';

/// Interceptor that attaches the Algolia agent to outgoing requests.
///
/// This interceptor modifies the query parameters of each request to include the
/// formatted representation of the Algolia agent.
class AgentInterceptor extends Interceptor {
  /// The Algolia agent to be attached to outgoing requests.
  final AlgoliaAgent agent;

  /// Constructs an [AgentInterceptor] with the provided Algolia agent.
  AgentInterceptor({required this.agent});

  @override
  void onRequest(RequestOptions options, RequestInterceptorHandler handler) {
    Platform.algoliaAgent(options, agent.formatted());
    super.onRequest(options, handler);
  }
}
