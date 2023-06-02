import 'dart:core';

import 'package:algolia_client_core/src/config/agent_segment.dart';

/// Handles Algolia agent segments.
///
/// An instance of this class maintains a set of [AgentSegment]s, and provides
/// methods to add, remove, and format these segments.
final class AlgoliaAgent {
  final Set<AgentSegment> _segments = {};

  /// Constructs an [AlgoliaAgent] with the provided [clientVersion].
  AlgoliaAgent(String clientVersion) {
    _segments.add(
      AgentSegment(value: "Algolia for Dart", version: clientVersion),
    );
  }

  /// Adds a new [segment] to the agent segments.
  bool add(AgentSegment segment) => _segments.add(segment);

  /// Adds all [segments] to the agent segments.
  void addAll(Iterable<AgentSegment> segments) => _segments.addAll(segments);

  /// Removes [segment] from the agent segments.
  bool remove(AgentSegment segment) => _segments.remove(segment);

  /// Formats the agent segments into a semicolon-separated string.
  String formatted() => _segments.map((it) => it.formatted()).join("; ");

  @override
  String toString() {
    return 'AlgoliaAgent{segments: $_segments}';
  }
}

/// Provides a formatted string representation for [AgentSegment].
extension on AgentSegment {
  String formatted() {
    StringBuffer sb = StringBuffer();
    sb.write(value);
    if (version != null) {
      sb.write(" (");
      sb.write(version);
      sb.write(")");
    }
    return sb.toString();
  }
}
