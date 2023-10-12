// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost
// - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.

package com.algolia.model.abtesting;

import com.fasterxml.jackson.annotation.*;
import com.fasterxml.jackson.databind.annotation.*;
import java.util.Objects;

/** Empty searches removed from the A/B test as a result of configuration settings. */
public class FilterEffectsEmptySearch {

  @JsonProperty("usersCount")
  private Integer usersCount;

  @JsonProperty("trackedSearchesCount")
  private Integer trackedSearchesCount;

  public FilterEffectsEmptySearch setUsersCount(Integer usersCount) {
    this.usersCount = usersCount;
    return this;
  }

  /** Number of users removed from the A/B test. */
  @javax.annotation.Nullable
  public Integer getUsersCount() {
    return usersCount;
  }

  public FilterEffectsEmptySearch setTrackedSearchesCount(Integer trackedSearchesCount) {
    this.trackedSearchesCount = trackedSearchesCount;
    return this;
  }

  /** Number of tracked searches removed from the A/B test. */
  @javax.annotation.Nullable
  public Integer getTrackedSearchesCount() {
    return trackedSearchesCount;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FilterEffectsEmptySearch filterEffectsEmptySearch = (FilterEffectsEmptySearch) o;
    return (
      Objects.equals(this.usersCount, filterEffectsEmptySearch.usersCount) &&
      Objects.equals(this.trackedSearchesCount, filterEffectsEmptySearch.trackedSearchesCount)
    );
  }

  @Override
  public int hashCode() {
    return Objects.hash(usersCount, trackedSearchesCount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FilterEffectsEmptySearch {\n");
    sb.append("    usersCount: ").append(toIndentedString(usersCount)).append("\n");
    sb.append("    trackedSearchesCount: ").append(toIndentedString(trackedSearchesCount)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}