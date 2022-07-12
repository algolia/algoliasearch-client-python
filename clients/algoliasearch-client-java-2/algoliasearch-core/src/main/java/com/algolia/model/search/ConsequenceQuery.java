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

/**
 * When providing a string, it replaces the entire query string. When providing an object, it
 * describes incremental edits to be made to the query string (but you can't do both).
 */
@JsonDeserialize(using = ConsequenceQuery.ConsequenceQueryDeserializer.class)
@JsonSerialize(using = ConsequenceQuery.ConsequenceQuerySerializer.class)
public abstract class ConsequenceQuery implements CompoundType {

  public static ConsequenceQuery of(ConsequenceQueryObject inside) {
    return new ConsequenceQueryConsequenceQueryObject(inside);
  }

  public static ConsequenceQuery of(String inside) {
    return new ConsequenceQueryString(inside);
  }

  public static class ConsequenceQuerySerializer extends StdSerializer<ConsequenceQuery> {

    public ConsequenceQuerySerializer(Class<ConsequenceQuery> t) {
      super(t);
    }

    public ConsequenceQuerySerializer() {
      this(null);
    }

    @Override
    public void serialize(ConsequenceQuery value, JsonGenerator jgen, SerializerProvider provider)
      throws IOException, JsonProcessingException {
      jgen.writeObject(value.getInsideValue());
    }
  }

  public static class ConsequenceQueryDeserializer extends StdDeserializer<ConsequenceQuery> {

    public ConsequenceQueryDeserializer() {
      this(ConsequenceQuery.class);
    }

    public ConsequenceQueryDeserializer(Class<?> vc) {
      super(vc);
    }

    @Override
    public ConsequenceQuery deserialize(JsonParser jp, DeserializationContext ctxt) throws IOException, JsonProcessingException {
      JsonNode tree = jp.readValueAsTree();
      ConsequenceQuery deserialized = null;

      int match = 0;
      JsonToken token = tree.traverse(jp.getCodec()).nextToken();
      String currentType = "";
      // deserialize ConsequenceQueryObject
      try {
        boolean attemptParsing = true;
        currentType = "ConsequenceQueryObject";
        if (
          ((currentType.equals("Integer") || currentType.equals("Long")) && token == JsonToken.VALUE_NUMBER_INT) |
          ((currentType.equals("Float") || currentType.equals("Double")) && token == JsonToken.VALUE_NUMBER_FLOAT) |
          (currentType.equals("Boolean") && (token == JsonToken.VALUE_FALSE || token == JsonToken.VALUE_TRUE)) |
          (currentType.equals("String") && token == JsonToken.VALUE_STRING) |
          (currentType.startsWith("List<") && token == JsonToken.START_ARRAY)
        ) {
          deserialized =
            ConsequenceQuery.of(
              (ConsequenceQueryObject) tree.traverse(jp.getCodec()).readValueAs(new TypeReference<ConsequenceQueryObject>() {})
            );
          match++;
        } else if (token == JsonToken.START_OBJECT) {
          try {
            deserialized =
              ConsequenceQuery.of(
                (ConsequenceQueryObject) tree.traverse(jp.getCodec()).readValueAs(new TypeReference<ConsequenceQueryObject>() {})
              );
            match++;
          } catch (IOException e) {
            // do nothing
          }
        }
      } catch (Exception e) {
        // deserialization failed, continue
        System.err.println(
          "Failed to deserialize oneOf ConsequenceQueryObject (error: " + e.getMessage() + ") (type: " + currentType + ")"
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
          deserialized = ConsequenceQuery.of((String) tree.traverse(jp.getCodec()).readValueAs(new TypeReference<String>() {}));
          match++;
        } else if (token == JsonToken.START_OBJECT) {
          try {
            deserialized = ConsequenceQuery.of((String) tree.traverse(jp.getCodec()).readValueAs(new TypeReference<String>() {}));
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
      throw new IOException(String.format("Failed deserialization for ConsequenceQuery: %d classes match result, expected 1", match));
    }

    /** Handle deserialization of the 'null' value. */
    @Override
    public ConsequenceQuery getNullValue(DeserializationContext ctxt) throws JsonMappingException {
      throw new JsonMappingException(ctxt.getParser(), "ConsequenceQuery cannot be null");
    }
  }
}

class ConsequenceQueryConsequenceQueryObject extends ConsequenceQuery {

  private final ConsequenceQueryObject insideValue;

  ConsequenceQueryConsequenceQueryObject(ConsequenceQueryObject insideValue) {
    this.insideValue = insideValue;
  }

  @Override
  public ConsequenceQueryObject getInsideValue() {
    return insideValue;
  }
}

class ConsequenceQueryString extends ConsequenceQuery {

  private final String insideValue;

  ConsequenceQueryString(String insideValue) {
    this.insideValue = insideValue;
  }

  @Override
  public String getInsideValue() {
    return insideValue;
  }
}