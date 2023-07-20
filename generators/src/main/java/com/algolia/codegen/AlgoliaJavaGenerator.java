package com.algolia.codegen;

import com.algolia.codegen.exceptions.*;
import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.oas.models.media.Schema;
import io.swagger.v3.oas.models.servers.Server;
import java.util.*;
import org.openapitools.codegen.*;
import org.openapitools.codegen.languages.JavaClientCodegen;
import org.openapitools.codegen.model.ModelMap;
import org.openapitools.codegen.model.ModelsMap;
import org.openapitools.codegen.model.OperationsMap;

@SuppressWarnings("unchecked")
public class AlgoliaJavaGenerator extends JavaClientCodegen {

  @Override
  public String getName() {
    return "algolia-java";
  }

  @Override
  public void processOpts() {
    // generator specific options
    String client = (String) additionalProperties.get("client");
    setSourceFolder("algoliasearch-core/src/main/java");
    setGroupId("com.algolia");
    setModelPackage("com.algolia.model." + Utils.camelize(client).toLowerCase());
    additionalProperties.put("invokerPackage", "com.algolia");
    setApiPackage("com.algolia.api");
    setApiNameSuffix(Utils.API_SUFFIX);

    super.processOpts();

    // Generation notice, added on every generated files
    Utils.setGenerationBanner(additionalProperties);

    // Prevent all useless file to generate
    apiTestTemplateFiles.clear();
    modelTestTemplateFiles.clear();
    apiDocTemplateFiles.clear();
    modelDocTemplateFiles.clear();

    supportingFiles.removeIf(file ->
      file.getTemplateFile().equals("build.gradle.mustache") ||
      file.getTemplateFile().equals("settings.gradle.mustache") ||
      file.getTemplateFile().equals("gradlew.mustache") ||
      file.getTemplateFile().equals("gitignore.mustache") ||
      file.getTemplateFile().equals("ApiClient.mustache") ||
      file.getTemplateFile().equals("ApiCallback.mustache") ||
      file.getTemplateFile().equals("ApiResponse.mustache") ||
      file.getTemplateFile().equals("AbstractOpenApiSchema.mustache") ||
      file.getTemplateFile().equals("maven.yml.mustache") ||
      file.getTemplateFile().equals("JSON.mustache") ||
      file.getTemplateFile().equals("ProgressRequestBody.mustache") ||
      file.getTemplateFile().equals("ProgressResponseBody.mustache") ||
      file.getTemplateFile().equals("Pair.mustache")
    );

    additionalProperties.put("isSearchClient", client.equals("search"));

    try {
      Utils.generateServer(client, additionalProperties);

      additionalProperties.put("packageVersion", Utils.getClientConfigField("java", "packageVersion"));
    } catch (GeneratorException e) {
      e.printStackTrace();
      System.exit(1);
    }
  }

  @Override
  protected void addAdditionPropertiesToCodeGenModel(CodegenModel codegenModel, Schema schema) {
    // this is needed to preserve additionalProperties: true
    super.addParentContainer(codegenModel, codegenModel.name, schema);
  }

  @Override
  public CodegenOperation fromOperation(String path, String httpMethod, Operation operation, List<Server> servers) {
    return Utils.specifyCustomRequest(super.fromOperation(path, httpMethod, operation, servers));
  }

  @Override
  public Map<String, ModelsMap> postProcessAllModels(Map<String, ModelsMap> objs) {
    Map<String, ModelsMap> models = super.postProcessAllModels(objs);

    for (ModelsMap modelContainer : models.values()) {
      // modelContainers always have 1 and only 1 model in our specs
      CodegenModel model = modelContainer.getModels().get(0).getModel();

      if (!model.oneOf.isEmpty()) {
        List<HashMap<String, String>> oneOfList = new ArrayList();

        for (String oneOf : model.oneOf) {
          HashMap<String, String> oneOfModel = new HashMap();

          oneOfModel.put("type", oneOf);
          oneOfModel.put("name", oneOf.replace("<", "Of").replace(">", ""));

          oneOfList.add(oneOfModel);
        }

        model.vendorExtensions.put("x-is-one-of-interface", true);
        model.vendorExtensions.put("x-one-of-list", oneOfList);

        model.vendorExtensions.put("x-one-of-explicit-name", Utils.shouldUseExplicitOneOfName(model.oneOf));
      }
    }

    GenericPropagator.propagateGenericsToModels(models);

    return models;
  }

  @Override
  public OperationsMap postProcessOperationsWithModels(OperationsMap objs, List<ModelMap> models) {
    OperationsMap operations = super.postProcessOperationsWithModels(objs, models);
    GenericPropagator.propagateGenericsToOperations(operations, models);
    return operations;
  }

  @Override
  public String toEnumVarName(String value, String datatype) {
    // when it's not a string, we don't want to change the name of the variable generated
    if (!"String".equals(datatype)) {
      return super.toEnumVarName(value, datatype);
    }

    // In some cases, the API might accept characters instead of the textual notation, we will
    // replace it internally so that it doesn't output the character itself.
    switch (value) {
      case "*":
        return "ALL";
    }

    if (!value.matches("[A-Z0-9_]+")) {
      // convert camelCase77String to CAMEL_CASE_77_STRING
      return value.replaceAll("-", "_").replaceAll("(.+?)([A-Z]|[0-9])", "$1_$2").toUpperCase(Locale.ROOT);
    }

    return super.toEnumVarName(value, datatype);
  }
}
