// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost
// - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.

package com.algolia.model.search;

import com.algolia.exceptions.AlgoliaRuntimeException;
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
import java.util.logging.Logger;

/** AttributeToUpdate */
@JsonDeserialize(using = AttributeToUpdate.AttributeToUpdateDeserializer.class)
@JsonSerialize(using = AttributeToUpdate.AttributeToUpdateSerializer.class)
public abstract class AttributeToUpdate implements CompoundType {

  private static final Logger LOGGER = Logger.getLogger(AttributeToUpdate.class.getName());

  public static AttributeToUpdate of(BuiltInOperation inside) {
    return new AttributeToUpdateBuiltInOperation(inside);
  }

  public static AttributeToUpdate of(String inside) {
    return new AttributeToUpdateString(inside);
  }

  public static class AttributeToUpdateSerializer extends StdSerializer<AttributeToUpdate> {

    public AttributeToUpdateSerializer(Class<AttributeToUpdate> t) {
      super(t);
    }

    public AttributeToUpdateSerializer() {
      this(null);
    }

    @Override
    public void serialize(AttributeToUpdate value, JsonGenerator jgen, SerializerProvider provider)
      throws IOException, JsonProcessingException {
      jgen.writeObject(value.getInsideValue());
    }
  }

  public static class AttributeToUpdateDeserializer extends StdDeserializer<AttributeToUpdate> {

    public AttributeToUpdateDeserializer() {
      this(AttributeToUpdate.class);
    }

    public AttributeToUpdateDeserializer(Class<?> vc) {
      super(vc);
    }

    @Override
    public AttributeToUpdate deserialize(JsonParser jp, DeserializationContext ctxt) throws IOException {
      JsonNode tree = jp.readValueAsTree();

      // deserialize BuiltInOperation
      if (tree.isObject()) {
        try (JsonParser parser = tree.traverse(jp.getCodec())) {
          BuiltInOperation value = parser.readValueAs(new TypeReference<BuiltInOperation>() {});
          return AttributeToUpdate.of(value);
        } catch (Exception e) {
          // deserialization failed, continue
          LOGGER.finest("Failed to deserialize oneOf BuiltInOperation (error: " + e.getMessage() + ") (type: BuiltInOperation)");
        }
      }

      // deserialize String
      if (tree.isValueNode()) {
        try (JsonParser parser = tree.traverse(jp.getCodec())) {
          String value = parser.readValueAs(new TypeReference<String>() {});
          return AttributeToUpdate.of(value);
        } catch (Exception e) {
          // deserialization failed, continue
          LOGGER.finest("Failed to deserialize oneOf String (error: " + e.getMessage() + ") (type: String)");
        }
      }
      throw new AlgoliaRuntimeException(String.format("Failed to deserialize json element: %s", tree));
    }

    /** Handle deserialization of the 'null' value. */
    @Override
    public AttributeToUpdate getNullValue(DeserializationContext ctxt) throws JsonMappingException {
      throw new JsonMappingException(ctxt.getParser(), "AttributeToUpdate cannot be null");
    }
  }
}

class AttributeToUpdateBuiltInOperation extends AttributeToUpdate {

  private final BuiltInOperation insideValue;

  AttributeToUpdateBuiltInOperation(BuiltInOperation insideValue) {
    this.insideValue = insideValue;
  }

  @Override
  public BuiltInOperation getInsideValue() {
    return insideValue;
  }
}

class AttributeToUpdateString extends AttributeToUpdate {

  private final String insideValue;

  AttributeToUpdateString(String insideValue) {
    this.insideValue = insideValue;
  }

  @Override
  public String getInsideValue() {
    return insideValue;
  }
}