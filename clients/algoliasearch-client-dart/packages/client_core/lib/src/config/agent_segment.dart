/// Represents a segment of algolia agent header.
final class AgentSegment {
  /// Segment string value
  final String value;

  /// Optional version
  final String? version;

  /// Constructs an [AgentSegment] instance.
  const AgentSegment({
    required this.value,
    this.version,
  });

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is AgentSegment &&
          runtimeType == other.runtimeType &&
          value == other.value &&
          version == other.version;

  @override
  int get hashCode => value.hashCode ^ version.hashCode;

  @override
  String toString() {
    return 'AgentSegment{value: $value, version: $version}';
  }
}
