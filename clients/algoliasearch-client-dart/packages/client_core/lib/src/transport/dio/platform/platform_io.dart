import 'dart:io' as io;

import 'package:algolia_client_core/src/config/agent_segment.dart';
import 'package:dio/dio.dart' as dio;

/// [AgentSegment]s for native platforms.
Iterable<AgentSegment> platformAgentSegments() => [
      AgentSegment(
        value: 'Dart',
        version: io.Platform.version,
      ),
      AgentSegment(
        value: io.Platform.operatingSystem,
        version: io.Platform.operatingSystemVersion,
      ),
    ];

/// [AlgoliaAgent] for native platforms as user-agent.
void platformAlgoliaAgent(dio.RequestOptions options, String agent) {
  options.headers.addAll({"user-agent": agent});
}
