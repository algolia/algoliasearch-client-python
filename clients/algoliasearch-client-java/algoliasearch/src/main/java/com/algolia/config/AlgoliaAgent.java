package com.algolia.config;

import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import javax.annotation.Nonnull;

public final class AlgoliaAgent {

  private final Set<String> segments;

  private String finalValue;

  public AlgoliaAgent(String clientVersion) {
    this.finalValue = String.format("Algolia for Java (%s)", clientVersion);
    this.segments = new LinkedHashSet<>();
    this.addSegment(new Segment("JVM", System.getProperty("java.version")));
  }

  public AlgoliaAgent addSegment(@Nonnull Segment seg) {
    String segment = seg.toString();
    if (!segments.contains(segment)) {
      segments.add(segment);
      finalValue += segment;
    }
    return this;
  }

  public AlgoliaAgent addSegments(@Nonnull List<Segment> segments) {
    for (Segment segment : segments) {
      addSegment(segment);
    }
    return this;
  }

  public AlgoliaAgent removeSegment(@Nonnull Segment seg) {
    segments.remove(seg.toString());
    return this;
  }

  @Override
  public String toString() {
    return finalValue;
  }

  public static class Segment {

    private final String value;
    private final String version;

    public Segment(String value) {
      this(value, null);
    }

    public Segment(String value, String version) {
      this.value = value;
      this.version = version;
    }

    @Override
    public String toString() {
      StringBuilder sb = new StringBuilder();
      sb.append("; ").append(value);
      if (version != null) {
        sb.append(" (").append(version).append(")");
      }
      return sb.toString();
    }
  }
}
