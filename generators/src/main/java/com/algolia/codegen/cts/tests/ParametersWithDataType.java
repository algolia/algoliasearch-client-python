package com.algolia.codegen.cts.tests;

import com.algolia.codegen.Utils;
import com.algolia.codegen.exceptions.*;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import io.swagger.util.Json;
import java.util.*;
import java.util.Map.Entry;
import java.util.stream.Collectors;
import org.apache.commons.lang3.StringUtils;
import org.openapitools.codegen.CodegenComposedSchemas;
import org.openapitools.codegen.CodegenModel;
import org.openapitools.codegen.CodegenOperation;
import org.openapitools.codegen.CodegenParameter;
import org.openapitools.codegen.CodegenProperty;
import org.openapitools.codegen.CodegenResponse;
import org.openapitools.codegen.IJsonSchemaValidationProperties;

@SuppressWarnings("unchecked")
public class ParametersWithDataType {

  private final Map<String, CodegenModel> models;
  private final String language;

  public ParametersWithDataType(Map<String, CodegenModel> models, String language) {
    this.models = models;
    this.language = language;
  }

  public void enhanceParameters(Map<String, Object> parameters, Map<String, Object> bundle)
    throws CTSException, JsonMappingException, JsonProcessingException {
    this.enhanceParameters(parameters, bundle, null);
  }

  /**
   * @param parameters The object to traverse and annotate with type
   * @param bundle The output object
   * @param operation (optional) The model in which to look for spec
   * @param spec (optional) (mutually exclusive with operation) If the parameter is a root param,
   *     the spec must be provided, alongside it's paramName
   * @param paramName (optional) (required if spec) the parameter name
   */
  public void enhanceParameters(Map<String, Object> parameters, Map<String, Object> bundle, CodegenOperation operation)
    throws CTSException, JsonMappingException, JsonProcessingException {
    if (parameters != null && parameters.size() == 0) {
      bundle.put("parameters", "{}");
      return;
    }
    IJsonSchemaValidationProperties spec = null;
    String paramName = null;
    // special case if there is only bodyParam which is not an array
    if (operation != null && operation.allParams.size() == 1 && operation.bodyParams.size() == 1 && !operation.bodyParam.isArray) {
      spec = operation.bodyParam;
      paramName = operation.bodyParam.paramName;
    }

    List<Map<String, Object>> parametersWithDataType = new ArrayList<>();
    Map<String, Object> parametersWithDataTypeMap = new HashMap<>();

    if (paramName == null) {
      if (parameters != null) {
        for (Entry<String, Object> param : parameters.entrySet()) {
          CodegenParameter specParam = null;
          if (operation != null) {
            for (CodegenParameter sp : operation.allParams) {
              if (sp.paramName.equals(param.getKey())) {
                specParam = sp;
                break;
              }
            }
            if (specParam == null) {
              throw new CTSException("Parameter " + param.getKey() + " not found in the root parameter");
            }
          }
          Map<String, Object> paramWithType = traverseParams(param.getKey(), param.getValue(), specParam, "", 0);
          parametersWithDataType.add(paramWithType);
          parametersWithDataTypeMap.put((String) paramWithType.get("key"), paramWithType);
        }
      }
    } else {
      Map<String, Object> paramWithType = traverseParams(paramName, parameters, spec, "", 0);
      parametersWithDataType.add(paramWithType);
      parametersWithDataTypeMap.put((String) paramWithType.get("key"), paramWithType);
    }

    // Give the stringified version to mustache, for js
    bundle.put("parameters", Json.mapper().writeValueAsString(parameters));
    bundle.put("parametersWithDataType", parametersWithDataType);
    // Also provide a map version for those who know which keys to look for
    bundle.put("parametersWithDataTypeMap", parametersWithDataTypeMap);
  }

  private Map<String, Object> traverseParams(
    String paramName,
    Object param,
    IJsonSchemaValidationProperties spec,
    String parent,
    int suffix
  ) throws CTSException {
    if (spec == null) {
      return traverseParams(paramName, param, parent, suffix);
    }
    String baseType = getTypeName(spec);
    if (baseType == null) {
      throw new CTSException("Cannot determine type of " + paramName + " (value: " + param + ")");
    }

    boolean isCodegenModel = spec instanceof CodegenModel;

    if (!isCodegenModel) {
      // don't overwrite it if it's already a model sometimes it's in lowercase for some reason
      String lowerBaseType = baseType.substring(0, 1).toLowerCase() + baseType.substring(1);
      if (models.containsKey(baseType)) {
        // get the real model if possible
        spec = models.get(baseType);
      } else if (models.containsKey(lowerBaseType)) {
        spec = models.get(lowerBaseType);
      }
      isCodegenModel = spec instanceof CodegenModel;
    }

    String finalParamName = paramName;
    if (language.equals("java") && paramName.startsWith("_")) {
      finalParamName = paramName.substring(1);
    }

    // type is a reserved keyword in go, we need to add more generic way to handle reversed keywords
    // for all languages.
    if (language.equals("go") && paramName.equals("type")) {
      finalParamName = "type_";
    }

    Map<String, Object> testOutput = createDefaultOutput();
    testOutput.put("key", finalParamName);
    testOutput.put("isKeyAllUpperCase", StringUtils.isAllUpperCase(finalParamName));
    testOutput.put("parentSuffix", suffix - 1);
    testOutput.put("useAnonymousKey", !finalParamName.matches("(.*)_[0-9]$") && suffix != 0);
    testOutput.put("suffix", suffix);
    testOutput.put("parent", parent);
    testOutput.put("objectName", Utils.capitalize(baseType));

    if (param == null) {
      handleNull(testOutput);
    } else if (spec.getIsArray()) {
      handleArray(paramName, param, testOutput, spec, suffix);
    } else if (isEnum(spec)) {
      handleEnum(param, testOutput);
    } else if (spec.getIsModel() || isCodegenModel) {
      // recursive object
      handleModel(paramName, param, testOutput, spec, baseType, parent, suffix);
    } else if (baseType.equals("Object")) {
      // not var, no item, pure free form
      handleObject(paramName, param, testOutput, suffix);
    } else if (spec.getIsMap()) {
      // free key but only one type
      handleMap(paramName, param, testOutput, spec, suffix);
    } else {
      handlePrimitive(param, testOutput, spec);
    }
    return testOutput;
  }

  /** Same method but with inference only */
  private Map<String, Object> traverseParams(String paramName, Object param, String parent, int suffix) throws CTSException {
    String finalParamName = paramName;
    if (language.equals("java") && paramName.startsWith("_")) {
      finalParamName = paramName.substring(1);
    }

    Map<String, Object> testOutput = createDefaultOutput();
    testOutput.put("key", finalParamName);
    testOutput.put("parentSuffix", suffix - 1);
    testOutput.put("useAnonymousKey", !finalParamName.matches("(.*)_[0-9]$") && suffix != 0);
    testOutput.put("suffix", suffix);
    testOutput.put("parent", parent);
    // cannot determine objectName with inference
    // testOutput.put("objectName", Utils.capitalize(baseType));

    if (param == null) {
      handleNull(testOutput);
    } else if (param instanceof List) {
      handleArray(paramName, param, testOutput, null, suffix);
    } else if (param instanceof Map) {
      handleObject(paramName, param, testOutput, suffix);
    } else {
      handlePrimitive(param, testOutput, null);
    }
    return testOutput;
  }

  private Map<String, Object> createDefaultOutput() {
    Map<String, Object> testOutput = new HashMap<>();

    // we need to set all types to false otherwise mustache will read the one from the parent
    // context and run into a infinite loop
    testOutput.put("isObject", false);
    testOutput.put("isArray", false);
    testOutput.put("isNull", false);
    testOutput.put("isFreeFormObject", false);
    testOutput.put("isAnyType", false);
    testOutput.put("isString", false);
    testOutput.put("isInteger", false);
    testOutput.put("isLong", false);
    testOutput.put("isDouble", false);
    testOutput.put("isNumber", false);
    testOutput.put("isBoolean", false);
    testOutput.put("isEnum", false);
    testOutput.put("isSimpleObject", false);
    testOutput.put("oneOfModel", false);
    testOutput.put("isAdditionalProperty", false);

    return testOutput;
  }

  private void handleNull(Map<String, Object> testOutput) {
    testOutput.put("isNull", true);
  }

  private void handleArray(
    String paramName,
    Object param,
    Map<String, Object> testOutput,
    IJsonSchemaValidationProperties spec,
    int suffix
  ) throws CTSException {
    List<Object> items = (List<Object>) param;

    List<Object> values = new ArrayList<>();
    for (int i = 0; i < items.size(); i++) {
      values.add(traverseParams(paramName + "_" + i, items.get(i), spec == null ? null : spec.getItems(), paramName, suffix + 1));
    }

    testOutput.put("isArray", true);
    testOutput.put("value", values);
  }

  private void handleEnum(Object param, Map<String, Object> testOutput) {
    testOutput.put("isEnum", true);
    testOutput.put("value", param);
    testOutput.put("valueEscaped", param + "_");
  }

  private void handleModel(
    String paramName,
    Object param,
    Map<String, Object> testOutput,
    IJsonSchemaValidationProperties spec,
    String baseType,
    String parent,
    int suffix
  ) throws CTSException {
    if (!spec.getHasVars()) {
      // In this case we might have a complex `allOf`, we will first check if it exists
      CodegenComposedSchemas composedSchemas = spec.getComposedSchemas();

      if (composedSchemas != null) {
        List<CodegenProperty> allOf = composedSchemas.getAllOf();

        if (allOf != null && !allOf.isEmpty()) {
          traverseParams(paramName, param, allOf.get(0), parent, suffix);

          return;
        }
      }
      // We only throw if there is no `composedSchemas`, because `oneOf` can also be handled below
      else {
        throw new CTSException("Spec has no vars.");
      }
    }

    if (spec.getItems() != null) {
      throw new CTSException("Spec has items.");
    }

    if (spec instanceof CodegenModel && ((CodegenModel) spec).oneOf.size() > 0) {
      // find a discriminator to handle oneOf
      CodegenModel model = (CodegenModel) spec;
      IJsonSchemaValidationProperties match = findMatchingOneOf(param, model);
      testOutput.clear();
      testOutput.putAll(traverseParams(paramName, param, match, parent, suffix));

      HashMap<String, Object> oneOfModel = new HashMap<>();
      IJsonSchemaValidationProperties current = match;
      String typeName = getTypeName(current);
      StringBuilder capitalizedTypeName = new StringBuilder(typeName);
      while (current.getItems() != null) {
        current = current.getItems();
        typeName += "Of" + getTypeName(current);
        capitalizedTypeName.append("Of").append(StringUtils.capitalize(getTypeName(current)));
      }

      boolean useExplicitName = false;
      CodegenComposedSchemas composedSchemas = model.getComposedSchemas();
      if (composedSchemas != null && composedSchemas.getOneOf() != null && composedSchemas.getOneOf().size() > 0) {
        useExplicitName =
        Utils.shouldUseExplicitOneOfName(composedSchemas.getOneOf().stream().map(x -> getTypeName(x)).collect(Collectors.toList()));
      } else {
        useExplicitName = Utils.shouldUseExplicitOneOfName(model.oneOf);
      }

      oneOfModel.put("parentClassName", Utils.capitalize(baseType));
      oneOfModel.put("type", typeName);
      oneOfModel.put("type-capitalized", capitalizedTypeName.toString());
      oneOfModel.put("x-one-of-explicit-name", useExplicitName);
      testOutput.put("oneOfModel", oneOfModel);
      return;
    }

    Map<String, Object> vars = (Map<String, Object>) param;
    List<Object> values = new ArrayList<>();
    for (Entry<String, Object> entry : vars.entrySet()) {
      IJsonSchemaValidationProperties varSpec = null;
      for (CodegenProperty vs : spec.getVars()) {
        if (vs.baseName.equals(entry.getKey())) {
          varSpec = vs;
          break;
        }
      }
      if (varSpec == null) {
        if (spec.getAdditionalPropertiesIsAnyType()) {
          // we hit an additionalProperties, infer it's type
          CodegenParameter additionalPropertiesSpec = new CodegenParameter();
          additionalPropertiesSpec.dataType = inferDataType(entry.getValue(), additionalPropertiesSpec, null);
          Map<String, Object> value = traverseParams(entry.getKey(), entry.getValue(), additionalPropertiesSpec, paramName, suffix + 1);
          value.put("isAdditionalProperty", true);
          values.add(value);
        } else {
          throw new CTSException(
            "Parameter '" +
            entry.getKey() +
            "' not found in '" +
            paramName +
            "'. Available properties are: " +
            spec.getVars().stream().map(v -> v.baseName).collect(Collectors.joining(", ")) +
            (spec.getAdditionalPropertiesIsAnyType() ? " (and any additional properties)" : "") +
            ". Or you might have a type conflict in the spec for '" +
            baseType +
            "'"
          );
        }
      } else {
        values.add(traverseParams(entry.getKey(), entry.getValue(), varSpec, paramName, suffix + 1));
      }
    }
    testOutput.put("isObject", true);
    testOutput.put("value", values);
  }

  private void handleObject(String paramName, Object param, Map<String, Object> testOutput, int suffix) throws CTSException {
    Map<String, Object> vars = (Map<String, Object>) param;

    List<Object> values = new ArrayList<>();
    for (Entry<String, Object> entry : vars.entrySet()) {
      CodegenParameter objSpec = new CodegenParameter();
      objSpec.dataType = inferDataType(entry.getValue(), objSpec, null);
      values.add(traverseParams(entry.getKey(), entry.getValue(), objSpec, paramName, suffix + 1));
    }
    // sometimes it's really just an object
    if (testOutput.getOrDefault("objectName", "").equals("Object")) {
      testOutput.put("isSimpleObject", true);
    }

    testOutput.put("isFreeFormObject", true);
    testOutput.put("value", values);
  }

  private void handleMap(String paramName, Object param, Map<String, Object> testOutput, IJsonSchemaValidationProperties spec, int suffix)
    throws CTSException {
    if (spec.getHasVars()) {
      throw new CTSException("Spec has vars.");
    }

    Map<String, Object> vars = (Map<String, Object>) param;

    List<Object> values = new ArrayList<>();

    CodegenProperty items = spec.getItems();

    for (Entry<String, Object> entry : vars.entrySet()) {
      IJsonSchemaValidationProperties itemType = items;

      // The generator consider a free form object type as an `object`, which
      // is wrong in our case, so we infer it to explore the right path in the traverseParams
      // function, but we keep the any type for the CTS.
      if (items == null || (items.openApiType.equals("object") && items.isFreeFormObject)) {
        CodegenParameter maybeMatch = new CodegenParameter();
        String paramType = inferDataType(entry.getValue(), maybeMatch, null);

        maybeMatch.dataType = paramType;
        maybeMatch.isAnyType = true;
        itemType = maybeMatch;
      }

      values.add(traverseParams(entry.getKey(), entry.getValue(), itemType, paramName, suffix + 1));
    }

    testOutput.put("isFreeFormObject", true);
    testOutput.put("value", values);
  }

  private void handlePrimitive(Object param, Map<String, Object> testOutput, IJsonSchemaValidationProperties spec) throws CTSException {
    if (spec != null && isPrimitiveType(spec)) {
      transferPrimitiveData(spec, testOutput);
    } else {
      inferDataType(param, null, testOutput);
      if (isAnyType(spec)) {
        testOutput.put("isAnyType", true);
      }
    }
    testOutput.put("value", param);
  }

  private String getTypeName(IJsonSchemaValidationProperties param) {
    if (param instanceof CodegenParameter) {
      return ((CodegenParameter) param).dataType;
    }
    if (param instanceof CodegenProperty) {
      return ((CodegenProperty) param).dataType;
    }
    if (param instanceof CodegenModel) {
      return ((CodegenModel) param).classname;
    }
    if (param instanceof CodegenResponse) {
      return ((CodegenResponse) param).dataType;
    }
    return null;
  }

  private boolean isAnyType(IJsonSchemaValidationProperties param) {
    if (param instanceof CodegenParameter) {
      return ((CodegenParameter) param).isAnyType;
    }
    if (param instanceof CodegenProperty) {
      return ((CodegenProperty) param).isAnyType;
    }
    if (param instanceof CodegenResponse) {
      return ((CodegenResponse) param).isAnyType;
    }
    return false;
  }

  private boolean isEnum(IJsonSchemaValidationProperties param) {
    if (param instanceof CodegenParameter) {
      return ((CodegenParameter) param).isEnum;
    }
    if (param instanceof CodegenProperty) {
      return ((CodegenProperty) param).isEnum;
    }
    if (param instanceof CodegenModel) {
      return ((CodegenModel) param).isEnum;
    }
    return false;
  }

  private boolean isPrimitiveType(IJsonSchemaValidationProperties param) {
    if (param instanceof CodegenParameter) {
      return ((CodegenParameter) param).isPrimitiveType;
    }
    if (param instanceof CodegenProperty) {
      return ((CodegenProperty) param).isPrimitiveType;
    }
    return false;
  }

  private String inferDataType(Object param, CodegenParameter spec, Map<String, Object> output) throws CTSException {
    switch (param.getClass().getSimpleName()) {
      case "String":
        if (spec != null) spec.setIsString(true);
        if (output != null) output.put("isString", true);
        return "String";
      case "Integer":
        if (spec != null) spec.setIsNumber(true);
        if (output != null) {
          output.put("isInteger", true);
          output.put("isNumber", true);
        }
        return "Integer";
      case "Long":
        if (spec != null) spec.setIsNumber(true);
        if (output != null) {
          output.put("isLong", true);
          output.put("isNumber", true);
        }
        return "Long";
      case "Double":
        if (spec != null) spec.setIsNumber(true);
        if (output != null) {
          output.put("isDouble", true);
          output.put("isNumber", true);
        }
        return "Double";
      case "Boolean":
        if (spec != null) spec.setIsBoolean(true);
        if (output != null) output.put("isBoolean", true);
        return "Boolean";
      case "ArrayList":
        if (spec != null) {
          spec.setIsArray(true);
          // This is just to find the correct path in `handlePrimitive`, but it's not always the
          // real type
          CodegenProperty baseItems = new CodegenProperty();
          baseItems.dataType = "String";
          spec.setItems(baseItems);
        }
        if (output != null) output.put("isArray", true);
        return "List";
      case "LinkedHashMap":
        if (spec != null) spec.baseType = "Object";
        if (output != null) output.put("isFreeFormObject", true);
        return "Object";
      default:
        throw new CTSException("Unknown type: " + param.getClass().getSimpleName());
    }
  }

  private void transferPrimitiveData(IJsonSchemaValidationProperties spec, Map<String, Object> output) throws CTSException {
    switch (getTypeName(spec)) {
      case "String":
        output.put("isString", true);
        break;
      case "Integer":
        output.put("isInteger", true);
        output.put("isNumber", true);
        break;
      case "Long":
        output.put("isLong", true);
        output.put("isNumber", true);
        break;
      case "Double":
        output.put("isDouble", true);
        output.put("isNumber", true);
        break;
      case "Boolean":
        output.put("isBoolean", true);
        break;
      default:
        throw new CTSException("Unknown primitive: " + getTypeName(spec));
    }
  }

  private IJsonSchemaValidationProperties findMatchingOneOf(Object param, CodegenModel model) throws CTSException {
    if (param instanceof Map) {
      // for object, check which has the most of property in common
      int maxCount = 0;
      CodegenModel bestOneOf = model.interfaceModels.get(0);
      for (CodegenModel oneOf : model.interfaceModels) {
        if (oneOf.vars.size() == 0) {
          continue;
        }

        Map<String, Object> map = (Map<String, Object>) param;
        int commonCount = 0;
        for (String prop : map.keySet()) {
          for (CodegenProperty propOneOf : oneOf.vars) {
            if (prop.equals(propOneOf.name) && couldMatchEnum(map.get(prop), propOneOf)) {
              commonCount++;
            }
          }
        }
        if (commonCount > maxCount) {
          maxCount = commonCount;
          bestOneOf = oneOf;
        }
      }
      return bestOneOf;
    }
    if (param instanceof List) {
      CodegenComposedSchemas composedSchemas = model.getComposedSchemas();

      if (composedSchemas != null) {
        List<CodegenProperty> oneOf = composedSchemas.getOneOf();

        // Somehow this is not yet enough
        if (oneOf != null && !oneOf.isEmpty()) {
          System.out.println("Choosing the first oneOf by default: " + oneOf.get(0).name + " (this won't stay correct forever)");
          return oneOf.get(0);
        }
      }

      return null;
    }

    CodegenParameter maybeMatch = new CodegenParameter();
    String paramType = inferDataType(param, maybeMatch, null);
    maybeMatch.dataType = paramType;

    boolean hasFloat = false;
    for (String oneOfName : model.oneOf) {
      if (oneOfName.equals(paramType)) {
        return maybeMatch;
      }
      if (oneOfName.equals("Float") || oneOfName.equals("Double")) {
        hasFloat = true;
      }
    }

    // If there is a number, try to use it as other number type, in the order
    // Integer, Long, Float, Double
    if (hasFloat && (paramType.equals("Integer") || paramType.equals("Long") || paramType.equals("Double"))) {
      return maybeMatch;
    }

    for (CodegenModel oneOf : model.interfaceModels) {
      // Somehow the dataType can be in lower case?
      if (oneOf.dataType.toLowerCase().equals(paramType.toLowerCase())) {
        return oneOf;
      }
    }
    return null;
  }

  // If the model is an enum and contains a valid list of allowed values,
  // it will check that 'value' is in the list.
  // Otherwise return true by default to avoid false negative.
  private boolean couldMatchEnum(Object value, CodegenProperty model) {
    if (!model.getIsEnumOrRef() || model.allowableValues == null || !model.allowableValues.containsKey("values")) return true;
    Object values = model.allowableValues.get("values");
    if (!(values instanceof List)) return true;

    return ((List) values).contains(value);
  }
}
