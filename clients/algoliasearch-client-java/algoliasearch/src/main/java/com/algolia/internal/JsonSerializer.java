package com.algolia.internal;

import com.algolia.exceptions.AlgoliaRuntimeException;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.*;
import com.fasterxml.jackson.databind.json.JsonMapper;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.function.Consumer;
import org.jetbrains.annotations.NotNull;

/**
 * Utility class for JSON serialization and deserialization using Jackson. It provides functionality
 * to convert Java objects to their JSON representation and vice versa.
 */
public final class JsonSerializer {

  private final ObjectMapper mapper;

  public static Builder builder() {
    return new Builder();
  }

  /**
   * Initializes a new JsonSerializer instance with a given ObjectMapper.
   *
   * @param mapper The Jackson ObjectMapper to be used for JSON operations.
   */
  JsonSerializer(@NotNull ObjectMapper mapper) {
    this.mapper = mapper;
  }

  /**
   * Serializes a Java object into its JSON representation.
   *
   * @param stream output steam.
   * @param object The Java object to serialize.
   */
  public void serialize(OutputStream stream, @NotNull Object object) {
    try {
      mapper.writeValue(stream, object);
    } catch (IOException e) {
      throw new AlgoliaRuntimeException(e);
    }
  }

  /** Deserializes a JSON ResponseBody into a Java object of a given type. */
  public <T> T deserialize(InputStream stream, JavaType returnType) {
    try {
      return mapper.readValue(stream, returnType);
    } catch (IOException e) {
      throw new AlgoliaRuntimeException(e);
    }
  }

  /**
   * Constructs a JavaType representation for a class with parameterized types.
   *
   * @param returnType The main class type.
   * @param innerType The parameterized type.
   * @return A JavaType representation of the parameterized class.
   */
  public JavaType getJavaType(@NotNull Class<?> returnType, @NotNull Class<?> innerType) {
    return mapper.getTypeFactory().constructParametricType(returnType, innerType);
  }

  /**
   * Constructs a JavaType representation for a class.
   *
   * @param returnType The main class type.
   * @return A JavaType representation of the parameterized class.
   */
  public JavaType getJavaType(@NotNull TypeReference<?> returnType) {
    return mapper.getTypeFactory().constructType(returnType);
  }

  public static class Builder {

    /**
     * A custom configuration for the JsonMapper builder, allowing clients to customize the built
     * ObjectMapper beyond the default settings provided in this class.
     */
    private Consumer<JsonMapper.Builder> customerConfig;

    /**
     * Sets a custom configuration to be applied to the JsonMapper builder.
     *
     * @param config A consumer function that specifies additional configurations for the JsonMapper
     *     builder.
     * @return The current JsonConfig instance, useful for method chaining.
     */
    public Builder setCustomConfig(Consumer<JsonMapper.Builder> config) {
      this.customerConfig = config;
      return this;
    }

    /** Builds JsonSerializer instance. */
    public JsonSerializer build() {
      JsonMapper.Builder builder = JsonMapper
        .builder()
        .disable(MapperFeature.ALLOW_COERCION_OF_SCALARS)
        .configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false)
        .enable(JsonGenerator.Feature.AUTO_CLOSE_JSON_CONTENT)
        .enable(DeserializationFeature.FAIL_ON_INVALID_SUBTYPE)
        .disable(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS)
        .disable(SerializationFeature.WRITE_DATE_TIMESTAMPS_AS_NANOSECONDS)
        .disable(DeserializationFeature.READ_DATE_TIMESTAMPS_AS_NANOSECONDS)
        .enable(SerializationFeature.WRITE_ENUMS_USING_TO_STRING)
        .enable(DeserializationFeature.READ_ENUMS_USING_TO_STRING)
        .serializationInclusion(JsonInclude.Include.NON_NULL);
      if (customerConfig != null) {
        customerConfig.accept(builder);
      }
      JsonMapper build = builder.build();
      return new JsonSerializer(build);
    }
  }
}
