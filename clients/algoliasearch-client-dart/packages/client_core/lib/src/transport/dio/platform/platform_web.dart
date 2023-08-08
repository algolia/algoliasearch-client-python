import 'dart:html' as web;

import 'package:algolia_client_core/src/config/agent_segment.dart';
import 'package:dio/dio.dart' as dio;

/// [AgentSegment]s for web platforms.
Iterable<AgentSegment> platformAgentSegments() => [
      AgentSegment(
        value: 'Platform',
        version: 'Web ${web.window.navigator.platform}',
      ),
    ];

/// [AlgoliaAgent] for web platforms as query param.
void platformAlgoliaAgent(dio.RequestOptions options, String agent) {
  options.queryParameters["X-Algolia-Agent"] = agent;
}
