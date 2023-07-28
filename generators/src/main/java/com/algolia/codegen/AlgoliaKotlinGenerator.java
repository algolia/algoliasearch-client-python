package com.algolia.codegen;

import com.algolia.codegen.exceptions.GeneratorException;
import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.oas.models.servers.Server;
import java.io.File;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import org.apache.commons.lang3.StringUtils;
import org.openapitools.codegen.*;
import org.openapitools.codegen.languages.KotlinClientCodegen;
import org.openapitools.codegen.model.ModelMap;
import org.openapitools.codegen.model.ModelsMap;
import org.openapitools.codegen.model.OperationsMap;

public class AlgoliaKotlinGenerator extends KotlinClientCodegen {

  @Override
  public String getName() {
    return "algolia-kotlin";
  }

  @Override
  public void processOpts() {
    // generator specific options
    setLibrary("multiplatform");
    setApiPackage("api");
    setApiSuffix(Utils.API_SUFFIX);
    setGroupId("com.algolia");
    setArtifactId("algoliasearch-client-kotlin");
    setApiPackage("com.algolia.client.api");
    setPackageName("com.algolia.client");
    String client = (String) additionalProperties.get("client");
    setModelPackage("com.algolia.client.model." + Utils.camelize(client).toLowerCase());
    additionalProperties.put(CodegenConstants.SOURCE_FOLDER, "client/src/commonMain/kotlin");

    super.processOpts();

    // Generation notice, added on every generated files
    Utils.setGenerationBanner(additionalProperties);

    // Remove auth files
    supportingFiles.removeIf(file -> file.getTemplateFile().contains("auth"));

    // Search config
    additionalProperties.put("isSearchClient", client.equals("search"));

    // We don't extend hashmap
    propertyAdditionalKeywords.clear();

    // Simplify types
    List<String> primitives = Arrays.asList(
      "Byte",
      "ByteArray",
      "Short",
      "Int",
      "Long",
      "Float",
      "Double",
      "Boolean",
      "Char",
      "String",
      "Array",
      "List",
      "MutableList",
      "Map",
      "MutableMap",
      "Set",
      "MutableSet"
    );
    languageSpecificPrimitives = new HashSet<>(primitives);

    // Types mapping
    typeMapping.put("string", "String");
    typeMapping.put("boolean", "Boolean");
    typeMapping.put("integer", "Int");
    typeMapping.put("float", "Double");
    typeMapping.put("number", "Double");
    typeMapping.put("long", "Long");
    typeMapping.put("double", "Double");
    typeMapping.put("array", "List"); // use List instead of Array
    typeMapping.put("list", "List");
    typeMapping.put("set", "Set");
    typeMapping.put("map", "Map");
    typeMapping.put("AnyType", "Any");
    typeMapping.put("object", "JsonObject"); // from kotlinx.serialization

    // Container types
    instantiationTypes.put("map", "AbstractMap");
    instantiationTypes.put("array", "AbstractList");
    instantiationTypes.put("set", "AbstractSet");

    // Prevent generating tests
    apiTestTemplateFiles.clear();
    modelTestTemplateFiles.clear();

    // Prevent generating custom docs
    apiDocTemplateFiles.clear();
    modelDocTemplateFiles.clear();
    supportingFiles.clear();

    // Add custom files
    final String packageFolder = (sourceFolder + File.separator + packageName).replace(".", "/");
    supportingFiles.add(new SupportingFile("BuildConfig.kt.mustache", packageFolder, "BuildConfig.kt"));
    final String apiFolder = (sourceFolder + File.separator + apiPackage).replace(".", "/");
    supportingFiles.add(new SupportingFile("ApiClient.kt.mustache", apiFolder, "ApiClient.kt"));
    supportingFiles.add(new SupportingFile("gradle.properties.mustache", "", "gradle.properties"));
    supportingFiles.add(new SupportingFile("README_BOM.mustache", "client-bom", "README.md"));

    additionalProperties.put("packageVersion", Utils.getClientConfigField("kotlin", "packageVersion"));

    try {
      Utils.generateServer(client, additionalProperties);
      hostForKotlin();
    } catch (GeneratorException e) {
      e.printStackTrace();
      System.exit(1);
    }
  }

  private void hostForKotlin() {
    String host = (String) additionalProperties.get("regionalHost");
    if (host != null) {
      String hostForKotlin = host.replaceAll("\\{([^}]+)}", "\\$$1");
      additionalProperties.put("hostForKotlin", hostForKotlin);
    }
  }

  @Override
  public CodegenOperation fromOperation(String path, String httpMethod, Operation operation, List<Server> servers) {
    CodegenOperation codegenOperation = Utils.specifyCustomRequest(super.fromOperation(path, httpMethod, operation, servers));
    // Set pathForKotlin by replacing the path variables with Kotlin's string
    // interpolation syntax
    List<String> segments = extractSegments(path);
    codegenOperation.vendorExtensions.put("pathSegments", segments);
    return codegenOperation;
  }

  private List<String> extractSegments(String input) {
    List<String> segments = new ArrayList<>();
    Pattern pattern = Pattern.compile("\\{([^}]+)}");
    for (String part : input.split("/")) {
      if (!part.isEmpty()) {
        Matcher matcher = pattern.matcher(part);
        StringBuilder sb = new StringBuilder();
        sb.append("\"");
        if (matcher.find()) {
          sb.append("$");
          sb.append(matcher.group(1));
        } else {
          sb.append(part);
        }
        sb.append("\"");
        segments.add(sb.toString());
      }
    }

    return segments;
  }

  @Override
  public Map<String, ModelsMap> postProcessAllModels(Map<String, ModelsMap> objs) {
    Map<String, ModelsMap> models = super.postProcessAllModels(objs);
    modelsOneOf(models);
    GenericPropagator.propagateGenericsToModels(models);
    jsonParent(models);
    typealias(models);
    return models;
  }

  private static void typealias(Map<String, ModelsMap> models) {
    for (ModelsMap modelContainer : models.values()) {
      CodegenModel compoundModel = modelContainer.getModels().get(0).getModel();
      if (compoundModel.allOf.size() == 1) {
        compoundModel.vendorExtensions.put("x-is-type-alias", true);
        ModelsMap modelsMap = models.get(compoundModel.allOf.iterator().next());
        CodegenModel alias = modelsMap.getModels().get(0).getModel();
        compoundModel.vendorExtensions.put("x-type-alias", alias.classname);
      }
    }
  }

  private static void jsonParent(Map<String, ModelsMap> models) {
    for (ModelsMap modelContainer : models.values()) {
      CodegenModel model = modelContainer.getModels().get(0).getModel();
      if (model.parent != null && model.parent.startsWith("AbstractMap")) {
        model.vendorExtensions.put("x-map-parent", true);
      }
    }
  }

  private void modelsOneOf(Map<String, ModelsMap> models) {
    for (ModelsMap modelContainer : models.values()) {
      // modelContainers always have 1 and only 1 model in our specs
      CodegenModel model = modelContainer.getModels().get(0).getModel();
      if (model.oneOf.isEmpty()) continue;

      List<Map<String, Object>> oneOfList = new ArrayList<>();
      for (String oneOf : model.oneOf) {
        Map<String, Object> oneOfModel = new HashMap<>();
        oneOfModel.put("type", oneOf);
        oneOfModel.put("name", oneOf.replace("<", "Of").replace(">", ""));
        oneOfModel.put("listElementType", oneOf.replace("List<", "").replace(">", ""));
        oneOfModel.put("isList", oneOf.contains("List"));

        // Mark compounds
        // 1. Find child model
        ModelsMap modelsMap = models.get(oneOf);
        if (modelsMap != null) {
          oneOfModel.put("isObject", true);
          // 2. add the child to parent model
          CodegenModel compoundModel = modelsMap.getModels().get(0).getModel();
          oneOfModel.put("child", compoundModel.classname);

          // 3. mark the child and add its parent (may have many)
          compoundModel.vendorExtensions.put("x-one-of-element", true);
          HashMap<String, String> parentInfo = new HashMap<>();
          parentInfo.put("parent_classname", model.classname);
          compoundParent(compoundModel).add(parentInfo);
          List<String> values = (List<String>) compoundModel.vendorExtensions.get("x-discriminator-fields");
          if (values != null) {
            List<Map<String, String>> newValues = values
              .stream()
              .map(value -> Collections.singletonMap("field", value))
              .collect(Collectors.toList());
            oneOfModel.put("discriminators", newValues);
          }
        }
        oneOfList.add(oneOfModel);
      }

      List<CodegenModel> sealedChilds = new ArrayList<>();
      for (String oneOf : model.oneOf) {
        ModelsMap modelsMap = models.get(oneOf);
        if (modelsMap != null) {
          CodegenModel compoundModel = modelsMap.getModels().get(0).getModel();
          compoundModel.vendorExtensions.put("x-one-of-explicit-name", compoundModel.classname);
          compoundModel.vendorExtensions.put("x-fully-qualified-classname", modelPackage + "." + compoundModel.classname);
          compoundModel.vendorExtensions.put("x-classname-or-alias", compoundModel.classname + "Impl");
          sealedChilds.add(compoundModel);
        } else {
          CodegenModel newModel = new CodegenModel();
          String name = oneOf.replace("<", "Of").replace(">", "");
          newModel.setClassname(name + "Wrapper");
          newModel.setDescription(model.classname + " as " + oneOf);
          CodegenProperty property = new CodegenProperty();
          property.setName("value");
          property.setRequired(true);
          property.setDatatypeWithEnum(oneOf);
          newModel.setVars(Collections.singletonList(property));
          newModel.vendorExtensions.put("x-is-number", newModel.isNumber);
          newModel.vendorExtensions.put("x-one-of-explicit-name", isNumberType(oneOf) ? "Number" : name);
          newModel.vendorExtensions.put("x-fully-qualified-classname", newModel.classname);
          sealedChilds.add(newModel);
        }
      }

      model.vendorExtensions.put("x-sealed-childs", sealedChilds);

      model.vendorExtensions.put("x-is-one-of-interface", true);
      model.vendorExtensions.put("x-one-of-list", oneOfList);
      model.vendorExtensions.put("x-one-of-explicit-name", Utils.shouldUseExplicitOneOfName(model.oneOf));
    }
  }

  private boolean isNumberType(String typeName) {
    return typeName.equals("Int") || typeName.equals("Double") || typeName.equals("Long");
  }

  private Set<Map<String, String>> compoundParent(CodegenModel model) {
    Set<Map<String, String>> parents = (Set<Map<String, String>>) model.vendorExtensions.get("x-one-of-element-parents");
    if (parents != null) return parents;
    parents = new HashSet<>();
    model.vendorExtensions.put("x-one-of-element-parents", parents);
    return parents;
  }

  @Override
  public OperationsMap postProcessOperationsWithModels(OperationsMap objs, List<ModelMap> models) {
    OperationsMap operations = super.postProcessOperationsWithModels(objs, models);
    GenericPropagator.propagateGenericsToOperations(operations, models);
    return operations;
  }

  @Override
  public String toEnumVarName(String value, String datatype) {
    if (!"String".equals(datatype)) return super.toEnumVarName(value, datatype);
    String enumVarName = value.replace("-", "_");
    return super.toEnumVarName(enumVarName, datatype);
  }

  @Override
  public String toVarName(String name) {
    String newName = super.toVarName(name);
    if (StringUtils.isAllUpperCase(newName)) { // e.g. LTE, GT.
      return StringUtils.lowerCase(newName);
    }
    return newName;
  }
}
