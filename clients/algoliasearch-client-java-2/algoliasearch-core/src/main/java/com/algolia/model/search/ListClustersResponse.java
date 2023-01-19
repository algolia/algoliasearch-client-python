// This file is generated, manual changes will be lost - read more on
// https://github.com/algolia/api-clients-automation.

package com.algolia.model.search;

import com.fasterxml.jackson.annotation.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/** Array of clusters. */
public class ListClustersResponse {

  @JsonProperty("topUsers")
  private List<String> topUsers = new ArrayList<>();

  public ListClustersResponse setTopUsers(List<String> topUsers) {
    this.topUsers = topUsers;
    return this;
  }

  public ListClustersResponse addTopUsers(String topUsersItem) {
    this.topUsers.add(topUsersItem);
    return this;
  }

  /**
   * Mapping of cluster names to top users.
   *
   * @return topUsers
   */
  @javax.annotation.Nonnull
  public List<String> getTopUsers() {
    return topUsers;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ListClustersResponse listClustersResponse = (ListClustersResponse) o;
    return Objects.equals(this.topUsers, listClustersResponse.topUsers);
  }

  @Override
  public int hashCode() {
    return Objects.hash(topUsers);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ListClustersResponse {\n");
    sb.append("    topUsers: ").append(toIndentedString(topUsers)).append("\n");
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