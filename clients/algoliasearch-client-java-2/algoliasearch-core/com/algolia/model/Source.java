package com.algolia.model;

import com.google.gson.annotations.SerializedName;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.util.Objects;

/** The source. */
@ApiModel(description = "The source.")
public class Source {

  public static final String SERIALIZED_NAME_SOURCE = "source";

  @SerializedName(SERIALIZED_NAME_SOURCE)
  private String source;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";

  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public Source source(String source) {
    this.source = source;
    return this;
  }

  /**
   * The IP range of the source.
   *
   * @return source
   */
  @javax.annotation.Nonnull
  @ApiModelProperty(
    example = "10.0.0.1/32",
    required = true,
    value = "The IP range of the source."
  )
  public String getSource() {
    return source;
  }

  public void setSource(String source) {
    this.source = source;
  }

  public Source description(String description) {
    this.description = description;
    return this;
  }

  /**
   * The description of the source.
   *
   * @return description
   */
  @javax.annotation.Nullable
  @ApiModelProperty(value = "The description of the source.")
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Source source = (Source) o;
    return (
      Objects.equals(this.source, source.source) &&
      Objects.equals(this.description, source.description)
    );
  }

  @Override
  public int hashCode() {
    return Objects.hash(source, description);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Source {\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
    sb
      .append("    description: ")
      .append(toIndentedString(description))
      .append("\n");
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