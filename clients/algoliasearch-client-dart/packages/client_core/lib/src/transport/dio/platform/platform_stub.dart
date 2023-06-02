import 'package:algolia_client_core/src/config/agent_segment.dart';
import 'package:algolia_client_core/src/transport/algolia_agent.dart';
import 'package:dio/dio.dart' as dio;

/// [AgentSegment]s for unsupported platforms.
Iterable<AgentSegment> platformAgentSegments() => const [];

/// [AlgoliaAgent] for unsupported platforms.
void platformAlgoliaAgent(dio.RequestOptions options, String agent) {
  // NO-OP.
}
