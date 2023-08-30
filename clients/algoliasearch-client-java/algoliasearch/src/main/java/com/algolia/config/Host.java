package com.algolia.config;

import java.util.Set;
import org.jetbrains.annotations.NotNull;

public final class Host {

  private final String url;

  private final Set<CallType> callTypes;

  private final String scheme;

  public Host(@NotNull String url, @NotNull Set<CallType> callType) {
    this(url, callType, "https");
  }

  public Host(String url, Set<CallType> callType, String scheme) {
    this.url = url;
    this.callTypes = callType;
    this.scheme = scheme;
  }

  @NotNull
  public String getUrl() {
    return url;
  }

  @NotNull
  public Set<CallType> getCallTypes() {
    return callTypes;
  }

  @NotNull
  public String getScheme() {
    return scheme;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;

    Host host = (Host) o;

    if (!url.equals(host.url)) return false;
    if (!callTypes.equals(host.callTypes)) return false;
    return scheme.equals(host.scheme);
  }

  @Override
  public int hashCode() {
    int result = url.hashCode();
    result = 31 * result + callTypes.hashCode();
    result = 31 * result + scheme.hashCode();
    return result;
  }
}
