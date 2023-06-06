package com.algolia.codegen;

import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.oas.models.servers.Server;
import java.util.*;
import org.openapitools.codegen.*;
import org.openapitools.codegen.languages.DartDioClientCodegen;
import org.openapitools.codegen.model.ModelMap;
import org.openapitools.codegen.model.ModelsMap;
import org.openapitools.codegen.model.OperationsMap;
import org.openapitools.codegen.utils.StringUtils;

public class AlgoliaDartGenerator extends DartDioClientCodegen {

  private final SchemaSupport support = new SchemaSupport();

  String libName;
  boolean isAlgoliasearchClient;

  @Override
  public String getName() {
    return "algolia-dart";
  }

  @Override
  public void processOpts() {
    String client = (String) additionalProperties.get("client");
    isAlgoliasearchClient = client.equals("algoliasearch");
    String version = Utils.getOpenApiToolsField("dart", client, "packageVersion");
    additionalProperties.put("isAlgoliasearchClient", isAlgoliasearchClient);

    // pubspec.yaml
    setPubAuthor("Algolia");
    setPubAuthorEmail("hey@algolia.com");
    setPubHomepage("https://www.algolia.com/doc/");
    setPubVersion(version);
    String clientName;
    String packageFolder;
    if (isAlgoliasearchClient) {
      libName = "algoliasearch";
      packageFolder = libName;
      clientName = "Search Lite";
      setPubName(libName);
      setPubLibrary(libName);
    } else {
      libName = "algolia_client_" + client;
      clientName = "Algolia " + client;
      setApiNameSuffix(Utils.API_SUFFIX);
      packageFolder = "client_" + client;
      setPubName(libName);
      setPubLibrary(libName);
    }
    setPubDescription("Algolia " + clientName + " API client to interact with Algolia");
    setPubRepository("https://github.com/algolia/algoliasearch-client-dart/packages/" + packageFolder);

    // configs
    additionalProperties.put(CodegenConstants.SERIALIZATION_LIBRARY, SERIALIZATION_LIBRARY_JSON_SERIALIZABLE);

    super.processOpts();

    if (isAlgoliasearchClient) {
      supportingFiles.removeIf(file -> file.getTemplateFile().contains("lib"));
      supportingFiles.add(new SupportingFile("lib.mustache", libPath, "algoliasearch_lite.dart"));
      additionalProperties.put("searchVersion", Utils.getOpenApiToolsField("dart", "search", "packageVersion"));
      additionalProperties.put("insightsVersion", Utils.getOpenApiToolsField("dart", "insights", "packageVersion"));
    }

    // disable documentation and tests
    apiTestTemplateFiles.clear();
    modelTestTemplateFiles.clear();
    apiDocTemplateFiles.clear();
    modelDocTemplateFiles.clear();

    // Generation notice, added on every generated files
    Utils.setGenerationBanner(additionalProperties);

    // Cleanup supporting files
    supportingFiles.removeIf(file -> file.getTemplateFile().contains("auth"));
    supportingFiles.removeIf(file -> file.getTemplateFile().contains("api_client"));
    supportingFiles.removeIf(file -> file.getTemplateFile().contains("gitignore"));
    supportingFiles.removeIf(file -> file.getTemplateFile().contains("build"));
    supportingFiles.removeIf(file -> file.getTemplateFile().contains("analysis_options"));

    final String srcFolder = libPath + sourceFolder;
    supportingFiles.add(new SupportingFile("version.mustache", srcFolder, "version.dart"));

    // Search config
    additionalProperties.put("isSearchClient", client.equals("search"));
    additionalProperties.put("packageVersion", Utils.getClientConfigField("dart", "packageVersion"));

    // typeMapping.put("object", "Map<String, dynamic>"); // from kotlinx.serialization

    // Generate server info
    Utils.generateServer(client, additionalProperties);
  }

  @Override
  public String toApiName(String name) {
    return isAlgoliasearchClient ? "SearchClient" : super.toApiName(name);
  }

  @Override
  public Map<String, ModelsMap> postProcessAllModels(Map<String, ModelsMap> objs) {
    Map<String, ModelsMap> modelsMap = super.postProcessAllModels(objs);
    return support.clearOneOfFromModels(libName, modelsMap);
  }

  @Override
  public CodegenOperation fromOperation(String path, String httpMethod, Operation operation, List<Server> servers) {
    CodegenOperation op = super.fromOperation(path, httpMethod, operation, servers);
    CodegenOperation codegenOperation = Utils.specifyCustomRequest(op);
    return support.clearOneOfFromOperation(codegenOperation);
  }

  @Override
  public OperationsMap postProcessOperationsWithModels(OperationsMap objs, List<ModelMap> allModels) {
    OperationsMap operationsMap = super.postProcessOperationsWithModels(objs, allModels);
    return support.clearOneOfFromApiImports(operationsMap);
  }

  @Override
  public String toModelFilename(String name) {
    return support.classnames().contains(name) ? null : super.toModelFilename(name);
  }
}

class SchemaSupport {

  private static final String GENERIC_TYPE = "dynamic";

  private final Map<String, String> oneOfs = new HashMap<>(); // Maintain a list of deleted class names

  public Set<String> classnames() {
    return oneOfs.keySet();
  }

  public Collection<String> imports() {
    return oneOfs.values();
  }

  Map<String, ModelsMap> clearOneOfFromModels(String libName, Map<String, ModelsMap> modelsMap) {
    removeModels(libName, modelsMap);
    updateFieldTypes(modelsMap);
    removeImports(modelsMap);
    return modelsMap;
  }

  private void removeModels(String libName, Map<String, ModelsMap> modelsMap) {
    Iterator<Map.Entry<String, ModelsMap>> iterator = modelsMap.entrySet().iterator();
    while (iterator.hasNext()) {
      Map.Entry<String, ModelsMap> entry = iterator.next();
      ModelsMap modelContainer = entry.getValue();
      ModelMap modelMap = modelContainer.getModels().get(0);
      CodegenModel model = modelMap.getModel();
      if (!model.oneOf.isEmpty()) {
        String classname = modelMap.getModel().classname;
        oneOfs.put(classname, asImport(libName, classname));
        iterator.remove();
      }
    }
  }

  private String asImport(String libName, String classname) {
    return "package:" + libName + "/src/model/" + StringUtils.underscore(classname) + ".dart";
  }

  private void updateFieldTypes(Map<String, ModelsMap> modelsMap) {
    for (ModelsMap modelContainer : modelsMap.values()) {
      List<ModelMap> models = modelContainer.getModels();
      if (models == null || models.isEmpty()) continue;
      ModelMap modelMap = models.get(0);
      CodegenModel model = modelMap.getModel();
      for (CodegenProperty property : model.vars) {
        if (oneOfs.containsKey(property.dataType)) {
          property.setDatatypeWithEnum(GENERIC_TYPE);
        } else if (property.isMap && oneOfs.containsKey(property.complexType)) {
          property.setDatatypeWithEnum("Map<String, " + GENERIC_TYPE + ">");
        } else if (property.isContainer && oneOfs.containsKey(property.complexType)) {
          property.setDatatypeWithEnum("Iterable<" + GENERIC_TYPE + ">");
        }
      }
    }
  }

  private void removeImports(Map<String, ModelsMap> modelsMap) {
    for (Map.Entry<String, ModelsMap> entry : modelsMap.entrySet()) {
      ModelsMap modelContainer = entry.getValue();
      ModelMap modelMap = modelContainer.getModels().get(0);
      CodegenModel model = modelMap.getModel();
      model.imports.removeIf(oneOfs::containsValue);
    }
  }

  CodegenOperation clearOneOfFromOperation(CodegenOperation operation) {
    for (CodegenParameter parameter : operation.allParams) {
      boolean isCleared = false;
      if (oneOfs.containsKey(parameter.dataType)) {
        parameter.dataType = GENERIC_TYPE;
        isCleared = true;
      } else if (parameter.isMap && oneOfs.containsKey(parameter.baseType)) {
        parameter.dataType = "Map<String, " + GENERIC_TYPE + ">";
        isCleared = true;
      } else if (parameter.isContainer && oneOfs.containsKey(parameter.baseType)) {
        parameter.dataType = "Iterable<" + GENERIC_TYPE + ">";
        isCleared = true;
      }
      if (isCleared) {
        parameter.isModel = false;
      }
    }
    return operation;
  }

  OperationsMap clearOneOfFromApiImports(OperationsMap operationsMap) {
    //noinspection unchecked
    List<String> imports = (List<String>) operationsMap.get("imports");
    imports.removeAll(imports());
    return operationsMap;
  }
}
