// This file is generated, manual changes will be lost - read more on
// https://github.com/algolia/api-clients-automation.

package com.algolia.model.search;

import com.fasterxml.jackson.annotation.*;
import java.util.Objects;

/** OK */
public class SearchUserIdsParams {

  @JsonProperty("query")
  private String query;

  @JsonProperty("clusterName")
  private String clusterName;

  @JsonProperty("page")
  private Integer page;

  @JsonProperty("hitsPerPage")
  private Integer hitsPerPage;

  public SearchUserIdsParams setQuery(String query) {
    this.query = query;
    return this;
  }

  /**
   * Query to search. The search is a prefix search with typoTolerance. Use empty query to retrieve
   * all users.
   *
   * @return query
   */
  @javax.annotation.Nonnull
  public String getQuery() {
    return query;
  }

  public SearchUserIdsParams setClusterName(String clusterName) {
    this.clusterName = clusterName;
    return this;
  }

  /**
   * Name of the cluster.
   *
   * @return clusterName
   */
  @javax.annotation.Nullable
  public String getClusterName() {
    return clusterName;
  }

  public SearchUserIdsParams setPage(Integer page) {
    this.page = page;
    return this;
  }

  /**
   * Specify the page to retrieve.
   *
   * @return page
   */
  @javax.annotation.Nullable
  public Integer getPage() {
    return page;
  }

  public SearchUserIdsParams setHitsPerPage(Integer hitsPerPage) {
    this.hitsPerPage = hitsPerPage;
    return this;
  }

  /**
   * Set the number of hits per page.
   *
   * @return hitsPerPage
   */
  @javax.annotation.Nullable
  public Integer getHitsPerPage() {
    return hitsPerPage;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SearchUserIdsParams searchUserIdsParams = (SearchUserIdsParams) o;
    return (
      Objects.equals(this.query, searchUserIdsParams.query) &&
      Objects.equals(this.clusterName, searchUserIdsParams.clusterName) &&
      Objects.equals(this.page, searchUserIdsParams.page) &&
      Objects.equals(this.hitsPerPage, searchUserIdsParams.hitsPerPage)
    );
  }

  @Override
  public int hashCode() {
    return Objects.hash(query, clusterName, page, hitsPerPage);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SearchUserIdsParams {\n");
    sb.append("    query: ").append(toIndentedString(query)).append("\n");
    sb.append("    clusterName: ").append(toIndentedString(clusterName)).append("\n");
    sb.append("    page: ").append(toIndentedString(page)).append("\n");
    sb.append("    hitsPerPage: ").append(toIndentedString(hitsPerPage)).append("\n");
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