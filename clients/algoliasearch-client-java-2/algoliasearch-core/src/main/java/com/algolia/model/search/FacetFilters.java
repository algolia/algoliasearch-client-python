// This file is generated, manual changes will be lost - read more on
// https://github.com/algolia/api-clients-automation.

package com.algolia.model.search;

import com.algolia.utils.CompoundType;
import com.fasterxml.jackson.annotation.*;
import com.fasterxml.jackson.core.*;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.*;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.databind.deser.std.StdDeserializer;
import com.fasterxml.jackson.databind.ser.std.StdSerializer;
import java.io.IOException;
import java.util.List;

/** Filter hits by facet value. */
@JsonDeserialize(using = FacetFilters.FacetFiltersDeserializer.class)
@JsonSerialize(using = FacetFilters.FacetFiltersSerializer.class)
public abstract class FacetFilters implements CompoundType {

  public static FacetFilters of(List<MixedSearchFilters> inside) {
    return new FacetFiltersListOfMixedSearchFilters(inside);
  }

  public static FacetFilters of(String inside) {
    return new FacetFiltersString(inside);
  }

  public static class FacetFiltersSerializer extends StdSerializer<FacetFilters> {

    public FacetFiltersSerializer(Class<FacetFilters> t) {
      super(t);
    }

    public FacetFiltersSerializer() {
      this(null);
    }

    @Override
    public void serialize(FacetFilters value, JsonGenerator jgen, SerializerProvider provider) throws IOException, JsonProcessingException {
      jgen.writeObject(value.getInsideValue());
    }
  }

  public static class FacetFiltersDeserializer extends StdDeserializer<FacetFilters> {

    public FacetFiltersDeserializer() {
      this(FacetFilters.class);
    }

    public FacetFiltersDeserializer(Class<?> vc) {
      super(vc);
    }

    @Override
    public FacetFilters deserialize(JsonParser jp, DeserializationContext ctxt) throws IOException, JsonProcessingException {
      JsonNode tree = jp.readValueAsTree();
      FacetFilters deserialized = null;

      int match = 0;
      JsonToken token = tree.traverse(jp.getCodec()).nextToken();
      String currentType = "";
      // deserialize List<MixedSearchFilters>
      try {
        boolean attemptParsing = true;
        currentType = "List<MixedSearchFilters>";
        if (
          ((currentType.equals("Integer") || currentType.equals("Long")) && token == JsonToken.VALUE_NUMBER_INT) |
          ((currentType.equals("Float") || currentType.equals("Double")) && token == JsonToken.VALUE_NUMBER_FLOAT) |
          (currentType.equals("Boolean") && (token == JsonToken.VALUE_FALSE || token == JsonToken.VALUE_TRUE)) |
          (currentType.equals("String") && token == JsonToken.VALUE_STRING) |
          (currentType.startsWith("List<") && token == JsonToken.START_ARRAY)
        ) {
          deserialized =
            FacetFilters.of(
              (List<MixedSearchFilters>) tree.traverse(jp.getCodec()).readValueAs(new TypeReference<List<MixedSearchFilters>>() {})
            );
          match++;
        } else if (token == JsonToken.START_OBJECT) {
          try {
            deserialized =
              FacetFilters.of(
                (List<MixedSearchFilters>) tree.traverse(jp.getCodec()).readValueAs(new TypeReference<List<MixedSearchFilters>>() {})
              );
            match++;
          } catch (IOException e) {
            // do nothing
          }
        }
      } catch (Exception e) {
        // deserialization failed, continue
        System.err.println(
          "Failed to deserialize oneOf List<MixedSearchFilters> (error: " + e.getMessage() + ") (type: " + currentType + ")"
        );
      }

      // deserialize String
      try {
        boolean attemptParsing = true;
        currentType = "String";
        if (
          ((currentType.equals("Integer") || currentType.equals("Long")) && token == JsonToken.VALUE_NUMBER_INT) |
          ((currentType.equals("Float") || currentType.equals("Double")) && token == JsonToken.VALUE_NUMBER_FLOAT) |
          (currentType.equals("Boolean") && (token == JsonToken.VALUE_FALSE || token == JsonToken.VALUE_TRUE)) |
          (currentType.equals("String") && token == JsonToken.VALUE_STRING) |
          (currentType.startsWith("List<") && token == JsonToken.START_ARRAY)
        ) {
          deserialized = FacetFilters.of((String) tree.traverse(jp.getCodec()).readValueAs(new TypeReference<String>() {}));
          match++;
        } else if (token == JsonToken.START_OBJECT) {
          try {
            deserialized = FacetFilters.of((String) tree.traverse(jp.getCodec()).readValueAs(new TypeReference<String>() {}));
            match++;
          } catch (IOException e) {
            // do nothing
          }
        }
      } catch (Exception e) {
        // deserialization failed, continue
        System.err.println("Failed to deserialize oneOf String (error: " + e.getMessage() + ") (type: " + currentType + ")");
      }

      if (match == 1) {
        return deserialized;
      }
      throw new IOException(String.format("Failed deserialization for FacetFilters: %d classes match result, expected 1", match));
    }

    /** Handle deserialization of the 'null' value. */
    @Override
    public FacetFilters getNullValue(DeserializationContext ctxt) throws JsonMappingException {
      throw new JsonMappingException(ctxt.getParser(), "FacetFilters cannot be null");
    }
  }
}

class FacetFiltersListOfMixedSearchFilters extends FacetFilters {

  private final List<MixedSearchFilters> insideValue;

  FacetFiltersListOfMixedSearchFilters(List<MixedSearchFilters> insideValue) {
    this.insideValue = insideValue;
  }

  @Override
  public List<MixedSearchFilters> getInsideValue() {
    return insideValue;
  }
}

class FacetFiltersString extends FacetFilters {

  private final String insideValue;

  FacetFiltersString(String insideValue) {
    this.insideValue = insideValue;
  }

  @Override
  public String getInsideValue() {
    return insideValue;
  }
}