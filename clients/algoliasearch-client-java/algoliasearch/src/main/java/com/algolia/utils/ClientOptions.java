package com.algolia.utils;

import com.algolia.utils.retry.StatefulHost;
import java.util.ArrayList;
import java.util.List;

public class ClientOptions {

  private Requester requester;
  private List<AlgoliaAgent.Segment> algoliaAgentSegments;
  private List<StatefulHost> hosts;

  public ClientOptions() {
    algoliaAgentSegments = new ArrayList<>();
  }

  public Requester getRequester() {
    return this.requester;
  }

  public ClientOptions setRequester(Requester requester) {
    this.requester = requester;
    return this;
  }

  public List<AlgoliaAgent.Segment> getAlgoliaAgentSegments() {
    return this.algoliaAgentSegments;
  }

  public ClientOptions setAlgoliaAgentSegments(List<AlgoliaAgent.Segment> algoliaAgentSegments) {
    this.algoliaAgentSegments = algoliaAgentSegments;
    return this;
  }

  public ClientOptions addAlgoliaAgentSegment(AlgoliaAgent.Segment algoliaAgentSegment) {
    this.algoliaAgentSegments.add(algoliaAgentSegment);
    return this;
  }

  public ClientOptions addAlgoliaAgentSegment(String value, String version) {
    this.algoliaAgentSegments.add(new AlgoliaAgent.Segment(value, version));
    return this;
  }

  public ClientOptions addAlgoliaAgentSegment(String value) {
    this.algoliaAgentSegments.add(new AlgoliaAgent.Segment(value));
    return this;
  }

  public List<StatefulHost> getHosts() {
    return this.hosts;
  }

  public ClientOptions setHosts(List<StatefulHost> hosts) {
    this.hosts = hosts;
    return this;
  }
}
