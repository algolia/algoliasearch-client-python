// This file is generated, manual changes will be lost - read more on
// https://github.com/algolia/api-clients-automation.

package com.algolia.model.predict;

import com.fasterxml.jackson.annotation.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/** GetSegmentUsersResponse */
public class GetSegmentUsersResponse {

  @JsonProperty("segmentID")
  private String segmentID;

  @JsonProperty("users")
  private List<UserProfile> users = new ArrayList<>();

  @JsonProperty("previousPageToken")
  private String previousPageToken;

  @JsonProperty("nextPageToken")
  private String nextPageToken;

  public GetSegmentUsersResponse setSegmentID(String segmentID) {
    this.segmentID = segmentID;
    return this;
  }

  /**
   * The ID of the segment.
   *
   * @return segmentID
   */
  @javax.annotation.Nonnull
  public String getSegmentID() {
    return segmentID;
  }

  public GetSegmentUsersResponse setUsers(List<UserProfile> users) {
    this.users = users;
    return this;
  }

  public GetSegmentUsersResponse addUsers(UserProfile usersItem) {
    this.users.add(usersItem);
    return this;
  }

  /**
   * Get users
   *
   * @return users
   */
  @javax.annotation.Nonnull
  public List<UserProfile> getUsers() {
    return users;
  }

  public GetSegmentUsersResponse setPreviousPageToken(String previousPageToken) {
    this.previousPageToken = previousPageToken;
    return this;
  }

  /**
   * The token is used to navigate backward in the user list. To navigate from the current user list
   * to the previous page, the API generates the previous page token and it sends the token in the
   * response, beside the current user list. NOTE: This body param cannot be used with
   * `nextPageToken` at the same time.
   *
   * @return previousPageToken
   */
  @javax.annotation.Nullable
  public String getPreviousPageToken() {
    return previousPageToken;
  }

  public GetSegmentUsersResponse setNextPageToken(String nextPageToken) {
    this.nextPageToken = nextPageToken;
    return this;
  }

  /**
   * The token is used to navigate forward in the user list. To navigate from the current user list
   * to the next page, the API generates the next page token and it sends the token in the response,
   * beside the current user list. NOTE: This body param cannot be used with `previousPageToken` at
   * the same time.
   *
   * @return nextPageToken
   */
  @javax.annotation.Nullable
  public String getNextPageToken() {
    return nextPageToken;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetSegmentUsersResponse getSegmentUsersResponse = (GetSegmentUsersResponse) o;
    return (
      Objects.equals(this.segmentID, getSegmentUsersResponse.segmentID) &&
      Objects.equals(this.users, getSegmentUsersResponse.users) &&
      Objects.equals(this.previousPageToken, getSegmentUsersResponse.previousPageToken) &&
      Objects.equals(this.nextPageToken, getSegmentUsersResponse.nextPageToken)
    );
  }

  @Override
  public int hashCode() {
    return Objects.hash(segmentID, users, previousPageToken, nextPageToken);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetSegmentUsersResponse {\n");
    sb.append("    segmentID: ").append(toIndentedString(segmentID)).append("\n");
    sb.append("    users: ").append(toIndentedString(users)).append("\n");
    sb.append("    previousPageToken: ").append(toIndentedString(previousPageToken)).append("\n");
    sb.append("    nextPageToken: ").append(toIndentedString(nextPageToken)).append("\n");
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
