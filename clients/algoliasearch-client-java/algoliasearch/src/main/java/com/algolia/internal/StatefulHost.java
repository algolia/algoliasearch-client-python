package com.algolia.internal;

import com.algolia.config.CallType;
import com.algolia.config.Host;
import com.algolia.utils.DateTimeUtils;
import java.time.OffsetDateTime;
import java.util.Set;

public final class StatefulHost {

  private final Host host;
  private boolean up = true;
  private int retryCount;
  private OffsetDateTime lastUse = DateTimeUtils.nowUTC();

  public StatefulHost(Host host) {
    this.host = host;
  }

  public String getHost() {
    return host.getUrl();
  }

  public String getScheme() {
    return this.host.getScheme();
  }

  public boolean isUp() {
    return up;
  }

  public int getRetryCount() {
    return retryCount;
  }

  public void incrementRetryCount() {
    this.retryCount++;
  }

  public OffsetDateTime getLastUse() {
    return lastUse;
  }

  public Set<CallType> getAccept() {
    return this.host.getCallTypes();
  }

  public void reset() {
    this.up = true;
    this.lastUse = DateTimeUtils.nowUTC();
    this.retryCount = 0;
  }

  public void hasTimedOut() {
    this.up = true;
    this.lastUse = DateTimeUtils.nowUTC();
    this.retryCount++;
  }

  public void hasFailed() {
    this.up = false;
    this.lastUse = DateTimeUtils.nowUTC();
  }
}
