// This file is generated, manual changes will be lost - read more on
// https://github.com/algolia/api-clients-automation.

package com.algolia.model.search;

import com.fasterxml.jackson.annotation.*;
import java.util.Objects;

/** The response with a taskID and an updatedAt timestamp. */
public class UpdatedAtResponse {

  @JsonProperty("taskID")
  private Long taskID;

  @JsonProperty("updatedAt")
  private String updatedAt;

  public UpdatedAtResponse setTaskID(Long taskID) {
    this.taskID = taskID;
    return this;
  }

  /**
   * taskID of the task to wait for.
   *
   * @return taskID
   */
  @javax.annotation.Nonnull
  public Long getTaskID() {
    return taskID;
  }

  public UpdatedAtResponse setUpdatedAt(String updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

  /**
   * Date of last update (ISO-8601 format).
   *
   * @return updatedAt
   */
  @javax.annotation.Nonnull
  public String getUpdatedAt() {
    return updatedAt;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdatedAtResponse updatedAtResponse = (UpdatedAtResponse) o;
    return Objects.equals(this.taskID, updatedAtResponse.taskID) && Objects.equals(this.updatedAt, updatedAtResponse.updatedAt);
  }

  @Override
  public int hashCode() {
    return Objects.hash(taskID, updatedAt);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdatedAtResponse {\n");
    sb.append("    taskID: ").append(toIndentedString(taskID)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
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