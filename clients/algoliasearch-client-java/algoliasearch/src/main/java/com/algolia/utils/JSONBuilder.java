package com.algolia.utils;

import static com.fasterxml.jackson.core.JsonGenerator.Feature;

import com.fasterxml.jackson.annotation.*;
import com.fasterxml.jackson.databind.*;
import com.fasterxml.jackson.databind.json.JsonMapper;

public class JSONBuilder {

  private boolean failOnUnknown = false;

  public JSONBuilder() {}

  public JSONBuilder failOnUnknown(boolean failOnUnknown) {
    this.failOnUnknown = failOnUnknown;
    return this;
  }

  public ObjectMapper build() {
    ObjectMapper mapper = JsonMapper.builder().disable(MapperFeature.ALLOW_COERCION_OF_SCALARS).build();
    mapper.setSerializationInclusion(JsonInclude.Include.NON_NULL);
    mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, this.failOnUnknown);
    mapper.enable(Feature.AUTO_CLOSE_JSON_CONTENT);
    mapper.enable(DeserializationFeature.FAIL_ON_INVALID_SUBTYPE);
    mapper.disable(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS);
    mapper.disable(SerializationFeature.WRITE_DATE_TIMESTAMPS_AS_NANOSECONDS);
    mapper.disable(DeserializationFeature.READ_DATE_TIMESTAMPS_AS_NANOSECONDS);
    mapper.enable(SerializationFeature.WRITE_ENUMS_USING_TO_STRING);
    mapper.enable(DeserializationFeature.READ_ENUMS_USING_TO_STRING);
    return mapper;
  }
}
