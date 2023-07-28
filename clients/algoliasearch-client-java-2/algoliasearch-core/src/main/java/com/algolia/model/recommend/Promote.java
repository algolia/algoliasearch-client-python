// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost
// - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.

package com.algolia.model.recommend;

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

/** Promote */
@JsonDeserialize(using = Promote.PromoteDeserializer.class)
@JsonSerialize(using = Promote.PromoteSerializer.class)
public abstract class Promote implements CompoundType {

  private static final Logger LOGGER = Logger.getLogger(Promote.class.getName());

  public static Promote of(PromoteObjectID inside) {
    return new PromotePromoteObjectID(inside);
  }

  public static Promote of(PromoteObjectIDs inside) {
    return new PromotePromoteObjectIDs(inside);
  }

  public static class PromoteSerializer extends StdSerializer<Promote> {

    public PromoteSerializer(Class<Promote> t) {
      super(t);
    }

    public PromoteSerializer() {
      this(null);
    }

    @Override
    public void serialize(Promote value, JsonGenerator jgen, SerializerProvider provider) throws IOException, JsonProcessingException {
      jgen.writeObject(value.getInsideValue());
    }
  }

  public static class PromoteDeserializer extends StdDeserializer<Promote> {

    public PromoteDeserializer() {
      this(Promote.class);
    }

    public PromoteDeserializer(Class<?> vc) {
      super(vc);
    }

    @Override
    public Promote deserialize(JsonParser jp, DeserializationContext ctxt) throws IOException {
      JsonNode tree = jp.readValueAsTree();

      // deserialize PromoteObjectID
      if (tree.isObject()) {
        try (JsonParser parser = tree.traverse(jp.getCodec())) {
          PromoteObjectID value = parser.readValueAs(new TypeReference<PromoteObjectID>() {});
          return Promote.of(value);
        } catch (Exception e) {
          // deserialization failed, continue
          LOGGER.finest("Failed to deserialize oneOf PromoteObjectID (error: " + e.getMessage() + ") (type: PromoteObjectID)");
        }
      }

      // deserialize PromoteObjectIDs
      if (tree.isObject()) {
        try (JsonParser parser = tree.traverse(jp.getCodec())) {
          PromoteObjectIDs value = parser.readValueAs(new TypeReference<PromoteObjectIDs>() {});
          return Promote.of(value);
        } catch (Exception e) {
          // deserialization failed, continue
          LOGGER.finest("Failed to deserialize oneOf PromoteObjectIDs (error: " + e.getMessage() + ") (type: PromoteObjectIDs)");
        }
      }
      throw new AlgoliaRuntimeException(String.format("Failed to deserialize json element: %s", tree));
    }

    /** Handle deserialization of the 'null' value. */
    @Override
    public Promote getNullValue(DeserializationContext ctxt) throws JsonMappingException {
      throw new JsonMappingException(ctxt.getParser(), "Promote cannot be null");
    }
  }
}

class PromotePromoteObjectID extends Promote {

  private final PromoteObjectID insideValue;

  PromotePromoteObjectID(PromoteObjectID insideValue) {
    this.insideValue = insideValue;
  }

  @Override
  public PromoteObjectID getInsideValue() {
    return insideValue;
  }
}

class PromotePromoteObjectIDs extends Promote {

  private final PromoteObjectIDs insideValue;

  PromotePromoteObjectIDs(PromoteObjectIDs insideValue) {
    this.insideValue = insideValue;
  }

  @Override
  public PromoteObjectIDs getInsideValue() {
    return insideValue;
  }
}
